# OAuth & OpenID Link List

A list of selected specifications in the OAuth &amp; OpenID spaces and where to find them.

<details>
<summary>Abbreviations/key:</summary>

- **ImD**: Implementer's Draft (OIDF, provides IPR protection to the Implementers)
- **WG**: Working Group Draft
- **InD**: Individual Draft
- **ED**: Editor's Copy (version that reflects the most recent changes since the last WG draft)
- **Git**: Git Repository of the specification

*&nbsp;marks a status that is not yet official, under discussion, or proposed.
</details>

## Verifiable Credentials (VC)

### Credential Formats & Related Specifications


| **Name**                    | **Description**                                   | **Working Group** | **Status**          | **Links**                                                                                                                                                                                                                                                                             |
| --------------------------- | ------------------------------------------------- | ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SD-JWT**                  | Selective Disclosure for JWTs                     | IETF OAuth        | Working Group Draft | [WD](https://www.ietf.org/archive/id/draft-ietf-oauth-selective-disclosure-jwt-05.html)&nbsp;[ED](https://oauth-wg.github.io/oauth-selective-disclosure-jwt/#go.draft-ietf-oauth-selective-disclosure-jwt.html)&nbsp;[Git](https://github.com/oauth-wg/oauth-selective-disclosure-jwt) |
| **SD-JWT VC**               | Verifiable Credentials with SD-JWT                | IETF OAuth        | Working Group Draft | [WD](https://datatracker.ietf.org/doc/html/draft-terbu-oauth-sd-jwt-vc)&nbsp;[ED](https://vcstuff.github.io/draft-terbu-sd-jwt-vc/#go.draft-terbu-sd-jwt-vc.html)&nbsp;[Git](https://github.com/vcstuff/draft-terbu-sd-jwt-vc)                                                         |
| **JWT and CWT Status List** | Status list mechanism for JWT and CWT credentials | IETF OAuth*       | Individual Draft    | [ED](https://vcstuff.github.io/draft-looker-oauth-jwt-cwt-status-list/#go.draft-looker-oauth-jwt-cwt-status-list.html)&nbsp;[InD](https://datatracker.ietf.org/doc/html/draft-looker-oauth-jwt-cwt-status-list)                                                                       |

### Credential Issuance and Presentation

| **Name**                                              | **Description**                                                   | **Working Group** | **Status**              | **Links**                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------- | ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OpenID for Verifiable Presentations**               | OAuth 2.0-based mechanism for presentation of VCs                 | OpenID Connect    | 2nd Implementer's Draft | [ImD](https://openid.net/specs/openid-4-verifiable-presentations-1_0-ID2.html)&nbsp;[WD](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)&nbsp;[ED](https://openid.bitbucket.io/connect/openid-4-verifiable-presentations-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/connect/src/master/) |
| **OpenID for VC Issuance**                            | OAuth 2.0-based authorization for VC issuance                     | OpenID Connect    | Working Group Draft     | [WD](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)&nbsp;[ED](https://openid.bitbucket.io/connect/openid-4-verifiable-credential-issuance-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/connect/src/master/)                                                                         |
| **Self-Issued OpenID Provider v2** (SIOPv2)           | Enables End-Users to use OpenID Providers (OPs) that they control | OpenID Connect    | 1st Implementer's Draft | [WD](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html)&nbsp;[ED](https://openid.bitbucket.io/connect/openid-connect-self-issued-v2-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/connect/src/master/)                                                                                             |
| **OpenID for Verifiable Presentations over BLE**      | Using BLE for requesting the presentation of VCs                  | OpenID Connect    | Working Group Draft     | [WD](https://openid.net/specs/openid-4-verifiable-presentations-over-ble-1_0.html)&nbsp;[ED](https://openid.bitbucket.io/connect/openid-4-verifiable-presentations-over-ble-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/connect/src/master/)                                                                   |
| **OpenID Connect UserInfo Verifiable Credentials**    | UserInfo endpoint responses with Verifiable Credentials           | OpenID Connect    | Working Group Draft     | [WD](https://openid.net/specs/openid-connect-userinfo-vc-1_0-00.html)&nbsp;[ED](https://openid.bitbucket.io/connect/openid-connect-userinfo-vc-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/connect/src/master/)                                                                                                |
| **Security & Trust**                                  | Structured Security Analysis                                      | OpenID Connect*   | Early Draft             | [ED](https://vcstuff.github.io/oid4vc-security-and-trust/draft-oid4vc-security-and-trust.html)&nbsp;[Git](https://github.com/vcstuff/oid4vc-security-and-trust)                                                                                                                                                      |
| **OAuth 2.0 Attestation-Based Client Authentication** |                                                                   | IETF OAuth WG     | Working Group Draft     | WD&nbsp;[ED](https://vcstuff.github.io/draft-ietf-oauth-attestation-based-client-auth/draft-ietf-oauth-attestation-based-client-auth.html)&nbsp;[Git](https://github.com/vcstuff/draft-ietf-oauth-attestation-based-client-auth)                                                                                     |

### Profiles

| **Name**                                                             | **Description** | **Working Group** | **Status** | **Links**                                                                                                                                        |
| -------------------------------------------------------------------- | --------------- | ----------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **OpenID4VC High Assurance Interoperability Profile with SD-JWT VC** |                 | TBD               | Draft      | [ED](https://vcstuff.github.io/oid4vc-haip-sd-jwt-vc/#go.oid4vc-haip-sd-jwt-vc.html)&nbsp;[Git](https://github.com/vcstuff/oid4vc-haip-sd-jwt-vc) |

### Related

<!-- markdown-link-check-disable -->
| **Name**                      | **Description** | **Working Group** | **Status** | **Links**                                                                                                                           |
| ----------------------------- | --------------- | ----------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **DIF Presentation Exchange** |                 | DIF               | Draft      | [ED](https://identity.foundation/presentation-exchange/)&nbsp;[Git](https://github.com/decentralized-identity/presentation-exchange) |
<!-- markdown-link-check-enable -->

## eKYC & Identity Assurance

| **Name**                                            | **Description** | **Working Group** | **Status**            | **Links**                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------- | --------------- | ----------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OpenID Connect for Identity Assurance 1.0**       |                 | OpenID eKYC & IDA | Implementer's Draft 4 | [ImD](https://openid.net/specs/openid-connect-4-identity-assurance-1_0-ID4.html)&nbsp;[WD](https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html)&nbsp;[ED](https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html)&nbsp;[Git](https://bitbucket.org/openid/ekyc-ida/src/master/) |
| **OpenID Connect Authority claims extension**       |                 | OpenID eKYC & IDA | Working Group Draft   | [ED](https://openid.bitbucket.io/ekyc/openid-authority.html)&nbsp;[Git](https://bitbucket.org/openid/ekyc-ida/src/master/)                                                                                                                                                                                       |
| **OpenID Connect Advanced Syntax for Claims (ASC)** |                 | OpenID eKYC & IDA | Working Group Draft   | [ED](https://openid.bitbucket.io/ekyc/openid-connect-advanced-syntax-for-claims.html)&nbsp;[Git](https://bitbucket.org/openid/ekyc-ida/src/master/)                                                                                                                                                              |

## RFC6749 OAuth & Related

| **Name**                                     | **Description** | **Working Group** | **Status**          | **Links**                                                                                                                                                                                                                                                             |
| -------------------------------------------- | --------------- | ----------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OAuth 2.0 Security Best Current Practice** |                 | IETF OAuth        | Working Group Draft | [WD](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)&nbsp;[ED](https://oauthstuff.github.io/draft-ietf-oauth-security-topics/draft-ietf-oauth-security-topics.html)&nbsp;[Git](https://github.com/oauthstuff/draft-ietf-oauth-security-topics) |


# Other Drafts

* [IETF OAuth Datatracker](https://datatracker.ietf.org/wg/oauth/documents/)
* [OpenID Foundation Specifications](https://openid.net/developers/specs/)
  * [OpenID Connect](https://openid.net/wg/connect/specifications/) ([Repository](https://bitbucket.org/openid/connect/overview))
  * [OpenID FAPI](https://openid.net/wg/fapi/specifications/) ([Repository](https://bitbucket.org/openid/fapi/))
  * [OpenID eKYC and IDA](https://openid.net/wg/ekyc-ida/specifications/) ([Repository](https://bitbucket.org/openid/ekyc-ida/))
