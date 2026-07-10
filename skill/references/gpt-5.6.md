# GPT-5.6 Reference

Read this reference only for GPT-5.6 model selection, effort selection, multi-agent execution, Programmatic Tool Calling, or availability questions.

## Model family

- **Sol**: flagship tier for the hardest coding, knowledge-work, cybersecurity, and science tasks.
- **Terra**: balanced lower-cost tier for everyday work.
- **Luna**: fastest, most cost-efficient tier for high-volume or lighter tasks.

## Effort and orchestration

- Use the normal/default effort for bounded work with a clear implementation and verification path.
- Consider `max` when the task benefits from more reasoning, alternatives, checks, and revision.
- Consider `ultra` only when work can be divided into independent streams and the environment makes it available. It coordinates multiple agents and trades higher token use for faster, stronger results.
- Decompose before parallelizing. Give each stream a concrete output, then synthesize and verify the result once.

## Delegated model selection

- Let the orchestrator constrain the permitted tiers, efforts, budget/latency, risk tolerance, and parallelism. Let a subagent choose the lowest sufficient option within those constraints.
- Use Terra or normal effort for bounded implementation, analysis, and review. Consider Luna for lightweight, high-volume, or low-consequence work. Escalate to Sol when correctness stakes, ambiguity, system breadth, or verification burden make the extra capability worthwhile.
- Keep `max` and `ultra` opt-in escalation choices. A subagent must state why a lower tier or effort is insufficient before requesting them.
- Report the selected or requested tier and effort with the task result. The orchestrator approves escalations and remains accountable for synthesis and final verification.

## Surface boundaries

- Availability, model pickers, effort controls, and plan entitlements vary by product and workspace. Verify them from current official OpenAI documentation and the active session before telling a user to select one.
- Programmatic Tool Calling and API multi-agent are Responses API features. Treat them as implementation options for API-backed agent systems, not as generic ChatGPT or Codex behavior.
- Do not present benchmark figures, pricing, token limits, or rollout details as durable knowledge. Check the current documentation for those values.

## Safety

- For cybersecurity or biological requests, preserve safeguards and access restrictions. Use capabilities only in authorized, defensive, and lawful contexts.
- Do not seek to circumvent a model's safety checks, account controls, trusted-access requirements, or workspace policy.

## Source of truth

Verify current facts against OpenAI's GPT-5.6 announcement and associated developer documentation before making model-specific recommendations: <https://openai.com/index/gpt-5-6/>.
