> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).** Started 10 Oct 2026, 18:53 CEST. The TODO section below is filled after that run's END (04:30 CEST Sun 11 Oct) and chain count, before the GO for 11 Oct.
>
> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Lessons from 10 Oct 2026, for run 2026-10-11

Back to [README](../README.md). Older lessons: [LESSONS.md](LESSONS.md). The rule book that uses them: [go/README.md](../go/README.md#lessons-from-10-oct-built-in). Times are CEST first, UTC second. Labels: see the [README](../README.md#results).

## Known so far (before run 2026-10-10)

| # | What happened on 10 Oct | CEST (UTC) | Label | What this plan does |
|---|---|---|---|---|
| 1 | **Public-node test.** Bot senders only on the five public TN10 nodes, n2 for reads. Peak about **3,168 tx/s submitted** (about 2,969 accepted) at 14:38 on 22 senders; clean hold about **880 to 985 tx/s on 14 senders**, 0 rejects in the clean phase, fee 400 from 14:26. Build sent to the same nodes from about 14:22, so network counts were combined. | 14:23–15:57 (12:23–13:57), torn down 16:18 (14:18) | Claim (measured on TN10) | The bot submits only to the public nodes; 15 senders, a fixed count. [RESULTS-public-nodes.md](RESULTS-public-nodes.md) |
| 2 | **n2 tip freeze.** n2 stopped advancing at its tip during the public-node test, about 20 minutes behind; the 16:15 gate failed and the scheduler held the senders at 0 though the public nodes were fine. A restart on the same flags fixed it. | about 15:57–16:19 (13:57–14:19) | Claim (measured on TN10); cause Not sure / open for debate | n2 is a reader only; a freeze over 3 minutes triggers one restart (at most once per 20 minutes); a failed G1 never zeros the senders. |
| 3 | **Launcher overspawn.** Two launchers ran at once, senders piled up past 20, the rate fell from about 2,850 to about 200 tx/s; the out-of-memory killer took n2. Each relaunch claimed fresh coins, and the coin list ran to 0 unclaimed. | about 14:51 (12:51); coins at 0 about 15:10 (13:10) | Claim (measured on TN10) | One locked scheduler; staggered launches; at most one relaunch per sender per minute and 8 per run; no launch under 1.5 GB free RAM; coin buffer check every 30 minutes. |
| 4 | **Evaluation 0-count bug.** The 17:10–17:20 bot step (target 60) sent about 56 tx/s but was logged "0 sent, not clean", because the public-node senders keep no per-transaction file and the evaluation looked there. | 17:21 (15:21) | Claim (measured on TN10) | Step counts come from the senders' per-second files; a step with 0 submitted while senders logged sends is flagged as a counting bug. |
| 5 | **The 17:00 run was halted because Build had not started.** stp: "halt, stop run, forgot to send Build". Scheduler, 15 senders and the miner stopped; n2 and the read-only loggers stayed up. A watchdog had restarted senders after an earlier kill. | T0 17:00 (15:00), halted 17:39 (15:39) | Claim | G2 ready check with **BUILD-OK** (Build's ready file or stp's word); the bot does not send without it; halt order: watchdog first, then scheduler, then senders. |
| 6 | Some public nodes (boson-10, electron-10, neutrino-10) often refused connections when many senders booted at once; muon-10 and vector-10 took most ok submits. | afternoon | Claim; cause Not sure / open for debate | Staggered launches; each sender holds four of the five nodes at random; per-node back-off. |
| 7 | Free disk on the box fell about 2 GB an hour under load (29 to 26.2 GB in about 90 minutes). | afternoon | Claim (measured on TN10) | Sender pause at 8 GB; re-read disk before G1 on 11 Oct. |

## TODO after run 2026-10-10 ends

Filled after END (04:30 CEST Sun 11 Oct / 02:30 UTC) and the chain count (to 06:30 CEST), from the logs in [tn10-storm-1010](https://github.com/STP-KAS/tn10-storm-1010) (to become `tn10-run-2026-10-10`). Then the GO files, [go/README.md](../go/README.md) and [go/clock.py](../go/clock.py) are updated, the DRAFT banners come off, and stp sends the GO.

- [ ] **Headline:** network unique accepted per step (median), HOLD median, success line met or not.
- [ ] **What went wrong:** every `deviation`, node death, n2 restart, fallback, sit-out, with CEST time and cause.
- [ ] **Public nodes over 8 hours:** did any node throttle, refuse or drop for long? Keep all five, or drop one?
- [ ] **Build's desk node:** lag, freezes, RAM, time on the public fallback. Is the desk node fit for 75% again, or does the split change?
- [ ] **Rates:** was MAX (3,500) clean? Was HOLD (3,200) held? Change targets for 11 Oct only if run 2026-10-10 shows a clear reason.
- [ ] **Fees:** did 400/600 hold with no sit-outs? Did any node quote above 400?
- [ ] **Coins:** tKAS used vs planned (bot about 64,000 tKAS of fees planned after the +10%); size the 11 Oct fill.
- [ ] **Disk and RAM on the box:** free disk at END; is there room for another 8 hours before G1 (11:30 CEST)?
- [ ] **Logging:** did the live summary, the counting from per-second files and the chain count work? Fix any column that was empty.
- [ ] **Kaspa Pulse's count** of run 2026-10-10, if he sends one: what to change.
- [ ] **Improvements** list for this plan, each with the line it changes.
- [ ] **Renames** in [RENAME-MAP.md](RENAME-MAP.md) done after END, and links in this repo updated to the new names.
