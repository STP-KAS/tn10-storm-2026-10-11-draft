> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Lessons behind this plan

Back to [README](../README.md). The 10 Oct lessons in one page, with a TODO for after run 2026-10-10: [LESSONS-from-2026-10-10.md](LESSONS-from-2026-10-10.md). The full tables: [go/README.md, What we kept and what we cut](../go/README.md#what-we-kept-and-what-we-cut) and [Lessons from today, built in](../go/README.md#lessons-from-today-built-in). Every storm before this run: [history/MASTER.md](../history/MASTER.md).

| Lesson | Label | What the plan does now |
|---|---|---|
| n0 filled its disk while pruning (to 8 Oct) | Claim (measured on TN10) | n0 retired; disk guard on n2 |
| locus aborted at 03:28, 08:52 and 09:26 CEST (9 and 10 Oct); keel and locus lagged and froze about every 10 minutes on 9 Oct | Claim (measured on TN10) | Build's senders fall back to the public nodes when its desk node lags or freezes, and come back after 2 minutes healthy |
| Node B likely crashed when the desk's 32 GB ran out while building its UTXO index on 9 Oct | Not sure / open for debate | At least 4 GB RAM free on the desk; tight memory moves senders to the fallback |
| Build pushed over 3,000 tx/s into blocks from the desk last week | Claim | Build's own desk node is primary for its 75% share |
| n2 froze at its tip at about 15:57 CEST; a restart fixed it | Claim (measured on TN10) | n2 is the bot's reader only; its lag never zeros the bot's senders |
| The public-node launcher spawned twice and the rate collapsed | Claim (measured on TN10) | One locked scheduler, a fixed sender count, staggered launches |
| The coin list ran to 0 unclaimed at about 15:10 CEST | Claim (measured on TN10) | A coin buffer check every 30 minutes, with a top-up |
| The step evaluation counted 0 for the public-node senders | Claim (measured on TN10) | Counts come from the senders' per-second files |
| The 16:15 CEST gate failed and held the senders at 0 though the public nodes were fine | Claim (measured on TN10) | A failed G1 never blocks the public-node senders |
| Build was not started at 17:00 CEST; stp halted at 17:39 CEST | Claim | G2 ready check with **Build started?** and a handoff file |
| Senders kept firing at a dead node | Claim (measured on TN10) | Kaspa Pulse's node-dead rule, per node |
| Multi-hour public-node endurance; full five-node balance | Needs more testing | Run 2026-10-10's hold measures it first; this run's hold confirms or not |

Afternoon numbers: [RESULTS-public-nodes.md](RESULTS-public-nodes.md).
