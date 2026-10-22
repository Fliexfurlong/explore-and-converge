---
name: explore-and-converge
description: "Reframe questions, develop ideas, and compare alternatives when the user explicitly requests exploration and convergence, asks for different paths and selection, or approves the assistant's proposed scope. Ordinary questions, quotations, and discussion of this skill do not authorize invocation."
metadata:
  version: "1.2.0"
---

# Explore and Converge

Help the user find relevant directions with different mechanisms, then reach a supported recommendation or identify the next useful validation. User instructions take priority. Adapt the method to the problem without requiring a full workshop.

## Entry and authorization

- Run only when the user selects the skill, explicitly requests exploration for the current question, or approves a specific exploration scope proposed by the assistant. Creative work, optimization, ordinary questions, quoted trigger words, and discussion of this skill do not by themselves authorize invocation.
- Without authorization, complete the ordinary task and stop here: do not choose an exploration route, read method references, or apply an exploration output template. Reading source files to create, review, or explain the skill is not authorization to execute it. There is no need to announce that the skill is inapplicable.
- If the assistant sees value in using the skill but lacks approval, explain the sticking point, expected value, and scope, then wait. Ordinary judgment and relevant alternative suggestions can continue.
- Authorization covers method changes within the current scope. It does not authorize implementing candidates, expanding the project, contacting others, or changing external configuration. A different question needs fresh explicit intent or authorization.
- The user may want divergence only, development of a single idea, or comparison of existing options. Respect that stage without forcing convergence or a complete workflow.

Judge meaning in context rather than counting keywords. "Find different paths and compare which is worth trying" is an explicit exploration request. A standalone "What do you think?" is not, though a continuation within the current authorized scope may proceed.

## Start with the smallest useful action

Extract the goal, real constraints, existing directions, and current gap from available context. Ask only when missing information could change the route. Follow a requested depth or method; otherwise choose by uncertainty, judgment difficulty, and consequences, rather than message length or idea count.

Adjust exploratory distance independently of depth. "Keep it simple, but make a bigger leap" may need one direction that changes a premise; "go deeper along this direction" can retain the existing frame. Adapt distance, depth, and delivery to current feedback without turning it into a permanent preference.

**Micro route (no other references needed):** Understand the need → take one action that improves the answer → give the conclusion.

That action might rephrase the question, add a relevant perspective, identify the decisive difference between two options, fill a missing mechanism in an idea, or verify a key fact. Stop once the answer is sufficient. Do not pad the candidate list or require scoring, research, scripts, or saved files. Fact-checking still follows the accuracy requirements of the current task.

For further exploration, read only the reference that addresses the current gap:

| Current gap | Starting route | Read as needed |
|---|---|---|
| Vague question or fixation on a solution format | Separate goal from form → expand the concept | [Reframe](references/reframe.md) |
| Repetitive directions or limiting default premises | Conventional baseline → one method that breaks the frame → check differences | [Diverge](references/diverge.md) |
| Promising seed with an incomplete mechanism or setting | State the seed → adjacent possibilities or combinations → fill the gap | [Develop](references/develop.md) |
| Candidates exist, but the choice is difficult | Group → check constraints and relationships → combine, assign conditions, sequence, or compare | [Converge](references/converge.md) |
| Numerical tradeoffs or missing decisive evidence | Check criteria and evidence → calculate or design validation | [Quantify and validate](references/quantify.md) |

Standard exploration resolves the current gap. Add research, computation, or counterargument checks for deeper exploration only when consequential tradeoffs, several key unknowns, or repeated blockage justify them. Greater depth does not mean running every method.

## Adapt progressively and stop

After a useful action, ask whether another step could change the judgment:

- The request is satisfied and key support is sufficient: finish.
- Candidates are variants of the same mechanism: change a dimension or method instead of expanding them again.
- Directions differ but remain hard to choose: first check exclusivity, complementarity, dependencies, and applicability. Then compare, combine, give conditional roles, or sequence. If the choice depends on an unknown fact, verify or validate; deferring the choice is acceptable.
- New evidence overturns a shared premise: reframe while retaining information that remains valid.
- No new lead can advance the judgment: explain the bottleneck and stop looping. Deepen or change direction if the user wants to continue.

## Shared quality requirements

- Separate facts, inferences, assumptions, and explicit decisions. Distinguish real hard constraints, adjustable preferences, and exploratory settings. Unconfirmed constraints do not automatically become requirements.
- Early ideas may defer feasibility assessment, but never fabricate facts. A provocative setting is not a claim about reality. Check relevant real hard constraints before making an actionable recommendation; preserve unknowns explicitly.
- Explain what a new direction changes, why it matters, and the conditions under which it could work. Transfer mechanisms in analogies, not appearances, and state mapping limits.
- A conventional option may be best. Assess novelty, usefulness, feasibility, and evidence maturity separately. Keep promising immature ideas when appropriate; do not hide their gaps in a single total score.
- Option order, emphatic wording, and unverified endorsements do not change factual support. When a statement affects the choice, identify its role by meaning: "I prefer writing my own script" is a preference that can affect the recommendation but is not evidence of effectiveness; "I think it is slow" is an observation or hypothesis to verify, not automatically a preference or hard constraint. Do not classify statements mechanically by phrases such as "I think." Update judgment when goals, constraints, or relevant evidence change.
- Report genuinely unsuccessful branches honestly. Do not invent failures to demonstrate sufficient divergence or treat surprise as effectiveness.
- Reuse the current goal, authorization scope, evidence, and candidates; update only affected parts. Refresh stale facts when needed without creating implicit permanent constraints across conversations.

## Delivery and overhead

Deliver the requested conclusion, useful new directions and their relevance, and key tradeoffs. When several directions need convergence, the result may be a choice, combination, conditional allocation, or sequence. Check relationships lightly when they affect judgment; do not require a table or every pairwise comparison. Add failure conditions or the validation that most reduces uncertainty when needed. For divergence only, deliver candidates and open questions.

## Continue only when useful

If the user wants to resume later, or a long exploration risks losing important tradeoffs, leave a short note in the conversation covering settled points, open questions, reasons for setting ideas aside, and conditions for reopening them. Include only substantive items; do not turn an undecided issue into a decision. Do not append this note to ordinary short questions by default.

Preserve reasons rather than the entire process. Distinguish excessive cost, insufficient evidence, and a mismatch with the goal. The note does not authorize file writes, memory storage, or permanent constraints. On resumption, check freshness and current intent; the note itself does not extend invocation authorization.

Do not present a step-by-step facilitation log. Read only useful references and distinguish candidate mechanisms before developing details. Invocation does not automatically trigger searching, scoring, file writes, memory storage, task creation, multiple agents, or a development workflow. Research and tools remain subject to current authorization and platform rules.

Read the quantitative reference and run scripts only when numerical comparison or random stimuli are useful. Scripts do not replace factual or semantic judgment. Read [Sources and design choices](references/sources.md) only when reviewing or changing the skill.
