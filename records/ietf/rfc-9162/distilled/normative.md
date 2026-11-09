---
record: rfc-9162
kind: normative
title: "rfc-9162 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent line rather than quoted twice. The keyword-less binding text pass 1 added (candidate-stated and hunted entries) is interleaved in source order. Generated together with requirements.yaml: 488 requirements, of which 125 skeleton, 30 split children, 154 from candidates, 151 hunted and 28 inferred; pass 2 added 3 hunted (R-0489 to R-0491), 491 in all.

## §1.1

The BCP 14 recital. Not a requirement and not an entry: quoting it would add its eleven keywords to the extracted count. It is the reason lowercase may, must and should in this document are not BCP 14.

<!-- q L223-227 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

## §1.2

<!-- q L231-232 -->
> Data structures are defined and encoded according to the conventions laid out in Section 3 of [RFC8446].

R-0126 · no candidate (hunted)

## §2.1.1

<!-- q L323-325 "Throughout" .. "HASH_SIZE." -->
> Throughout this document, the hash algorithm in use is referred to as HASH and the size of its output in bytes is referred to as HASH_SIZE.

R-0127 · no candidate (hunted)

<!-- q L325-328 "The input" .. "Hash." -->
> The input to the Merkle Tree Hash is a list of data entries; these entries will be hashed to form the leaves of the Merkle Tree. The output is a single HASH_SIZE Merkle Tree Hash.

R-0128 · no candidate (hunted)

<!-- q L328-329 "Given an" .. "follows:" -->
> Given an ordered list of n inputs, D_n = {d[0], d[1], ..., d[n-1]}, the Merkle Tree Hash (MTH) is thus defined as follows:

R-0129 · no candidate (hunted)

<!-- q L331-333 -->
> The hash of an empty list is the hash of an empty string: MTH({}) = HASH().

R-0130 · no candidate (hunted)

<!-- q L335-337 -->
> The hash of a list with one entry (also known as a leaf hash) is: MTH({d[0]}) = HASH(0x00 || d[0]).

R-0131 · no candidate (hunted)

<!-- q L339-343 -->
> For n > 1, let k be the largest power of two smaller than n (i.e., k < n <= 2k). The Merkle Tree Hash of an n-element list D_n is then defined recursively as: MTH(D_n) = HASH(0x01 || MTH(D[0:k]) || MTH(D[k:n])),

R-0132 · no candidate (hunted)

<!-- q L347-347 -->
> * || denotes concatenation

R-0133 · candidate C-0032

<!-- q L349-349 -->
> * : denotes concatenation of lists

R-0134 · candidate C-0033

<!-- q L351-352 -->
> * D[k1:k2] = D'_(k2-k1) denotes the list {d'[0] = d[k1], d'[1] = d[k1+1], ..., d'[k2-k1-1] = d[k2-1]} of length (k2 - k1).

R-0135 · candidate C-0034

## §2.1.2

<!-- q L366-369 -->
> When a client has a complete list of entries from 0 up to tree_size - 1 and wishes to verify this list against a tree head root_hash returned by the log for the same tree_size, the following algorithm may be used:

R-0136 · candidate C-0038

<!-- q L371-371 -->
> 1. Set stack to an empty stack.

R-0137 · candidate C-0039

<!-- q L373-373 -->
> 2. For each i from 0 up to tree_size - 1:

R-0138 · candidate C-0040

<!-- q L375-375 -->
> a. Push HASH(0x00 || entries[i]) to stack.

R-0139 · no candidate (hunted)

<!-- q L377-381 -->
> b. Set merge_count to the lowest value (0 included) such that LSB(i >> merge_count) is not set, where LSB means the least significant bit. In other words, set merge_count to the number of consecutive 1s found starting at the least significant bit of i.

R-0140 · no candidate (hunted)

<!-- q L383-383 -->
> c. Repeat merge_count times:

R-0141 · no candidate (hunted)

<!-- q L385-385 -->
> i. Pop right from stack.

R-0142 · no candidate (hunted)

<!-- q L387-387 -->
> ii. Pop left from stack.

R-0143 · no candidate (hunted)

<!-- q L389-389 -->
> iii. Push HASH(0x01 || left || right) to stack.

R-0144 · no candidate (hunted)

<!-- q L391-393 -->
> 3. If there is more than one element in the stack, repeat the same merge procedure (the sub-items of Step 2(c) above) until only a single element remains.

R-0145 · candidate C-0041

<!-- q L395-397 -->
> 4. The remaining element in stack is the Merkle Tree Hash for the given tree_size and should be compared by equality against the supplied root_hash.

R-0146 · candidate C-0042

## §2.1.3.1

<!-- q L415-417 -->
> Given an ordered list of n inputs to the tree, D_n = {d[0], d[1], ..., d[n-1]}, the Merkle inclusion proof PATH(m, D_n) for the (m+1)th input d[m], 0 <= m < n, is defined as follows:

R-0147 · no candidate (hunted)

<!-- q L419-422 -->
> The proof for the single leaf in a tree with a one-element input list D[1] = {d[0]} is empty: PATH(0, {d[0]}) = {}

R-0148 · no candidate (hunted)

<!-- q L424-426 -->
> For n > 1, let k be the largest power of two smaller than n. The proof for the (m+1)th element d[m] in a list of n > m elements is then defined recursively as:

R-0149 · no candidate (hunted)

<!-- q L428-428 -->
> PATH(m, D_n) = PATH(m, D[0:k]) : MTH(D[k:n]) for m < k; and

R-0150 · no candidate (hunted)

<!-- q L430-430 -->
> PATH(m, D_n) = PATH(m - k, D[k:n]) : MTH(D[0:k]) for m >= k,

R-0151 · no candidate (hunted)

## §2.1.3.2

<!-- q L436-440 -->
> When a client has received an inclusion proof (e.g., in a TransItem of type inclusion_proof_v2) and wishes to verify inclusion of an input hash for a given tree_size and root_hash, the following algorithm may be used to prove the hash was included in the root_hash:

R-0152 · candidate C-0046

<!-- q L442-443 "1. Compare" .. "tree_size." -->
> 1. Compare leaf_index from the inclusion_proof_v2 structure against tree_size.

R-0153 · candidate C-0047

<!-- q L443-444 "If leaf_index" .. "verification." -->
> If leaf_index is greater than or equal to tree_size, then fail the proof verification.

R-0154 · candidate C-0048

<!-- q L446-446 -->
> 2. Set fn to leaf_index and sn to tree_size - 1.

R-0155 · candidate C-0049

<!-- q L448-448 -->
> 3. Set r to hash.

R-0156 · candidate C-0050

<!-- q L450-450 -->
> 4. For each value p in the inclusion_path array:

R-0157 · candidate C-0051

<!-- q L452-453 -->
> a. If sn is 0, then stop the iteration and fail the proof verification.

R-0158 · no candidate (hunted)

<!-- q L455-455 "If LSB(fn)" .. "then:" -->
> If LSB(fn) is set, or if fn is equal to sn, then:

R-0159 · candidate C-0052

<!-- q L457-457 -->
> i. Set r to HASH(0x01 || p || r).

R-0160 · no candidate (hunted)

<!-- q L459-460 "If LSB(fn)" .. "is 0." -->
> If LSB(fn) is not set, then right-shift both fn and sn equally until either LSB(fn) is set or fn is 0.

R-0161 · candidate C-0053

<!-- q L462-464 -->
> Otherwise: i. Set r to HASH(0x01 || r || p).

R-0162 · no candidate (hunted)

<!-- q L466-466 -->
> c. Finally, right-shift both fn and sn one time.

R-0163 · no candidate (hunted)

<!-- q L468-468 "5. Compare" .. "root_hash." -->
> 5. Compare sn to 0. Compare r against the root_hash.

R-0164 · candidate C-0054

<!-- q L468-470 "If sn is" .. "hash." -->
> If sn is equal to 0 and r and the root_hash are equal, then the log has proven the inclusion of hash.

R-0165 · candidate C-0055

<!-- q L470-471 "Otherwise," .. "verification." -->
> Otherwise, fail the proof verification.

R-0166 · candidate C-0056

## §2.1.4.1

<!-- q L487-491 -->
> Given an ordered list of n inputs to the tree, D_n = {d[0], d[1], ..., d[n-1]}, the Merkle consistency proof PROOF(m, D_n) for a previous Merkle Tree Hash MTH(D[0:m]), 0 < m < n, is defined as: PROOF(m, D_n) = SUBPROOF(m, D_n, true)

R-0167 · no candidate (hunted)

<!-- q L493-497 -->
> In SUBPROOF, the boolean value represents whether the subtree created from D[0:m] is a complete subtree of the Merkle Tree created from D_n and, consequently, whether the subtree Merkle Tree Hash MTH(D[0:m]) is known. The initial call to SUBPROOF sets this to be true, and SUBPROOF is then defined as follows:

R-0168 · no candidate (hunted)

<!-- q L499-505 -->
> The subproof for m = n is empty if m is the value for which PROOF was originally requested (meaning that the subtree created from D[0:m] is a complete subtree of the Merkle Tree created from the original D_n for which PROOF was requested and the subtree Merkle Tree Hash MTH(D[0:m]) is known): SUBPROOF(m, D_m, true) = {}

R-0169 · no candidate (hunted)

<!-- q L507-510 -->
> Otherwise, the subproof for m = n is the Merkle Tree Hash committing inputs D[0:m]: SUBPROOF(m, D_m, false) = {MTH(D_m)}

R-0170 · no candidate (hunted)

<!-- q L512-514 -->
> For m < n, let k be the largest power of two smaller than n. The subproof is then defined recursively, using the appropriate step below:

R-0171 · no candidate (hunted)

<!-- q L516-517 "If m <= k," .. "tree." -->
> If m <= k, the right subtree entries D[k:n] only exist in the current tree.

R-0172 · candidate C-0061

<!-- q L520-520 -->
> SUBPROOF(m, D_n, b) = SUBPROOF(m, D[0:k], b) : MTH(D[k:n])

R-0173 · no candidate (hunted)

<!-- q L522-523 "If m > k," .. "trees." -->
> If m > k, the left subtree entries D[0:k] are identical in both trees.

R-0174 · no candidate (hunted)

<!-- q L526-526 -->
> SUBPROOF(m, D_n, b) = SUBPROOF(m - k, D[k:n], false) : MTH(D[0:k])

R-0175 · no candidate (hunted)

<!-- q L528-529 -->
> The number of nodes in the resulting proof is bounded above by ceil(log2(n)) + 1.

R-0176 · no candidate (hunted)

## §2.1.4.2

<!-- q L535-539 -->
> When a client has a tree head first_hash for tree size first, has a tree head second_hash for tree size second where 0 < first < second, and has received a consistency proof between the two (e.g., in a TransItem of type consistency_proof_v2), the following algorithm may be used to verify the consistency proof:

R-0177 · candidate C-0062

<!-- q L541-542 -->
> 1. If consistency_path is an empty array, stop and fail the proof verification.

R-0178 · candidate C-0063

<!-- q L544-545 -->
> 2. If first is an exact power of 2, then prepend first_hash to the consistency_path array.

R-0179 · candidate C-0064

<!-- q L547-547 -->
> 3. Set fn to first - 1 and sn to second - 1.

R-0180 · candidate C-0065

<!-- q L549-550 -->
> 4. If LSB(fn) is set, then right-shift both fn and sn equally until LSB(fn) is not set.

R-0181 · candidate C-0066

<!-- q L552-553 -->
> 5. Set both fr and sr to the first value in the consistency_path array.

R-0182 · candidate C-0067

<!-- q L555-555 -->
> 6. For each subsequent value c in the consistency_path array:

R-0183 · candidate C-0068

<!-- q L557-558 -->
> a. If sn is 0, then stop the iteration and fail the proof verification.

R-0184 · no candidate (hunted)

<!-- q L560-560 "If LSB(fn)" .. "then:" -->
> If LSB(fn) is set, or if fn is equal to sn, then:

R-0185 · candidate C-0069

<!-- q L562-562 -->
> i. Set fr to HASH(0x01 || c || fr).

R-0186 · no candidate (hunted)

<!-- q L564-564 -->
> ii. Set sr to HASH(0x01 || c || sr).

R-0187 · no candidate (hunted)

<!-- q L566-567 "If LSB(fn)" .. "is 0." -->
> If LSB(fn) is not set, then right-shift both fn and sn equally until either LSB(fn) is set or fn is 0.

R-0188 · candidate C-0070

<!-- q L569-571 -->
> Otherwise: i. Set sr to HASH(0x01 || sr || c).

R-0189 · no candidate (hunted)

<!-- q L573-573 -->
> c. Finally, right-shift both fn and sn one time.

R-0190 · no candidate (hunted)

<!-- q L575-578 -->
> 7. After completing iterating through the consistency_path array as described above, verify that the fr calculated is equal to the first_hash supplied, that the sr calculated is equal to the second_hash supplied, and that sn is 0.

R-0191 · candidate C-0071

## §2.2

<!-- q L650-652 -->
> When signing data structures, a log MUST use one of the signature algorithms from the IANA "Signature Algorithms" registry, described in Section 10.2.2.

R-0001

## §3

<!-- q L658-661 "In order" .. "5.7)." -->
> In order to enable attribution of each logged certificate or precertificate to its issuer, each submission MUST be accompanied by all additional certificates required to verify the chain up to an accepted trust anchor (Section 5.7).

R-0002

<!-- q L661-663 "The trust" .. "submission." -->
> The trust anchor (a root or intermediate CA certificate) MAY be omitted from the submission.

R-0003

<!-- q L666-669 "The submitter" .. "certificate." -->
> The submitter SHOULD validate the returned SCT, as described in Section 8.1, if they understand its format and they intend to use it directly in a TLS handshake or to construct a certificate.

R-0004

<!-- q L669-671 "If the submitter" .. "SCT." -->
> If the submitter does not need the SCT (for example, the certificate is being submitted simply to make it available in the log), it MAY validate the SCT.

R-0005

## §3.1

<!-- q L675-675 "Any entity" .. "log." -->
> Any entity can submit a certificate (Section 5.1) to a log.

R-0192 · no candidate (hunted)

## §3.2

<!-- q L684-685 "The CA MAY" .. "certificate." -->
> The CA MAY incorporate the returned SCT in the issued certificate.

R-0006

<!-- q L690-691 -->
> A precertificate is a CMS [RFC5652] signed-data object that conforms to the following profile:

R-0193 · no candidate (hunted)

<!-- q L693-693 -->
> * It MUST be DER encoded, as described in [X690].

R-0007

<!-- q L695-695 -->
> * SignedData.version MUST be v3(3).

R-0008

<!-- q L697-698 -->
> * SignedData.digestAlgorithms MUST be the same as the SignerInfo.digestAlgorithm OID value (see below).

R-0009

<!-- q L702-702 -->
> - eContentType MUST be the OID 1.3.101.78.

R-0010

<!-- q L704-707 -->
> - eContent MUST contain a TBSCertificate [RFC5280] that will be identical to the TBSCertificate in the issued certificate, except that the Transparency Information (Section 7.1) extension MUST be omitted.

R-0011 · split: R-0194, R-0195

<!-- q L709-709 -->
> * SignedData.certificates MUST be omitted.

R-0012

<!-- q L711-711 -->
> * SignedData.crls MUST be omitted.

R-0013

<!-- q L713-713 -->
> * SignedData.signerInfos MUST contain one SignerInfo:

R-0014

<!-- q L715-715 -->
> - version MUST be v3(3).

R-0015

<!-- q L717-717 -->
> - sid MUST use the subjectKeyIdentifier option.

R-0016

<!-- q L719-721 -->
> - digestAlgorithm MUST be one of the hash algorithm OIDs listed in the IANA "Hash Algorithms" registry, described in Section 10.2.1.

R-0017

<!-- q L723-723 -->
> - signedAttrs MUST be present and MUST contain two attributes:

R-0018 · split: R-0196, R-0197

<!-- q L725-726 -->
> o a content-type attribute whose value is the same as SignedData.encapContentInfo.eContentType and

R-0198 · candidate C-0079

<!-- q L728-729 -->
> o a message-digest attribute whose value is the message digest of SignedData.encapContentInfo.eContent.

R-0199 · candidate C-0080

<!-- q L731-732 -->
> - signatureAlgorithm MUST be the same OID as TBSCertificate.signature.

R-0019

<!-- q L734-736 -->
> - signature MUST be from the same (root or intermediate) CA that intends to issue the corresponding certificate (see Section 3.2.1).

R-0020

<!-- q L738-738 -->
> - unsignedAttrs MUST be omitted.

R-0021

## §3.2.1

<!-- q L753-755 "Nevertheless," .. "that:" -->
> Nevertheless, a precertificate's signature indicates the CA's binding intent to issue the corresponding certificate, which means that:

R-0200 · no candidate (hunted)

<!-- q L757-758 "* Misissuance" .. "certificate." -->
> * Misissuance of a precertificate is considered equivalent to misissuance of the corresponding certificate.

R-0201 · candidate C-0082

<!-- q L762-763 "* Upon observing" .. "issued." -->
> * Upon observing a precertificate, a client can reasonably presume that the corresponding certificate has been issued.

R-0202 · candidate C-0084

## §4

<!-- q L777-778 -->
> A log is a single, append-only Merkle Tree of submitted certificate and precertificate entries.

R-0203 · candidate C-0087

<!-- q L780-782 "When it receives" .. "precertificate." -->
> When it receives and accepts a valid submission, the log MUST return an SCT that corresponds to the submitted certificate or precertificate.

R-0022

<!-- q L782-786 "If the log" .. "structure)." -->
> If the log has previously seen this valid submission, it SHOULD return the same SCT as it returned before, as discussed in Section 11.3. If different SCTs are produced for the same submission, multiple log entries will have to be created, one for each SCT (as the timestamp is a part of the leaf structure).

R-0023 · split: R-0204, R-0205

<!-- q L787-790 -->
> Note that if a certificate was previously logged as a precertificate, then the precertificate's SCT of type precert_sct_v2 would not be appropriate; instead, a fresh SCT of type x509_sct_v2 should be generated.

R-0206 · candidate C-0088

<!-- q L792-793 "An SCT is" .. "submission." -->
> An SCT is the log's promise to append to its Merkle Tree an entry for the accepted submission.

R-0207 · no candidate (hunted)

<!-- q L793-796 "Upon producing" .. "4.1):" -->
> Upon producing an SCT, the log MUST fulfill this promise by performing the following actions within a fixed amount of time known as the Maximum Merge Delay (MMD), which is one of the log's parameters (see Section 4.1):

R-0024

<!-- q L798-799 -->
> * Allocate a tree index to the entry representing the accepted submission.

R-0208 · candidate C-0089

<!-- q L801-801 -->
> * Calculate the root of the tree.

R-0209 · candidate C-0090

<!-- q L803-803 -->
> * Sign the root of the tree (see Section 4.10).

R-0210 · candidate C-0091

<!-- q L805-806 -->
> The log may append multiple entries before signing the root of the tree.

R-0211 · candidate C-0092

<!-- q L808-809 -->
> Log operators SHOULD NOT impose any conditions on retrieving or sharing data from the log.

R-0025

## §4.1

<!-- q L813-815 "A log is" .. "artifacts." -->
> A log is defined by a collection of immutable parameters, which are used by clients to communicate with the log and to verify log artifacts.

R-0212 · candidate C-0093

<!-- q L815-816 "Except for" .. "log." -->
> Except for the Final STH, each of these parameters MUST be established before the log operator begins to operate the log.

R-0026

<!-- q L818-819 "Base URL:" .. "Section 5)." -->
> Base URL: The prefix used to construct URLs [RFC3986] for client messages (see Section 5).

R-0213 · no candidate (hunted)

<!-- q L819-822 "The base" .. "https://ct.example.org/blue." -->
> The base URL MUST be an "https" URL, MAY contain a port, and MAY contain a path with any number of path segments but MUST NOT contain a query string, fragment, or trailing "/". Example: https://ct.example.org/blue.

R-0027 · split: R-0214, R-0215, R-0216, R-0217 · the quote runs on past the entry text (its text ends in a double quote, which a marker anchor cannot hold)

<!-- q L824-825 -->
> Hash Algorithm: The hash algorithm used for the Merkle Tree (see Section 10.2.1).

R-0218 · no candidate (hunted)

<!-- q L827-827 -->
> Signature Algorithm: The signature algorithm used (see Section 2.2).

R-0219 · no candidate (hunted)

<!-- q L829-830 "Public Key:" .. "log." -->
> Public Key: The public key used to verify signatures generated by the log.

R-0220 · no candidate (hunted)

<!-- q L830-830 "A log MUST" .. "log." -->
> A log MUST NOT use the same keypair as any other log.

R-0028

<!-- q L832-832 -->
> Log ID: The OID that uniquely identifies the log.

R-0221 · no candidate (hunted)

<!-- q L834-834 "Maximum Merge" .. "committed to." -->
> Maximum Merge Delay: The MMD the log has committed to.

R-0222 · no candidate (hunted)

<!-- q L838-839 -->
> Version: The version of the protocol supported by the log (currently 1 or 2).

R-0223 · no candidate (hunted)

<!-- q L841-842 -->
> Maximum Chain Length: The longest certificate chain submission the log is willing to accept, if the log imposes any limit.

R-0224 · no candidate (hunted)

<!-- q L844-845 -->
> STH Frequency Count: The maximum number of STHs the log may produce in any period equal to the Maximum Merge Delay (see Section 4.10).

R-0225 · candidate C-0095

<!-- q L848-850 "In this case," .. "detection." -->
> In this case, the client should know the final valid STH in the log to ensure no new entries can be added without detection.

R-0226 · candidate C-0097

<!-- q L850-851 "This value" .. "signed_tree_head_v2." -->
> This value MUST be provided in the form of a TransItem of type signed_tree_head_v2.

R-0029

<!-- q L852-853 -->
> If a log is still accepting entries, this value should not be provided.

R-0227 · candidate C-0098

## §4.2

<!-- q L865-866 "If the acceptance" .. "submission." -->
> If the acceptance criteria are met, the log SHOULD accept the submission.

R-0030

<!-- q L866-868 "(A log may" .. "attacks.)" -->
> (A log may decide, for example, to temporarily reject acceptable submissions to protect itself against denial-of-service attacks.)

R-0228 · candidate C-0100

<!-- q L870-872 "The log SHALL" .. "certificate." -->
> The log SHALL allow retrieval of its list of accepted trust anchors (see Section 5.7), each of which is a root or intermediate CA certificate.

R-0031

## §4.2.1

<!-- q L877-881 -->
> To ensure that logged certificates and precertificates are attributable to an accepted trust anchor, to set clear expectations for what monitors would find in the log, and to avoid being overloaded by invalid submissions, the log MUST reject a submission if any of the following conditions are not met:

R-0032

<!-- q L883-886 -->
> * The submission, type, and chain inputs MUST be set as described in Section 5.1. The log MUST NOT accommodate misordered CA certificates or use any other source of intermediate CA certificates to attempt certification path construction.

R-0033 · split: R-0229, R-0230

<!-- q L888-889 -->
> * Each of the zero or more intermediate CA certificates in the chain MUST have one or both of the following features:

R-0034

<!-- q L891-891 -->
> - The Basic Constraints extension with the cA boolean asserted.

R-0231 · candidate C-0101

<!-- q L893-893 -->
> - The Key Usage extension with the keyCertSign bit asserted.

R-0232 · candidate C-0102

<!-- q L895-897 -->
> * Each certificate in the chain MUST fall within the limits imposed by the zero or more Basic Constraints pathLenConstraint values found higher up the chain.

R-0035

<!-- q L899-900 -->
> * Precertificate submissions MUST conform to all of the requirements in Section 3.2.

R-0036

## §4.2.2

<!-- q L904-909 "If the minimum" .. "discretion." -->
> If the minimum acceptance criteria are met but the submission is not fully valid according to [RFC5280] verification rules (e.g., the certificate or precertificate has expired, is not yet valid, has been revoked, exhibits ASN.1 DER encoding errors but the log can still parse it, etc.), then the acceptability of the submission is left to the log's discretion.

R-0233 · no candidate (hunted)

<!-- q L917-917 "Logs SHOULD" .. "accept." -->
> Logs SHOULD limit the length of chain they will accept.

R-0037

## §4.3

<!-- q L922-923 "If a submission" .. "verification." -->
> If a submission is accepted and an SCT is issued, the accepting log MUST store the entire chain used for verification.

R-0038

<!-- q L923-927 "This chain" .. "submission)." -->
> This chain MUST include the certificate or precertificate itself, the zero or more intermediate CA certificates provided by the submitter, and the trust anchor used to verify the chain (even if it was omitted from the submission).

R-0039

<!-- q L927-929 "The log MUST" .. "chain." -->
> The log MUST provide this chain for auditing upon request (see Section 5.6) so that the CA cannot avoid blame by logging a partial or empty chain.

R-0040

<!-- q L929-930 "Each log" .. "precert_entry_v2." -->
> Each log entry is a TransItem structure of type x509_entry_v2 or precert_entry_v2.

R-0234 · no candidate (hunted)

<!-- q L930-931 "However," .. "format." -->
> However, a log may store its entries in any format.

R-0235 · candidate C-0104

<!-- q L931-933 "If a log" .. "structure." -->
> If a log does not store this TransItem in full, it must store the timestamp and sct_extensions of the corresponding TimestampedCertificateEntryDataV2 structure.

R-0236 · candidate C-0105

## §4.4

<!-- q L939-941 "Each log" .. "log." -->
> Each log is identified by an OID, which is one of the log's parameters (see Section 4.1) and which MUST NOT be used to identify any other log.

R-0041

<!-- q L941-943 "A log's operator" .. "10.2.5)." -->
> A log's operator MUST either allocate the OID themselves or request an OID from the Log ID registry (see Section 10.2.5).

R-0042

<!-- q L950-953 "Various data" .. "LogID<2..127>;" -->
> Various data structures include the DER encoding of this OID, excluding the ASN.1 tag and length bytes, in an opaque vector: opaque LogID<2..127>;

R-0237 · no candidate (hunted)

<!-- q L955-959 -->
> Note that the ASN.1 length and the opaque vector length are identical in size (1 byte) and value, so the full DER encoding (including the tag and length) of the OID can be reproduced simply by prepending an OBJECT IDENTIFIER tag (0x06) to the opaque vector length and contents.

R-0238 · candidate C-0110

<!-- q L961-963 -->
> The OID used to identify a log is limited such that the DER encoding of its value, excluding the tag and length, MUST be no longer than 127 octets.

R-0043

## §4.5

<!-- q L971-995 -->
> enum { x509_entry_v2(0x0100), precert_entry_v2(0x0101), x509_sct_v2(0x0102), precert_sct_v2(0x0103), signed_tree_head_v2(0x0104), consistency_proof_v2(0x0105), inclusion_proof_v2(0x0106), /* Reserved Code Points */ reserved_rfc6962(0x0000..0x00FF), reserved_experimentaluse(0xE000..0xEFFF), reserved_privateuse(0xF000..0xFFFF), (0xFFFF) } VersionedTransType; struct { VersionedTransType versioned_type; select (versioned_type) { case x509_entry_v2: TimestampedCertificateEntryDataV2; case precert_entry_v2: TimestampedCertificateEntryDataV2; case x509_sct_v2: SignedCertificateTimestampDataV2; case precert_sct_v2: SignedCertificateTimestampDataV2; case signed_tree_head_v2: SignedTreeHeadDataV2; case consistency_proof_v2: ConsistencyProofDataV2; case inclusion_proof_v2: InclusionProofDataV2; } data; } TransItem;

R-0239 · no candidate (hunted)

<!-- q L997-1000 -->
> versioned_type is a value from the IANA registry in Section 10.2.3 that identifies the type of the encapsulated data structure and the earliest version of this protocol to which it conforms. This document is v2.

R-0240 · no candidate (hunted)

<!-- q L1002-1002 "data is the" .. "structure." -->
> data is the encapsulated data structure.

R-0241 · no candidate (hunted)

<!-- q L1012-1015 -->
> Future versions of this protocol may reuse VersionedTransType values defined in this document as long as the corresponding data structures are not modified and may add new VersionedTransType values for new or modified data structures.

R-0242 · candidate C-0113

## §4.6

<!-- q L1019-1026 -->
> enum { reserved(65535) } ExtensionType; struct { ExtensionType extension_type; opaque extension_data<0..2^16-1>; } Extension;

R-0243 · no candidate (hunted)

<!-- q L1029-1031 "The interpretation" .. "field." -->
> The interpretation of the extension_data field is determined solely by the value of the extension_type field.

R-0244 · no candidate (hunted)

<!-- q L1034-1037 "Each document" .. "extension_data." -->
> Each document that registers a new ExtensionType must specify the context in which it may be used (e.g., SCT, STH, or both) and describe how to interpret the corresponding extension_data.

R-0245 · candidate C-0115

## §4.7

<!-- q L1042-1044 "Each leaf" .. "structure." -->
> Each leaf is the leaf hash (Section 2.1) of a TransItem structure of type x509_entry_v2 or precert_entry_v2, which encapsulates a TimestampedCertificateEntryDataV2 structure.

R-0246 · no candidate (hunted)

<!-- q L1044-1046 "Note that" .. "parameters." -->
> Note that leaf hashes are calculated as HASH(0x00 || TransItem), where the hash algorithm is one of the log's parameters.

R-0247 · no candidate (hunted)

<!-- q L1048-1055 -->
> opaque TBSCertificate<1..2^24-1>; struct { uint64 timestamp; opaque issuer_key_hash<32..2^8-1>; TBSCertificate tbs_certificate; Extension sct_extensions<0..2^16-1>; } TimestampedCertificateEntryDataV2;

R-0248 · no candidate (hunted)

<!-- q L1057-1061 "timestamp" .. "order." -->
> timestamp is the date and time at which the certificate or precertificate was accepted by the log, in the form of a 64-bit unsigned number of milliseconds elapsed since the Unix Epoch (1 January 1970 00:00:00 UTC -- see [UNIXTIME]), ignoring leap seconds, in network byte order.

R-0249 · no candidate (hunted)

<!-- q L1061-1062 "Note that" .. "order." -->
> Note that the leaves of a log's Merkle Tree are not required to be in strict chronological order.

R-0250 · candidate C-0116

<!-- q L1064-1066 "issuer_key_hash" .. "[RFC5280]." -->
> issuer_key_hash is the HASH of the public key of the CA that issued the certificate or precertificate, calculated over the DER encoding of the key represented as SubjectPublicKeyInfo [RFC5280].

R-0251 · no candidate (hunted)

<!-- q L1070-1071 "The length" .. "HASH_SIZE." -->
> The length of the issuer_key_hash MUST match HASH_SIZE.

R-0044

<!-- q L1073-1074 "tbs_certificate" .. "submission." -->
> tbs_certificate is the DER-encoded TBSCertificate from the submission.

R-0252 · no candidate (hunted)

<!-- q L1078-1079 -->
> sct_extensions is byte-for-byte identical to the SCT extensions of the corresponding SCT.

R-0253 · no candidate (hunted)

<!-- q L1081-1082 -->
> The type of the TransItem corresponds to the value of the type parameter supplied in the Section 5.1 call.

R-0254 · no candidate (hunted)

## §4.8

<!-- q L1086-1088 -->
> An SCT is a TransItem structure of type x509_sct_v2 or precert_sct_v2, which encapsulates a SignedCertificateTimestampDataV2 structure:

R-0255 · no candidate (hunted)

<!-- q L1090-1095 -->
> struct { LogID log_id; uint64 timestamp; Extension sct_extensions<0..2^16-1>; opaque signature<1..2^16-1>; } SignedCertificateTimestampDataV2;

R-0256 · no candidate (hunted)

<!-- q L1097-1098 -->
> log_id is this log's unique ID, encoded in an opaque vector, as described in Section 4.4.

R-0257 · no candidate (hunted)

<!-- q L1100-1101 -->
> timestamp is equal to the timestamp from the corresponding TimestampedCertificateEntryDataV2 structure.

R-0258 · no candidate (hunted)

<!-- q L1103 "sct_extensions is a vector" .. "SCT extensions." -->
> sct_extensions is a vector of 0 or more SCT extensions.

R-0489 · no candidate (hunted, pass 2)

<!-- q L1103-1105 "This vector" .. "extension_type." -->
> This vector MUST NOT include more than one extension with the same extension_type.

R-0045

<!-- q L1105-1106 "The extensions" .. "first." -->
> The extensions in the vector MUST be ordered by the value of the extension_type field, smallest value first.

R-0046

<!-- q L1106-1109 "All SCT extensions" .. "understand." -->
> All SCT extensions are similar to noncritical X.509v3 extensions (i.e., the mustUnderstand field is not set), and a recipient SHOULD ignore any extension it does not understand.

R-0047

<!-- q L1109-1110 "Furthermore," .. "understand." -->
> Furthermore, an implementation MAY choose to ignore any extension(s) that it does understand.

R-0048

<!-- q L1112-1115 -->
> signature is computed over a TransItem structure of type x509_entry_v2 or precert_entry_v2 (see Section 4.7) using the signature algorithm declared in the log's parameters (see Section 4.1).

R-0259 · candidate C-0118

## §4.9

<!-- q L1121-1128 -->
> opaque NodeHash<32..2^8-1>; struct { uint64 timestamp; uint64 tree_size; NodeHash root_hash; Extension sth_extensions<0..2^16-1>; } TreeHeadDataV2;

R-0260 · no candidate (hunted)

<!-- q L1130-1130 -->
> The length of NodeHash MUST match HASH_SIZE of the log.

R-0049

<!-- q L1132-1133 -->
> timestamp is the current date and time, using the format defined in Section 4.7.

R-0261 · no candidate (hunted)

<!-- q L1135-1136 -->
> tree_size is the number of entries currently in the log's Merkle Tree.

R-0262 · no candidate (hunted)

<!-- q L1138-1138 -->
> root_hash is the root of the Merkle Tree.

R-0263 · no candidate (hunted)

<!-- q L1140 "sth_extensions is a vector" .. "STH extensions." -->
> sth_extensions is a vector of 0 or more STH extensions.

R-0490 · no candidate (hunted, pass 2)

<!-- q L1140-1142 "This vector" .. "extension_type." -->
> This vector MUST NOT include more than one extension with the same extension_type.

R-0050

<!-- q L1142-1143 "The extensions" .. "first." -->
> The extensions in the vector MUST be ordered by the value of the extension_type field, smallest value first.

R-0051

<!-- q L1143-1145 "If an implementation" .. "extension." -->
> If an implementation sees an extension that it does not understand, it SHOULD ignore that extension.

R-0052

<!-- q L1145-1146 "Furthermore," .. "understand." -->
> Furthermore, an implementation MAY choose to ignore any extension(s) that it does understand.

R-0053

## §4.10

<!-- q L1150-1151 "Periodically," .. "STH." -->
> Periodically, each log SHOULD sign its current tree head information (see Section 4.9) to produce an STH.

R-0054

<!-- q L1151-1153 "When a client" .. "MMD." -->
> When a client requests a log's latest STH (see Section 5.2), the log MUST return an STH that is no older than the log's MMD.

R-0055

<!-- q L1153-1156 "However," .. "4.1)." -->
> However, since STHs could be used to mark individual clients (by producing a new STH for each query), a log MUST NOT produce STHs more frequently than its parameters declare (see Section 4.1).

R-0056

<!-- q L1156-1159 "In general," .. "timestamp." -->
> In general, there is no need to produce a new STH unless there are new entries in the log; however, in the event that a log does not accept any submissions during an MMD period, the log MUST sign the same Merkle Tree Hash with a fresh timestamp.

R-0057

<!-- q L1161-1162 -->
> An STH is a TransItem structure of type signed_tree_head_v2, which encapsulates a SignedTreeHeadDataV2 structure:

R-0264 · no candidate (hunted)

<!-- q L1164-1168 -->
> struct { LogID log_id; TreeHeadDataV2 tree_head; opaque signature<1..2^16-1>; } SignedTreeHeadDataV2;

R-0265 · no candidate (hunted)

<!-- q L1170-1171 -->
> log_id is this log's unique ID encoded in an opaque vector, as described in Section 4.4.

R-0266 · no candidate (hunted)

<!-- q L1173-1174 "The timestamp" .. "tree." -->
> The timestamp in tree_head MUST be at least as recent as the most recent SCT timestamp in the tree.

R-0058

<!-- q L1174-1175 "Each subsequent" .. "update." -->
> Each subsequent timestamp MUST be more recent than the timestamp of the previous update.

R-0059

<!-- q L1177-1178 -->
> tree_head contains the latest tree head information (see Section 4.9).

R-0267 · candidate C-0119

<!-- q L1180-1181 -->
> signature is computed over the tree_head field using the signature algorithm declared in the log's parameters (see Section 4.1).

R-0268 · candidate C-0120

## §4.11

<!-- q L1185-1187 -->
> To prepare a Merkle consistency proof for distribution to clients, the log produces a TransItem structure of type consistency_proof_v2, which encapsulates a ConsistencyProofDataV2 structure:

R-0269 · no candidate (hunted)

<!-- q L1189-1194 -->
> struct { LogID log_id; uint64 tree_size_1; uint64 tree_size_2; NodeHash consistency_path<0..2^16-1>; } ConsistencyProofDataV2;

R-0270 · no candidate (hunted)

<!-- q L1196-1197 -->
> log_id is this log's unique ID encoded in an opaque vector, as described in Section 4.4.

R-0271 · no candidate (hunted)

<!-- q L1199-1199 -->
> tree_size_1 is the size of the older tree.

R-0272 · no candidate (hunted)

<!-- q L1201-1201 -->
> tree_size_2 is the size of the newer tree.

R-0273 · no candidate (hunted)

<!-- q L1203-1204 -->
> consistency_path is a vector of Merkle Tree nodes proving the consistency of two STHs, as described in Section 2.1.4.

R-0274 · no candidate (hunted)

## §4.12

<!-- q L1208-1210 -->
> To prepare a Merkle inclusion proof for distribution to clients, the log produces a TransItem structure of type inclusion_proof_v2, which encapsulates an InclusionProofDataV2 structure:

R-0275 · no candidate (hunted)

<!-- q L1212-1217 -->
> struct { LogID log_id; uint64 tree_size; uint64 leaf_index; NodeHash inclusion_path<0..2^16-1>; } InclusionProofDataV2;

R-0276 · no candidate (hunted)

<!-- q L1219-1220 -->
> log_id is this log's unique ID encoded in an opaque vector, as described in Section 4.4.

R-0277 · no candidate (hunted)

<!-- q L1222-1223 -->
> tree_size is the size of the tree on which this inclusion proof is based.

R-0278 · no candidate (hunted)

<!-- q L1225-1226 -->
> leaf_index is the 0-based index of the log entry corresponding to this inclusion proof.

R-0279 · no candidate (hunted)

<!-- q L1228-1230 -->
> inclusion_path is a vector of Merkle Tree nodes proving the inclusion of the chosen certificate or precertificate, as described in Section 2.1.3.

R-0280 · no candidate (hunted)

## §4.13

<!-- q L1238-1239 "In order" .. "taken:" -->
> In order to avoid that, the following actions SHOULD be taken:

R-0060

<!-- q L1241-1241 -->
> * Make it known to clients and monitors that the log will be frozen.

R-0281 · candidate C-0122

<!-- q L1245-1246 -->
> * Stop accepting new submissions (the error code "shutdown" should be returned for such requests).

R-0282 · candidate C-0124

<!-- q L1248-1250 "* Once MMD" .. "parameters." -->
> * Once MMD from the last accepted submission has passed and all pending submissions are incorporated, issue a final STH and publish it as one of the log's parameters.

R-0283 · candidate C-0125

<!-- q L1253-1254 "At this point," .. "destroyed." -->
> At this point, the log's private key is no longer needed and can be destroyed.

R-0284 · candidate C-0127

<!-- q L1256-1259 -->
> * Keep the log running until the certificates in all of its entries have expired or exist in other logs (this can be determined by scanning other logs or connecting to domains mentioned in the certificates and inspecting the SCTs served).

R-0285 · candidate C-0128

## §5

<!-- q L1263-1263 "Messages" .. "requests." -->
> Messages are sent as HTTPS GET or POST requests.

R-0286 · no candidate (hunted)

<!-- q L1263-1265 "Parameters" .. "[RFC8259]." -->
> Parameters for POSTs and all responses are encoded as JavaScript Object Notation (JSON) objects [RFC8259].

R-0287 · no candidate (hunted)

<!-- q L1265-1268 "Parameters" .. "[HTML401]." -->
> Parameters for GETs are encoded as order-independent key/value URL parameters, using the "application/x-www-form-urlencoded" format described in the "HTML 4.01 Specification" [HTML401].

R-0288 · no candidate (hunted)

<!-- q L1268-1269 "Binary data" .. "messages." -->
> Binary data is base64 encoded according to Section 4 of [RFC4648], as specified in the individual messages.

R-0289 · no candidate (hunted)

<!-- q L1272-1273 "Clients construct" .. "URL." -->
> Clients construct URLs for requests by appending suffixes to this base URL.

R-0290 · no candidate (hunted)

<!-- q L1279-1280 "Note that" .. "experimentation." -->
> Note that JSON objects and URL parameters may contain fields not specified here to allow for experimentation.

R-0291 · candidate C-0129

<!-- q L1280-1281 "Any fields" .. "ignored." -->
> Any fields that are not understood SHOULD be ignored.

R-0061

<!-- q L1288-1291 "Front ends" .. "STH)." -->
> Front ends MUST only serve data that is free of gaps (that is, for example, no front end will respond with an STH unless it is also able to prove consistency from all log entries logged within that STH).

R-0062

<!-- q L1302-1305 -->
> If the log is unable to process a client's request, it MUST return an HTTP response code of 4xx/5xx (see [RFC7231]), and, in place of the responses outlined in the subsections below, the body SHOULD be a JSON problem details object (see Section 3 of [RFC7807]) containing:

R-0063 · split: R-0292, R-0293

<!-- q L1307-1307 "type: A URN" .. "problem." -->
> type: A URN reference identifying the problem.

R-0294 · no candidate (hunted)

<!-- q L1307-1310 -->
> type: A URN reference identifying the problem. To facilitate automated response to errors, this document defines a set of standard tokens for use in the type field within the URN namespace of: "urn:ietf:params:trans:error:".

R-0295 · candidate C-0134 · the quote runs on past the entry text (its text ends in a double quote, which a marker anchor cannot hold)

<!-- q L1312-1314 -->
> detail: A human-readable string describing the error that prevented the log from processing the request, ideally with sufficient detail to enable the error to be rectified.

R-0296 · candidate C-0135

<!-- q L1326-1329 "The one exception" .. "document:" -->
> The one exception is the "malformed" error type, which indicates that the log server could not parse the client's request because it did not comply with this document:

R-0297 · candidate C-0138

<!-- q L1331-1335 -->
> +===========+==================================+ | type | detail | +===========+==================================+ | malformed | The request could not be parsed. | +-----------+----------------------------------+

R-0298 · no candidate (hunted)

<!-- q L1339-1341 "Clients SHOULD" .. "date." -->
> Clients SHOULD treat 500 Internal Server Error and 503 Service Unavailable responses as transient failures and MAY retry the same request without modification at a later date.

R-0064 · split: R-0299, R-0300

<!-- q L1341-1344 "Note that" .. "request." -->
> Note that in the case of a 503 response, the log MAY include a Retry-After header field per [RFC7231] in order to request a minimum time for the client to wait before retrying the request.

R-0065

<!-- q L1347-1348 -->
> Clients SHOULD treat any 4xx error as a problem with the request and not attempt to resubmit without some modification to the request.

R-0066

<!-- q L1349-1349 -->
> The full status code MAY provide additional details.

R-0067

## §5.1

<!-- q L1356-1356 -->
> POST <Base URL>/ct/v2/submit-entry

R-0301 · no candidate (hunted)

<!-- q L1359-1359 -->
> submission: The base64-encoded certificate or precertificate.

R-0302 · no candidate (hunted)

<!-- q L1361-1363 -->
> type: The VersionedTransType integer value that indicates the type of the submission: 1 for x509_entry_v2 or 2 for precert_entry_v2.

R-0303 · no candidate (hunted)

<!-- q L1365-1370 -->
> chain: An array of zero or more JSON strings, each of which is a base64-encoded CA certificate. The first element is the certifier of the submission, the second certifies the first, etc. The last element of chain (or, if chain is an empty array, the submission) is certified by an accepted trust anchor.

R-0304 · no candidate (hunted)

<!-- q L1373-1375 -->
> sct: A base64-encoded TransItem of type x509_sct_v2 or precert_sct_v2, signed by this log, that corresponds to the submission.

R-0305 · no candidate (hunted)

<!-- q L1377-1378 -->
> If the submitted entry is immediately appended to (or already exists in) this log's tree, then the log SHOULD also output:

R-0068

<!-- q L1380-1381 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2 signed by this log.

R-0306 · no candidate (hunted)

<!-- q L1383-1385 -->
> inclusion: A base64-encoded TransItem of type inclusion_proof_v2 whose inclusion_path array of Merkle Tree nodes proves the inclusion of the submission in the returned sth.

R-0307 · no candidate (hunted)

<!-- q L1389-1409 -->
> +================+===============================================+ | type | detail | +================+===============================================+ | badSubmission | submission is neither a valid certificate nor | | a valid precertificate. | +----------------+-----------------------------------------------+ | badType | type is neither 1 nor 2. | +----------------+-----------------------------------------------+ | badChain | The first element of chain is not the | | certifier of the submission, or the second | | element does not certify the first, etc. | +----------------+-----------------------------------------------+ | badCertificate | One or more certificates in chain are not | | valid (e.g., not properly encoded). | +----------------+-----------------------------------------------+ | unknownAnchor | The last element of chain (or, if chain is an | | empty array, the submission) is not, nor is | | it certified by, an accepted trust anchor. | +----------------+-----------------------------------------------+ | shutdown | The log is no longer accepting submissions. | +----------------+-----------------------------------------------+

R-0308 · candidate C-0142

<!-- q L1414-1414 "It MUST NOT" .. "error." -->
> It MUST NOT construe this as an error.

R-0069

<!-- q L1418-1420 "If a log" .. "error." -->
> If a log detects bad encoding in a chain that otherwise verifies correctly, then the log MUST either log the certificate or return the "badCertificate" error.

R-0070

<!-- q L1420-1421 "If the certificate" .. "issued." -->
> If the certificate is logged, an SCT MUST be issued.

R-0071

<!-- q L1425-1427 "If submission" .. "error." -->
> If submission is an accepted trust anchor whose certifier is neither an accepted trust anchor nor the first element of chain, then the log MUST return the "unknownAnchor" error.

R-0072

<!-- q L1431-1433 "If the returned" .. "clients." -->
> If the returned sct is intended to be provided to TLS clients, then sth and inclusion (if returned) SHOULD also be provided to TLS clients.

R-0073

## §5.2

<!-- q L1438-1438 -->
> GET <Base URL>/ct/v2/get-sth

R-0309 · no candidate (hunted)

<!-- q L1440-1440 -->
> No inputs.

R-0310 · no candidate (hunted)

<!-- q L1443-1444 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2 signed by this log that is no older than the log's MMD.

R-0311 · no candidate (hunted)

## §5.3

<!-- q L1448-1448 -->
> GET <Base URL>/ct/v2/get-sth-consistency

R-0312 · no candidate (hunted)

<!-- q L1451-1451 -->
> first: The tree_size of the older tree, in decimal.

R-0313 · no candidate (hunted)

<!-- q L1453-1453 -->
> second: The tree_size of the newer tree, in decimal (optional).

R-0314 · candidate C-0147

<!-- q L1455-1455 "Both tree" .. "STHs." -->
> Both tree sizes must be from existing v2 STHs.

R-0315 · candidate C-0148

<!-- q L1457-1458 "If both are" .. "returned." -->
> If both are known, then only the consistency output is returned.

R-0316 · candidate C-0150

<!-- q L1458-1461 "If the first" .. "latest." -->
> If the first is known but the second is not (or has been omitted), then the latest known STH is returned, along with a consistency proof between the first STH and the latest.

R-0317 · no candidate (hunted)

<!-- q L1461-1462 "If neither" .. "proof." -->
> If neither are known, then the latest known STH is returned without a consistency proof.

R-0318 · no candidate (hunted)

<!-- q L1464-1467 "Outputs:" .. "input." -->
> Outputs: consistency: A base64-encoded TransItem of type consistency_proof_v2 whose tree_size_1 MUST match the first input.

R-0074

<!-- q L1467-1468 "If the sth" .. "input." -->
> If the sth output is omitted, then tree_size_2 MUST match the second input.

R-0075

<!-- q L1468-1470 "If first" .. "elements)." -->
> If first and second are equal and correspond to a known STH, the returned consistency proof MUST be empty (a consistency_path array with zero elements).

R-0076

<!-- q L1472-1473 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2, signed by this log.

R-0319 · no candidate (hunted)

<!-- q L1480-1490 -->
> +===================+======================================+ | type | detail | +===================+======================================+ | firstUnknown | first is before the latest known STH | | but is not from an existing STH. | +-------------------+--------------------------------------+ | secondUnknown | second is before the latest known | | STH but is not from an existing STH. | +-------------------+--------------------------------------+ | secondBeforeFirst | second is smaller than first. | +-------------------+--------------------------------------+

R-0320 · no candidate (hunted)

## §5.4

<!-- q L1499-1499 -->
> GET <Base URL>/ct/v2/get-proof-by-hash

R-0321 · no candidate (hunted)

<!-- q L1502-1502 -->
> hash: A base64-encoded v2 leaf hash.

R-0322 · no candidate (hunted)

<!-- q L1504-1505 -->
> tree_size: The tree_size of the tree on which to base the proof, in decimal.

R-0323 · no candidate (hunted)

<!-- q L1507-1508 "The hash" .. "tree_size." -->
> The hash must be calculated as defined in Section 4.7. A v2 STH must exist for the tree_size.

R-0325 · candidate C-0153 · split: R-0324, R-0326

<!-- q L1509-1511 "In that case," .. "STH." -->
> In that case, it will return the latest STH it knows, along with an inclusion proof to that STH.

R-0327 · no candidate (hunted)

<!-- q L1511-1512 "If the front" .. "returned." -->
> If the front end knows the requested tree head, then only inclusion is returned.

R-0328 · candidate C-0155

<!-- q L1515-1518 -->
> inclusion: A base64-encoded TransItem of type inclusion_proof_v2 whose inclusion_path array of Merkle Tree nodes proves the inclusion of the certificate (as specified by the hash parameter) in the selected STH.

R-0329 · no candidate (hunted)

<!-- q L1520-1521 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2, signed by this log.

R-0330 · no candidate (hunted)

<!-- q L1528-1537 -->
> +=================+=====================================+ | type | detail | +=================+=====================================+ | hashUnknown | hash is not the hash of a known | | leaf (may be caused by skew or by a | | known certificate not yet merged). | +-----------------+-------------------------------------+ | treeSizeUnknown | hash is before the latest known STH | | but is not from an existing STH. | +-----------------+-------------------------------------+

R-0331 · candidate C-0158

## §5.5

<!-- q L1547-1547 -->
> GET <Base URL>/ct/v2/get-all-by-hash

R-0332 · no candidate (hunted)

<!-- q L1550-1550 -->
> hash: A base64-encoded v2 leaf hash.

R-0333 · no candidate (hunted)

<!-- q L1552-1553 -->
> tree_size: The tree_size of the tree on which to base the proofs, in decimal.

R-0334 · no candidate (hunted)

<!-- q L1555-1556 -->
> The hash must be calculated as defined in Section 4.7. A v2 STH must exist for the tree_size.

R-0336 · candidate C-0159 · split: R-0335, R-0337

<!-- q L1561-1573 -->
> +=====================+=====================================+ | Case | Response | +=====================+=====================================+ | latest STH < | Return latest STH. | | requested tree head | | +---------------------+-------------------------------------+ | latest STH > | Return latest STH and a consistency | | requested tree head | proof between it and the requested | | tree head (see Section 5.3). | +---------------------+-------------------------------------+ | index of requested | Return inclusion. | | hash < latest STH | | +---------------------+-------------------------------------+

R-0338 · no candidate (hunted)

<!-- q L1577-1578 "Note that" .. "union." -->
> Note that more than one case can be true; in which case, the returned data is their union.

R-0339 · candidate C-0161

<!-- q L1578-1579 "It is also" .. "response." -->
> It is also possible for none to be true; in which case, the front end MUST return an empty response.

R-0077

<!-- q L1582-1585 -->
> inclusion: A base64-encoded TransItem of type inclusion_proof_v2 whose inclusion_path array of Merkle Tree nodes proves the inclusion of the certificate (as specified by the hash parameter) in the selected STH.

R-0340 · no candidate (hunted)

<!-- q L1587-1588 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2, signed by this log.

R-0341 · no candidate (hunted)

<!-- q L1590-1592 -->
> consistency: A base64-encoded TransItem of type consistency_proof_v2 that proves the consistency of the requested tree head and the returned STH.

R-0342 · no candidate (hunted)

<!-- q L1598-1598 -->
> Errors are the same as in Section 5.4.

R-0343 · no candidate (hunted)

## §5.6

<!-- q L1606-1606 -->
> GET <Base URL>/ct/v2/get-entries

R-0344 · no candidate (hunted)

<!-- q L1609-1609 -->
> start: 0-based index of first entry to retrieve, in decimal.

R-0345 · no candidate (hunted)

<!-- q L1611-1611 -->
> end: 0-based index of last entry to retrieve, in decimal.

R-0346 · no candidate (hunted)

<!-- q L1614-1614 -->
> entries: An array of objects, each consisting of:

R-0347 · no candidate (hunted)

<!-- q L1616-1617 -->
> log_entry: The base64-encoded TransItem structure of type x509_entry_v2 or precert_entry_v2 (see Section 4.3).

R-0348 · no candidate (hunted)

<!-- q L1619-1622 -->
> submitted_entry: JSON object equivalent to inputs that were submitted to submit-entry, with the addition of the trust anchor to the chain field if the submission did not include it.

R-0349 · no candidate (hunted)

<!-- q L1624-1625 -->
> sct: The base64-encoded TransItem of type x509_sct_v2 or precert_sct_v2, corresponding to this log entry.

R-0350 · no candidate (hunted)

<!-- q L1627-1628 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2, signed by this log.

R-0351 · no candidate (hunted)

<!-- q L1632-1632 "All leaves" .. "be v2." -->
> All leaves MUST be v2.

R-0078

<!-- q L1632-1633 "However," .. "error." -->
> However, a compliant v2 client MUST NOT construe an unrecognized TransItem type as an error.

R-0079

<!-- q L1634-1637 -->
> This means it may be unable to parse some entries, but note that each client can inspect the entries it does recognize as well as verify the integrity of the data by treating unrecognized leaves as opaque input to the tree.

R-0352 · candidate C-0164

<!-- q L1639-1640 -->
> The start and end parameters SHOULD be within the range 0 <= x < tree_size, as returned by get-sth in Section 5.2.

R-0080

<!-- q L1642-1642 -->
> The start parameter MUST be less than or equal to the end parameter.

R-0081

<!-- q L1644-1646 "Each submitted_entry" .. "5.1)." -->
> Each submitted_entry output parameter MUST include the trust anchor that the log used to verify the submission, even if that trust anchor was not provided to submit-entry (see Section 5.1).

R-0082

<!-- q L1646-1648 "If the submission" .. "submission." -->
> If the submission does not certify itself, then the first element of chain MUST be present and MUST certify the submission.

R-0083 · split: R-0353, R-0354

<!-- q L1650-1653 "Log servers" .. "skew." -->
> Log servers MUST honor requests where 0 <= start < tree_size and end >= tree_size by returning a partial response covering only the valid entries in the specified range. end >= tree_size could be caused by skew.

R-0084

<!-- q L1655-1656 "Logs MAY" .. "request." -->
> Logs MAY restrict the number of entries that can be retrieved per get-entries request.

R-0085

<!-- q L1656-1658 "If a client" .. "permissible." -->
> If a client requests more than the permitted number of entries, the log SHALL return the maximum number of entries permissible.

R-0086

<!-- q L1658-1659 "These entries" .. "start." -->
> These entries SHALL be sequential beginning with the entry specified by start.

R-0087

<!-- q L1659-1662 "Note that" .. "4.1." -->
> Note that a limit on the number of entries is not immutable, and therefore the restriction may be changed or lifted at any time and is not listed with the other Log Parameters in Section 4.1.

R-0355 · candidate C-0166

<!-- q L1665-1666 "In this case," .. "array." -->
> In this case, it MUST return an empty entries array.

R-0088

<!-- q L1668-1669 -->
> In any case, the log server MUST return the latest STH it knows about.

R-0089

<!-- q L1676-1684 -->
> +================+==================================+ | type | detail | +================+==================================+ | startUnknown | start is greater than the number | | of entries in the Merkle Tree. | +----------------+----------------------------------+ | endBeforeStart | start cannot be greater than | | end. | +----------------+----------------------------------+

R-0356 · candidate C-0168

## §5.7

<!-- q L1690-1690 -->
> GET <Base URL>/ct/v2/get-anchors

R-0357 · no candidate (hunted)

<!-- q L1692-1692 -->
> No inputs.

R-0358 · no candidate (hunted)

<!-- q L1695-1696 -->
> certificates: An array of JSON strings, each of which is a base64-encoded CA certificate that is acceptable to the log.

R-0359 · no candidate (hunted)

<!-- q L1698-1701 -->
> max_chain_length: If the server has chosen to limit the length of chains it accepts, this is the maximum number of certificates in the chain, in decimal. If there is no limit, this is omitted.

R-0360 · no candidate (hunted)

## §6

<!-- q L1708-1711 "CT-using" .. "certificate." -->
> CT-using TLS servers MUST use at least one of the mechanisms described below to present one or more SCTs from one or more logs to each TLS client during full TLS handshakes, when requested by the client, where each SCT corresponds to the server certificate.

R-0090

<!-- q L1713-1714 "Servers SHOULD" .. "STHs." -->
> Servers SHOULD also present corresponding inclusion proofs and STHs.

R-0091

<!-- q L1716-1717 "A server" .. "6.5)." -->
> A server can provide SCTs using a TLS 1.3 extension (Section 4.2 of [RFC8446]) with type transparency_info (see Section 6.5).

R-0361 · no candidate (hunted)

<!-- q L1722-1724 "The server" .. "handshake." -->
> The server may also use an Online Certificate Status Protocol (OCSP) [RFC6960] response extension (see Section 7.1.1), providing the OCSP response as part of the TLS handshake.

R-0362 · candidate C-0171

<!-- q L1725-1727 "For TLS 1.3," .. "[RFC8446]." -->
> For TLS 1.3, the information is encoded as an extension in the status_request extension data; see Section 4.4.2.1 of [RFC8446].

R-0363 · candidate C-0172

<!-- q L1727-1729 "For TLS 1.2" .. "[RFC6066]." -->
> For TLS 1.2 [RFC5246], the information is encoded in the CertificateStatus message; see Section 8 of [RFC6066].

R-0364 · candidate C-0173

<!-- q L1732-1733 "CT information" .. "7.1.2)." -->
> CT information can also be encoded as an extension in the X.509v3 certificate (see Section 7.1.2).

R-0365 · no candidate (hunted)

## §6.2

<!-- q L1760-1760 -->
> CT-using TLS servers SHOULD send SCTs from multiple logs because:

R-0092

## §6.3

<!-- q L1793-1794 -->
> Multiple SCTs, inclusion proofs, and indeed TransItem structures of any type are combined into a list as follows:

R-0366 · no candidate (hunted)

<!-- q L1796-1800 -->
> opaque SerializedTransItem<1..2^16-1>; struct { SerializedTransItem trans_item_list<1..2^16-1>; } TransItemList;

R-0367 · no candidate (hunted)

<!-- q L1802-1803 "Here, SerializedTransItem" .. "structure." -->
> Here, SerializedTransItem is an opaque byte string that contains the serialized TransItem structure.

R-0368 · candidate C-0188

## §6.4

<!-- q L1811-1813 -->
> In each TransItemList that is sent during a TLS handshake, the TLS server MUST include a TransItem structure of type x509_sct_v2 or precert_sct_v2.

R-0093

<!-- q L1817-1819 "Therefore," .. "TransItemList." -->
> Therefore, if the TLS server can obtain them, it SHOULD also include TransItems of type inclusion_proof_v2 and signed_tree_head_v2 in the TransItemList.

R-0094

## §6.5

<!-- q L1823-1825 -->
> Provided that a TLS client includes the transparency_info extension type in the ClientHello and the TLS server supports the transparency_info extension:

R-0369 · no candidate (hunted)

<!-- q L1827-1828 -->
> * The TLS server MUST verify that the received extension_data is empty.

R-0095

<!-- q L1830-1833 "* The TLS" .. "7.1)." -->
> * The TLS server MUST construct a TransItemList of relevant TransItems (see Section 6.4), which SHOULD omit any TransItems that are already embedded in the server certificate or the stapled OCSP response (see Section 7.1).

R-0096 · split: R-0370, R-0371

<!-- q L1833-1836 "If the constructed" .. "TransItemList." -->
> If the constructed TransItemList is not empty, then the TLS server MUST include the transparency_info extension with the extension_data set to this TransItemList.

R-0097

<!-- q L1836-1837 "If the list" .. "array." -->
> If the list is empty, then the server SHOULD omit the extension_data element but MAY send it with an empty array.

R-0098 · split: R-0372, R-0373

<!-- q L1839-1840 -->
> TLS servers MUST only include this extension in the following messages:

R-0099

<!-- q L1842-1842 -->
> * the ServerHello message (for TLS 1.2 or earlier)

R-0374 · candidate C-0190

<!-- q L1844-1844 -->
> * the Certificate or CertificateRequest message (for TLS 1.3)

R-0375 · candidate C-0191

<!-- q L1846-1848 -->
> TLS servers MUST NOT process or include this extension when a TLS session is resumed, since session resumption uses the original session information.

R-0100

## §7.1

<!-- q L1854-1856 "The Transparency" .. "TransItemList." -->
> The Transparency Information X.509v3 extension, which has OID 1.3.101.75 and SHOULD be noncritical, contains one or more TransItem structures in a TransItemList.

R-0101

<!-- q L1856-1858 "This extension" .. "7.1.2)." -->
> This extension MAY be included in OCSP responses (see Section 7.1.1) and certificates (see Section 7.1.2).

R-0102

<!-- q L1858-1860 "Since [RFC5280]" .. "directly." -->
> Since [RFC5280] requires the extnValue field (an OCTET STRING) of each X.509v3 extension to include the DER encoding of an ASN.1 value, a TransItemList MUST NOT be included directly.

R-0103

<!-- q L1861-1862 -->
> Instead, it MUST be wrapped inside an additional OCTET STRING, which is then put into the extnValue field:

R-0104

<!-- q L1864-1864 -->
> TransparencyInformationSyntax ::= OCTET STRING

R-0376 · no candidate (hunted)

<!-- q L1866-1866 -->
> TransparencyInformationSyntax contains a TransItemList.

R-0377 · candidate C-0192

## §7.1.1

<!-- q L1870-1872 "A certification" .. "response." -->
> A certification authority MAY include a Transparency Information X.509v3 extension in the singleExtensions of a SingleResponse in an OCSP response.

R-0105

<!-- q L1872-1874 "All included" .. "certificate." -->
> All included SCTs and inclusion proofs MUST be for the certificate identified by the certID of that SingleResponse or for a precertificate that corresponds to that certificate.

R-0106

## §7.1.2

<!-- q L1878-1879 "A certification" .. "certificate." -->
> A certification authority MAY include a Transparency Information X.509v3 extension in a certificate.

R-0107

<!-- q L1879-1881 "All included" .. "certificate." -->
> All included SCTs and inclusion proofs MUST be for a precertificate that corresponds to this certificate.

R-0108

## §7.2

<!-- q L1885-1889 -->
> A certification authority SHOULD NOT issue any certificate that identifies the transparency_info TLS extension in a TLS feature extension [RFC7633], because TLS servers are not required to support the transparency_info TLS extension in order to participate in CT (see Section 6).

R-0109

## §8.1.1

<!-- q L1910-1911 "CT-using" .. "Section 6)." -->
> CT-using TLS clients MUST implement all of the three mechanisms by which TLS servers may present SCTs (see Section 6).

R-0110

<!-- q L1913-1915 "TLS clients" .. "extension_data." -->
> TLS clients that support the transparency_info TLS extension (see Section 6.5) SHOULD include it in ClientHello messages, with empty extension_data.

R-0111

<!-- q L1915-1917 "If a TLS" .. "handshake." -->
> If a TLS server includes the transparency_info TLS extension when resuming a TLS session, the TLS client MUST abort the handshake.

R-0112

## §8.1.2

<!-- q L1921-1923 -->
> Validation of an SCT for a certificate (where the type of the TransItem is x509_sct_v2) uses the unmodified TBSCertificate component of the certificate.

R-0378 · no candidate (hunted)

<!-- q L1925-1928 -->
> Before an SCT for a precertificate (where the type of the TransItem is precert_sct_v2) can be validated, the TBSCertificate component of the precertificate needs to be reconstructed from the TBSCertificate component of the certificate as follows:

R-0379 · candidate C-0197

<!-- q L1930-1930 -->
> * Remove the Transparency Information extension (see Section 7.1).

R-0380 · candidate C-0198

<!-- q L1932-1933 "* Remove" .. "[RFC6962])." -->
> * Remove embedded v1 SCTs, identified by OID 1.3.6.1.4.1.11129.2.4.2 (see Section 3.3 of [RFC6962]).

R-0381 · candidate C-0199

## §8.1.3

<!-- q L1938-1939 -->
> In order to make use of a received SCT, the TLS client MUST first validate it as follows:

R-0113

<!-- q L1941-1943 "* Compute" .. "type." -->
> * Compute the signature input by constructing a TransItem of type x509_entry_v2 or precert_entry_v2, depending on the SCT's TransItem type.

R-0382 · candidate C-0201

<!-- q L1943-1944 "The TimestampedCertificateEntryDataV2" .. "manner:" -->
> The TimestampedCertificateEntryDataV2 structure is constructed in the following manner:

R-0383 · candidate C-0202

<!-- q L1946-1946 -->
> - timestamp is copied from the SCT.

R-0384 · candidate C-0203

<!-- q L1948-1949 -->
> - tbs_certificate is the reconstructed TBSCertificate portion of the server certificate, as described in Section 8.1.2.

R-0385 · candidate C-0204

<!-- q L1951-1951 -->
> - issuer_key_hash is computed as described in Section 4.7.

R-0386 · candidate C-0205

<!-- q L1953-1953 -->
> - sct_extensions is copied from the SCT.

R-0387 · candidate C-0206

<!-- q L1955-1957 "* Verify" .. "log_id." -->
> * Verify the SCT's signature against the computed signature input using the public key of the corresponding log, which is identified by the log_id.

R-0388 · candidate C-0207

<!-- q L1957-1958 "The required" .. "parameters." -->
> The required signature algorithm is one of the log's parameters.

R-0389 · candidate C-0208

<!-- q L1960-1961 "If the TLS" .. "SCT." -->
> If the TLS client does not have the corresponding log's parameters, it cannot attempt to validate the SCT.

R-0390 · candidate C-0209

<!-- q L1961-1963 "When evaluating" .. "validate." -->
> When evaluating compliance (see Section 8.1.6), the TLS client will consider only those SCTs that it was able to validate.

R-0391 · candidate C-0210

<!-- q L1965-1966 -->
> Note that SCT validation is not a substitute for the normal validation of the server certificate and its chain.

R-0392 · no candidate (hunted)

## §8.1.4

<!-- q L1970-1973 -->
> When a TLS client has validated a received SCT but does not yet possess a corresponding inclusion proof, the TLS client MAY request the inclusion proof directly from a log using get-proof-by-hash (Section 5.4) or get-all-by-hash (Section 5.5).

R-0114

## §8.1.5

<!-- q L1983-1985 "When a TLS" .. "STH." -->
> When a TLS client has received, or fetched, an inclusion proof (and an STH), it SHOULD proceed to verify the inclusion proof to the provided STH.

R-0115

<!-- q L1985-1986 "The TLS client" .. "about." -->
> The TLS client SHOULD also verify consistency between the provided STH and an STH it knows about.

R-0116

<!-- q L1988-1990 "If the TLS" .. "5.3)." -->
> If the TLS client holds an STH that predates the SCT, it MAY, in the process of auditing, request a new STH from the log (Section 5.2) and then verify it by requesting a consistency proof (Section 5.3).

R-0117

## §8.1.6

<!-- q L2003-2005 "Therefore," .. "ClientHello." -->
> Therefore, a TLS client MUST NOT evaluate compliance if it did not include both the transparency_info and status_request TLS extensions in the ClientHello.

R-0118

## §8.2

<!-- q L2014-2015 -->
> A monitor MUST at least inspect every new entry in every log it watches, and it MAY also choose to keep copies of entire logs.

R-0119 · split: R-0393, R-0394

<!-- q L2017-2018 -->
> To inspect all of the existing entries, the monitor SHOULD follow these steps once for each log:

R-0120

<!-- q L2020-2020 -->
> 1. Fetch the current STH (Section 5.2).

R-0395 · candidate C-0214

<!-- q L2022-2022 -->
> 2. Verify the STH signature.

R-0396 · candidate C-0215

<!-- q L2024-2025 -->
> 3. Fetch all the entries in the tree corresponding to the STH (Section 5.6).

R-0397 · candidate C-0216

<!-- q L2027-2028 -->
> 4. If applicable, check each entry to see if it's a certificate of interest.

R-0398 · candidate C-0217

<!-- q L2030-2031 -->
> 5. Confirm that the tree made from the fetched entries produces the same hash as that in the STH.

R-0399 · candidate C-0218

<!-- q L2033-2034 -->
> To inspect new entries, the monitor SHOULD follow these steps repeatedly for each log:

R-0121

<!-- q L2036-2036 "1. Fetch" .. "5.2)." -->
> 1. Fetch the current STH (Section 5.2).

R-0400 · candidate C-0219

<!-- q L2036-2037 "Repeat until" .. "changes." -->
> Repeat until the STH changes.

R-0401 · candidate C-0220

<!-- q L2040-2040 -->
> 2. Verify the STH signature.

R-0402 · candidate C-0222

<!-- q L2042-2043 "3. Fetch" .. "5.6)." -->
> 3. Fetch all the new entries in the tree corresponding to the STH (Section 5.6).

R-0403 · candidate C-0223

<!-- q L2043-2045 "If they remain" .. "log." -->
> If they remain unavailable for an extended period, then this should be viewed as misbehavior on the part of the log.

R-0404 · candidate C-0224

<!-- q L2047-2048 -->
> 4. If applicable, check each entry to see if it's a certificate of interest.

R-0405 · candidate C-0225

<!-- q L2050-2050 -->
> 5. Either:

R-0406 · candidate C-0226

<!-- q L2052-2053 -->
> a. Verify that the updated list of all entries generates a tree with the same hash as the new STH.

R-0407 · no candidate (hunted)

<!-- q L2055-2055 -->
> Or, if it is not keeping all log entries:

R-0408 · no candidate (hunted)

<!-- q L2057-2058 -->
> a. Fetch a consistency proof for the new STH with the previous STH (Section 5.3).

R-0409 · no candidate (hunted)

<!-- q L2060-2060 -->
> b. Verify the consistency proof.

R-0410 · no candidate (hunted)

<!-- q L2062-2063 -->
> c. Verify that the new entries generate the corresponding elements in the consistency proof.

R-0411 · no candidate (hunted)

<!-- q L2065-2065 -->
> 6. Repeat from Step 1.

R-0412 · candidate C-0227

## §8.3

<!-- q L2074-2075 -->
> In particular, there are four properties of log behavior that should be checked:

R-0413 · candidate C-0229

<!-- q L2077-2077 -->
> * the Maximum Merge Delay (MMD)

R-0414 · candidate C-0230

<!-- q L2079-2079 -->
> * the STH Frequency Count

R-0415 · candidate C-0231

<!-- q L2081-2081 -->
> * the append-only property

R-0416 · candidate C-0232

<!-- q L2083-2083 -->
> * the consistency of the log view presented to all query sources

R-0417 · candidate C-0233

<!-- q L2101-2103 "A TLS client" .. "5.4)." -->
> A TLS client (Section 8.1) can audit by verifying an SCT against any STH dated after the SCT timestamp + the Maximum Merge Delay by requesting a Merkle inclusion proof (Section 5.4).

R-0418 · no candidate (hunted)

<!-- q L2103-2106 "It can also verify" .. "certificate)." -->
> It can also verify that the SCT corresponds to the server certificate it arrived with (i.e., the log entry is that certificate or is a precertificate corresponding to that certificate).

R-0491 · no candidate (hunted, pass 2)

## §9

<!-- q L2115-2116 -->
> It is not possible for a log to change either of its algorithms part way through its lifetime:

R-0419 · no candidate (hunted)

<!-- q L2125-2128 -->
> Allowing multiple signature or hash algorithms for a log would require that all data structures support it and would significantly complicate client implementation, which is why it is not supported by this document.

R-0420 · candidate C-0240

<!-- q L2130-2132 "If it should" .. "started." -->
> If it should become necessary to deprecate an algorithm used by a live log, then the log MUST be frozen, as specified in Section 4.13, and a new log SHOULD be started.

R-0122 · split: R-0421, R-0422

<!-- q L2132-2134 "Certificates" .. "instead." -->
> Certificates in the frozen log that have not yet expired and require new SCTs SHOULD be submitted to the new log and the SCTs from that log used instead.

R-0123

## §10.1.1

<!-- q L2150-2157 -->
> +=====+===================+===+===========+=============+===========+ |Value| Extension Name |TLS| DTLS-Only | Recommended | Reference | | |1.3| | | | +=====+===================+===+===========+=============+===========+ |52 | transparency_info |CH,| N | Y | RFC 9162 | | |CR,| | | | | |CT | | | | +-----+-------------------+---+-----------+-------------+-----------+

R-0423 · candidate C-0244

## §10.1.2

<!-- q L2167-2170 -->
> Registry name: trans Specification: RFC 9162 Repository: <https://www.iana.org/assignments/trans> Index value: No transformation needed.

R-0424 · candidate C-0247

## §10.2.1

<!-- q L2185-2193 -->
> +===========+=========================+ | Range | Registration Procedures | +===========+=========================+ | 0x00-0xDF | Specification Required | +-----------+-------------------------+ | 0xE0-0xEF | Experimental Use | +-----------+-------------------------+ | 0xF0-0xFF | Private Use | +-----------+-------------------------+

R-0425 · candidate C-0251

<!-- q L2199-2212 -->
> +========+==================+========================+===========+ | Value | Hash Algorithm | OID | Reference | +========+==================+========================+===========+ | 0x00 | SHA-256 | 2.16.840.1.101.3.4.2.1 | [RFC6234] | +--------+------------------+------------------------+-----------+ | 0x01 - | Unassigned | | RFC 9162 | | 0xDF | | | | +--------+------------------+------------------------+-----------+ | 0xE0 - | Reserved for | | RFC 9162 | | 0xEF | Experimental Use | | | +--------+------------------+------------------------+-----------+ | 0xF0 - | Reserved for | | RFC 9162 | | 0xFF | Private Use | | | +--------+------------------+------------------------+-----------+

R-0426 · candidate C-0254

<!-- q L2216-2218 "The designated" .. "attacks." -->
> The designated expert(s) should ensure that the proposed algorithm has a public specification and is suitable for use as a cryptographic hash algorithm with no known preimage or collision attacks.

R-0427 · candidate C-0256

## §10.2.2

<!-- q L2228-2230 "*Note:* This" .. "for CT." -->
> *Note:* This is a subset of the "TLS SignatureScheme" registry, limited to those algorithms that are appropriate for CT.

R-0428 · candidate C-0260

<!-- q L2235-2238 "While this" .. "server." -->
> While this may be confusing, it is okay because the verification process is the same for both algorithms, and the choice of which to use when generating a signature is purely internal to the log server.

R-0429 · candidate C-0263

<!-- q L2243-2253 -->
> +===============+=========================+ | Range | Registration Procedures | +===============+=========================+ | 0x0000-0x0807 | Specification Required | +---------------+-------------------------+ | 0x0808-0xFDFF | Expert Review | +---------------+-------------------------+ | 0xFE00-0xFEFF | Experimental Use | +---------------+-------------------------+ | 0xFF00-0xFFFF | Private Use | +---------------+-------------------------+

R-0430 · candidate C-0265

<!-- q L2259-2281 -->
> +========================+===========================+=============+ | SignatureScheme Value | Signature Algorithm | Reference | +========================+===========================+=============+ | 0x0000 - 0x0402 | Unassigned | | +------------------------+---------------------------+-------------+ | ecdsa_secp256r1_sha256 | ECDSA (NIST P-256) with | [FIPS186-4] | | (0x0403) | SHA-256 | | +------------------------+---------------------------+-------------+ | ecdsa_secp256r1_sha256 | Deterministic ECDSA (NIST | [RFC6979] | | (0x0403) | P-256) with HMAC-SHA256 | | +------------------------+---------------------------+-------------+ | 0x0404 - 0x0806 | Unassigned | | +------------------------+---------------------------+-------------+ | ed25519 (0x0807) | Ed25519 (PureEdDSA with | [RFC8032] | | the edwards25519 curve) | | +------------------------+---------------------------+-------------+ | 0x0808 - 0xFDFF | Unassigned | | +------------------------+---------------------------+-------------+ | 0xFE00 - 0xFEFF | Reserved for Experimental | RFC 9162 | | Use | | +------------------------+---------------------------+-------------+ | 0xFF00 - 0xFFFF | Reserved for Private Use | RFC 9162 | +------------------------+---------------------------+-------------+

R-0431 · candidate C-0268

<!-- q L2285-2288 -->
> The designated expert(s) should ensure that the proposed algorithm has a public specification, has a value assigned to it in the "TLS SignatureScheme" registry (which was established by [RFC8446]), and is suitable for use as a cryptographic signature algorithm.

R-0432 · candidate C-0270

## §10.2.3

<!-- q L2297-2299 -->
> *Note:* The range 0x0000..0x00FF is reserved so that v1 SCTs are distinguishable from v2 SCTs and other TransItem structures.

R-0433 · candidate C-0273

<!-- q L2304-2312 -->
> +===============+=========================+ | Range | Registration Procedures | +===============+=========================+ | 0x0100-0xDFFF | Specification Required | +---------------+-------------------------+ | 0xE000-0xEFFF | Experimental Use | +---------------+-------------------------+ | 0xF000-0xFFFF | Private Use | +---------------+-------------------------+

R-0434 · candidate C-0275

<!-- q L2318-2342 -->
> +=================+===============================+===========+ | Value | Type and Version | Reference | +=================+===============================+===========+ | 0x0000 - 0x00FF | Reserved | [RFC6962] | +-----------------+-------------------------------+-----------+ | 0x0100 | x509_entry_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0101 | precert_entry_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0102 | x509_sct_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0103 | precert_sct_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0104 | signed_tree_head_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0105 | consistency_proof_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0106 | inclusion_proof_v2 | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0x0107 - 0xDFFF | Unassigned | | +-----------------+-------------------------------+-----------+ | 0xE000 - 0xEFFF | Reserved for Experimental Use | RFC 9162 | +-----------------+-------------------------------+-----------+ | 0xF000 - 0xFFFF | Reserved for Private Use | RFC 9162 | +-----------------+-------------------------------+-----------+

R-0435 · candidate C-0278

<!-- q L2346-2348 -->
> The designated expert(s) should review the public specification to ensure that it is detailed enough to ensure implementation interoperability.

R-0436 · candidate C-0280

## §10.2.4

<!-- q L2358-2366 -->
> +===============+=========================+ | Range | Registration Procedures | +===============+=========================+ | 0x0000-0xDFFF | Specification Required | +---------------+-------------------------+ | 0xE000-0xEFFF | Experimental Use | +---------------+-------------------------+ | 0xF000-0xFFFF | Private Use | +---------------+-------------------------+

R-0437 · candidate C-0283

<!-- q L2372-2382 -->
> +=================+===============================+=====+===========+ | ExtensionType | Status | Use | Reference | +=================+===============================+=====+===========+ | 0x0000 - 0xDFFF | Unassigned | n/a | | +-----------------+-------------------------------+-----+-----------+ | 0xE000 - 0xEFFF | Reserved for | n/a | RFC 9162 | | Experimental Use | | | +-----------------+-------------------------------+-----+-----------+ | 0xF000 - 0xFFFF | Reserved for | n/a | RFC 9162 | | Private Use | | | +-----------------+-------------------------------+-----+-----------+

R-0438 · candidate C-0286

<!-- q L2386-2386 -->
> The "Use" column should contain one or both of the following values:

R-0439 · candidate C-0288

<!-- q L2388-2389 -->
> * "SCT", for extensions specified for use in Signed Certificate Timestamps.

R-0440 · candidate C-0289

<!-- q L2391-2391 -->
> * "STH", for extensions specified for use in Signed Tree Heads.

R-0441 · candidate C-0290

<!-- q L2393-2395 "The designated" .. "interoperability." -->
> The designated expert(s) should review the public specification to ensure that it is detailed enough to ensure implementation interoperability.

R-0442 · candidate C-0291

<!-- q L2395-2397 "They should" .. "both)." -->
> They should also verify that the extension is appropriate to the contexts in which it is specified to be used (SCT, STH, or both).

R-0443 · candidate C-0292

## §10.2.5

<!-- q L2403-2403 -->
> The registry's registration procedure is First Come First Served.

R-0444 · candidate C-0294

<!-- q L2407-2415 -->
> +================+==============+==============+===========+ | Log ID | Log Base URL | Log Operator | Reference | +================+==============+==============+===========+ | 1.3.101.8192 - | Unassigned | Unassigned | | | 1.3.101.16383 | | | | +----------------+--------------+--------------+-----------+ | 1.3.101.80.0 - | Unassigned | Unassigned | | | 1.3.101.80.* | | | | +----------------+--------------+--------------+-----------+

R-0445 · candidate C-0296

<!-- q L2421-2423 "*Note:* All" .. "IDs." -->
> *Note:* All OIDs in the range from 1.3.101.8192 to 1.3.101.16383 have been set aside for Log IDs.

R-0446 · candidate C-0299

<!-- q L2423-2424 "This is a" .. "octets." -->
> This is a limited resource of 8,192 OIDs, each of which has an encoded length of 4 octets.

R-0447 · candidate C-0300

<!-- q L2426-2427 "*Note:* The" .. "IDs." -->
> *Note:* The 1.3.101.80 arc has also been set aside for Log IDs.

R-0448 · candidate C-0301

<!-- q L2427-2430 "This is an" .. "octets." -->
> This is an unlimited resource, but only the 128 OIDs from 1.3.101.80.0 to 1.3.101.80.127 have an encoded length of only 4 octets.

R-0449 · candidate C-0302

<!-- q L2432-2433 -->
> Each application for the allocation of a Log ID MUST be accompanied by:

R-0124

<!-- q L2435-2435 -->
> * the Log's Base URL (see Section 4.1) and

R-0450 · candidate C-0303

<!-- q L2437-2437 -->
> * the Log Operator's contact details.

R-0451 · candidate C-0304

<!-- q L2439-2441 -->
> IANA is asked to reject any request to update a Log ID or Log Base URL in this registry because these fields are immutable (see Section 4.1).

R-0452 · candidate C-0305

<!-- q L2443-2444 -->
> IANA is asked to accept requests from log operators to update their contact details in this registry.

R-0453 · candidate C-0306

## §10.2.6

<!-- q L2455-2456 -->
> The registration procedure for this registry is Specification Required.

R-0454 · candidate C-0309

<!-- q L2460-2468 -->
> +============+========+===========+ | Field Name | Type | Reference | +============+========+===========+ | Identifier | string | RFC 9162 | +------------+--------+-----------+ | Meaning | string | RFC 9162 | +------------+--------+-----------+ | Reference | string | RFC 9162 | +------------+--------+-----------+

R-0455 · candidate C-0311

<!-- q L2475-2532 -->
> +===================+===================================+===========+ | Identifier | Meaning | Reference | +===================+===================================+===========+ | malformed | The request could not be | RFC 9162 | | parsed. | | +-------------------+-----------------------------------+-----------+ | badSubmission | submission is neither a | RFC 9162 | | valid certificate nor a | | | valid precertificate. | | +-------------------+-----------------------------------+-----------+ | badType | type is neither 1 nor 2. | RFC 9162 | +-------------------+-----------------------------------+-----------+ | badChain | The first element of chain | RFC 9162 | | is not the certifier of the | | | submission, or the second | | | element does not certify the | | | first, etc. | | +-------------------+-----------------------------------+-----------+ | badCertificate | One or more certificates in | RFC 9162 | | chain are not valid (e.g., | | | not properly encoded). | | +-------------------+-----------------------------------+-----------+ | unknownAnchor | The last element of chain | RFC 9162 | | (or, if chain is an empty | | | array, the submission) is | | | not, nor is it certified by, | | | an accepted trust anchor. | | +-------------------+-----------------------------------+-----------+ | shutdown | The log is no longer | RFC 9162 | | accepting submissions. | | +-------------------+-----------------------------------+-----------+ | firstUnknown | first is before the latest | RFC 9162 | | known STH but is not from an | | | existing STH. | | +-------------------+-----------------------------------+-----------+ | secondUnknown | second is before the latest | RFC 9162 | | known STH but is not from an | | | existing STH. | | +-------------------+-----------------------------------+-----------+ | secondBeforeFirst | second is smaller than | RFC 9162 | | first. | | +-------------------+-----------------------------------+-----------+ | hashUnknown | hash is not the hash of a | RFC 9162 | | known leaf (may be caused by | | | skew or by a known | | | certificate not yet merged). | | +-------------------+-----------------------------------+-----------+ | treeSizeUnknown | hash is before the latest | RFC 9162 | | known STH but is not from an | | | existing STH. | | +-------------------+-----------------------------------+-----------+ | startUnknown | start is greater than the | RFC 9162 | | number of entries in the | | | Merkle Tree. | | +-------------------+-----------------------------------+-----------+ | endBeforeStart | start cannot be greater than | RFC 9162 | | end. | | +-------------------+-----------------------------------+-----------+

R-0456 · candidate C-0314

## §10.3

<!-- q L2542-2546 -->
> +=========+=========================+============+ | Decimal | Description | References | +=========+=========================+============+ | 102 | id-mod-public-notary-v2 | RFC 9162 | +---------+-------------------------+------------+

R-0457 · candidate C-0317

## §11.3

<!-- q L2597-2599 "These checks" .. "certificate." -->
> These checks can be asynchronous and need only be done once per certificate.

R-0458 · candidate C-0323

<!-- q L2613-2613 "Logs SHOULD" .. "either:" -->
> Logs SHOULD mitigate this risk by either:

R-0125

<!-- q L2615-2615 -->
> * using deterministic signature schemes or

R-0459 · candidate C-0328

<!-- q L2617-2618 "* producing" .. "tree_size." -->
> * producing no more than one SCT for each distinct submission and no more than one STH for each distinct tree_size.

R-0460 · candidate C-0329

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in `derived_from`. R-0461 (§2.1.3.2), R-0462 (§2.1.4.2), R-0463 (§5.3), R-0464 (§2.1.4.1), R-0465 (§4.12), R-0466 (§4.11), R-0467 (§4.7), R-0468 (§8.1.3), R-0469 (§4.9), R-0470 (§4.9), R-0471 (§5), R-0472 (§5), R-0473 (§5), R-0474 (§4), R-0475 (§4), R-0476 (§8.1.5), R-0477 (§4.7), R-0478 (§4.2.1), R-0479 (§3.2), R-0480 (§5.1), R-0481 (§5.6), R-0482 (§5.6), R-0483 (§5.6), R-0484 (§5.3), R-0485 (§5.4), R-0486 (§6.5), R-0487 (§6.3), R-0488 (§2.1.1).

## Source defects

Inconsistencies in RFC 9162 itself, found reading the source for this pass. Each quotes the lines it rests on; the prose is ours. Severity: SD-2, SD-4, SD-5, SD-6, SD-7, SD-8 and SD-20 leave an implementer two incompatible readings; the rest are editorial or narrow. The table at the end of this section joins these ids to the lane-local ids in the other artifacts.

### SD-1 — §2.1.3.2 step 4.b.ii and §2.1.4.2 step 6.b.iii: the `fn is 0` exit cannot fire (RFC Errata ID 8670, editorial, is on the loop wording of these two steps per record.yaml; its text was not read, so whether it reports this defect is not established)

At both steps the branch was entered with LSB(fn) clear, which happens only when fn equals sn. The step before (4.a, 6.a) already failed the proof if sn was 0, so sn, and therefore fn, is non-zero here, and right-shifting a non-zero fn reaches a set low bit before it reaches 0. The exit is dead text; removing it changes no result. Executed by this pass for every tree size below 70 (2415 inclusion and 2346 consistency proofs generated by PATH and PROOF): the exit never fired, every valid proof verified, and no proof with a node added or dropped did. Requirements affected: R-0161, R-0188.

<!-- q L459-460 -->
> ii. If LSB(fn) is not set, then right-shift both fn and sn equally until either LSB(fn) is set or fn is 0.

<!-- q L566-567 -->
> iii. If LSB(fn) is not set, then right-shift both fn and sn equally until either LSB(fn) is set or fn is 0.

<!-- q L452-453 -->
> a. If sn is 0, then stop the iteration and fail the proof verification.

### SD-2 — §5.1 `type` input values 1 and 2 are not the VersionedTransType code points they are said to be

L1361-1363 calls `type` the VersionedTransType integer value and gives 1 and 2, while §4.5 (L972) and Table 13 (L2323-2325) assign 0x0100 and 0x0101, and 0x0000-0x00FF is reserved for v1 (L2298-2299). badType (L1395, L2485) follows the 1-or-2 reading; §4.7 (L1081-1082) needs a mapping from `type` to the leaf versioned_type that no line states; and L1433 says `type` 2 indicates precert_sct_v2 where L1362-1363 says precert_entry_v2. An implementation has to accept 1 and 2 as printed and map them to 0x0100 and 0x0101 by assumption. Requirements affected: R-0303, R-0254, R-0308, R-0456.

<!-- q L1361-1363 -->
> type: The VersionedTransType integer value that indicates the type of the submission: 1 for x509_entry_v2 or 2 for precert_entry_v2.

<!-- q L972-972 -->
> x509_entry_v2(0x0100), precert_entry_v2(0x0101),

<!-- q L1395-1395 -->
> | badType | type is neither 1 nor 2. |

<!-- q L1081-1082 -->
> The type of the TransItem corresponds to the value of the type parameter supplied in the Section 5.1 call.

<!-- q L1433-1434 "For example, if type" .. "in the certificate." -->
> For example, if type was 2 (indicating precert_sct_v2), then all three TransItems could be embedded in the certificate.

<!-- q L2298-2299 -->
> The range 0x0000..0x00FF is reserved so that v1 SCTs are distinguishable from v2 SCTs and other TransItem structures.

### SD-3 — Table 4 and Table 18: the treeSizeUnknown condition is written about `hash`

The condition is about the requested tree_size (compare firstUnknown, L1483-1484), but both tables print it about the hash; a hash is not before or after an STH. Table 18 copies the wording. Requirements affected: R-0331, R-0456.

<!-- q L1535-1536 -->
> | treeSizeUnknown | hash is before the latest known STH | | but is not from an existing STH. |

<!-- q L1483-1484 -->
> | firstUnknown | first is before the latest known STH | | but is not from an existing STH. |

### SD-4 — §5.6: `sth` is defined inside each element of `entries`, yet must be returned in any case

The Outputs list puts sth beside log_entry, submitted_entry and sct, as a member of each entry object (the XML nests it in the same per-entry definition list). L1668-1669 requires the latest STH in every response, including the empty entries array L1664-1666 mandates, where no entry object exists to carry it; the section title also promises entries and STH. A top-level sth is the only reading under which both hold, and it is not what the text defines. Requirements affected: R-0088, R-0089, R-0351.

<!-- q L1614-1614 -->
> entries: An array of objects, each consisting of:

<!-- q L1627-1628 -->
> sth: A base64-encoded TransItem of type signed_tree_head_v2, signed by this log.

<!-- q L1664-1666 "Because of skew" .. "entries array." -->
> Because of skew, it is possible the log server will not have any entries between start and end. In this case, it MUST return an empty entries array.

<!-- q L1668-1669 -->
> In any case, the log server MUST return the latest STH it knows about.

### SD-5 — §5.6: start beyond the number of entries meets both startUnknown and the empty-array rule

For a start greater than the number of entries a front end holds, the server has no entries between start and end, so L1664-1666 mandates an empty entries array, and Table 6 defines startUnknown for exactly that start. One request, two mandated answers (an error and a normal response). The boundary start equal to tree_size meets only the empty-array rule (R-0481). Requirements affected: R-0088, R-0356.

<!-- q L1664-1666 "Because of skew" .. "entries array." -->
> Because of skew, it is possible the log server will not have any entries between start and end. In this case, it MUST return an empty entries array.

<!-- q L1679-1680 -->
> | startUnknown | start is greater than the number | | of entries in the Merkle Tree. |

### SD-6 — §5.5 get-all-by-hash: empty response versus hashUnknown, and an undefined selected STH

When the requested tree head equals the latest STH and the hash is not known, no Table 5 case holds, so L1577-1579 mandates an empty response; L1598 imports the §5.4 errors, and hashUnknown fits the same request. Empty response is itself undefined (an empty JSON object, or no body). Table 5 compares an STH with a tree head and an index with an STH where sizes are meant. And when a newer STH is returned with a consistency proof, the inclusion output proves inclusion in the selected STH (L1582-1585) without saying whether that is the requested tree head or the returned one. Requirements affected: R-0077, R-0338, R-0340, R-0343.

<!-- q L1577-1579 -->
> Note that more than one case can be true; in which case, the returned data is their union. It is also possible for none to be true; in which case, the front end MUST return an empty response.

<!-- q L1598-1598 -->
> Errors are the same as in Section 5.4.

<!-- q L1561-1573 -->
> +=====================+=====================================+ | Case | Response | +=====================+=====================================+ | latest STH < | Return latest STH. | | requested tree head | | +---------------------+-------------------------------------+ | latest STH > | Return latest STH and a consistency | | requested tree head | proof between it and the requested | | tree head (see Section 5.3). | +---------------------+-------------------------------------+ | index of requested | Return inclusion. | | hash < latest STH | | +---------------------+-------------------------------------+

<!-- q L1582-1585 -->
> inclusion: A base64-encoded TransItem of type inclusion_proof_v2 whose inclusion_path array of Merkle Tree nodes proves the inclusion of the certificate (as specified by the hash parameter) in the selected STH.

### SD-7 — §6.4 versus §6.5: every TransItemList needs an SCT, but already-embedded SCTs should be left out

R-0093 requires an x509_sct_v2 or precert_sct_v2 item in each TransItemList sent in a handshake. R-0371 says the transparency_info list should omit items already embedded in the certificate or the stapled OCSP response. A server whose SCTs are all embedded, and which adds inclusion proofs or STHs over the extension as R-0094 recommends, can follow the SHOULD only by breaking the MUST. The MUST prevails, so such a server re-sends at least one SCT. Requirements affected: R-0093, R-0371, R-0094.

<!-- q L1811-1813 -->
> In each TransItemList that is sent during a TLS handshake, the TLS server MUST include a TransItem structure of type x509_sct_v2 or precert_sct_v2.

<!-- q L1830-1833 -->
> * The TLS server MUST construct a TransItemList of relevant TransItems (see Section 6.4), which SHOULD omit any TransItems that are already embedded in the server certificate or the stapled OCSP response (see Section 7.1). If the constructed TransItemList

### SD-8 — §6.5: omitting the extension_data element, and an empty array, for an empty TransItemList

A TLS extension has extension_data, possibly zero-length; there is no element to omit, so R-0372 can only mean leaving the extension out. And TransItemList is trans_item_list<1..2^16-1> (L1799), so an empty array is not a TransItemList at all: R-0373 permits a value R-0097 and §6.3 cannot express. Requirements affected: R-0098, R-0372, R-0373, R-0367.

<!-- q L1836-1837 "If the list is empty" .. "empty array." -->
> If the list is empty, then the server SHOULD omit the extension_data element but MAY send it with an empty array.

<!-- q L1799-1799 -->
> SerializedTransItem trans_item_list<1..2^16-1>;

### SD-9 — §6.5: CertificateRequest has no defined meaning, and §6 calls the extension TLS 1.3-only

R-0099 allows a server to put transparency_info in a TLS 1.3 CertificateRequest (also CR in Table 7), which in TLS 1.3 asks the client about its own certificate; §6.1 says the document does not describe CT for client certificates, so the request has no defined content or consequence. Separately, §6 introduces the mechanism as a TLS 1.3 extension (L1716-1717), while L1842 places it in the TLS 1.2 ServerHello. Requirements affected: R-0099, R-0375, R-0361.

<!-- q L1844-1844 -->
> * the Certificate or CertificateRequest message (for TLS 1.3)

<!-- q L1745-1746 "This specification" .. "client certificates." -->
> This specification includes no description of how a TLS server can use CT for TLS client certificates.

<!-- q L1716-1717 "A server can provide" .. "(see Section 6.5)." -->
> A server can provide SCTs using a TLS 1.3 extension (Section 4.2 of [RFC8446]) with type transparency_info (see Section 6.5).

<!-- q L1842-1842 -->
> * the ServerHello message (for TLS 1.2 or earlier)

### SD-10 — §7.1 SHOULD be noncritical versus Appendix B CRITICALITY { FALSE }

In the RFC 5912 EXTENSION class, CRITICALITY lists the criticality values allowed, so { FALSE } permits only non-critical: a MUST where §7.1 says SHOULD. Appendix B is informative (L2847), so §7.1 governs and a critical extension is non-conforming only to a SHOULD. Requirements affected: R-0101.

<!-- q L1854-1856 "The Transparency Information X.509v3 extension, which" .. "TransItemList." -->
> The Transparency Information X.509v3 extension, which has OID 1.3.101.75 and SHOULD be noncritical, contains one or more TransItem structures in a TransItemList.

<!-- q L2893-2896 -->
> ext-transparencyInfo EXTENSION ::= { SYNTAX TransparencyInformationSyntax IDENTIFIED BY id-ce-transparencyInfo CRITICALITY { FALSE } }

<!-- q L2847-2847 -->
> Appendix B. An ASN.1 Module (Informative)

### SD-11 — §3.2: the eContent exception list omits the v1 SCT extension that §8.1.2 strips and Appendix A adds

The precertificate TBSCertificate must equal the issued one except for the Transparency Information extension. §8.1.2 also removes embedded v1 SCTs before validating a precertificate SCT, and the Appendix A procedure embeds v1 SCTs into the final TBSCertificate after the CMS precertificate exists. A certificate built that way differs from its precertificate by the v1 SCT extension too, which R-0194 as printed forbids. Validation works (§8.1.2 strips both), so the defect is in the CA-side rule. Requirements affected: R-0011, R-0194, R-0381.

<!-- q L704-707 -->
> - eContent MUST contain a TBSCertificate [RFC5280] that will be identical to the TBSCertificate in the issued certificate, except that the Transparency Information (Section 7.1) extension MUST be omitted.

<!-- q L1932-1933 "Remove embedded" .. "[RFC6962])." -->
> Remove embedded v1 SCTs, identified by OID 1.3.6.1.4.1.11129.2.4.2 (see Section 3.3 of [RFC6962]).

<!-- q L2841-2845 -->
> * Embed the v1 SCTs in the TBSCertificate, as described in Section 3.3 of [RFC6962]. * Sign that TBSCertificate (which now contains v1 and v2 SCTs) to issue the final X.509 certificate.

### SD-12 — §11.3 option 2 (one STH per tree_size) versus §4.10 (re-sign when idle)

R-0057 obliges a log that accepts no submissions for an MMD period to sign the same tree hash with a fresh timestamp, that is, a second STH for the same tree_size. Option 2 of R-0125 says no more than one STH per distinct tree_size. A quiet log can keep option 2 only by breaking R-0057; option 1 (deterministic signatures) is the only fully compatible mitigation. The tracking risk the option targets (same timestamp and data, different signatures) is not created by a re-signed head with a new timestamp, so the option is worded more strictly than its purpose. Requirements affected: R-0057, R-0125, R-0460.

<!-- q L2617-2618 "producing no more" .. "distinct tree_size." -->
> producing no more than one SCT for each distinct submission and no more than one STH for each distinct tree_size.

<!-- q L1157-1159 "in the event that" .. "fresh timestamp." -->
> in the event that a log does not accept any submissions during an MMD period, the log MUST sign the same Merkle Tree Hash with a fresh timestamp.

### SD-13 — §4.13 key destruction versus §4.10 freshness rules

After the final STH the private key can be destroyed, yet R-0055 still requires get-sth to return an STH no older than MMD and R-0057 requires a fresh signature each idle MMD period. Nothing suspends those rules for a frozen log, and the Final STH is a log parameter (R-0029), not a get-sth answer. Clients auditing a frozen log will see a stale STH that the rules call misbehaviour. Requirements affected: R-0055, R-0057, R-0284.

<!-- q L1253-1254 "At this point" .. "can be destroyed." -->
> At this point, the log's private key is no longer needed and can be destroyed.

<!-- q L1151-1153 "When a client requests" .. "than the log's MMD." -->
> When a client requests a log's latest STH (see Section 5.2), the log MUST return an STH that is no older than the log's MMD.

<!-- q L1157-1159 "in the event that" .. "fresh timestamp." -->
> in the event that a log does not accept any submissions during an MMD period, the log MUST sign the same Merkle Tree Hash with a fresh timestamp.

### SD-14 — §9 MUST be frozen as specified in §4.13, whose actions are SHOULD

R-0122 makes freezing mandatory and defines it by reference to §4.13, where the actions themselves are recommendations (R-0060). Which of the four actions become mandatory when an algorithm is deprecated is not determinable from the text. Requirements affected: R-0421, R-0060.

<!-- q L2130-2131 "If it should become" .. "Section 4.13" -->
> If it should become necessary to deprecate an algorithm used by a live log, then the log MUST be frozen, as specified in Section 4.13

<!-- q L1238-1239 "In order to avoid that" .. "SHOULD be taken:" -->
> In order to avoid that, the following actions SHOULD be taken:

### SD-15 — Appendix B: the module identifier is an unreplaced placeholder

The module header carries a comment asking for the id-mod-public-notary-v2 OID to be filled in from above, not the OID itself, although §10.3 records the assigned value 102 (in the PKIX module arc). The module therefore has no machine-readable identifier, and a compiler sees only a name. Requirements affected: R-0457.

<!-- q L2852-2855 -->
> CertificateTransparencyV2Module-2021 -- { id-mod-public-notary-v2 from above, in iso(1) identified-organization(3) ... form }

<!-- q L2545-2545 -->
> | 102 | id-mod-public-notary-v2 | RFC 9162 |

### SD-16 — §2.1.2 has no answer for tree_size 0

With no entries the loop never runs, the stack is empty, and step 4 refers to a remaining element that does not exist; MTH of the empty list is defined (HASH()), and an empty log must still sign tree heads (R-0055, R-0057). Requirements affected: R-0136, R-0146, R-0488.

<!-- q L391-397 -->
> 3. If there is more than one element in the stack, repeat the same merge procedure (the sub-items of Step 2(c) above) until only a single element remains. 4. The remaining element in stack is the Merkle Tree Hash for the given tree_size and should be compared by equality against the supplied root_hash.

<!-- q L331-333 -->
> The hash of an empty list is the hash of an empty string: MTH({}) = HASH().

### SD-17 — Chain length: what is counted is not said

The Maximum Chain Length parameter and the max_chain_length output both bound a chain length (lines quoted below), but the submit-entry `chain` input holds CA certificates only (the submission is separate) and may omit the trust anchor. Whether the submission and the anchor count is unstated, so a client counting one way and a log the other disagree at the limit. Requirements affected: R-0037, R-0224, R-0360.

<!-- q L841-842 -->
> Maximum Chain Length: The longest certificate chain submission the log is willing to accept, if the log imposes any limit.

<!-- q L1698-1700 "max_chain_length:" .. "in decimal." -->
> max_chain_length: If the server has chosen to limit the length of chains it accepts, this is the maximum number of certificates in the chain, in decimal.

<!-- q L1365-1366 "chain:" .. "CA certificate." -->
> chain: An array of zero or more JSON strings, each of which is a base64-encoded CA certificate.

### SD-18 — §4.6 names ExtensionType 65535 reserved; §10.2.4 puts it in Private Use

Minor: the enum value may only be the presentation-language idiom for fixing a two-octet width (VersionedTransType uses a bare (0xFFFF) for that), but it is named reserved, while Table 14 assigns 0xF000-0xFFFF, 0xFFFF included, to Private Use. Requirements affected: R-0243, R-0437.

<!-- q L1019-1021 -->
> enum { reserved(65535) } ExtensionType;

<!-- q L2365-2365 -->
> | 0xF000-0xFFFF | Private Use |

### SD-19 — §5.1 chain definition versus unknownAnchor when the anchor is included

The input definition requires the final chain element, or the submission when the array is empty, to be certified by an accepted anchor; the unknownAnchor condition accepts a final element that either is an accepted anchor or is certified by one. A submitter that includes an intermediate trust anchor as the last element (allowed, since leaving it out is only a MAY, R-0003) satisfies the error rule but not the literal input definition. Requirements affected: R-0304, R-0308.

<!-- q L1368-1370 "The last element of chain" .. "trust anchor." -->
> The last element of chain (or, if chain is an empty array, the submission) is certified by an accepted trust anchor.

<!-- q L1404-1406 -->
> | unknownAnchor | The last element of chain (or, if chain is an | | empty array, the submission) is not, nor is | | it certified by, an accepted trust anchor. |

### SD-20 — §5.3 versus §2.1.4: the empty proof mandated for equal sizes has no verification, and the algorithm fails it

When first and second are equal and correspond to a known STH, §5.3 requires an empty consistency_path (R-0076). §2.1.4.1 defines PROOF only for 0 < m < n, §2.1.4.2 is stated only for 0 < first < second, and its step 1 fails any empty path, so the document gives no way to verify the one proof it mandates for this case. Not a contradiction in the letter, since §2.1.4.2 does not claim the equal case; a gap every lane met: messages.yaml SD-02, protocol.yaml SD-01, state-machine.yaml SD-01, examples/README.md. A client compares the two root hashes itself (R-0463, inferred). Executed: examples/reproduce.py rejects the empty proof at first = second for every tree size 1 to 65. Requirements affected: R-0076, R-0178, R-0463. Added by pass 2.

<!-- q L1468-1470 "If first and second" .. "zero elements)." -->
> If first and second are equal and correspond to a known STH, the returned consistency proof MUST be empty (a consistency_path array with zero elements).

<!-- q L535-539 "When a client has a tree head first_hash" .. "0 < first < second," -->
> When a client has a tree head first_hash for tree size first, has a tree head second_hash for tree size second where 0 < first < second,

<!-- q L541-542 -->
> 1. If consistency_path is an empty array, stop and fail the proof verification.

### SD-21 — §5.7: max_chain_length is "in decimal", and a JSON number or a string is not said

The get-anchors output describes max_chain_length as a number of certificates "in decimal" without saying whether the JSON member is a number or a string of decimal digits. A client and a log can disagree on the encoding of the one numeric member of that response. Narrow; messages.yaml SD-05 carries it, the derived schema accepts both. Requirements affected: R-0360.

<!-- q L1698-1700 "max_chain_length:" .. "in decimal." -->
> max_chain_length: If the server has chosen to limit the length of chains it accepts, this is the maximum number of certificates in the chain, in decimal.

### SD-22 — §2.1.5: the worked example calls leaf hashes non-leaf nodes

The example of Section 2.1.5 says that non-leaf nodes c, d and j are used in the proofs of hash0 and hash2, but in the figure c, d and j sit directly over the leaves d2, d3 and d6, so they are leaf hashes. The proofs listed are right (they agree with §2.1.4.1 and examples/reproduce.py); only the word is wrong. Editorial. protocol.yaml SD-10, examples/README.md and design-notes.md section 4 carry it. Requirements affected: none (explanatory text, no requirement).

<!-- q L637-639 "Non-leaf" .. "hash0." -->
> Non-leaf nodes c, g are used to verify hash0, and non-leaf nodes d, l are additionally used to show hash is consistent with hash0.

<!-- q L645-646 "Non-leaf" .. "hash2." -->
> Non-leaf nodes k, i are used to verify hash2, and non-leaf node j is additionally used to show hash is consistent with hash2.

### Cross-reference of defect ids across the artifacts

The lanes numbered defects independently; this table is the join. A dash means that artifact does not carry the defect (it is not part of that artifact's content, or it was recorded only here).

| normative.md | messages.yaml | protocol.yaml | state-machine.yaml | design-notes.md |
|---|---|---|---|---|
| SD-1 | n/a | SD-11 | SD-11 | section 4 (loop reading) |
| SD-2 | SD-01 | SD-02 | n/a | open question 8 |
| SD-3 | SD-06 | SD-03 | n/a | n/a |
| SD-4 | SD-04 | SD-09 | n/a | n/a |
| SD-5 | n/a | SD-05 | n/a | n/a |
| SD-6 | n/a | SD-04, OI-03 | n/a | n/a |
| SD-7 | n/a | SD-06 | SD-06 | n/a |
| SD-8 | SD-03 | SD-07 | SD-07 | n/a |
| SD-9 | n/a | OI-07 | n/a | n/a |
| SD-10 | SD-07 | n/a | n/a | n/a |
| SD-11 | n/a | OI-09 | OI-09 | n/a |
| SD-12 | n/a | OI-10 | OI-10 | open question 6 |
| SD-13 | n/a | SD-08 | SD-08 | S-03, open question 11 |
| SD-14 | n/a | OI-11 | OI-11 | A-06, open question 11 |
| SD-15 | SD-10 | n/a | n/a | n/a |
| SD-16 | n/a | SD-12 | SD-12 | n/a |
| SD-17 | SD-11 | OI-01, OI-12 | n/a | n/a |
| SD-18 | SD-09 | n/a | n/a | n/a |
| SD-19 | n/a | SD-13 | n/a | n/a |
| SD-20 | SD-02 | SD-01 | SD-01 | open question 7, C-03 |
| SD-21 | SD-05 | n/a | n/a | n/a |
| SD-22 | n/a | SD-10 | n/a | section 4 |

messages.yaml SD-08 is not a defect of the source (a skeleton labelling error, listed there because that lane found it) and has no row. protocol.yaml OI-02, OI-04, OI-05, OI-06 and OI-08 are gaps in what the source specifies rather than inconsistencies in it, so they have no row either.

## Code blocks and figures (verbatim from the RFC XML)

- §2.1.1, L333-333 `artwork` → `examples/fig-01.verbatim.txt`
- §2.1.1, L337-337 `artwork` → `examples/fig-02.verbatim.txt`
- §2.1.1, L343-343 `artwork` → `examples/fig-03.verbatim.txt`
- §2.1.3.1, L422-422 `artwork` → `examples/fig-04.verbatim.txt`
- §2.1.3.1, L428-430 `artwork` → `examples/fig-05.verbatim.txt`
- §2.1.4.1, L491-491 `artwork` → `examples/fig-06.verbatim.txt`
- §2.1.4.1, L505-505 `artwork` → `examples/fig-07.verbatim.txt`
- §2.1.4.1, L510-510 `artwork` → `examples/fig-08.verbatim.txt`
- §2.1.4.1, L520-520 `artwork` → `examples/fig-09.verbatim.txt`
- §2.1.4.1, L526-526 `artwork` → `examples/fig-10.verbatim.txt`
- §2.1.5, L584-598 `artwork` → `examples/fig-11.verbatim.txt`
- §2.1.5, L610-634 `artwork` → `examples/fig-12.verbatim.txt`
- §4.4, L953-953 `tls-presentation` → `examples/ex-01.verbatim.txt`
- §4.5, L971-995 `tls-presentation` → `examples/ex-02.verbatim.txt`
- §4.6, L1019-1026 `tls-presentation` → `examples/ex-03.verbatim.txt`
- §4.7, L1048-1055 `tls-presentation` → `examples/ex-04.verbatim.txt`
- §4.8, L1090-1095 `tls-presentation` → `examples/ex-05.verbatim.txt`
- §4.9, L1121-1128 `tls-presentation` → `examples/ex-06.verbatim.txt`
- §4.10, L1164-1168 `tls-presentation` → `examples/ex-07.verbatim.txt`
- §4.11, L1189-1194 `tls-presentation` → `examples/ex-08.verbatim.txt`
- §4.12, L1212-1217 `tls-presentation` → `examples/ex-09.verbatim.txt`
- §5, L1320-1323 `json` → `examples/ex-10.verbatim.json`
- §6.3, L1796-1800 `tls-presentation` → `examples/ex-11.verbatim.txt`
- §7.1, L1864-1864 `asn.1` → `schema/rfc-9162-01.verbatim.asn1`
- Appendix B, L2852-2928 `asn.1` → `schema/rfc-9162-02.verbatim.asn1`

Corrected by pass 1: the skeleton filed the L2852-2928 module under Appendix A; it is in Appendix B (heading at L2847).
