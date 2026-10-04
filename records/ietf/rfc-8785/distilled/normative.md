---
record: rfc-8785
kind: normative
title: "rfc-8785 — normative statements"
extracted: "2026-10-03"
reviewed_by: ""
---

<!-- FX-1 pass 1. Every normative statement and normative block of RFC 8785
     (JSON Canonicalization Scheme), VERBATIM, with its locator, in source
     order. Verbatim source only: no analysis, no paraphrase, no opinion.
     Blockquotes delimit verbatim text; everything outside a blockquote is
     structure (headings, locators, labels) only. -->

Source: RFC 8785, "JSON Canonicalization Scheme (JCS)", A. Rundgren,
B. Jordan, S. Erdtman, June 2020. Independent Submission, Category:
Informational, ISSN: 2070-1721.

BCP 14 keyword census of the source body (Section 3 onward, excluding the
Section 2 boilerplate enumeration): 25 `MUST`, 4 `MUST NOT`, 2 `RECOMMENDED`,
1 `SHOULD` = 32 occurrences. No `SHALL`, `SHALL NOT`, `SHOULD NOT`,
`NOT RECOMMENDED`, `MAY`, `OPTIONAL` or `REQUIRED` occurs outside Section 2.

Entries flagged `_[lowercase/implied]_` are normative in effect but are **not**
BCP 14 flagged in the source. They are recorded in the source's own words and
are neither demoted nor upgraded.


## Section 2. Terminology

**1.** (§2) _[lowercase/implied]_

> Note that this document is not on the IETF standards track. However, a
> conformant implementation is supposed to adhere to the specified behavior
> for security and interoperability reasons. This text uses BCP 14 to describe
> that necessary behavior.

**2.** (§2)

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
> "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
> "OPTIONAL" in this document are to be interpreted as described in BCP 14
> [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as
> shown here.


## Section 3. Detailed Operation

**3.** (§3) _[lowercase/implied]_

> This section describes the details related to creating a canonical JSON
> representation and how they are addressed by JCS.

**4.** (§3)

> Appendix F describes the RECOMMENDED way of adding JCS support to existing
> JSON tools.


### Section 3.1. Creation of Input Data

**5.** (§3.1)

> Irrespective of the method used, the data to be serialized MUST be adapted
> for I-JSON [RFC7493] formatting, which implies the following:

**6.** (§3.1 (bullet 1))

> JSON objects MUST NOT exhibit duplicate property names.

**7.** (§3.1 (bullet 2))

> JSON string data MUST be expressible as Unicode [UNICODE].

**8.** (§3.1 (bullet 3))

> JSON number data MUST be expressible as IEEE 754 [IEEE754] double-precision
> values. For applications needing higher precision or longer integers than
> offered by IEEE 754 double precision, it is RECOMMENDED to represent such
> numbers as JSON strings; see Appendix D for details on how this can be
> performed in an interoperable and extensible way.

**9.** (§3.1)

> An additional constraint is that parsed JSON string data MUST NOT be altered
> during subsequent serializations. For more information, see Appendix E.

**10.** (§3.1 (Note))

> That is, all components involved in a scheme depending on JCS MUST preserve
> Unicode string data "as is".


#### Lowercase / implied obligations (§3.1)

**11.** (§3.1) _[lowercase/implied]_

> Data to be canonically serialized is usually created by:

**12.** (§3.1 (Note)) _[lowercase/implied]_

> Note: Although the Unicode standard offers the possibility of rearranging
> certain character sequences, referred to as "Unicode Normalization"
> [UCNORM], JCS-compliant string processing does not take this into
> consideration.


### Section 3.2. Generation of Canonical JSON Data

**13.** (§3.2) _[lowercase/implied]_

> The following subsections describe the steps required to create a canonical
> JSON representation of the data elaborated on in the previous section.

**14.** (§3.2) _[lowercase/implied]_

> Appendix A shows sample code for an ECMAScript-based canonicalizer, matching
> the JCS specification.


### Section 3.2.1. Whitespace

**15.** (§3.2.1)

> Whitespace between JSON tokens MUST NOT be emitted.


### Section 3.2.2. Serialization of Primitive Data Types

**16.** (§3.2.2 (input))

> Assume the following JSON object is parsed:
>
> ```text
>      {
>        "numbers": [333333333.33333329, 1E30, 4.50,
>                    2e-3, 0.000000000000000000000000001],
>        "string": "\u20ac$\u000F\u000aA'\u0042\u0022\u005c\\\"\/",
>        "literals": [null, true, false]
>      }
> ```

**17.** (§3.2.2 (output))

> If the parsed data is subsequently serialized using a serializer compliant
> with ECMAScript's "JSON.stringify()", the result would (with a line wrap
> added for display purposes only) be rather divergent with respect to the
> original data:
>
> ```text
>      {"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27],"string":
>      "€$\u000f\nA'B\"\\\\\"/","literals":[null,true,false]}
> ```

**18.** (§3.2.2) _[lowercase/implied]_

> The reason for the difference between the parsed data and its serialized
> counterpart is due to a wide tolerance on input data (as defined by JSON
> [RFC8259]), while output data (as defined by ECMAScript) has a fixed
> representation. As can be seen in the example, numbers are subject to
> rounding as well.

**19.** (§3.2.2) _[lowercase/implied]_

> The following subsections describe the serialization of primitive JSON data
> types according to JCS. This part is identical to that of ECMAScript. In the
> (unlikely) event that a future version of ECMAScript would invalidate any of
> the following serialization methods, it will be up to the developer
> community to either stick to this specification or create a new
> specification.


### Section 3.2.2.1. Serialization of Literals

**20.** (§3.2.2.1)

> In accordance with JSON [RFC8259], the literals "null", "true", and "false"
> MUST be serialized as null, true, and false, respectively.


### Section 3.2.2.2. Serialization of Strings

**21.** (§3.2.2.2)

> For JSON string data (which includes JSON object property names as well),
> each Unicode code point MUST be serialized as described below (see Section
> 24.3.2.2 of [ECMA-262]):

**22.** (§3.2.2.2 (bullet 1))

> ```text
>    *  If the Unicode value falls within the traditional ASCII control
>       character range (U+0000 through U+001F), it MUST be serialized
>       using lowercase hexadecimal Unicode notation (\uhhhh) unless it is
>       in the set of predefined JSON control characters U+0008, U+0009,
>       U+000A, U+000C, or U+000D, which MUST be serialized as \b, \t, \n,
>       \f, and \r, respectively.
> ```

**23.** (§3.2.2.2 (bullet 2))

> ```text
>    *  If the Unicode value is outside of the ASCII control character
>       range, it MUST be serialized "as is" unless it is equivalent to
>       U+005C (\) or U+0022 ("), which MUST be serialized as \\ and \",
>       respectively.
> ```

**24.** (§3.2.2.2)

> Finally, the resulting sequence of Unicode code points MUST be enclosed in
> double quotes (").

**25.** (§3.2.2.2 (Note))

> Note: Since invalid Unicode data like "lone surrogates" (e.g., U+DEAD) may
> lead to interoperability issues including broken signatures, occurrences of
> such data MUST cause a compliant JCS implementation to terminate with an
> appropriate error.


### Section 3.2.2.3. Serialization of Numbers

**26.** (§3.2.2.3)

> ECMAScript builds on the IEEE 754 [IEEE754] double-precision standard for
> representing JSON number data. Such data MUST be serialized according to
> Section 7.1.12.1 of [ECMA-262], including the "Note 2" enhancement.

**27.** (§3.2.2.3 (Note))

> Note: Since Not a Number (NaN) and Infinity are not permitted in JSON,
> occurrences of NaN or Infinity MUST cause a compliant JCS implementation to
> terminate with an appropriate error.

**28.** (§3.2.2.3) _[lowercase/implied]_

> Due to the relative complexity of this part, the algorithm itself is not
> included in this document. For implementers of JCS-compliant number
> serialization, Google's implementation in V8 [V8] may serve as a reference.
> Another compatible number serialization reference implementation is Ryu
> [RYU], which is used by the JCS open-source Java implementation mentioned in
> Appendix G. Appendix B holds a set of IEEE 754 sample values and their
> corresponding JSON serialization.


### Section 3.2.3. Sorting of Object Properties

**29.** (§3.2.3) _[lowercase/implied]_

> Although the previous step normalized the representation of primitive JSON
> data types, the result would not yet qualify as "canonical" since JSON
> object properties are not in lexicographic (alphabetical) order.

**30.** (§3.2.3 (canonicalized output))

> Applied to the sample in Section 3.2.2, a properly canonicalized version
> should (with a line wrap added for display purposes only) read as:
>
> ```text
>      {"literals":[null,true,false],"numbers":[333333333.3333333,
>      1e+30,4.5,0.002,1e-27],"string":"€$\u000f\nA'B\"\\\\\"/"}
> ```

**31.** (§3.2.3)

> The rules for lexicographic sorting of JSON object properties according to
> JCS are as follows:

**32.** (§3.2.3 (sorting rule bullet 1))

> JSON object properties MUST be sorted recursively, which means that JSON
> child Objects MUST have their properties sorted as well.

**33.** (§3.2.3 (sorting rule bullet 2))

> JSON array data MUST also be scanned for the presence of JSON objects (if an
> object is found, then its properties MUST be sorted), but array element
> order MUST NOT be changed.

**34.** (§3.2.3)

> When a JSON object is about to have its properties sorted, the following
> measures MUST be adhered to:

**35.** (§3.2.3 (measure 1))

> The sorting process is applied to property name strings in their "raw"
> (unescaped) form. That is, a newline character is treated as U+000A.

**36.** (§3.2.3 (measure 2))

> Property name strings to be sorted are formatted as arrays of UTF-16
> [UNICODE] code units. The sorting is based on pure value comparisons, where
> code units are treated as unsigned integers, independent of locale settings.

**37.** (§3.2.3 (measure 3))

> Property name strings either have different values at some index that is a
> valid index for both strings, or their lengths are different, or both. If
> they have different values at one or more index positions, let k be the
> smallest such index; then, the string whose value at position k has the
> smaller value, as determined by using the "<" operator, lexicographically
> precedes the other string. If there is no index position at which they
> differ, then the shorter string lexicographically precedes the longer
> string.

**38.** (§3.2.3 (measure 3, plain-English ordering))

> In plain English, this means that property names are sorted in ascending
> order like the following:
>
> ```text
>               ""
>               "a"
>               "aa"
>               "ab"
> ```

**39.** (§3.2.3) _[lowercase/implied]_

> The rationale for basing the sorting algorithm on UTF-16 code units is that
> it maps directly to the string type in ECMAScript (featured in web browsers
> and Node.js), Java, and .NET. In addition, JSON only supports escape
> sequences expressed as UTF-16 code units, making knowledge and handling of
> such data a necessity anyway. Systems using another internal representation
> of string data will need to convert JSON property name strings into arrays
> of UTF-16 code units before sorting. The conversion from UTF-8 or UTF-32 to
> UTF-16 is defined by the Unicode [UNICODE] standard.

**40.** (§3.2.3 (sorting test vector))

> The following JSON test data can be used for verifying the correctness of
> the sorting scheme in a JCS implementation:
>
> ```text
>      {
>        "\u20ac": "Euro Sign",
>        "\r": "Carriage Return",
>        "\ufb33": "Hebrew Letter Dalet With Dagesh",
>        "1": "One",
>        "\ud83d\ude00": "Emoji: Grinning Face",
>        "\u0080": "Control",
>        "\u00f6": "Latin Small Letter O With Diaeresis"
>      }
> ```

**41.** (§3.2.3 (expected order))

> Expected argument order after sorting property strings:
>
> ```text
>      "Carriage Return"
>      "One"
>      "Control"
>      "Latin Small Letter O With Diaeresis"
>      "Euro Sign"
>      "Emoji: Grinning Face"
>      "Hebrew Letter Dalet With Dagesh"
> ```

**42.** (§3.2.3 (Note)) _[lowercase/implied]_

> Note: For the purpose of obtaining a deterministic property order, sorting
> of data encoded in UTF-8 or UTF-32 would also work, but the outcome for JSON
> data like above would differ and thus be incompatible with this
> specification. However, in practice, property names are rarely defined
> outside of 7-bit ASCII, making it possible to sort string data in UTF-8 or
> UTF-32 format without conversion to UTF-16 and still be compatible with JCS.
> Whether or not this is a viable option depends on the environment JCS is
> used in.


### Section 3.2.4. UTF-8 Generation

**43.** (§3.2.4)

> Finally, in order to create a platform-independent representation, the
> result of the preceding step MUST be encoded in UTF-8.

**44.** (§3.2.4 (hex bytes))

> Applied to the sample in Section 3.2.3, this should yield the following
> bytes, here shown in hexadecimal notation:
>
> ```text
>      7b 22 6c 69 74 65 72 61 6c 73 22 3a 5b 6e 75 6c 6c 2c 74 72
>      75 65 2c 66 61 6c 73 65 5d 2c 22 6e 75 6d 62 65 72 73 22 3a
>      5b 33 33 33 33 33 33 33 33 33 2e 33 33 33 33 33 33 33 2c 31
>      65 2b 33 30 2c 34 2e 35 2c 30 2e 30 30 32 2c 31 65 2d 32 37
>      5d 2c 22 73 74 72 69 6e 67 22 3a 22 e2 82 ac 24 5c 75 30 30
>      30 66 5c 6e 41 27 42 5c 22 5c 5c 5c 5c 5c 22 2f 22 7d
> ```

**45.** (§3.2.4) _[lowercase/implied]_

> This data is intended to be usable as input to cryptographic methods.


## Section 4. IANA Considerations

**46.** (§4)

> This document has no IANA actions.


## Section 5. Security Considerations

**47.** (§5) _[lowercase/implied]_

> It is crucial to perform sanity checks on input data to avoid overflowing
> buffers and similar things that could affect the integrity of the system.

**48.** (§5 (three-step ordered procedure))

> When JCS is applied to signature schemes like the one described in Appendix
> F, applications MUST perform the following operations before acting upon
> received data:
>
> ```text
>    1.  Parse the JSON data and verify that it adheres to I-JSON.
> 
>    2.  Verify the data for correctness according to the conventions
>        defined by the ecosystem where it is to be used.  This also
>        includes locating the property holding the signature data.
> 
>    3.  Verify the signature.
> ```

**49.** (§5)

> If any of these steps fail, the operation in progress MUST be aborted.


## Appendix A. ECMAScript Sample Canonicalizer

**50.** (Appendix A)

> Below is an example of a JCS canonicalizer for usage with ECMAScript-based
> systems:
>
> ```text
>      ////////////////////////////////////////////////////////////
>      // Since the primary purpose of this code is highlighting //
>      // the core of the JCS algorithm, error handling and      //
>      // UTF-8 generation were not implemented.                 //
>      ////////////////////////////////////////////////////////////
>      var canonicalize = function(object) {
> 
>          var buffer = '';
>          serialize(object);
>          return buffer;
> 
>          function serialize(object) {
>              if (object === null || typeof object !== 'object' ||
>                  object.toJSON != null) {
>                  /////////////////////////////////////////////////
>                  // Primitive type or toJSON, use "JSON"        //
>                  /////////////////////////////////////////////////
>                  buffer += JSON.stringify(object);
> 
>              } else if (Array.isArray(object)) {
>                  /////////////////////////////////////////////////
>                  // Array - Maintain element order              //
>                  /////////////////////////////////////////////////
>                  buffer += '[';
>                  let next = false;
>                  object.forEach((element) => {
>                      if (next) {
>                          buffer += ',';
>                      }
>                      next = true;
>                      /////////////////////////////////////////
>                      // Array element - Recursive expansion //
>                      /////////////////////////////////////////
>                      serialize(element);
>                  });
>                  buffer += ']';
> 
>              } else {
>                  /////////////////////////////////////////////////
>                  // Object - Sort properties before serializing //
>                  /////////////////////////////////////////////////
>                  buffer += '{';
>                  let next = false;
>                  Object.keys(object).sort().forEach((property) => {
>                      if (next) {
>                          buffer += ',';
>                      }
>                      next = true;
>                      /////////////////////////////////////////////
>                      // Property names are strings, use "JSON"  //
>                      /////////////////////////////////////////////
>                      buffer += JSON.stringify(property);
>                      buffer += ':';
>                      //////////////////////////////////////////
>                      // Property value - Recursive expansion //
>                      //////////////////////////////////////////
>                      serialize(object[property]);
>                  });
>                  buffer += '}';
>              }
>          }
>      };
> ```


## Appendix B. Number Serialization Samples

**51.** (Appendix B)

> The following table holds a set of ECMAScript-compatible number
> serialization samples, including some edge cases. The column "IEEE 754"
> refers to the internal ECMAScript representation of the "Number" data type,
> which is based on the IEEE 754 [IEEE754] standard using 64-bit
> (double-precision) values, here expressed in hexadecimal.

**52.** (Appendix B (Table 1))

> ```text
>    +==================+===========================+====================+
>    |     IEEE 754     |    JSON Representation    |      Comment       |
>    +==================+===========================+====================+
>    | 0000000000000000 | 0                         | Zero               |
>    +------------------+---------------------------+--------------------+
>    | 8000000000000000 | 0                         | Minus zero         |
>    +------------------+---------------------------+--------------------+
>    | 0000000000000001 | 5e-324                    | Min pos number     |
>    +------------------+---------------------------+--------------------+
>    | 8000000000000001 | -5e-324                   | Min neg number     |
>    +------------------+---------------------------+--------------------+
>    | 7fefffffffffffff | 1.7976931348623157e+308   | Max pos number     |
>    +------------------+---------------------------+--------------------+
>    | ffefffffffffffff | -1.7976931348623157e+308  | Max neg number     |
>    +------------------+---------------------------+--------------------+
>    | 4340000000000000 | 9007199254740992          | Max pos int    (1) |
>    +------------------+---------------------------+--------------------+
>    | c340000000000000 | -9007199254740992         | Max neg int    (1) |
>    +------------------+---------------------------+--------------------+
>    | 4430000000000000 | 295147905179352830000     | ~2**68         (2) |
>    +------------------+---------------------------+--------------------+
>    | 7fffffffffffffff |                           | NaN            (3) |
>    +------------------+---------------------------+--------------------+
>    | 7ff0000000000000 |                           | Infinity       (3) |
>    +------------------+---------------------------+--------------------+
>    | 44b52d02c7e14af5 | 9.999999999999997e+22     |                    |
>    +------------------+---------------------------+--------------------+
>    | 44b52d02c7e14af6 | 1e+23                     |                    |
>    +------------------+---------------------------+--------------------+
>    | 44b52d02c7e14af7 | 1.0000000000000001e+23    |                    |
>    +------------------+---------------------------+--------------------+
>    | 444b1ae4d6e2ef4e | 999999999999999700000     |                    |
>    +------------------+---------------------------+--------------------+
>    | 444b1ae4d6e2ef4f | 999999999999999900000     |                    |
>    +------------------+---------------------------+--------------------+
>    | 444b1ae4d6e2ef50 | 1e+21                     |                    |
>    +------------------+---------------------------+--------------------+
>    | 3eb0c6f7a0b5ed8c | 9.999999999999997e-7      |                    |
>    +------------------+---------------------------+--------------------+
>    | 3eb0c6f7a0b5ed8d | 0.000001                  |                    |
>    +------------------+---------------------------+--------------------+
>    | 41b3de4355555553 | 333333333.3333332         |                    |
>    +------------------+---------------------------+--------------------+
>    | 41b3de4355555554 | 333333333.33333325        |                    |
>    +------------------+---------------------------+--------------------+
>    | 41b3de4355555555 | 333333333.3333333         |                    |
>    +------------------+---------------------------+--------------------+
>    | 41b3de4355555556 | 333333333.3333334         |                    |
>    +------------------+---------------------------+--------------------+
>    | 41b3de4355555557 | 333333333.33333343        |                    |
>    +------------------+---------------------------+--------------------+
>    | becbf647612f3696 | -0.0000033333333333333333 |                    |
>    +------------------+---------------------------+--------------------+
>    | 43143ff3c1cb0959 | 1424953923781206.2        | Round to even  (4) |
>    +------------------+---------------------------+--------------------+
> 
>       Table 1: ECMAScript-Compatible JSON Number Serialization Samples
> ```

**53.** (Appendix B (Note 1))

> For maximum compliance with the ECMAScript "JSON" object, values that are to
> be interpreted as true integers SHOULD be in the range -9007199254740991 to
> 9007199254740991. However, how numbers are used in applications does not
> affect the JCS algorithm.

**54.** (Appendix B (Note 2)) _[lowercase/implied]_

> Although a set of specific integers like 2**68 could be regarded as having
> extended precision, the JCS/ECMAScript number serialization algorithm does
> not take this into consideration.

**55.** (Appendix B (Note 3)) _[lowercase/implied]_

> Values out of range are not permitted in JSON. See Section 3.2.2.3.

**56.** (Appendix B (Note 4)) _[lowercase/implied]_

> This number is exactly 1424953923781206.25 but will, after the "Note 2" rule
> mentioned in Section 3.2.2.3, be truncated and rounded to the closest even
> value.

**57.** (Appendix B) _[lowercase/implied]_

> For a more exhaustive validation of a JCS number serializer, you may test
> against a file (currently) available in the development portal (see Appendix
> I) containing a large set of sample values. Another option is running V8
> [V8] as a live reference together with a program generating a substantial
> amount of random IEEE 754 values.


## Appendix C. Canonicalized JSON as "Wire Format"

**58.** (Appendix C) _[lowercase/implied]_

> Since the result from the canonicalization process (see Section 3.2.4) is
> fully valid JSON, it can also be used as "Wire Format". However, this is
> just an option since cryptographic schemes based on JCS, in most cases,
> would not depend on that externally supplied JSON data already being
> canonicalized.

**59.** (Appendix C (address record example))

> In fact, the ECMAScript standard way of serializing objects using
> "JSON.stringify()" produces a more "logical" format, where properties are
> kept in the order they were created or received. The example below shows an
> address record that could benefit from ECMAScript standard serialization:
>
> ```text
>      {
>        "name": "John Doe",
>        "address": "2000 Sunset Boulevard",
>        "city": "Los Angeles",
>        "zip": "90001",
>        "state": "CA"
>      }
> ```

**60.** (Appendix C) _[lowercase/implied]_

> Using canonicalization, the properties above would be output in the order
> "address", "city", "name", "state", and "zip", which adds fuzziness to the
> data from a human (developer or technical support) perspective.
> Canonicalization also converts JSON data into a single line of text, which
> may be less than ideal for debugging and logging.


## Appendix D. Dealing with Big Numbers

**61.** (Appendix D (sample object))

> There are several issues associated with the JSON number type, here
> illustrated by the following sample object:
>
> ```text
>      {
>        "giantNumber": 1.4e+9999,
>        "payMeThis": 26000.33,
>        "int64Max": 9223372036854775807
>      }
> ```

**62.** (Appendix D) _[lowercase/implied]_

> Although the sample above conforms to JSON [RFC8259], applications would
> normally use different native data types for storing "giantNumber" and
> "int64Max". In addition, monetary data like "payMeThis" would presumably not
> rely on floating-point data types due to rounding issues with respect to
> decimal arithmetic.

**63.** (Appendix D) _[lowercase/implied]_

> The established way of handling this kind of "overloading" of the JSON
> number type (at least in an extensible manner) is through mapping
> mechanisms, instructing parsers what to do with different properties based
> on their name. However, this greatly limits the value of using the JSON
> number type outside of its original, somewhat constrained JavaScript
> context. The ECMAScript "JSON" object does not support mappings to the JSON
> number type either.

**64.** (Appendix D)

> Due to the above, numbers that do not have a natural place in the current
> JSON ecosystem MUST be wrapped using the JSON string type. This is close to
> a de facto standard for open systems. This is also applicable for other data
> types that do not have direct support in JSON, like "DateTime" objects as
> described in Appendix E.

**65.** (Appendix D (BigNumber example))

> Aided by a system using the JSON string type, be it programmatic like
>
> ```text
>      var obj = JSON.parse('{"giantNumber": "1.4e+9999"}');
>      var biggie = new BigNumber(obj.giantNumber);
> ```

**66.** (Appendix D) _[lowercase/implied]_

> or declarative schemes like OpenAPI [OPENAPI], JCS imposes no limits on
> applications, including when using ECMAScript.


## Appendix E. String Subtype Handling

**67.** (Appendix E)

> Due to the limited set of data types featured in JSON, the JSON string type
> is commonly used for holding subtypes. This can, depending on JSON parsing
> method, lead to interoperability problems, which MUST be dealt with by
> JCS-compliant applications targeting a wider audience.

**68.** (Appendix E (subtype sample object))

> Assume you want to parse a JSON object where the schema designer assigned
> the property "big" for holding a "BigInt" subtype and "time" for holding a
> "DateTime" subtype, while "val" is supposed to be a JSON number compliant
> with JCS. The following example shows such an object:
>
> ```text
>      {
>        "time": "2019-01-28T07:45:10Z",
>        "big": "055",
>        "val": 3.5
>      }
> ```

**69.** (Appendix E (parse statement))

> Parsing of this object can be accomplished by the following ECMAScript
> statement:
>
> ```text
>      var object = JSON.parse(JSON_object_featured_as_a_string);
> ```

**70.** (Appendix E (subtype extraction))

> After parsing, the actual data can be extracted, which for subtypes, also
> involves a conversion step using the result of the parsing process (an
> ECMAScript object) as input:
>
> ```text
>      ... = new Date(object.time); // Date object
>      ... = BigInt(object.big);    // Big integer
>      ... = object.val;            // JSON/JS number
> ```

**71.** (Appendix E) _[lowercase/implied]_

> Note that the "BigInt" data type is currently only natively supported by V8
> [V8].

**72.** (Appendix E (canonicalized result, plain JSON.parse))

> Canonicalization of "object" using the sample code in Appendix A would
> return the following string:
>
> ```text
>      {"big":"055","time":"2019-01-28T07:45:10Z","val":3.5}
> ```

**73.** (Appendix E (stream-based parsing))

> Although this is (with respect to JCS) technically correct, there is another
> way of parsing JSON data, which also can be used with ECMAScript as shown
> below:
>
> ```text
>      // "BigInt" requires the following code to become JSON serializable
>      BigInt.prototype.toJSON = function() {
>          return this.toString();
>      };
> 
>      // JSON parsing using a "stream"-based method
>      var object = JSON.parse(JSON_object_featured_as_a_string,
>          (k,v) => k == 'time' ? new Date(v) : k == 'big' ? BigInt(v) : v
>      );
> ```

**74.** (Appendix E (canonicalized result, reviver-based parse))

> If you now apply the canonicalizer in Appendix A to "object", the following
> string would be generated:
>
> ```text
>      {"big":"55","time":"2019-01-28T07:45:10.000Z","val":3.5}
> ```

**75.** (Appendix E) _[lowercase/implied]_

> In this case, the string arguments for "big" and "time" have changed with
> respect to the original, presumably making an application depending on JCS
> fail.

**76.** (Appendix E) _[lowercase/implied]_

> The reason for the deviation is that in stream- and schema-based JSON
> parsers, the original string argument is typically replaced on the fly by
> the native subtype that, when serialized, may exhibit a different and
> platform-dependent pattern.

**77.** (Appendix E)

> That is, stream- and schema-based parsing MUST treat subtypes as "pure"
> (immutable) JSON string types and perform the actual conversion to the
> designated native type in a subsequent step. In modern programming platforms
> like Go, Java, and C#, this can be achieved with moderate efforts by
> combining annotations, getters, and setters. Below is an example in
> C#/Json.NET showing a part of a class that is serializable as a JSON object:

**78.** (Appendix E (C#/Json.NET pure-string pattern))

> ```text
>      // The "pure" string solution uses a local
>      // string variable for JSON serialization while
>      // exposing another type to the application
>      [JsonProperty("amount")]
>      private string _amount;
> 
>      [JsonIgnore]
>      public decimal Amount {
>          get { return decimal.Parse(_amount); }
>          set { _amount = value.ToString(); }
>      }
> ```

**79.** (Appendix E) _[lowercase/implied]_

> In an application, "Amount" can be accessed as any other property while it
> is actually represented by a quoted string in JSON contexts.

**80.** (Appendix E (Note)) _[lowercase/implied]_

> Note: The example above also addresses the constraints on numeric data
> implied by I-JSON (the C# "decimal" data type has quite different
> characteristics compared to IEEE 754 double precision).


### Appendix E.1. Subtypes in Arrays

**81.** (Appendix E.1) _[lowercase/implied]_

> Since the JSON array construct permits mixing arbitrary JSON data types,
> custom parsing and serialization code may be required to cope with subtypes
> anyway.


## Appendix F. Implementation Guidelines

**82.** (Appendix F) _[lowercase/implied]_

> The optimal solution is integrating support for JCS directly in JSON
> serializers (parsers need no changes). That is, canonicalization would just
> be an additional "mode" for a JSON serializer. However, this is currently
> not the case. Fortunately, JCS support can be introduced through externally
> supplied canonicalizer software acting as a post processor to existing JSON
> serializers. This arrangement also relieves the JCS implementer from having
> to deal with how underlying data is to be represented in JSON.

**83.** (Appendix F (signature creation scheme, six ordered steps))

> The post processor concept enables signature creation schemes like the
> following:
>
> ```text
>    1.  Create the data to be signed.
> 
>    2.  Serialize the data using existing JSON tools.
> 
>    3.  Let the external canonicalizer process the serialized data and
>        return canonicalized result data.
> 
>    4.  Sign the canonicalized data.
> 
>    5.  Add the resulting signature value to the original JSON data
>        through a designated signature property.
> 
>    6.  Serialize the completed (now signed) JSON object using existing
>        JSON tools.
> ```

**84.** (Appendix F (signature verification scheme, six ordered steps))

> A compatible signature verification scheme would then be as follows:
>
> ```text
>    1.  Parse the signed JSON data using existing JSON tools.
> 
>    2.  Read and save the signature value from the designated signature
>        property.
> 
>    3.  Remove the signature property from the parsed JSON object.
> 
>    4.  Serialize the remaining JSON data using existing JSON tools.
> 
>    5.  Let the external canonicalizer process the serialized data and
>        return canonicalized result data.
> 
>    6.  Verify that the canonicalized data matches the saved signature
>        value using the algorithm and key used for creating the
>        signature.
> ```

**85.** (Appendix F) _[lowercase/implied]_

> A canonicalizer like above is effectively only a "filter", potentially
> usable with a multitude of quite different cryptographic schemes.

**86.** (Appendix F) _[lowercase/implied]_

> Using a JSON serializer with integrated JCS support, the serialization
> performed before the canonicalization step could be eliminated for both
> processes.


## Appendix G. Open-Source Implementations

**87.** (Appendix G)

> The following open-source implementations have been verified to be
> compatible with JCS:
>
> ```text
>    *  JavaScript: <https://www.npmjs.com/package/canonicalize>
> 
>    *  Java: <https://github.com/erdtman/java-json-canonicalization>
> 
>    *  Go: <https://github.com/cyberphone/json-
>       canonicalization/tree/master/go>
> 
>    *  .NET/C#: <https://github.com/cyberphone/json-
>       canonicalization/tree/master/dotnet>
> 
>    *  Python: <https://github.com/cyberphone/json-
>       canonicalization/tree/master/python3>
> ```


## Appendix H. Other JSON Canonicalization Efforts

**88.** (Appendix H)

> There are (and have been) other efforts creating "Canonical JSON". Below is
> a list of URLs to some of them:
>
> ```text
>    *  <https://tools.ietf.org/html/draft-staykov-hu-json-canonical-form-
>       00>
> 
>    *  <https://gibson042.github.io/canonicaljson-spec/>
> 
>    *  <http://wiki.laptop.org/go/Canonical_JSON>
> ```

**89.** (Appendix H) _[lowercase/implied]_

> The listed efforts all build on text-level JSON-to-JSON transformations. The
> primary feature of text-level canonicalization is that it can be made
> neutral to the flavor of JSON used. However, such schemes also imply major
> changes to the JSON parsing process, which is a likely hurdle for adoption.
> Albeit at the expense of certain JSON and application constraints, JCS was
> designed to be compatible with existing JSON tools.


## Appendix I. Development Portal

**90.** (Appendix I)

> ```text
>    The JCS specification is currently developed at:
>    <https://github.com/cyberphone/ietf-json-canon>.
> 
>    JCS source code and extensive test data is available at:
>    <https://github.com/cyberphone/json-canonicalization>.
> ```


## Section 6.1. Normative References

**91.** (§6.1)

> ```text
>    [ECMA-262] ECMA International, "ECMAScript 2019 Language
>               Specification", Standard ECMA-262 10th Edition, June 2019,
>               <https://www.ecma-international.org/ecma-262/10.0/
>               index.html>.
> 
>    [IEEE754]  IEEE, "IEEE Standard for Floating-Point Arithmetic", IEEE
>               754-2019, DOI 10.1109/IEEESTD.2019.8766229,
>               <https://ieeexplore.ieee.org/document/8766229>.
> 
>    [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
>               Requirement Levels", BCP 14, RFC 2119,
>               DOI 10.17487/RFC2119, March 1997,
>               <https://www.rfc-editor.org/info/rfc2119>.
> 
>    [RFC7493]  Bray, T., Ed., "The I-JSON Message Format", RFC 7493,
>               DOI 10.17487/RFC7493, March 2015,
>               <https://www.rfc-editor.org/info/rfc7493>.
> 
>    [RFC8174]  Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC
>               2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174,
>               May 2017, <https://www.rfc-editor.org/info/rfc8174>.
> 
>    [RFC8259]  Bray, T., Ed., "The JavaScript Object Notation (JSON) Data
>               Interchange Format", STD 90, RFC 8259,
>               DOI 10.17487/RFC8259, December 2017,
>               <https://www.rfc-editor.org/info/rfc8259>.
> 
>    [UCNORM]   The Unicode Consortium, "Unicode Normalization Forms",
>               <https://www.unicode.org/reports/tr15/>.
> 
>    [UNICODE]  The Unicode Consortium, "The Unicode Standard",
>               <https://www.unicode.org/versions/latest/>.
> ```
