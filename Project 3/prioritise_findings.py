#!/usr/bin/env python3
"""Illustrative prioritisation from fictional findings.

This is a portfolio learning artefact, not a CVSS calculator or company policy.
It makes each assumption visible and requires human risk-owner review.

Usage: python3 prioritise_findings.py fictional_findings.csv remediation_queue.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

EXPOSURE = {"internet-facing": 1.50, "partner-facing": 1.30, "internal": 1.00, "isolated": 0.60}
EXPLOIT = {"active-exploitation": 1.50, "credible-public-exploit": 1.25, "no-known-exploit": 1.00}
CONTROL = {"weak": 1.25, "partial": 1.00, "strong": 0.75}


def band(value: float) -> str:
    if value >= 45:
        return "Critical — review/treatment decision within 24 hours"
    if value >= 30:
        return "High — treatment decision within 5 business days"
    if value >= 15:
        return "Medium — treatment decision within 30 days"
    return "Low — normal risk-owner review cycle"


def score(row: dict[str, str]) -> float:
    cvss, criticality = float(row["cvss"]), int(row["asset_criticality"])
    if not 0 <= cvss <= 10 or not 1 <= criticality <= 5:
        raise ValueError(f"Invalid score/criticality for {row['finding_id']}")
    return round(cvss * criticality * EXPOSURE[row["exposure"]] * EXPLOIT[row["exploit_context"]] * CONTROL[row["control_strength"]], 1)


def main(input_file: Path, output_file: Path) -> None:
    with input_file.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    queue = []
    for row in rows:
        priority = score(row)
        queue.append({**row, "illustrative_priority_score": priority, "proposed_priority": band(priority), "human_review_required": "Yes — validate scope, evidence, business impact and risk treatment"})
    queue.sort(key=lambda item: float(item["illustrative_priority_score"]), reverse=True)
    with output_file.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=queue[0].keys())
        writer.writeheader()
        writer.writerows(queue)
    print(f"Wrote {len(queue)} fictional findings to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python3 prioritise_findings.py fictional_findings.csv remediation_queue.csv")
    main(Path(sys.argv[1]), Path(sys.argv[2]))

