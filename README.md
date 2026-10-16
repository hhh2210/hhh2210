# Zhuoyuan Hao (Larry Hao / 郝卓远)

[Website](https://www.alphaxiv.org/@zhuoyuan-hao) · [Publications](https://hhh2210.github.io/publications/) · [Google Scholar](https://scholar.google.com/citations?user=hjooI9QAAAAJ) · [X](https://x.com/larryhaonlp) · [CV](https://hhh2210.github.io/assets/files/resume-en.pdf) · [hzy2210@gmail.com](mailto:hzy2210@gmail.com)

I publish papers as **Zhuoyuan Hao** and use **Larry Hao** professionally; both names refer to the same person.

Finished my CS degree at **HITSZ in three years** (2023–2026), now an MPhil
student at **HKUST**. I study the mechanisms behind LLM reasoning: why models
reason the way they do, and how RL post-training quietly breaks them. Outside
research I contribute upstream a lot: **87 merged PRs across 17 repositories**,
plus code co-authored with maintainers.

## Research

**Echo of Prompt** · first author, ICLR 2026. Reasoning models almost always
restate the question to themselves before they start reasoning. Everyone filed
this under "SFT artifact." It's more than that: the echo re-anchors attention and
keeps a long chain of thought from drifting, and models pay for it when it's
missing. I show the probabilistic cost, trace the information flow, and turn the
effect into a prompt-time trick that beats baseline under a fixed token budget.
→ [evidence page](https://hhh2210.github.io/papers/echoes-as-anchors/) · [code](https://github.com/hhh2210/echoes-as-anchors) · [OpenReview](https://openreview.net/forum?id=vndn1Wrult)

**Reward Hacking in Rubric-based RL** (CHERRL) · co-first author.
When an LLM judge hands out the reward, the policy can learn to exploit the
judge's blind spots instead of actually improving. We built a controllable
sandbox: inject a known bias, reproduce the hack cleanly, and pin down the exact
step it starts. Then an agent reads the training logs and flags that onset on its own.
→ [project summary](https://hhh2210.github.io/projects/cherrl/) · [code](https://github.com/THUAIS-Lab/CHERRL) · [arXiv](https://arxiv.org/abs/2606.04923)

## Open source

I'd rather fix the tool than work around it, and then send the fix upstream.

| Project | Contribution |
| --- | --- |
| [Mole](https://github.com/tw93/Mole) · 60k★ | 3 merged PRs |
| [CodexBar](https://github.com/steipete/CodexBar) · 19k★ | 22 merged PRs |
| [Sub-Store](https://github.com/sub-store-org/Sub-Store) · 10k★ | 2 merged PRs |
| [mlx-audio](https://github.com/Blaizzy/mlx-audio) · 7.6k★ | 2 merged PRs |
| [clash-for-linux](https://github.com/wnlen/clash-for-linux) · 5.7k★ | 1 merged PR |
| [tectonic](https://github.com/tectonic-typesetting/tectonic) · 5k★ | 2 merged PRs |
| [WeatherKit](https://github.com/NSRingo/WeatherKit) (iRingo) | Credited contributor, 15 commits: next-hour forecasts ahead of the iOS 27 cutoff, air-quality scale migration, daily precipitation totals |
| [magpie](https://github.com/yetone/magpie) | Co-authored with the maintainer: saved Claude accounts refresh their allowance without switching |

## Industry

- **Tencent CodeBuddy** (Research Intern, 2026): mid-training data work for
  Tencent's coding assistant: data-mixing strategies for code usage data,
  quality rubrics, and knowledge distillation into 8B models.
- **Tencent IEG** (Research Intern, 2025): built an agentic SRE assistant and
  the fault-injection and tool-invocation framework it runs in; the model was
  open-sourced to ModelScope via CAICT.
- **Date-Match**: co-founder and algorithm lead. A questionnaire-based matching
  app; 100K+ questionnaires in the first 10 days, 170K+ in a month, all organic.

<details>
<summary><b>Small tools I built for my own workflow</b></summary>

- [powervpn-cli](https://github.com/hhh2210/powervpn-cli): native arm64 client for an abandoned campus VPN GUI, built to coexist with Surge.
- [glance](https://github.com/hhh2210/glance): maintained fork of a notch face-unlock app, with enrollment feedback and a Homebrew cask.
- [atrust-surge-bridge](https://github.com/hhh2210/atrust-surge-bridge): runs a campus VPN client in a Colima VM so it stops fighting Surge.
- [auto-skill](https://github.com/hhh2210/auto-skill): induce a reusable agent skill from a few examples.
- [threads-cli](https://github.com/hhh2210/threads-cli) · [paper-tracker](https://github.com/hhh2210/paper-tracker) · [btd600-fw](https://github.com/hhh2210/btd600-fw) · [homebrew-tap](https://github.com/hhh2210/homebrew-tap)

</details>

## Say hi

LLM reasoning, RL, agents: happy to talk, happier to build. hzy2210@gmail.com

---

<img src="./github-metrics.svg" alt="GitHub metrics for hhh2210" width="480">
