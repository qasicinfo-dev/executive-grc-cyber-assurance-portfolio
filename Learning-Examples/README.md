# Independent cybersecurity learning examples

**Tinu Adewumi | QASIC Cyber | Training and learning portfolio**

These examples sit alongside, and separately from, the three fictional executive case studies. The first two are **illustrative learning exercises**: commands, data and scenarios are examples, not captured lab results. The Hashcat note records observations from a training screenshot supplied during learning; the screenshot itself is not published here.

## Linux and SQL: investigating login events

**Purpose:** Practise using Linux to inspect an authorised sample log and SQL to ask focused questions about login events.

**Context:** The following file, database table, usernames and commands are a hypothetical teaching example. They are not a claim that this exact exercise or result was captured.

1. Work within an authorised practice environment and identify the sample file.
2. Check file details and inspect sample lines:

```bash
ls -l training-auth.log
head -n 20 training-auth.log
grep -i 'failed' training-auth.log
```

`ls -l` displays file information; `head` displays the first lines; `grep` looks for matching text without regard to case. The file must exist in the current directory for these examples to work.

3. In a training database that contains a fictional `login_events` table with `event_time`, `username` and `status` columns, filter for failed logins:

```sql
SELECT event_time, username, status
FROM login_events
WHERE status = 'failed'
ORDER BY event_time DESC;
```

4. Consider what additional context is needed: authorised users, time window, source and any corroborating events. A matching line or query result alone does not establish compromise.

**Evidence status:** Illustrative commands and query only; no output or screenshot is claimed. An appropriately redacted real lab capture can be added later.

## IDS: understanding a Suricata alert

**Purpose:** Understand how a network intrusion detection rule and alert support investigation.

**Context:** This is a conceptual training example, not an observed Suricata result. Work only with authorised traffic or a supplied training capture.

1. Identify the monitoring scope and understand the traffic being inspected.
2. Review the rule's protocol, direction, addresses, ports, message and rule identifier. For illustration, this rule matches TCP traffic to destination port 80:

```text
alert tcp any any -> any 80 (msg:"TRAINING: TCP to port 80"; sid:1000001; rev:1;)
```

3. In a permitted lab, a rule can be evaluated against a suitable capture using the lab's configured Suricata setup. Investigate any resulting alert with the surrounding packet and log context.
4. Record the observation, source, time, limitations and next decision. This example rule is deliberately broad: a match can reflect ordinary traffic and is not proof of malicious activity.

**Evidence status:** Illustrative rule and investigation workflow. No alert, packet capture, screenshot or run is claimed here.

## Hashcat: interpreting a salted-hash training run

**Purpose:** Interpret progress and recovery status in the TryHackMe *Crack the Hash* learning room.

**Evidence basis:** Notes transcribed from my shared training screenshot. The screenshot itself is not included in this public repository. The challenge used a salted SHA-512 crypt hash and the `rockyou.txt` wordlist in a training environment.

- The displayed status showed **0 of 1 hashes recovered** at that point and **6,784 of 14,344,384 candidates** tested, approximately **0.05%**.
- The screen showed an estimated completion time of about **13 hours** at the displayed speed; that was an estimate, not the time actually taken to find an answer.
- After the run had stopped, the visible command was:

```bash
hashcat -m 1800 --show level2_3.txt
```

- The following prompt appeared without a recovered value. That is consistent with no result being available to `--show` in that context at the time; it does not prove that the hash is uncrackable.
- A later screenshot showed TryHackMe accepting an answer to the question, but it does not establish how that answer was obtained or that the earlier run recovered it.

**Learning:** Understand hash format, wordlist coverage, progress, runtime estimates and recovery status. Use `--show` to display results already saved in Hashcat's potfile for the specified hash and mode. Retest or review evidence before drawing conclusions.

[Return to the main portfolio](../README.md)
