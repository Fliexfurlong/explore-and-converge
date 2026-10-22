#!/usr/bin/env python3
"""Sample exploratory prompts; no network, file writes, or semantic scoring."""

import argparse
import json
import random
import secrets
import sys


POOLS = {'actors': ('If someone new to the problem must benefit, which implicit knowledge needs to become '
            'explicit?',
            'How would the mechanism change if providers and users exchanged part of their work?',
            'How could the process be reorganized so people unwilling to participate in the '
            'routine still gain value?',
            'Which steps could disappear if one person used this independently rather than as part '
            'of a team?',
            'Which feedback becomes more direct if maintainers are the primary users?',
            'How could triggering work if beneficiaries did not have to initiate the action '
            'themselves?'),
 'resources': ('If available time were one tenth of the original amount, which value must still be '
               'preserved?',
               'If the most familiar tool were temporarily unavailable, what other mechanism could '
               'achieve the goal?',
               'If this must remain useful fully offline, what work could be completed in advance?',
               'If added maintenance had to approach zero, which existing processes could be used?',
               'If resources increased by an order of magnitude, would the original bottleneck '
               'still be the bottleneck?',
               'If you could only remove existing steps rather than add features, how could '
               'results improve?'),
 'inversions': ('If more frequent use were harmful, which outcome should replace frequency as the '
                'goal?',
                'If interruptions were normal rather than exceptional, how could recovery be '
                'designed?',
                'If users needed only the next step rather than a complete answer, how would '
                'delivery change?',
                'If results came first and inputs were added gradually afterward, which conditions '
                'would have to change?',
                'If less information could produce better judgment, what should be removed?',
                'If a step usually treated as a cost could also create value, what would the '
                'mechanism be?'),
 'combinations': ('How could combining problem solving with an existing habit reduce additional '
                  'startup effort?',
                  'How could the same feedback serve users and maintainers without creating '
                  'conflicting goals?',
                  'When immediate help and long-term accumulation are combined, which data could '
                  'remain naturally?',
                  'When individual autonomy and collective coordination are combined, what needs '
                  'sharing and what can remain private?',
                  'How could integrating recovery from failure into the routine reduce the cost of '
                  'restarting?',
                  'How could combining problem detection and improvement validation shorten the '
                  'feedback loop?'),
 'domains': ('Consider traffic scheduling: could routing, queues, or priorities address the '
             'corresponding bottleneck?',
             'Consider a library: which flows and states correspond to indexing, borrowing, and '
             'returning?',
             'Consider kitchen preparation: which work can be done ahead, and which must happen at '
             'the time of use?',
             'Consider an ecosystem: which local feedback could reduce reliance on centralized '
             'coordination?',
             'Consider stage rehearsal: how could local failures be exposed and corrected at low '
             'cost?',
             'Consider emergency triage: how could the few cases that truly need immediate '
             'handling be identified?')}


def generate(category="all", count=3, seed=None):
    if category not in (*POOLS, "all"):
        raise ValueError("unknown category")
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("count must be a positive integer")
    if seed is not None and (isinstance(seed, bool) or not isinstance(seed, int)):
        raise ValueError("seed must be an integer")
    categories = list(POOLS) if category == "all" else [category]
    capacity = sum(len(POOLS[name]) for name in categories)
    if count > capacity:
        raise ValueError(f"count exceeds available pool ({capacity})")
    actual_seed = secrets.randbits(64) if seed is None else seed
    rng = random.Random(actual_seed)
    remaining = {name: list(enumerate(POOLS[name], start=1)) for name in categories}
    for pool in remaining.values():
        rng.shuffle(pool)
    selected = []
    while len(selected) < count:
        active = [name for name in categories if remaining[name]]
        rng.shuffle(active)
        for name in active:
            number, prompt = remaining[name].pop()
            selected.append({"id": f"{name}-{number}", "category": name, "prompt": prompt})
            if len(selected) == count:
                break
    return {
        "pool_version": 1,
        "seed": actual_seed,
        "category": category,
        "count": count,
        "stimuli": selected,
        "note": "Exploration prompts, not facts or confirmed requirements.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category", choices=["all", *POOLS], default="all")
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    try:
        result = generate(args.category, args.count, args.seed)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
