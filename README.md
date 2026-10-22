# Explore and Converge

[简体中文](README.zh-CN.md)

An explicitly invoked skill for exploring different approaches, developing rough ideas, and reaching a supported choice, combination, sequence, or next validation.

**Status:** v1.2.0, public trial. Stable gains in real-world decisions have not been established. English is the publication language, not a claim of better model performance.

## What it helps with

- A question assumes one solution format before its goal is clear.
- Suggestions keep repeating the same mechanism under new names.
- An intuition has promise but lacks a concrete mechanism.
- Several options need comparison, or might actually complement or depend on one another.
- A decision needs a small calculation or a check of its decisive unknown.

The skill starts with the smallest useful action. A micro exploration can be one changed perspective and a conclusion. More involved questions load only relevant references. It does not require a workshop, a candidate quota, a scoring table, or a file after every use.

## Use

Get the files:

```sh
git clone https://github.com/Fliexfurlong/explore-and-converge.git
```

Install this directory as `explore-and-converge` using your agent's supported skill installation mechanism. Keep `SKILL.md`, `references/`, `scripts/`, and `agents/` together. The directory is the installable skill; this README is for people and is not required reading during invocation.

Select the skill explicitly, or invoke it by name in a supporting agent:

```text
$explore-and-converge Keep this small. I lose my train of thought after
interrupting a writing session. Give me one direction worth trying and why.
Do not implement anything.
```

```text
$explore-and-converge I keep collecting research material but postpone
writing. Explore mechanisms different from classification and reminders.
I can spend only 30 extra minutes per week and cannot add tools or staff.
Compare when each direction could work and suggest what to try first.
```

```text
$explore-and-converge Compare these three options. First check whether
they are alternatives, complements, or prerequisites. Keep uncertain
costs explicit and identify what fact would change your recommendation.
```

These are usage prompts, not benchmark results or promises of effectiveness. You can ask for divergence only, development of one seed, comparison only, or a particular method. English instructions do not require English answers; the skill follows the current user's language and instructions.

Ordinary questions and discussions about the skill do not authorize its execution. If the assistant proposes exploration, it asks for approval of the scope first. Approval to explore does not authorize implementation.

`agents/openai.yaml` preserves Codex's `allow_implicit_invocation: false` policy. Loader behavior varies; this metadata has not been validated across all agents. Other hosts may need their own explicit-invocation settings. Semantic requests operate within the host's loading rules; the instruction text alone cannot guarantee that a host discovers or loads the skill.

## Optional tools

The skill instructions require no Python. The two optional Python 3 scripts use only the standard library and do not access the network or write user files:

```sh
python scripts/stimulus.py --category all --count 3 --seed 17
python scripts/compare.py score --input comparison.json
python scripts/compare.py pareto --input comparison.json
python scripts/compare.py sensitivity --input comparison.json
```

Run from the skill directory or resolve script paths relative to it. The comparison JSON contract and a complete minimal example are in [Quantify and validate](references/quantify.md). The sampler's prompts are English translations of the Chinese pool, with category and item ordering preserved. Fixed seeds reproduce selections in the same pool and runtime; English and Chinese prompt text naturally differs.

Scripts handle selection and calculation. They do not verify input evidence, determine whether analogies are valid, or demonstrate that a recommendation works.

## Structure

```text
SKILL.md                     Authorization, micro route, routing, stopping
agents/openai.yaml           Display metadata and explicit-invocation policy
references/reframe.md        Goals, premises, and problem framing
references/diverge.md        Method selection and mechanism differences
references/develop.md        Develop a promising but incomplete seed
references/converge.md       Relationships, tradeoffs, and output forms
references/quantify.md       Calculation contracts and focused validation
references/methods/          Optional analogy and inversion procedures
references/sources.md        Inspirations and design choices
scripts/                     Optional sampler and comparison tools
```

## Evidence and limits

Earlier checks support script correctness and basic routing. Small behavioral trials show promising cases and failures; they do not establish a consistent advantage over an unassisted model. Method and language comparisons did not establish that fuller instructions or English instructions are generally better. An entrypoint compression pilot did not demonstrate meaningful total-token savings.

The English translation is not the same experimental condition as those earlier studies. See [Evaluation scope](docs/evaluation.md) for distinctions and limitations. No claim is made of universal creativity gains, better real-world decisions, or reduced cost.

Useful feedback includes the original request, model and host, what was loaded, a concrete helpful or harmful difference, and whether it changed a decision. Remove private information before sharing examples.

## Sources

The design draws on bfw, lateral-thinking, and jwynia/agent-skills while using independently written instructions and scripts. See [Sources and design choices](references/sources.md) for links and adaptations.

## License

[MIT](LICENSE).
