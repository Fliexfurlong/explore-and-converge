#!/usr/bin/env python3
"""Deterministic comparison of explicitly supplied scores and feasibility."""

import argparse
import json
import math
from pathlib import Path
import sys


EPSILON = 1e-9
STATES = ("pass", "fail", "unknown")


def number(value, label, minimum=0, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    try:
        valid = math.isfinite(value)
    except OverflowError:
        valid = False
    if not valid or value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"{label} is outside its finite valid range")
    return value


def identifier(value, label):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{label} must be a nonempty, trimmed string")
    return value


def object_list(value, label):
    if not isinstance(value, list) or not value or any(not isinstance(v, dict) for v in value):
        raise ValueError(f"{label} must be a nonempty list of objects")
    return value


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    criteria = object_list(data.get("criteria"), "criteria")
    weights = {}
    for criterion in criteria:
        key = identifier(criterion.get("id"), "criterion id")
        if key in weights:
            raise ValueError(f"duplicate criterion id: {key}")
        weights[key] = number(criterion.get("weight"), f"weight {key}", maximum=1)
    if not math.isclose(math.fsum(weights.values()), 1, abs_tol=EPSILON, rel_tol=0):
        raise ValueError("weights must sum to 1; no automatic normalization")
    options = object_list(data.get("options"), "options")
    ids = set()
    for option in options:
        key = identifier(option.get("id"), "option id")
        if key in ids:
            raise ValueError(f"duplicate option id: {key}")
        ids.add(key)
        if option.get("feasibility") not in STATES:
            raise ValueError(f"option {key} requires feasibility pass, fail, or unknown")
        scores = option.get("scores")
        if not isinstance(scores, dict) or set(scores) != set(weights):
            raise ValueError(f"option {key} must have exactly the declared criteria")
        for criterion, score in scores.items():
            number(score, f"score {key}.{criterion}", maximum=5)
    return weights, options


def rank(options, weights):
    input_order = {option["id"]: index for index, option in enumerate(options)}
    values = [
        {"id": option["id"], "total": math.fsum(weights[k] * option["scores"][k] for k in weights)}
        for option in options
    ]
    # The comparator is intentionally an exact total ordering. Tolerances are
    # applied to each group's leader afterwards, avoiding non-transitive ties.
    values.sort(key=lambda row: -row["total"])
    grouped = []
    anchor = None
    group_rank = 0
    group = []
    for position, row in enumerate(values, start=1):
        if anchor is None or anchor - row["total"] > EPSILON:
            if group:
                grouped.extend(sorted(group, key=lambda entry: entry["input_order"]))
            anchor = row["total"]
            group_rank = position
            group = []
        group.append({**row, "rank": group_rank, "input_order": input_order[row["id"]]})
    grouped.extend(sorted(group, key=lambda entry: entry["input_order"]))
    for row in grouped:
        del row["input_order"]
    return grouped


def leaders(ranking):
    return [row["id"] for row in ranking if row["rank"] == 1]


def dominates(left, right, criteria):
    differences = [left["scores"][k] - right["scores"][k] for k in criteria]
    return all(value >= 0 for value in differences) and any(value > EPSILON for value in differences)


def pareto(options, criteria):
    # No deterioration is tolerated. The improvement threshold ignores numerical
    # dust without introducing non-transitive, approximately-better cycles.
    relations = {
        option["id"]: [other["id"] for other in options
                       if other["id"] != option["id"] and dominates(other, option, criteria)]
        for option in options
    }
    return {
        "frontier": [option["id"] for option in options if not relations[option["id"]]],
        "dominated": [{"id": key, "dominated_by": value} for key, value in relations.items() if value],
    }


def sensitivity(data, options, weights):
    spec = data.get("sensitivity")
    if not isinstance(spec, dict):
        raise ValueError("sensitivity requires a declared criterion")
    criterion = identifier(spec.get("criterion"), "sensitivity criterion")
    if criterion not in weights:
        raise ValueError("sensitivity requires a declared criterion")
    values = spec.get("values")
    if not isinstance(values, list) or not values:
        raise ValueError("sensitivity requires explicit nonempty values")
    other_sum = math.fsum(value for key, value in weights.items() if key != criterion)
    scenarios = []
    baseline = leaders(rank(options, weights))
    for value in values:
        number(value, "sensitivity weight", maximum=1)
        if other_sum == 0 and value != 1:
            raise ValueError("cannot redistribute weight: all other original weights are zero")
        updated = {
            key: (value if key == criterion else original / other_sum * (1 - value) if other_sum else 0)
            for key, original in weights.items()
        }
        ranking = rank(options, updated)
        winner_ids = leaders(ranking)
        scenarios.append({"weights": updated, "ranking": ranking, "leaders": winner_ids,
                          "changed_from_baseline": set(winner_ids) != set(baseline)})
    return {
        "baseline_leaders": baseline,
        "scenarios": scenarios,
        "leaders_changed": any(scenario["changed_from_baseline"] for scenario in scenarios),
    }


def evaluate(data, command):
    weights, options = validate(data)
    eligible = [option for option in options if option["feasibility"] == "pass"]
    result = {
        "operation": command,
        "eligible": [option["id"] for option in eligible],
        "excluded": {
            state: [option for option in options if option["feasibility"] == state]
            for state in ("fail", "unknown")
        },
        "basis": {option["id"]: option["basis"] for option in options if "basis" in option},
        "warnings": ["Results depend on supplied estimates, criteria, and feasibility assessments."],
    }
    if not eligible:
        result["warnings"].append("No confirmed feasible options; no winner selected.")
    if command == "score":
        result["weights"] = weights
        result["ranking"] = rank(eligible, weights)
        result["leaders"] = leaders(result["ranking"])
    elif command == "pareto":
        result.update(pareto(eligible, weights))
    elif command == "sensitivity":
        result.update(sensitivity(data, eligible, weights))
    else:
        raise ValueError("unknown comparison operation")
    return result


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("score", "pareto", "sensitivity"))
    parser.add_argument("--input", required=True, type=Path, help="UTF-8 JSON file; never modified")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"),
                          object_pairs_hook=unique_object, parse_constant=reject_constant)
        result = evaluate(data, args.operation)
        output = json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2)
    except (ValueError, OSError, RecursionError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
