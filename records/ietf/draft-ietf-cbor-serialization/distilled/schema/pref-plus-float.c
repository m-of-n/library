// =====================================================================
// pref-plus-float.c
//
// VERBATIM.  This file is NOT ours.  Everything between the BEGIN and
// END markers below is reproduced byte-for-byte, including the draft's
// three-space page margin and its interior alignment, from:
//
//   draft-ietf-cbor-serialization-08, "CBOR Serialization and
//   Determinism", L. Lundblade, Security Theory LLC, 29 July 2026,
//   Appendix D ("Code for Encoding Preferred-Plus Floating-Point
//   Values"), in full, ending with the Figure 1 caption.
//   Lines 1588-1744 of the cached text rendering
//   (.cache/draft-ietf-cbor-serialization.txt, sha256
//   a612e6c4f674da61b1c888431a06dca13457aaea53c1cd86c8b50f8999b47112).
//
// THE ONE ALTERATION, stated so nobody has to diff for it.  Appendix D
// spans three printed pages, and each page boundary interrupts the code
// with eight lines of page furniture: three blank lines, the running
// footer ("Lundblade ... [Page NN]"), a form feed (0x0C), the running
// header ("Internet-Draft ... July 2026") and two more blank lines.
// Those three eight-line blocks - source lines 1621-1628, 1677-1684 and
// 1733-1740 - are deleted in full and nothing is put in their place.
// Deleting rather than replacing with a blank line is what reconstructs
// the author's text: break 2 falls inside an `else if` body and break 3
// between two closing braces, where no blank line can have existed, and
// break 1 falls between a comment and the #define it introduces, which
// is exactly how the parallel "Converting double to single" comment is
// laid out eleven lines later with no blank between them.  No other
// byte is changed, added or re-wrapped.
//
// WHAT IT IS.  Appendix D is the draft's only executable artifact and
// the only place where the hardest preferred-plus rule - Section 4.1
// rule 4, "Values MUST be encoded in the shortest of double, single or
// half-precision that preserves precision" - is given as a procedure
// rather than as a sentence.  The draft introduces it: "Preferred-plus
// (Section 4.1) and deterministic serialization require that floating-
// point values fitting in single-precision and half-precision be
// encoded as such.  This C code implements that conversion."  It is the
// encoder-side counterpart to Appendix D of [STD94], which gives
// decoding code for half-precision.
//
// HOW TO CALL IT, from the draft's own prose: "If the input is a
// double, pref_plus_double_to_single() must be called first; if it
// succeeds, pref_plus_single_to_half() is then called to complete the
// conversion from double to half.  If the input is already a single,
// only pref_plus_single_to_half() need be called."  Both return the bit
// pattern of the narrower value, or -1 when the conversion would lose
// precision or go out of range - and -1 is therefore the signal to keep
// the wider encoding, not an error.
//
// IT IS LABELLED "Example ... Code", NOT NORMATIVE.  The caption reads
// "Figure 1: Example C Code for Preferred-Plus Floating-Point
// Encoding", and the draft calls it "example code".  Section 4.1 rule 4
// is the requirement; this is one implementation of it.  Cite the rule,
// not the function.
//
// AND IT DECIDES ONE THING THE PROSE ONLY IMPLIES.  Both functions
// return -1 for every NaN except the canonical quiet one, and that
// branch is commented "non-trivial NaN" - so the code refuses to narrow
// a NaN with a payload or a set sign bit instead of silently dropping
// the payload.  The matching sentence is Section 4.1 rule 4 bullet 3,
// "Encoders MUST NOT output any NaN other than the half-precision NaN
// 0xf9 0x7e 0x00 ... the encoder MUST either reject it or encode it as
// 0xf9 0x7e 0x00"; the code takes the "reject" half of that choice and
// leaves the "encode it as 0xf97e00" half to the caller.  Note too that
// pref_plus_single_to_half() will not narrow a *negative* trivial NaN
// (it tests `sign == 0`), which is consistent: Appendix C.1 counts a
// NaN with the sign bit set as non-trivial.
//
// The draft ships no other code and no ABNF.  Its only other formal
// artifacts are two CDDL fragments, held here as bignums.cddl and
// serial-control-operator.cddl.  Everything else in this directory is
// derived - see README.md.
//
// COMPILATION NOTE.  The three-space margin is the draft's page margin
// and is kept so the region stays byte-identical to the source; C is
// insensitive to it, so the file compiles as-is.  The trailing Figure 1
// caption line is part of the verbatim region and is not C: strip it,
// or keep it inside a comment, before feeding the file to a compiler.
// =====================================================================

/* ---- BEGIN VERBATIM (draft-ietf-cbor-serialization-08, Appendix D) ---- */
   /* Constants based on IEEE 754; _LEN is in bits */

   /* Half-precision */
   #define HLF_MANT_LEN          10
   #define HLF_EXP_LEN           5
   #define HLF_MANT_BITS         0x3ffUL /* 10 bits */
   #define HLF_SIGN_BIT         (0x01UL << (HLF_EXP_LEN + HLF_MANT_LEN))
   #define HLF_NAN_INF_EXP_BITS  0x7c00
   #define HLF_QUIET_NAN        (0x1UL << (HLF_MANT_LEN-1))

   /* Single-precision */
   #define SGL_MANT_LEN          23
   #define SGL_EXP_LEN           8
   #define SGL_MANT_BITS         0x7fffffUL /* 23 bits */
   #define SGL_SIGN_BIT         (0x01UL << (SGL_EXP_LEN + SGL_MANT_LEN))
   #define SGL_EXP_BITS          0xffUL /* 8 bits */
   #define SGL_QUIET_NAN        (0x1UL << (SGL_MANT_LEN - 1))
   #define SGL_ZERO_SUBNORM_EXP  0
   #define SGL_NAN_INF_EXP       255
   #define SGL_NAN_INF_EXP_BITS (SGL_NAN_INF_EXP << SGL_MANT_LEN)
   #define SGL_MANT_ADD_ONE     (0x01UL << SGL_MANT_LEN)

   /* Double-precision */
   #define DBL_MANT_LEN          52
   #define DBL_EXP_LEN           11
   #define DBL_MANT_BITS         0xfffffffffffffULL /* 52 bits */
   #define DBL_EXP_BITS          0x7ffULL /* 11 bits */
   #define DBL_QUIET_NAN        (0x1ULL << (DBL_MANT_LEN-1))
   #define DBL_ZERO_SUBNORM_EXP  0
   #define DBL_NAN_INF_EXP       2047
   #define DBL_MANT_ADD_ONE     (0x01ULL << (DBL_MANT_LEN))

   /* Converting single to half; _EXP are biased single exponents */
   #define S2H_SIGN_SHIFT       16
   #define S2H_BIAS_DIFF_EXP   (127 - 15)
   #define S2H_MIN_NORM_EXP     113
   #define S2H_MIN_SUBNORM_EXP  102
   #define S2H_SUBNORM_SHIFT    126
   #define S2H_MAX_NORM_EXP     142
   #define S2H_LOST_BITS        0x1fffUL /* 23 - 10 bits */

   /* Converting double to single; _EXP are biased double exponents */
   #define D2S_SIGN_SHIFT       32
   #define D2S_BIAS_DIFF_EXP   (1023 - 127)
   #define D2S_MIN_NORM_EXP     898
   #define D2S_MIN_SUBNORM_EXP  874
   #define D2S_SUBNORM_SHIFT    926
   #define D2S_MAX_NORM_EXP     1150
   #define D2S_LOST_BITS        0x1fffffffULL /* 52 - 23 bits */


   long pref_plus_single_to_half(unsigned long single) {
     const unsigned long sign = single >> S2H_SIGN_SHIFT & HLF_SIGN_BIT;
     const unsigned long mant = single & SGL_MANT_BITS;
     const unsigned long exp  = single >> SGL_MANT_LEN & SGL_EXP_BITS;

     if (exp == SGL_ZERO_SUBNORM_EXP) {
       if (mant == 0) {
         return (long)sign; /* +/- 0.0 */
       } else {
         return -1; /* single subnormals are out of range for half */
       }
     } else if (exp >= S2H_MIN_SUBNORM_EXP && exp < S2H_MIN_NORM_EXP) {
       if (mant & ((1UL << (S2H_SUBNORM_SHIFT - exp)) - 1)) {
         return -1;   /* bits lost in conversion to half subnormal */
       } else {
         return (long)(sign + /* converts to half subnormal */
              ((mant + SGL_MANT_ADD_ONE) >> (S2H_SUBNORM_SHIFT - exp)));
       }
     } else if (exp >= S2H_MIN_NORM_EXP && exp <= S2H_MAX_NORM_EXP) {
       if (mant & S2H_LOST_BITS) {
         return -1; /* bits lost in conversion */
       } else {
         return (long)(sign + /* Converts to normal */
                      ((exp - S2H_BIAS_DIFF_EXP) << HLF_MANT_LEN) +
                      (mant >> (SGL_MANT_LEN - HLF_MANT_LEN)));
       }
     } else if (exp == SGL_NAN_INF_EXP) {
       if (mant == 0) {
         return (long)(sign + HLF_NAN_INF_EXP_BITS); /* +/- infinity */
       } else if (mant == SGL_QUIET_NAN && sign == 0) {
          return HLF_QUIET_NAN + HLF_NAN_INF_EXP_BITS; /* trivial NaN */
       } else {
          return -1; /* non-trivial NaN */
       }
     } else {
        return -1; /* large exponent -- out of range for half */
     }
   }


   long long pref_plus_double_to_single(unsigned long long dbl) {
     const unsigned long long sign =
                                   dbl >> D2S_SIGN_SHIFT & SGL_SIGN_BIT;
     const unsigned long long mant = dbl & DBL_MANT_BITS;
     const unsigned long long exp  = dbl >> DBL_MANT_LEN & DBL_EXP_BITS;

     if (exp == DBL_ZERO_SUBNORM_EXP) {
       if (mant == 0) {
         return (long long)sign; /* +/- 0.0 */
       } else {
         return -1; /* double subnormals are out of range for single */
       }
     } else if (exp >= D2S_MIN_SUBNORM_EXP && exp < D2S_MIN_NORM_EXP) {
       if (mant & ((1ULL << (D2S_SUBNORM_SHIFT - exp)) - 1)) {
         return -1; /* bits lost in conversion to single subnormal */
       } else {
         return (long long)(sign + /* converts to single subnormal */
              ((mant + DBL_MANT_ADD_ONE) >> (D2S_SUBNORM_SHIFT - exp)));
        }
     } else if (exp >= D2S_MIN_NORM_EXP && exp <= D2S_MAX_NORM_EXP) {
       if (mant & D2S_LOST_BITS) {
         return -1; /* bits lost in conversion */
       } else {
          return (long long)(sign + /* Converts to normal */
                           ((exp - D2S_BIAS_DIFF_EXP) << SGL_MANT_LEN) +
                            (mant >> (DBL_MANT_LEN - SGL_MANT_LEN)));
       }
     } else if (exp == DBL_NAN_INF_EXP) {
       if (mant == 0) {
         /* +/- infinity */
         return (long long)(sign + SGL_NAN_INF_EXP_BITS);
       } else if (mant == DBL_QUIET_NAN && sign == 0) {
          return SGL_QUIET_NAN + SGL_NAN_INF_EXP_BITS; /* quiet NaN */
       } else {
          return -1; /* non-trivial NaN */
       }
     } else {
        return -1; /* large exponent -- out of range for single */
     }
   }

    Figure 1: Example C Code for Preferred-Plus Floating-Point Encoding
/* ---- END VERBATIM ---- */
