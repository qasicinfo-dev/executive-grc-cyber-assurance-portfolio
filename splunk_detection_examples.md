# Illustrative Splunk detection artefacts

Use only against authorised lab or fictional data. Validate fields, time range and false-positive risk before operational use.

```spl
index=network sourcetype=firewall action=allowed
| bin _time span=5m
| stats dc(dest_port) as distinct_ports count as connection_attempts by _time src_ip
| where distinct_ports >= 10 AND connection_attempts >= 25
| eval decision_note="Requires analyst validation; does not prove malicious activity"
| table _time src_ip distinct_ports connection_attempts decision_note
```

**Executive relevance:** illustrates how an observed pattern becomes a triage decision with documented uncertainty, accountable owner and escalation threshold.

