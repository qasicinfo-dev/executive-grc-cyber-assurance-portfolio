# 03 | Executive Vulnerability Governance and Secure Change Investment

## Executive question

How should finite remediation capacity be prioritised across customer-facing change, resilience and growth priorities without treating every CVSS score as the final business decision?

## Fictional case study

Luma Retail Group is a fictional omnichannel retailer preparing a seasonal release. Controlled assurance activity identifies application, host and configuration observations. Leadership needs a defensible process for risk-based remediation, exceptions and investment planning.

## Authorised technical grounding

- Web-request inspection and triage: Burp Suite.
- Controlled vulnerability scanning/validation: Metasploit Framework.
- Host auditing: Nmap and Lynis.
- Vulnerability reference/prioritisation: CVE and CVSS.
- OWASP, Nikto and OWASP ZAP learning in authorised labs where applicable.

## Executive deliverables

1. [Executive vulnerability-investment paper](docs/executive_vulnerability_investment_paper.md).
2. Redacted authorised-lab evidence and a validated fictional findings register.
3. A risk-based remediation queue generated from fictional data.
4. A 90-day backlog-reduction plan and 12-month secure-change roadmap.
5. Dashboard measures: critical-service exposure, finding ageing, expiring exceptions, validated closure and recurring root causes.

## Automation workflow

```text
Finding → validation → CVSS + exposure + asset criticality + controls → prioritisation queue
→ remediation/change → exception or closure validation → executive trend reporting
```

The automation is an illustrative prioritisation aid. A named risk owner still validates evidence, business impact, treatment and acceptance.

## Distinction standard

Show why identical technical severity can require different business decisions. Include asset/service criticality, exposure, exploit context, compensating controls, testing, rollback, ownership, exception expiry and closure evidence.

## Interview prompts

- Why should CVSS not be used as the only prioritisation factor?
- What makes an exception acceptable, and how would you govern its expiry?
- How would you demonstrate that an action has actually reduced risk?

