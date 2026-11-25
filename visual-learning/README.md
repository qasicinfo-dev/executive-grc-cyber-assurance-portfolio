# Visual learning: cybersecurity workflows

**Tinu Adewumi | QASIC Cyber**

This collection brings together visual study aids from my cybersecurity training. Each illustration is accompanied by an explanation of the workflow, the purpose of the tools and its connection to my portfolio. These illustrations summarise concepts and examples; they are not screenshots of a completed assessment and do not, by themselves, show that every depicted step or tool was used in a particular lab.

Use these techniques only in environments you own or are explicitly authorised to assess. Example addresses in the illustrations are illustrative.

## 1. Nmap: from scope to recorded results

**Learning focus:** Host discovery, port states, service identification and recording results.  
**Tools and concepts:** Kali Linux, Nmap, IP addressing, TCP/UDP ports and service-version detection.  
**Portfolio connection:** [Project 3: vulnerability governance and secure change](../Project%203/) considers how findings are assessed and prioritised for business risk. The project is a fictional case study; this visual is a separate study aid.

![Illustrated Nmap workflow showing scope, discovery, port selection, scan types, interpreting results, service and operating-system detection, and saving output.](images/nmap-workflow.png)

### How the workflow fits together

1. **Set the scope.** Identify the authorised lab target and network interface; record the purpose and limits of the exercise.
2. **Discover hosts.** Nmap's `-sn` performs host discovery without a port scan. A lack of response is not conclusive proof that a host is absent.
3. **Select ports and scan type.** Choose relevant ports and a suitable TCP or UDP scan. Some scan methods require elevated privileges.
4. **Interpret the output.** Distinguish open, closed and filtered ports, considering how firewalls and network conditions affect visibility.
5. **Investigate and record.** Service-version detection (`-sV`) can provide clues; operating-system detection (`-O`) is an estimate. Save the output, record scope and time, and validate findings before treating them as vulnerabilities.

**Reading note:** The visual describes `-p-` as including port 0. In Nmap, `-p-` selects ports **1–65535**; port 0 requires explicit specification. Scan options are case-sensitive, and the example address is illustrative.

## 2. Vulnerability management: discovery to validation

**Learning focus:** Connecting technical discovery and vulnerability research to risk assessment and controlled remediation.  
**Tools and concepts:** Kali Linux, Nmap, Apache, systemctl, package management, CVE, CVSS, NVD and security controls.  
**Portfolio connection:** [Project 3: vulnerability governance and secure change](../Project%203/) applies risk prioritisation and decision-making to a fictional retail scenario.

![Illustrated vulnerability management workflow from service discovery and research through assessment, mitigation, rescan and reporting.](images/vulnerability-management-workflow.png)

### How the workflow fits together

1. **Identify the asset and service.** In a controlled lab, understand the service and whether its exposure is within the agreed scope.
2. **Discover and investigate.** Identify visible ports and possible service versions. Research advisories and CVE entries, checking whether they apply to the product and configuration.
3. **Assess the risk.** Consider CVSS alongside exposure, exploit information, asset criticality and existing controls. A score alone does not establish business priority.
4. **Plan a controlled response.** Select remediation or compensating controls and consider change approval, testing, rollback and service impact.
5. **Validate and report.** Retest the relevant condition, record evidence and limitations, and communicate the result to an accountable owner.

**Reading note:** The graphic is a simplified study aid. Its commands and tools are examples, not a claim that all were run or that a specific vulnerability was found or fixed. Changing services or packages can affect a system; use a suitable test environment and follow its change procedures.

---

**About these visuals:** These study illustrations come from my Week 4 learning materials. They are learning aids, not proof of a live incident or of an actual result. Additional examples can be added after checking their source, accuracy and suitability for public sharing.

[Return to the main portfolio](../README.md)
