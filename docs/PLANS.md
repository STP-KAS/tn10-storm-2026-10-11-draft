> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Plans, old and new

Back to [README](../README.md).

| Plan | Nodes | Result |
|---|---|---|
| Up to 8 Oct | Box node n0 (+ public nodes for Build) | n0 filled its disk while pruning and was retired. |
| 9 Oct night, 10 Oct take 2 ([tn10-locus](https://github.com/STP-KAS/tn10-storm-2026-10-09); to become `tn10-run-2026-10-09-locus`) | Two nodes on one desk: locus (Build) and keel (bot, via a tunnel) | keel lagged; locus aborted at 03:28, 08:52 and 09:26 CEST. Failed as a test of the plan. |
| 10 Oct 17:00 CEST ([tn10-private](https://github.com/STP-KAS/tn10-storm-2026-10-10-plan) shape, refined in tn10-storm-1010; tn10-private to become `tn10-run-2026-10-10-private`) | n2 for the bot (public-node submit from 14:36 CEST), a desk node for Build | Halted by stp at 17:39 CEST: Build had not been started. The bot's S1 row (60 tx/s) was evaluated clean; S3 ran at 60 tx/s and was not evaluated before the halt. [history/2026-10-10-1700-halted.md](../history/2026-10-10-1700-halted.md). |
| 10 Oct public-node test, 14:23 to 16:18 CEST ([tn10-storm-1010-public-nodes](https://github.com/STP-KAS/tn10-storm-2026-10-10-public-nodes), private; to become `tn10-run-2026-10-10-public-nodes`) | Bot senders on the five public nodes, n2 for reads | Peak about 3,168 bot tx/s; clean hold about 880 to 985 bot tx/s on 14 senders. Lessons are folded into both plans. |
| 10 Oct, T0 20:30 CEST, END 04:30 CEST Sun ([tn10-storm-1010](https://github.com/STP-KAS/tn10-storm-2026-10-10), private; to become `tn10-run-2026-10-10`) | Bot: five public nodes, n2 for reads. Build: its own desk node, public nodes as fallback | Run 2026-10-10. Result filled after its END. |
| **11 Oct, T0 12:00 CEST, END 20:00 CEST** (this repo, `tn10-run-2026-10-11`) | Same as run 2026-10-10 | This run. DRAFT until updated after run 2026-10-10. |
