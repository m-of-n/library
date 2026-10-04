// =====================================================================
// canonicalizer.ecmascript.js
//
// VERBATIM.  This file is NOT ours.  Everything between the BEGIN and
// END markers below is reproduced byte-for-byte, including the RFC's
// five-space left margin and its comment banners, from:
//
//   RFC 8785, "JSON Canonicalization Scheme (JCS)",
//   A. Rundgren, B. Jordan, S. Erdtman, June 2020,
//   Independent Submission stream, Category: Informational,
//   DOI 10.17487/RFC8785,
//   <https://www.rfc-editor.org/rfc/rfc8785.txt>
//
//   Appendix A, "ECMAScript Sample Canonicalizer", in full.
//   Lines 518-579 of the cached text rendering
//   (.cache/rfc-8785.txt, sha256
//   63d52294eb0e3f0014174288186d388b4ddbf2c67d1ce8af1d9726eb0c3ab240).
//
// Introduced in the source by: "Below is an example of a JCS
// canonicalizer for usage with ECMAScript-based systems:" (Appendix A).
//
// This is the source's OWN sample code, copied verbatim and not
// authored by us.  It must not be edited.  The five-space indentation
// is the RFC's page margin and is retained so the region stays
// byte-identical to the source; JavaScript is insensitive to it, so
// the file still parses and runs as-is.
//
// RFC 8785 ships NO CDDL, NO ABNF and NO JSON Schema.  This sample is
// the whole of the document's formal, machine-consumable material.
// See README.md.
//
// IMPORTANT, from the source's own banner below: this sample
// implements neither error handling nor UTF-8 generation.  It
// therefore does NOT enforce three of the document's MUST-level
// rules -- lone-surrogate rejection (Section 3.2.2.2), NaN/Infinity
// rejection (Section 3.2.2.3), and the UTF-8 output encoding
// (Section 3.2.4) -- nor the I-JSON duplicate-property-name rule of
// Section 3.1 (an ECMAScript object cannot hold duplicates by the
// time this function sees it).  It is a specification aid, not a
// conformant implementation.  Appendix G lists implementations the
// source states have been verified compatible with JCS.
//
// Copyright (c) 2020 IETF Trust and the persons identified as the
// document authors.  All rights reserved.  Reproduced under the IETF
// Trust's Legal Provisions Relating to IETF Documents
// (https://trustee.ietf.org/license-info); code components are
// licensed under the Revised BSD License as described in Section 4.e
// of the Trust Legal Provisions.
// =====================================================================

// ---- BEGIN VERBATIM (RFC 8785 Appendix A) ----
     ////////////////////////////////////////////////////////////
     // Since the primary purpose of this code is highlighting //
     // the core of the JCS algorithm, error handling and      //
     // UTF-8 generation were not implemented.                 //
     ////////////////////////////////////////////////////////////
     var canonicalize = function(object) {

         var buffer = '';
         serialize(object);
         return buffer;

         function serialize(object) {
             if (object === null || typeof object !== 'object' ||
                 object.toJSON != null) {
                 /////////////////////////////////////////////////
                 // Primitive type or toJSON, use "JSON"        //
                 /////////////////////////////////////////////////
                 buffer += JSON.stringify(object);

             } else if (Array.isArray(object)) {
                 /////////////////////////////////////////////////
                 // Array - Maintain element order              //
                 /////////////////////////////////////////////////
                 buffer += '[';
                 let next = false;
                 object.forEach((element) => {
                     if (next) {
                         buffer += ',';
                     }
                     next = true;
                     /////////////////////////////////////////
                     // Array element - Recursive expansion //
                     /////////////////////////////////////////
                     serialize(element);
                 });
                 buffer += ']';

             } else {
                 /////////////////////////////////////////////////
                 // Object - Sort properties before serializing //
                 /////////////////////////////////////////////////
                 buffer += '{';
                 let next = false;
                 Object.keys(object).sort().forEach((property) => {
                     if (next) {
                         buffer += ',';
                     }
                     next = true;
                     /////////////////////////////////////////////
                     // Property names are strings, use "JSON"  //
                     /////////////////////////////////////////////
                     buffer += JSON.stringify(property);
                     buffer += ':';
                     //////////////////////////////////////////
                     // Property value - Recursive expansion //
                     //////////////////////////////////////////
                     serialize(object[property]);
                 });
                 buffer += '}';
             }
         }
     };
// ---- END VERBATIM (RFC 8785 Appendix A) ----
