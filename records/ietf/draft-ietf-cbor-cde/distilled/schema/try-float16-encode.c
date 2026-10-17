/* =====================================================================
 * try-float16-encode.c
 *
 * VERBATIM.  This file is NOT ours.  Everything between the BEGIN and END
 * markers below is reproduced byte-for-byte, including the document's
 * three-space page margin, its interior comment alignment and the figure
 * caption, from:
 *
 *   draft-ietf-cbor-cde-13, "CBOR Common Deterministic Encoding (CDE)",
 *   C. Bormann, Universitaet Bremen TZI, 14 October 2025,
 *   <https://www.ietf.org/archive/id/draft-ietf-cbor-cde-13.txt>
 *
 *   Appendix F, "Example Code for Encoding into 16-bit Floating Point",
 *   Figure 1, in full.  Cached source lines 2195-2215, caption at 2217
 *   (.cache/draft-ietf-cbor-cde.txt, sha256
 *   bc554e3d2d37182f5f37c88aac2e61298089438068ccbc7c674d0940e675605c).
 *
 * Introduced in the source by (cached source lines 2186-2193): "Given that
 * CDE implementations that support floating point Numbers not only need to
 * decode, but also to encode their 16-bit format, this appendix provides
 * example C code to convert a floating point number that is in 64-bit form
 * ("Double Precision", binary64) into binary16.  If such a conversion is
 * not possible (i.e., there is no 16-bit representation for the 64-bit
 * value given), the function try_float16_encode returns -1.  Otherwise it
 * returns a two-byte integer (range 0x0000 to 0xFFFF) that, prefixed with
 * 0xF9, is suitable to encode the value."
 *
 * This function and the one CDDL rule in cde-control-operator.cddl are the
 * WHOLE of this document's formal, machine-consumable material.  It must
 * not be edited; the three-space indentation is the page margin and is
 * retained so the region stays byte-identical to the source.  C is
 * insensitive to it, so the file still compiles as-is.
 *
 * Scope, and what it does NOT cover -- read before treating this as the
 * encoder:
 *   - It implements only the binary64 -> binary16 leg of shortest-head
 *     float encoding.  CDE needs the full cascade f16, then f32, then f64
 *     (Appendix C.1.1 item 2: "If multiple of these encodings preserve the
 *     precision of the value to be encoded, only the shortest form of
 *     these MUST be emitted").  The document supplies NO binary64 ->
 *     binary32 counterpart.  The cascade is written out in
 *     float-shortest-head.derived.pseudocode.txt.
 *   - Its input is a binary64 BIT PATTERN in an unsigned long, not a
 *     double; `unsigned long` is assumed to be at least 64 bits.
 *   - For NaN it returns s16 + 0x7c00 + (mant >> 42), which preserves the
 *     sign bit and the quiet bit and trims 42 payload bits; the
 *     "trimming is permitted only if the removed bits are zero" rule of
 *     Appendix C.1.1 is enforced by the earlier
 *     `if (mant & 0x3ffffffffffUL) return -1;` (0x3ffffffffff is 42 bits).
 *   - Non-zero binary64 subnormals always fall through to the final
 *     `return -1`; the comment "f64 denorms are out of range" sits on the
 *     exp==0 && mant==0 branch, which handles only 0.0 and -0.0.
 *
 * Per the document's Copyright Notice: "Code Components extracted from
 * this document must include Revised BSD License text as described in
 * Section 4.e of the Trust Legal Provisions and are provided without
 * warranty as described in the Revised BSD License."  This copy is held
 * for study and cross-checking, is attributed above, and is governed by
 * that notice -- not by this library's licence.
 * =====================================================================
 */

/* ---- BEGIN VERBATIM (draft-ietf-cbor-cde-13, Appendix F, Figure 1) ---- */
   /* returns 0..0xFFFF if float16 encoding possible, -1 otherwise.
      b64 is a binary64 floating point as an unsigned long. */
   int try_float16_encode(unsigned long b64) {
     unsigned long s16 = b64 >> 48 & 0x8000UL;
     unsigned long mant = b64 & 0xfffffffffffffUL;
     unsigned long exp = b64 >> 52 & 0x7ffUL;
     if (exp == 0 && mant == 0)    /* f64 denorms are out of range */
       return s16;                 /* so handle 0.0 and -0.0 only */
     if (exp >= 999 && exp < 1009) { /* f16 denorm, exp16 = 0 */
       if (mant & ((1UL << (1051 - exp)) - 1))
         return -1;                /* bits lost in f16 denorm */
       return s16 + ((mant + 0x10000000000000UL) >> (1051 - exp));
     }
     if (mant & 0x3ffffffffffUL)   /* bits lost in f16 */
       return -1;
     if (exp >= 1009 && exp <= 1038) /* normalized f16 */
       return s16 + ((exp - 1008) << 10) + (mant >> 42);
     if (exp == 2047)              /* Inf, NaN */
       return s16 + 0x7c00 + (mant >> 42);
     return -1;
   }

           Figure 1: Example C Code for a Half-Precision Encoder
/* ---- END VERBATIM ---- */
