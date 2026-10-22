# Sources and design choices

The instruction structure, explanations, stimulus pool, and Python scripts were independently written for this skill. Upstream scripts were not ported, and skill bodies were not copied paragraph by paragraph. The sources below informed the design; they are not runtime dependencies. Check the relevant license and attribution before incorporating upstream text or code directly.

| Source | Ideas retained | Changes or deferred features |
|---|---|---|
| [bastien-gallay/bfw](https://github.com/bastien-gallay/bfw/blob/main/skills/brainstorm/SKILL.md) and its [technique library](https://github.com/bastien-gallay/bfw/blob/main/skills/brainstorm/techniques.md) | Problem routing, adaptation, comparison, and action organization | Removed fixed workshops, feedback after each step, automatic logs, and automatic memory. Define implementation scope after choosing a direction. |
| [danium/lateral-thinking](https://github.com/danium/lateral-thinking/blob/main/skills/lateral/SKILL.md) | Choosing a method for a sticking point, structural analogy, inversion, and honest reporting of unproductive directions | No rigid one-method limit. Added convergence, removed invented-failure requirements, and retained design exploration related to technical work. |
| [jwynia/agent-skills brainstorming](https://github.com/jwynia/agent-skills/blob/main/skills/general/ideation/brainstorming/SKILL.md) | Breaking habitual patterns, seed development, dimension changes, difference checks, and random constraints | No mandatory enumeration of conventional answers, file saves, or Deno. Conventional routes remain eligible despite low novelty. |

Methods are not evidence of reliability. Sampling, scoring, Pareto analysis, and sensitivity address stimulus selection or computation. They do not establish truthful inputs, original ideas, or effective recommendations.

The optional structural-analogy and assumption-inversion references were inspired by lateral-thinking's [analogy](https://github.com/danium/lateral-thinking/blob/main/skills/analogy/SKILL.md) and [inversion](https://github.com/danium/lateral-thinking/blob/main/skills/inversion/SKILL.md). Steps and hypothetical examples were rewritten for this skill's goals. They retain abstraction, mapping, transfer, applicability conditions, and mismatch checks without fixed domain quotas, mandatory failed branches, or a requirement that every retained idea already have a real-world precedent. The micro route does not load them. Comparisons of original and translated method materials describe only the tested conditions, not universal superiority of a method or language.

Deferred: complex optimization, automatic semantic clustering, longitudinal review systems, automatic memory, default multiple agents, and automatic development handoff. Expand only when concrete usage evidence establishes a need.
