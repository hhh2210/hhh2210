# Larry Hao (郝卓远)

CS undergrad at HITSZ, finishing my thesis two semesters early. I work on LLM
reasoning and RL — why models reason the way they do, and where RL training
quietly goes wrong — with Jing Li (HITSZ) and Xiaozhi Wang (Tsinghua). In
between, I intern in industry and ship the occasional product.

## Research

**Echo of Prompt** — first author, ICLR 2026. Reasoning models almost always
restate the question to themselves before they start reasoning. Everyone filed
this under "SFT artifact." It's more than that: the echo re-anchors attention and
keeps a long chain of thought from drifting, and models pay for it when it's
missing. I show the probabilistic cost, trace the information flow, and turn the
effect into a prompt-time trick that beats baseline under a fixed token budget.
→ https://github.com/hhh2210/echoes-as-anchors · https://openreview.net/forum?id=vndn1Wrult

**Reward Hacking in Rubric-based RL** (CHERRL) — co-first author.
When an LLM judge hands out the reward, the policy can learn to exploit the
judge's blind spots instead of actually improving. Real hacking is covert and
tangled with several biases at once, so we built a controllable sandbox: inject a
known bias, reproduce the hack cleanly, and pin down the exact step it starts.
Then an agent reads the training logs and flags that onset on its own.
→ https://github.com/THUAIS-Lab/CHERRL · https://arxiv.org/abs/2606.04923

## Industry

- **Tencent IEG** (Research Intern, 2025) — built an agentic SRE assistant for
  the group's internal ops. Wrote the fault-injection and tool-invocation
  framework it runs in, used SFT-CoT distillation to claw back reasoning, and the
  model got open-sourced to ModelScope via CAICT.
- **Tencent CodeBuddy** (Research Intern, 2026) — mid-training data work for
  Tencent's coding assistant: data-mixing strategies for code usage data, quality
  rubrics, and knowledge distillation into 8B models.

## Things I've built

- **Date-Match** — co-founder and algorithm lead. A questionnaire-based matching
  app for young users; 100K+ questionnaires in the first 10 days, 170K+ in a
  month, all organic across campuses. Now incubating at MiraclePlus (YC China).
- **auto-skill** — feed it a few examples, get a reusable agent skill back.
- **CodexBar** — a small macOS menu-bar app for watching Codex / Claude Code usage.

## Say hi

LLM reasoning, RL, agents — happy to talk, happier to build. Got a research idea
or a prototype that needs to ship? hzy2210@gmail.com
