# 02 | Executive Incident Decision-Making and Resilience

## Executive question

When a potentially material cyber event is still uncertain, how should leadership make proportionate containment, communication and resilience decisions without overstating the facts?

## Fictional case study

Harbour Mutual is a fictional insurer. Its SIEM identifies possible port-scan activity after an employee reports a suspicious email and link click. There is no proof of compromise, data loss or incident. Leadership needs a clear decision process that preserves evidence, protects services and sets escalation thresholds.

## Authorised technical grounding

- Splunk and Wireshark analysis of network/port-scan evidence.
- Phishing email-header and link triage.
- Sample malware-PCAP forensics.
- Snort detection and UFW/Snort alert correlation.
- Selected security-operations and SIEM learning labs.

## Executive deliverables

1. [Executive incident decision paper](executive_incident_decision_paper.md).
2. Redacted lab evidence with timeline, source and confidence level.
3. An incident-triage record and MITRE ATT&CK mapping where relevant.
4. A 90-day exercise and control-improvement plan.
5. An executive dashboard: alert-to-decision time, exercise readiness, action ageing and repeat-event trend.

## Incident decision workflow

```text
Alert → validation → evidence preservation → severity and business-impact assessment
→ containment options → executive authority → recovery validation → lessons/actions → resilience reporting
```

## Distinction standard

Distinguish an alert, event, investigation and confirmed incident. State evidence confidence and uncertainty. Treat privacy, legal, communications, continuity and regulatory-notification matters as decision points—not automatic conclusions.

## Interview prompts

- What would move this from a security event to a confirmed incident?
- Who is authorised to accept the business impact of isolating a critical device?
- How would you brief an executive team when the facts are incomplete?

