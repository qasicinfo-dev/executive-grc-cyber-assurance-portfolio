# 01 | Board-Level Cyber Control Assurance and Remediation

## Executive question

Can leadership rely on critical host, firewall and monitoring controls, and what risk-based investment and remediation sequence is required?

## Fictional case study

Northstar Payments Ltd is a fictional UK payments business. Its payments-support environment includes Linux administration hosts, firewall rules and intrusion-detection alerts. An assurance review identifies inconsistent evidence of host hardening, firewall review and alert triage. There is no assumed incident; the purpose is to assess control reliability and fund proportionate improvement.

## Authorised technical grounding

- Linux auditing and hardening: Nmap and Lynis.
- Firewall policy verification: UFW.
- Intrusion detection and alert correlation: Snort and UFW/Snort.
- Traffic and port-scan analysis: Wireshark and Splunk.

## Executive deliverables

1. [Board assurance paper](docs/board_assurance_paper.md).
2. Redacted screenshots of your own authorised labs, each with a business-risk caption.
3. A control-test plan and risk register completed from your evidence.
4. A 90-day action plan and 12-month control-maturity roadmap.
5. A management dashboard with KRI/KCI thresholds and escalation triggers.

## Control-to-decision workflow

```text
Authorised lab evidence → control objective → design/operating test → finding and root cause
→ residual risk → remediation options → executive decision → closure validation → KRI/KCI reporting
```

## Distinction standard

Show why a configuration observation matters to service resilience and customer trust. Define owners, interim safeguards, change/rollback constraints, closure evidence and the point at which residual risk must be escalated to the committee.

## Interview prompts

- What evidence would prove that a firewall rule is governed, not just present?
- How would you distinguish a control-design weakness from an operating-effectiveness failure?
- What would you report to a Risk Committee if a critical action missed its target date?

