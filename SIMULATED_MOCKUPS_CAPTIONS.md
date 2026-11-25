# Authorised lab mockups — captions and use statement

## Use statement

The four accompanying PNG files are illustrative reconstructions based on authorised lab tasks completed during training. They are **not literal lab screenshots**, live-system records or production evidence. Keep the red authorised-lab-mockup banner visible if these are shown publicly.

## 01 | Lynis host hardening

- **Task:** Perform a Lynis hardening review in an authorised training-lab environment.
- **Observation:** Fictional output flags root SSH, an unused service and weak `/tmp` mount settings.
- **Control implication:** Baseline compliance cannot be relied on until exceptions are validated and governed.
- **Business risk:** Unauthorised access could increase service disruption, recovery effort and assurance risk.
- **Recommendation:** Remediate through approved change, evidence retest and monitor exceptions to closure.
- **Limitation:** A point-in-time lab output does not prove organisation-wide or sustained effectiveness.

## 02 | UFW policy verification

- **Task:** Inspect a UFW rule set in an authorised lab against a least-privilege firewall expectation.
- **Observation:** Fictional SSH access is open from Anywhere and requires a documented justification.
- **Control implication:** Policy state alone is insufficient; approval, review and monitoring evidence are needed.
- **Business risk:** Unnecessary exposure could increase likelihood of unauthorised access and response effort.
- **Recommendation:** Restrict sources, retain approval evidence and schedule periodic rule recertification.
- **Limitation:** A configuration view does not prove traffic flow, history or operating effectiveness.

## 03 | Snort alert correlation

- **Task:** Correlate UFW blocks and a Snort port-scan alert in an authorised training-lab scenario.
- **Observation:** The same fictional source reaches multiple ports within a short window and triggers a rule.
- **Control implication:** Detection value depends on correlation, triage, severity logic and an accountable decision route.
- **Business risk:** Untriaged alerts can cause material signals to be missed or waste capacity through false positives.
- **Recommendation:** Set a triage SLA, document authorised-scanner exceptions and review repeated patterns.
- **Limitation:** Correlation raises a question; it does not establish intent, attribution or confirmed compromise.

## 04 | Splunk network monitoring

- **Task:** Use a Splunk search in an authorised lab to identify unusual multi-port connection behaviour.
- **Observation:** A fictional source connects to 28 ports in five minutes, above the review threshold.
- **Control implication:** Monitoring needs defined thresholds, ownership, triage procedures and evidence retention.
- **Business risk:** Without useful monitoring, discovery activity may go unseen until it affects a critical service.
- **Recommendation:** Validate source and asset context, tune the use case and track alert-to-decision performance.
- **Limitation:** The fictional query does not prove a scan, malicious intent or organisation-wide coverage.

