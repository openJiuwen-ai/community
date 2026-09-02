# Guidelines for License and Special License Review of the openJiuwen Project Code

## Purpose

The openJiuwen community adheres to the [Open Source Definition](https://opensource.org/docs/osd). Software that satisfies this definition is recognized by the openJiuwen community as open-source software. These guidelines specify the open-source software licenses adopted by the project code within the openJiuwen community, as well as the accepted special licenses and the associated review processes and rules.

## Scope

These guidelines apply only to the project code distributed within the openJiuwen community and to third-party open-source software code introduced into the openJiuwen community. They do not apply to scenarios in which the openJiuwen project is used by individuals or enterprises to develop other products, nor to scenarios involving the standalone distribution of third-party open-source software.

## Definitions

openJiuwen project: openJiuwen is an open-source project incubated and operated by Huawei. Its goal is to provide an open, open-source intelligent-agent development and runtime framework for the AI era, enabling industries across all sectors to rapidly and at high quality deploy AI agents, and to benefit human society through AI.

Community hosting address of the openJiuwen project: https://gitcode.com/openJiuwen.

openJiuwen project contributed code: Code for which the contributor holds the copyright and that is contributed to the openJiuwen project, and that is distributed by the openJiuwen project at the project's community hosting address.

openJiuwen project third-party dependencies: Third-party open-source code on which the openJiuwen project depends, and that is redistributed by the openJiuwen project at the project's community hosting address following the depended-upon software.

##  License Whitelist for Contributed Code

In principle, all openJiuwen project contributed code should be provided in source-code form and distributed under an open-source license approved by the [Open Source Initiative (OSI)](https://opensource.org/).

Given the wide variety of open-source licenses, the openJiuwen project recommends that contributed code prioritize the use of licenses in the whitelist below for distribution.

The license whitelist for openJiuwen project contributed code includes:

- Apache License 2.0 (Apache-2.0)

##  List of Acceptable and Unacceptable Licenses for Third-Party Dependencies of the openJiuwen Project

The openJiuwen project may also introduce or depend on different third-party open-source software. The types and forms of licenses adopted by such third-party open-source software may vary. To ensure the open-source nature of the project, the depended-upon third-party open-source software must have a clearly defined upstream open-source community, and the introduction of the third-party open-source software must not give rise to legal issues of license compatibility.

### Whitelist of Acceptable Licenses for Third-Party Dependencies

Licenses compatible with the Apache-2.0 license may be accepted. The openJiuwen project recommends prioritizing the acceptance of third-party dependencies that adopt the following licenses:

- Academic Free License 3.0 (AFL-3.0)

- Apache License 2.0 (Apache-2.0)

- Apache Software License 1.1. Including variants:

  - PHP License 3.01
  - MX4J License

- Boost Software License (BSL-1.0)

- BSD License:

  - 3-clause BSD License
  - 2-clause BSD License
  - DOM4J license
  - PostgreSQL License

- ISC

- ICU

- MIT License (MIT) / X11

- MIT No Attribution License (MIT-0)

- Mulan Permissive Software License v2 (MulanPSL-2.0)

- The Unlicense

- W3C License (W3C)

- University of Illinois/NCSA

- X.Net

- zlib/libpng

- FSF autoconf license

- DejaVu Fonts (Bitstream Vera/Arev licenses)

- OOXML XSD ECMA License

- Microsoft Public License (MsPL)

- Python Software Foundation License

- Python Imaging Library Software License

- Adobe Postcript(R) AFM files

- Boost Software License Version 1.0

- WTF Public License

- The Romantic WTF public license

- UNICODE, INC. LICENSE AGREEMENT - DATA FILES AND SOFTWARE

- Zope Public License 2.0

- ACE license

- Oracle Universal Permissive License (UPL) Version 1.0

- Open Grid Forum License

- Google "Additional IP Rights Grant  (Patents)" file

- Historical Permission Notice and Disclaimer

### List of Licenses Not Recommended for Third-Party Dependencies

In principle, licenses that do not support commercial use, as well as other licenses that contain unreasonable restrictions or obligations, are not recommended for acceptance. The openJiuwen project does not recommend accepting third-party dependencies that adopt the following licenses:

- Intel Simplified Software License
- JSR-275 License
- Microsoft Limited Public License
- Amazon Software License (ASL)
- Java SDK for Satori RTM  license
- Redis Source Available License (RSAL)
- Booz Allen Public License
- Confluent Community License Version 1.0
- Any license including the Commons Clause License Condition v1.0
- Creative Commons Non-Commercial variants
- Sun Community Source License 3.0
- GNU GPL 3
- GNU Affero GPL 3
- BSD-4-Clause/BSD-4-Clause (University of California-Specific)
- Facebook BSD+Patents license
- NPL 1.0/NPL 1.1
- The Solipsistic Eclipse Public License
- The "Don't Be A Dick" Public License
- JSON License

## Rules for Introducing Special Licenses

In principle, the openJiuwen project accepts openJiuwen project contributed code according to the [project license whitelist](#license-whitelist-for-contributed-code) specified above, and introduces third-party dependencies according to the [license whitelist](#whitelist-of-acceptable-licenses-for-third-party-dependencies) specified above.

If a license outside the above whitelists needs to be accepted (hereinafter referred to as a "special license"; any license not within the whitelists defined in these guidelines is a special license), it must undergo the openJiuwen project code special license review and comply with the relevant rules.

### Special License Review Process of the openJiuwen Project

#### Organization of the Special License Review

The special license review is organized by the openJiuwen Compliance SIG. Participants must include at least a PMC representative, a legal representative, and a Compliance SIG representative.

#### Triggers for the Special License Review

A software module that intends to adopt a special license proactively submits an application.

During code development, when a special license is planned to be adopted, a declaration may be proactively submitted to the Compliance SIG to initiate a special license review. The special license application materials must include at least the following:

The name of the software module, a description of the business scenario, the name(s) of the special license(s) involved and related information (for third-party dependencies, the licenses used by both direct and indirect dependencies must be included), and the license compliance scanning tool's inspection report on the code (e.g., an OAT scan report).

The Compliance SIG periodically aggregates gate-check results to identify software modules that adopt special licenses and organizes reviews.

Based on tool inspection results, the Compliance SIG may organize a special license review upon discovering code that will adopt a special license (e.g., third-party dependencies adopting non-whitelist licenses, contributed code adopting proprietary licenses, or cases where only binary or object code is provided).

#### Conclusion of the Special License Review

Passing the special license review is a mandatory condition for a software module that adopts a special license to pass the code compliance check within the openJiuwen project. A software module that has not undergone the special license review cannot be merged into the openJiuwen main branch. The special license review conclusion for that software module must serve as a mandatory condition for its openJiuwen QA SIG exit review / incubation graduation review.

### Special License Review Rules

- **Rule 1**: Contributed code should prioritize the use of the Apache-2.0 license to ensure license uniformity. If contributed code adopts a license other than Apache-2.0, there must be a legitimate reason. The special license adopted for contributed code should avoid licenses that entail open-source obligations.

- **Rule 2**: The special license adopted for contributed code or third-party dependencies must satisfy the basic principles of distributability and compatibility for open-source licenses. That is, the special license must support downstream users in redistributing the relevant code, and the special license must not have compatibility issues with the licenses of the existing project code that has already been accepted.

- **Rule 3**: The special license adopted for contributed code or third-party dependencies must not contain unreasonable restrictions. For example: a special license that contains open-source license obligations that cannot be fulfilled or are difficult to fulfill may not be accepted, such as advertising clauses and beerware clauses; a special license that contains unreasonable restriction or constraint clauses may not be accepted, such as commercial-use restriction clauses, field-of-use restriction clauses, clauses that discriminate against particular technology fields, or clauses targeting specific products.

- **Rule 4**: The special license adopted for a third-party dependency must ensure that the third-party dependency does not affect or change the existing license of the relevant code.

- **Rule 5**: Where non-source-code form (binary or object code) contributions are involved or third-party dependencies are introduced, it must be ensured that the non-source-code form of the code adopts an open-source license and satisfies the above rules. If the code is provided in non-source-code form and adopts a self-drafted license, it must be approved by the PMC (in principle, only special licenses adopted for algorithms related to necessary hardware or their specific implementations may be accepted, such as GPU, Wi-Fi firmware, hardware codec algorithms, etc.). If the PMC approves, the corresponding self-drafted license must be further reviewed and approved by the openJiuwen Compliance SIG group.
