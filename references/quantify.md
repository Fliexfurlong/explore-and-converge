# Quantify and validate

Read only when calculation or evidence gathering could improve the current judgment. Establish goals, criteria, and evidence first. Precise computation cannot repair subjective inputs.

## Random stimuli

`python scripts/stimulus.py --category all --count 3 --seed 17`

Categories are `actors`, `resources`, `inversions`, `combinations`, `domains`, and `all`. Defaults are `all` and count 3. Without a seed, the runtime generates and returns one for replay. Identical arguments and seeds reproduce selections with the same pool version and Python runtime. Requests exceeding pool capacity fail explicitly rather than truncating silently.

Outputs are exploratory settings or analogy prompts, not facts or established user requirements. They do not prove randomness improves creativity. Run only when stuck, check for a useful connection, and do not force its application.

## Comparison input

Use the convergence reference to check candidate levels, goals, and relationships before deciding whether ranking is needed. `compare.py` calculates only explicitly supplied independent candidates. It does not detect complementarity or dependencies or optimize combinations. To compare A, B, and A+B, declare the combination separately with reassessed effects, cost, feasibility, and evidence. Do not simply add component scores. Evaluate different use cases under explicit conditions; resolve prerequisites before treating dependencies as choices.

`python scripts/compare.py score --input comparison.json`

The same input supports `pareto` and `sensitivity`. The script reads JSON without modifying it and writes JSON to stdout. Errors go to stderr with exit code 2. No network or third-party library is needed.

Minimal input (numbers illustrate the interface only, not a real decision):

```json
{
  "criteria": [{"id": "value", "weight": 0.6}, {"id": "ease", "weight": 0.4}],
  "options": [
    {"id": "A", "feasibility": "pass", "scores": {"value": 5, "ease": 1}},
    {"id": "B", "feasibility": "pass", "scores": {"value": 3, "ease": 4}},
    {"id": "C", "feasibility": "unknown", "scores": {"value": 5, "ease": 5}}
  ],
  "sensitivity": {"criterion": "value", "values": [0.3, 0.6, 0.8]}
}
```

- Criterion and option IDs must be unique nonempty strings. `criteria` and `options` must both be nonempty.
- Convert all criteria to a justified 0–5, higher-is-better scale; for example, express cost as a low-cost advantage. Retain original values, scoring reasons, and sources. Do not replace missing information with zero.
- Each `weight` must be finite and nonnegative, with the sum equal to 1 (absolute tolerance `1e-9`). Invalid weights are not automatically normalized. Every option must contain exactly all declared criteria with finite scores. Booleans are not numeric inputs.
- `feasibility` is required: `pass` means hard constraints are satisfied, `fail` means a confirmed violation, and `unknown` requires verification. If there are no hard constraints, explicitly use `pass`. Optional `basis` is returned unchanged; the script does not assess its truth.
- Scoring, Pareto comparison, and sensitivity use only `pass` options. Other options are listed separately. If none pass, return empty results and a warning rather than selecting a winner.

## Interpret calculations

- `score`: calculate `sum(weight * score)` and sort descending. Differences within `1e-9` are ties, with the same rank and subsequent competition-ranking gaps, such as `1,1,3`. Input order only stabilizes tied display; it is not priority.
- `pareto`: compare all declared criteria, including those with zero weight. Dominance permits no deterioration and requires improvement greater than `1e-9` in at least one criterion. Identical scores do not dominate each other. This preserves small tradeoffs and avoids approximate-dominance cycles. The result describes dominance under the supplied criteria and inputs, not objective superiority.
- `sensitivity`: explicitly provide a declared criterion and a nonempty list of weights in 0–1. Other weights scale proportionally to sum to `1-new_weight`. If all other original weights are zero and the new value requires assigning them weight, fail the invalid input. Results include scenario weights, rankings, tied leaders, and whether the leading set changes.
- Ordinal judgments, estimated ranges, and subjective weights do not become measured data through calculation. Use qualitative comparison when weights or scores lack a reasonable basis. Do not run sensitivity without justified variation ranges or claim robustness from it.

## Scenarios and validation

When environments differ rather than preferences, define scenario conditions and inputs and calculate them separately. Do not conflate this with weight sensitivity. Verify uncertain constraints or evidence before moving an option into the feasible set.

Prioritize unknowns that could change the route: identify the key assumption, what observation would support or refute it, and the cheapest way to obtain that observation. Research, prototypes, and experiments should address this disagreement without inventing a comprehensive test program.

The initial scripts do not solve complex budget combinations, continuous optimization, or constraint satisfaction. Choose an existing tool or propose a scoped extension only when the concrete task needs it. A simple budget check does not require a solver for procedural consistency.
