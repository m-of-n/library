---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-normative
record: cisa-secure-by-design-pledge-2024
type: normative
updated: "2026-10-02"
reviewed_by: ""
---

# CISA Secure by Design Pledge (May 2024) — normative statements

Source: 'Secure By Design Pledge' PDF, 7 pp (created 2024-05-06), sha256 3e9cd705…bcb, cross-checked against the live pledge web page (snapshot 2026-09-20). Every statement verbatim, grouped by goal; typed goal / recommendation / example-approach / example-evidence / note. Differences between PDF and web page: (1) Goal 6 — the web page's Goal line stops at 'demonstrate transparency in vulnerability reporting' and moves the CWE/CPE and timely-CVE criteria into Context; (2) the web page adds an Overview paragraph (WEB-1, WEB-2) and a disclaimer (WEB-3); (3) Goal 7 sub-bullets are run together on the web page. Otherwise identical.

## Preamble (PDF p.1)

- **PRE-1** (Preamble, p.1; *scope*, verb "focused on", actor: software manufacturer (pledge signer)) — "This is a voluntary pledge focused on enterprise software products and services, including on-premises software, cloud services, and software as a service (SaaS)."
- **PRE-2** (Preamble, p.1; *scope*, verb "are not scoped", actor: software manufacturer (pledge signer)) — "Physical products such as IoT devices and consumer products are not scoped in the pledge, though companies who wish to demonstrate progress in those areas are welcome to do so."
- **PRE-3** (Preamble, p.1; *commitment*, verb "are pledging", actor: software manufacturer (pledge signer)) — "By participating in the pledge, software manufacturers are pledging to make a good-faith effort to work towards the goals listed below over the following year."
- **PRE-4** (Preamble, p.1; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "In the case where a software manufacturer is able to make measurable progress towards a goal, the manufacturer should publicly document how they have achieved such progress within one year of signing the pledge."
- **PRE-5** (Preamble, p.1; *recommendation*, verb "is encouraged", actor: software manufacturer (pledge signer)) — "Where the software manufacturer is not able to make measurable progress, the manufacturer is encouraged to, within one year of signing the pledge, share with CISA how the manufacturer has worked towards the goal and any challenges faced."
- **PRE-6** (Preamble, p.1; *recommendation*, verb "is encouraged", actor: software manufacturer (pledge signer)) — "And, in the spirit of radical transparency, the manufacturer is encouraged to publicly document their approach so that others can learn."
- **PRE-7** (Preamble, p.1; *status*, verb "is voluntary", actor: software manufacturer (pledge signer)) — "This pledge is voluntary and not legally binding."
- **PRE-8** (Preamble, p.1; *permission*, verb "have the discretion", actor: software manufacturer (pledge signer)) — "To enable a variety of approaches, software manufacturers participating in the pledge have the discretion to decide how best they can meet and demonstrate the core criteria of each goal."
- **PRE-9** (Preamble, p.1; *permission*, verb "can take", actor: software manufacturer (pledge signer)) — "Demonstrating measurable progress across the manufacturer's products can take a variety of forms — such as by taking action on all the manufacturer's products, or by choosing a set of products to first address and publishing a roadmap for other products."
- **PRE-10** (Preamble, p.1; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "In such a case where a software manufacturer already meets or exceeds a goal, the manufacturer should publicly describe how they are doing so."

## Web-page-only statements

- **WEB-1** (Web page https://www.cisa.gov/securebydesign/pledge (snapshot 2026-09-20), Overview para 2 — not in the PDF; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "During the design phase of a product's development lifecycle, companies should implement Secure by Design principles to significantly decrease the number of exploitable flaws before introducing them to the market for widespread use or consumption."
- **WEB-2** (Web page https://www.cisa.gov/securebydesign/pledge (snapshot 2026-09-20), Overview para 2 — not in the PDF; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "Out-of-the-box, products should be secure with additional security features such as multi-factor authentication (MFA), logging, and single sign-on (SSO) available at no extra cost."
- **WEB-3** (Web page disclaimer (snapshot 2026-09-20) — not in the PDF; *status*, verb "does not enforce nor verify", actor: CISA) — "CISA does not enforce nor verify adherence to the pledge."

## Goal 1 — Multi-Factor Authentication (MFA)

- **G1** (Goal 1 MULTI-FACTOR AUTHENTICATION (MFA), p.2 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate actions taken to measurably increase the use of multi-factor authentication across the manufacturer's products."
- **G1-C1** (Goal 1 — CONTEXT; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "Manufacturers should seek to increase MFA enrollment among their customers across the board, with an emphasis where possible of adopting phishing-resistant MFA and increasing enrollment by administrators."
- **G1-N1** (Goal 1 — Note; *note*, verb "(note)", actor: software manufacturer (pledge signer)) — "Note: other phishing-resistant forms of authentication, such as passkeys, meet this definition even if they are the sole form of authentication."
- **G1-A1** (Goal 1 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Enabling MFA by default for users and administrators (e.g., upon first registration, requiring users and administrators to configure MFA)."
- **G1-A2** (Goal 1 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Implementing "seat belt chimes" in products to nudge users towards enabling MFA. This could include, for instance, banners or interstitials notifying users or administrators that MFA is not enabled or suggesting that administrators enable phishing-resistant MFA."
- **G1-A3** (Goal 1 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Supporting standards-based single sign-on (SSO) in the baseline version of the product, allowing customers to configure with their own identity provider that supports MFA."
- **G1-M1** (Goal 1 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing aggregate statistics of MFA adoption over time, broken down by user type (e.g., standard user, administrator) and MFA type (e.g., SMS, TOTP, FIDO2)."
- **G1-M2** (Goal 1 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a blog post describing measurable progress made, such as where MFA has been enabled by default, and highlighting where barriers exist."
- **G1-M3** (Goal 1 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Participating in fora to advance long-term standards around MFA or authentication and demonstrating how these will result in measurable progress towards this goal."
- **G1-N2** (Goal 1 — Note; *note*, verb "(note)", actor: software manufacturer (pledge signer)) — "Note: For this goal, manufacturers could demonstrate measurable progress either through results of customer behavior (such as a change in the use of MFA across their products), or through changes to the product itself (such as enabling MFA by default)."

## Goal 2 — Default Passwords

- **G2** (Goal 2 DEFAULT PASSWORDS, pp.2-3 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate measurable progress towards reducing default passwords across the manufacturers' products."
- **G2-C0** (Goal 2 — CONTEXT; *definition*, verb "defines", actor: software manufacturer (pledge signer)) — "Default passwords, which CISA defines as universally-shared passwords that are present by default across a product, continue to enable damaging cyberattacks."
- **G2-C1** (Goal 2 — CONTEXT; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "Default passwords should be replaced with more secure authentication mechanisms, as detailed in the examples below (and, preferably, MFA as detailed above)."
- **G2-C2** (Goal 2 — CONTEXT; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "At the end of provisioning, only the customer should possess their authentication credentials."
- **G2-A1** (Goal 2 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Providing random, instance-unique initial passwords for the product."
- **G2-A2** (Goal 2 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Requiring the user who installs the product to create a strong password at the start of the installation process."
- **G2-A3** (Goal 2 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Providing time-limited setup passwords that disable themselves when a setup process is complete and require configuration of a secure password (or more secure authentication approaches, such as phishing-resistant MFA)."
- **G2-A4** (Goal 2 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Requiring physical access for initial setup and the specification of instance-unique credentials."
- **G2-A5** (Goal 2 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Conducting campaigns or offering updates that transition existing deployments from default passwords to more secure authentication mechanisms."
- **G2-M1** (Goal 2 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a blog post describing how the manufacturer is moving past (or has already eliminated) default passwords in various product lines."
- **G2-M2** (Goal 2 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing the number of products that have default passwords over time."
- **G2-M3** (Goal 2 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing details on the number of customers transitioned from default passwords to more secure authentication mechanisms."

## Goal 3 — Reducing Entire Classes of Vulnerability

- **G3** (Goal 3 REDUCING ENTIRE CLASSES OF VULNERABILITY, pp.3-4 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate actions taken towards enabling a significant measurable reduction in the prevalence of one or more vulnerability classes across the manufacturer's products."
- **G3-C1** (Goal 3 — CONTEXT; *permission*, verb "can", actor: software manufacturer (pledge signer)) — "Software manufacturers can pick one or more vulnerability classes for the pledge that they work to reduce over the course of the year."
- **G3-A1** (Goal 3 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Consistently enforcing the use of parametrized queries to prevent SQL injection attacks."
- **G3-A2** (Goal 3 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Adopting web template frameworks with built-in protection against cross-site scripting vulnerabilities."
- **G3-A3** (Goal 3 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Developing a memory safe roadmap to transition to memory safe languages in a prioritized approach and writing new products in memory safe languages."
- **G3-A4** (Goal 3 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Providing secure defaults for developers, such as by providing "building blocks" of secure functions and libraries that make it impossible (or significantly more difficult) to introduce a certain class of vulnerability."
- **G3-M1** (Goal 3 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a blog on how the manufacturer has worked in the past year to significantly reduce the prevalence of one or more classes of vulnerability. This may include analysis of the root cause (CWE) of CVEs over time in the manufacturer's products."
- **G3-M1-note** (Goal 3 — Examples of demonstrating measurable progress; *note*, verb "should be regarded", actor: assessor / reader of progress reports) — "CISA notes that successfully achieving this goal may actually lead to a short-term increase in CVEs as the manufacturer works to reduce that class of vulnerability — this should be regarded as a success if that class of vulnerability is reduced over the long run."
- **G3-M2** (Goal 3 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a memory safety roadmap, or a similar roadmap for other classes of vulnerability."

## Goal 4 — Security Patches

- **G4** (Goal 4 SECURITY PATCHES, pp.4-5 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate actions taken to measurably increase the installation of security patches by customers."
- **G4-C1** (Goal 4 — CONTEXT; *recommendation*, verb "should", actor: software manufacturer (pledge signer)) — "In line with the first Secure by Design principle, software manufacturers should take ownership of security outcomes of their customers – even after products are shipped."
- **G4-A1** (Goal 4 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Providing functionality to allow automatic installation of software patches when possible and enabling this functionality by default, where appropriate."
- **G4-A2** (Goal 4 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "Offering support for security patches on a widespread basis to customers."
- **G4-A3** (Goal 4 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "In the cases where products are end of life and security patches are no longer supported, clearly communicate the expected lifespan at time of sale and, when the product reaches end of life, clearly communicate this to customers and invest in provisioning capabilities to ease customer transitions to supported versions."
- **G4-A4** (Goal 4 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "For cloud or SaaS products, applying patches so that the burden is not on customers to patch."
- **G4-M1** (Goal 4 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing aggregate statistics of patch adoption by product over time (e.g., the percent of users using various versions of each product)."
- **G4-M2** (Goal 4 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a blog post demonstrating actions made to foster greater deployment of security patches by users, or that otherwise reduce customers' burden of patching."
- **G4-N1** (Goal 4 — Note; *note*, verb "(note)", actor: software manufacturer (pledge signer)) — "Note: For this goal, manufacturers could demonstrate measurable progress either through results of customer behavior (such as a change in the percent of users on various versions of a product), or through changes to the product itself (such as by functionality for automatic software patches)."

## Goal 5 — Vulnerability Disclosure Policy

- **G5** (Goal 5 VULNERABILITY DISCLOSURE POLICY, p.5 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, publish a vulnerability disclosure policy (VDP) that authorizes testing by members of the public on products offered by the manufacturer, commits to not recommending or pursuing legal action against anyone engaging in good faith efforts to follow the VDP, provides a clear channel to report vulnerabilities, and allows for public disclosure of vulnerabilities in line with coordinated vulnerability disclosure best practices and international standards."
- **G5-N1** (Goal 5 — Note; *note*, verb "(note)", actor: software manufacturer (pledge signer)) — "Note: due to the specific nature of this item, examples of achieving this goal are not included."
- **G5-M1** (Goal 5 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a public vulnerability disclosure policy in line with the above criteria."
- **G5-M2** (Goal 5 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a machine-readable description of the vulnerability disclosure policy (e.g., a security.txt file) to better enable discovery by researchers."
- **G5-M3** (Goal 5 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing blog posts reviewing findings and lessons learned from the vulnerability disclosure policy."

## Goal 6 — CVEs

- **G6** (Goal 6 CVES, pp.5-6 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate transparency in vulnerability reporting by including accurate Common Weakness Enumeration (CWE) and Common Platform Enumeration (CPE) fields in every Common Vulnerabilities and Exposures (CVE) record for the manufacturer's products."
- **G6-2** (Goal 6 CVES, pp.5-6 — GOAL; *goal*, verb "issue", actor: software manufacturer (pledge signer)) — "Additionally, issue CVEs in a timely manner for, at minimum, all critical or high impact vulnerabilities (whether discovered internally or by a third party) that either require actions by a customer to patch or have evidence of active exploitation."
- **G6-3** (Goal 6 — GOAL (continued); *recommendation*, verb "are encouraged", actor: software manufacturer (pledge signer)) — "While not required for this goal, companies are encouraged to go above and beyond by filing CVEs for other vulnerabilities that do not meet these criteria for the reasons described below."
- **G6-4** (Goal 6 — GOAL (continued); *recommendation*, verb "are encouraged", actor: software manufacturer (pledge signer)) — "Companies are also encouraged to explore additional ways to enrich their CVE records to help customers better respond to vulnerabilities."
- **G6-C1** (Goal 6 — CONTEXT; *note*, verb "cautions", actor: assessor / reader of progress reports) — "CISA cautions against interpreting the mere presence of CVEs as a negative sign, as the number of CVEs reported may rise in the short term as a software manufacturer implements Secure by Design principles – more comprehensive reporting of CVEs benefits everyone."
- **G6-N1** (Goal 6 — Note; *note*, verb "(note)", actor: software manufacturer (pledge signer)) — "Note: due to the specific nature of this item, examples of achieving this goal are not included."
- **G6-M1** (Goal 6 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing CWE and CPE fields in every CVE record for the manufacturer's products."
- **G6-M2** (Goal 6 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publicly describing the manufacturer's policy for when a CVE is issued."

## Goal 7 — Evidence of Intrusions

- **G7** (Goal 7 EVIDENCE OF INTRUSIONS, pp.6-7 — GOAL; *goal*, verb "demonstrate / publish", actor: software manufacturer (pledge signer)) — "Within one year of signing the pledge, demonstrate a measurable increase in the ability for customers to gather evidence of cybersecurity intrusions affecting the manufacturer's products."
- **G7-A1** (Goal 7 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "As part of the baseline version of a product, making available logs related to areas such as:"
- **G7-A2** (Goal 7 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "For cloud service providers and SaaS products, retaining logs for a set timeframe (e.g., 6 months) at no additional charge."
- **G7-A3** (Goal 7 — Example approaches; *example-approach*, verb "(example)", actor: software manufacturer (pledge signer)) — "In the cases where a product does not support the collection of these types of logs, the manufacturer publishes details on how customers can monitor and respond to cybersecurity incidents affecting their product."
- **G7-M1** (Goal 7 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Documenting the manufacturer's policies around providing logs and log retention (for cloud providers)."
- **G7-M2** (Goal 7 — Examples of demonstrating (measurable) progress; *example-evidence*, verb "(example)", actor: software manufacturer (pledge signer)) — "Publishing a roadmap for adding or improving logging capabilities to products where they do not currently support collecting certain types of logs."

## Goal 7 example approach 1 — sub-bullets (verbatim)

- Configuration changes or reading configuration settings;
- Identity (e.g., sign-in and token creation) and network flows, if applicable; and
- Data access or creation of business-relevant data.

## Sign-up template (web page mailto link, verbatim)

"My company, [INSERT NAME], would like to sign CISA's Secure by Design Pledge. I confirm that:
- My company is an enterprise software manufacturer and provides software products to customers within the United States.
- I have reviewed the full Secure by Design pledge located on CISA's website and I have authority to commit to the pledge on behalf of my company."
(to SecureByDesign@cisa.dhs.gov, subject "Taking CISA's Secure by Design Pledge")

