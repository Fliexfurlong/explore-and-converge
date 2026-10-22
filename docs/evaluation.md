# Evaluation scope

This is a summary of local development records, not a reproducible public benchmark. Earlier private run logs are not included in this publication candidate. Results below are reported with their original scope rather than used as headline effectiveness claims.

## What was examined before translation

- **Engineering checks:** static structure, local references, deterministic calculation, input validation, and sampler behavior were exercised during development. Passing those checks supports implementation behavior, not the quality of recommendations.
- **A reported DeepSeek comparison:** a separate tester reported six scenarios, with skill-assisted answers scoring 38/42 against 32/42 for a control, across three wins, two losses, and one tie. Raw runs were not independently reproduced here. Small samples, subjective scoring, and forced file loading limit the conclusion. Treat it as preliminary reported evidence.
- **A method/language pilot:** two tasks, four method/language conditions, two runs each, and two anonymous reviewers. It compared compact versus fuller structural-analogy instructions in Chinese and English. It did not compare the entire current skill against no skill or against another complete package. It did not establish a consistent English-language advantage.
- **An entrypoint pilot:** two tasks, one generation per version and task. A candidate shortened the entrypoint by 35%, but the standard task's actual skill-text loading fell only about 3.5%, with essentially unchanged cumulative total tokens and tool rounds. The candidate was not installed. Cached input and repeated host context prevent treating these numbers as stable billing savings.

The generation and review setup in the local pilots used the same model family. Review scores near their maximum do not establish objective correctness or equivalence. The tasks do not cover all methods, host loaders, languages, or long-conversation behavior.

## This English candidate

The translation is based on the installed Chinese v1.2.0, not the uninstalled compressed candidate. It preserves method routing, authorization boundaries, stopping rules, numerical contracts, and reference paths. UI strings and all 30 stimulus prompts are translated. The comparison script is copied unchanged; the sampler's executable logic, categories, ordering, and CLI contract are preserved.

Source-equivalence review, local-link checks, static validation, and script checks can establish translation and packaging properties. They do not establish that this English candidate improves answers or real-world outcomes. New checks should be reported with their actual results and must not inherit earlier scores as if those scores measured the translated package.

## What remains unknown

- Reliable gains over ordinary model answers on diverse unseen tasks.
- Whether suggestions produce better outcomes after adoption.
- Long-conversation continuation and changes in goals or evidence.
- Invocation behavior across different models and host applications.
- Stable effects on latency, total tokens, or cost.

For feedback, describe a concrete decision-changing direction, a missed constraint, an unnecessary detour, or another observable difference. A longer answer or a more elaborate template is not itself evidence of usefulness.
