> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# MASTER: every TN10 storm, mid Sep to 10 Oct 2026

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)), for the questions and the outside count from 4 Oct on ([credits](../credits/KASPA-PULSE.md)).

One file, oldest first. Each run: date, setup, peak numbers, what broke, what we learned. Clocks are UTC. Older repos often wrote CEST; times here were converted.

**Every number is "reported": it is what the linked file says.** We did not re-measure it here. Where a number was not found, this page says so.

## Counters are not the same

Numbers from different eras are not directly comparable.

| Counter | Meaning |
|---|---|
| **Processed** | kaspad's block-body counter. All senders, and copies in parallel blocks. Overstates unique throughput. |
| **Seen accepted / included** | A sender saw its own transaction on a node's virtual chain. |
| **Submit-OK** | The node took it into its mempool. Not inclusion. |
| **Unique accepted** | Each id once, when the virtual chain accepts it. **This is the score now.** |
| **Accepted in blocks (Kaspa Pulse)** | His count on his own two nodes, per minute. |

## At a glance

| Date (UTC) | Run | Setup | Headline, reported | Counter | What broke |
|---|---|---|---|---|---|
| 14 Sep | Repo catalog | Build vs groks-wallet | 36-row snapshot | — | — |
| 18–21 Sep | Farm mining stress | One TN10 node, up to 150 CPU miners | not found as a tx rate | — | IBD stuck near 99% headers; `RouteIsFull` |
| 25 Sep | Break test, round 1 | n0 alone, small mempool cap | 6,466 tx/s mean, 10-s peak 9,274 | Processed | Mempool ~100k, 30,298 fee evictions; public indexer froze ≥ 3 d 15 h |
| 25–26 Sep | Rounds 2–6 with vprogs | n0 + own runners | Round 4: 1,219 tx/s for 1 h 32 min; round 6: 10,058,024 accepted | Accepted (runner) | Pruning disk; a 150× fee backfired |
| 26 Sep | Round 7 | n0 | 267.2/s unique vs 357.2/s Processed | Both | — |
| 1–3 Oct | Box storm, legs L1–L4 | n0 runners + Build via public nodes | 58,905,910 included; best 1 min 4,253 tx/s | Included | Public API lag 11.7 min, freeze ~85 min; n0 disk-full 3 Oct |
| 1–2 Oct | Full gusto | Desk, one public node | about 112 tx/s in one snapshot | Accepted (sender) | Public mempools > 100k |
| 6–7 Oct | Build desk runs | Desk via public nodes | 2,207 tx/s seen accepted for 6 h 1 min | Seen accepted | 6,321 was submit, not inclusion |
| 7 Oct | The mass ceiling | Desk | ~304–307 payments per full block, ~3,040 tx/s | Block reading | 3,500 not reached |
| 8 Oct | Checkout | Desk node locus | 2,191 submit / 2,143 accept tx/s (6 senders) | Submit / local accept | locus exited twice; n0 syncing |
| 9 Oct day | keel runs 1–5 | keel via tunnel | Unique accepted avg 1,627, max 2,435 tx/s | Unique accepted | keel lag up to 868.3 s |
| 9–10 Oct night | Friday storm | locus (Build) + keel (bot) | **7,541,103** in blocks; peak minute 1,223 tx/s | Kaspa Pulse | Wrong step file; locus died 01:28 |
| 10 Oct morning | Take 2 | locus + keel | Rehearsal row: 58 tx/s mean, clean | Submit | locus aborted 06:52 and 07:26; halted 08:06 |
| **10 Oct, from T0** | **This run** ([times](../go/README.md#key-times)) | **n2 (box) + Build's own desk node** | **pending** | Unique accepted | — |

## Mid September: first contact

### 14 Sep: repo catalog
- **Setup:** Grok Build tested STP-KAS repos against groks-wallet on TN10. Frozen 36-row snapshot.
- **Source:** [tn10-hard-test](https://github.com/STP-KAS/tn10-hard-test).

### 18–21 Sep: farm mining stress
- **Setup:** a dedicated TN10 kaspad with up to 150 one-thread CPU miners. Desk CPU miners from 27 Sep ([grok-desk-tn10](https://github.com/STP-KAS/grok-desk-tn10), private).
- **Reported:** IBD stuck near 99% headers on one peer; `RouteIsFull` on block submits under farm load; one datadir lock panic. A tx rate: not found.
- **Source:** [tn10-grok](https://github.com/STP-KAS/tn10-grok) (private); summary in the [mainnet-implications note §1](https://github.com/STP-KAS/tn10-storm-2026-10-public-report/blob/main/TN10-STORMS-MAINNET-IMPLICATIONS-2026-10-04.md).
- **Learned:** one node under farm load is fragile; mining load and tx load need separate watching.

## 25–26 Sep: the September storm, with vprogs

### 25 Sep: break test (round 1)
- **Setup:** box node n0 alone, small mempool cap.
- **Reported:** Processed counter mean **6,466 tx/s**, 10-s peak **9,274**; mempool 99.97k; **30,298** evictions by feerate; one panic at `100001 > 100000`.
- **Source:** [mainnet-implications note §2](https://github.com/STP-KAS/tn10-storm-2026-10-public-report/blob/main/TN10-STORMS-MAINNET-IMPLICATIONS-2026-10-04.md); [grok-bot-vprogs findings](https://github.com/STP-KAS/grok-bot-vprogs/blob/main/findings/overload-30m-summary.md) (private). Local handoff notes on the box (not on GitHub).
- **What broke:** the public api-tn10 indexer stopped advancing accepted transactions at **19:55:38** and still returned HTTP 503 on 29 Sep (at least 3 days 15 hours). Cause not proven; time correlation is not causation. [tn10-indexer-stall-2026-09](https://github.com/STP-KAS/tn10-indexer-stall-2026-09) (private).
- **Learned:** Processed is not unique throughput. A full mempool panics at its cap.

### 25–26 Sep: rounds 2–6
- **Setup:** about 17 hours of load on n0 while running vprogs and the vprog tic-tac-toe.
- **Reported:** round 2: 10-s samples median 1,548, mean 2,507, peak 12,175 "TPS", mixed regimes, peak mempool ~88k ([round 2](https://github.com/STP-KAS/grok-bot-vprogs-round2)). Round 4: **1,219 accepted tx/s** for 1 h 32 min, about 6.7M transactions, at a 6× fee ([round 4](https://github.com/STP-KAS/grok-bot-vprogs-round4)). Round 5: a 150× storm fee was counterproductive ([round 5](https://github.com/STP-KAS/grok-bot-vprogs-round5)). Round 6: **10,058,024** own-runner transactions accepted ([round 6](https://github.com/STP-KAS/grok-bot-vprogs-round6)).
- **What broke:** pruning disk spikes on n0 (round 4 "pruning disk emergency").
- **Source, overview:** [tn10-vprogs-stress-findings](https://github.com/STP-KAS/tn10-vprogs-stress-findings), [round 1 public](https://github.com/STP-KAS/grok-bot-vprogs-round1-public), [round 3](https://github.com/STP-KAS/grok-bot-vprogs-round3), [final verdict](https://github.com/STP-KAS/tn10-vprogs-final-verdict), opinions ([Build](https://github.com/STP-KAS/tn10-vprogs-build-opinion), [bot](https://github.com/STP-KAS/tn10-vprogs-grokbot-opinion)).
- **Learned:** paced load beats blasts; very high fees do not buy more room.

### 26 Sep: rounds 7 and 8, covenants under storm
- **Reported:** round 7, three counters side by side: **267.2/s** unique selected-chain accepted vs **357.2/s** Processed ([round 7](https://github.com/STP-KAS/tn10-vprogs-round7-ideas)). 3,208/3,208 illegal spends rejected (round 7); 8,927/8,927 (round 8, [repo](https://github.com/STP-KAS/tn10-vprogs-round8-covenants)).
- **Learned:** count unique accepted, not Processed.

### 26 Sep–3 Oct: n0 disk
- Pruning spikes and resyncs on n0, temporary disk 11–15 GB, a disk-full crash on 3 Oct ([mainnet-implications note §6](https://github.com/STP-KAS/tn10-storm-2026-10-public-report/blob/main/TN10-STORMS-MAINNET-IMPLICATIONS-2026-10-04.md)). Why later plans carry disk guards.

## 1–4 Oct: the box storm

### 1–3 Oct: legs L1–L4
- **Setup:** index-free runners on n0; Build adding load from the desk through public nodes.
- **Reported:** **58,905,910** box transactions included in four legs, 152 rejected, 361,814 tKAS fees. Best 1 min **4,253 tx/s**, best 10 min **3,717**, best 60 min **2,518**. Our block share 50–63% while the box miners ran.
- **What broke:** public API lagged up to 11.7 min and froze about 85 min on the night of 2 Oct; each episode we saw end recovered within 2–5 min. n0 disk-full on 3 Oct.
- **Source:** [tn10-storm-2026-10-public-report](https://github.com/STP-KAS/tn10-storm-2026-10-public-report); raw data and analysis in [tn10-storm-2026-10-analysis](https://github.com/STP-KAS/tn10-storm-2026-10-analysis) (private); [tn10-stress-tests](https://github.com/STP-KAS/tn10-stress-tests) (private); local box notes (not on GitHub).
- **Learned:** "about 5k TPS" does not hold as unique included transactions. Label every mainnet sentence A/B/C ([note, 4 Oct](https://github.com/STP-KAS/tn10-storm-2026-10-public-report/blob/main/TN10-STORMS-MAINNET-IMPLICATIONS-2026-10-04.md)).

### 1–2 Oct: full gusto
- **Setup:** desk wallet self-spend on one public node, avoiding public nodes whose mempools were over 100,000.
- **Reported:** one snapshot at 08:19:59 UTC, 2 Oct: about **112 tx/s**, 0 rejected. A run total: not found.
- **Source:** [tn10-gusto-20261002](https://github.com/STP-KAS/tn10-gusto-20261002), [tn10-gusto-ledger](https://github.com/STP-KAS/tn10-gusto-ledger), [tn10-full-gusto](https://github.com/STP-KAS/tn10-full-gusto), [full-gusto](https://github.com/STP-KAS/full-gusto) (all private).
- **Learned:** public mempools fill first; a private node is needed.

### 4 Oct: Kaspa Pulse's questions
- His five questions arrive by X DM; [tn10-storm-throughput-questions](https://github.com/STP-KAS/tn10-storm-throughput-questions) starts. See [credits](../credits/KASPA-PULSE.md).

## 5–7 Oct: method first, and the mass ceiling

- **5 Oct.** His four tightenings; the plan is rewritten around his questions ([NEXT-STORM-PLAN.md](https://github.com/STP-KAS/tn10-storm-throughput-questions/blob/main/plan/NEXT-STORM-PLAN.md)).
- **6–7 Oct, Build's desk runs via public nodes.** **Reported:** **6,321 tx/s** submit-OK for 20 s with about 1,900/s seen accepted, so 6,321 is submit, not inclusion. A hold of **2,207 tx/s seen accepted** from 6 Oct 23:53 to 7 Oct 05:54 (6 h 1 min), fee 200/300. Source: [tn10-build-desk-tps](https://github.com/STP-KAS/tn10-build-desk-tps).
- **7 Oct, the ceiling.** **Reported:** full blocks of about 304 payments at about 498,800 of 500,000 compute mass, about 3,040 tx/s for the network. A signed 1-in/1-out is about 1,624 mass, so about 308 per block and about 3,080 tx/s. 3,500 included was not reached. Source: [what-limits-tx-rate](https://github.com/STP-KAS/what-limits-tx-rate), [tn10-build-desk-tps-3500](https://github.com/STP-KAS/tn10-build-desk-tps-3500).
- **7 Oct, the Pulse window.** His count for 18:52–19:23 came out much lower than our screenshot; our log had stopped at 18:38:39. **Learned:** one window, one clock, sent and accepted kept apart ([PULSE-WINDOW-7-OCT.md](https://github.com/STP-KAS/tn10-storm-throughput-questions/blob/main/plan/PULSE-WINDOW-7-OCT.md)).
- **7 Oct.** [grok-bot-build-combo](https://github.com/STP-KAS/grok-bot-build-combo) hub; storm set for Fri 9 Oct. [tn10-storm-build-bot-challenge](https://github.com/STP-KAS/tn10-storm-build-bot-challenge) opens, still empty.

## 8 Oct: the checkout, and n0 retired

- **Setup:** desk node locus, ten rounds, 18:00–20:11.
- **Reported:** six senders: submit mean **2,191.2**, local accept mean **2,142.9** tx/s, 0 rejects. Ten senders: **2,100.1** / **1,954.1**. More senders added waiting, not throughput.
- **What broke:** locus exited twice (19:00:06 and 19:03:41) and was restarted. n0 had frozen at 06:54 UTC after pruning filled the disk and was resyncing, so the bot side was not measured (TN10 ops, 8 Oct message; not in git). n0 was retired.
- **Source:** [tonight-8-oct/RESULTS.md](https://github.com/STP-KAS/grok-bot-build-combo/blob/main/tonight-8-oct/RESULTS.md), [AFTER-8-OCT.md](https://github.com/STP-KAS/tn10-storm-throughput-questions/blob/main/plan/AFTER-8-OCT.md).
- **Learned:** a 126 GB box disk cannot hold an 86 GB node plus 14–18 GB pruning dips (TN10 ops, 8 Oct; not in git). One node on the desk is a single point of failure.

## 9 Oct day: keel pre-test and duplicates

- **Setup:** second desk node keel; the bot reached it through a tunnel. Light 643-mass hops, fee 200/300.
- **Reported:** 15 runners held 60 tx/s; 100 tx/s failed the p90 ≤ 10 s rule; run 5 ended on keel lag (302 s). 48–49% of tx slots in blocks were duplicates. Network unique accepted while keel kept up (12:24–13:15): average **1,627**, median 1,704, max **2,435** tx/s.
- **What broke:** with no bot load, keel lag reached **868.3 s** at 15:28:26 and keel froze for minutes about every 10 min from about 14:05. Cause not found.
- **Source:** [monitoring-result/bot-result](https://github.com/STP-KAS/tn10-locus/blob/main/monitoring-result/bot-result/README.md), [goal/OPINION.md](https://github.com/STP-KAS/tn10-locus/blob/main/goal/OPINION.md), [tn10-locus README](https://github.com/STP-KAS/tn10-locus).
- **Learned:** duplicates, not block space, keep unique accepted near 2,000. A node behind a tunnel lags.

## 9–10 Oct night: the Friday storm (failed as a test of the plan)

Details and both step tables: [2026-10-09-night.md](2026-10-09-night.md).

- **Setup:** locus (Build) and keel (bot, through a tunnel), one miner per node. Planned restart: gate 21:45, T0 22:30, end 06:30.
- **Reported by Kaspa Pulse (his own two nodes):** **7,541,103** tx accepted in blocks 21:25–05:35; **6,607,409** in 22:00–01:28, mean **526.9 tx/s**; peak minute **00:47, 1,223 tx/s**; 493–716 blocks/min, 9.92 blocks/s, longest gap 1.13 s; miners-off 22:01–22:24 confirmed; our count 1.2% higher in sum over 238 minutes (median 3.5%); base load about 55 tx/s after 01:28. Source: [his notes](../credits/kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt) (private).
- **What broke:** the desk ran the voided 21:00 step file from 21:52; a second holder started; the max step did not run; locus aborted at about 01:28 (`Rust cannot catch foreign exceptions`) and the hold kept "sending" to it until 04:45. Source: [RUN-REPORT.md](https://github.com/STP-KAS/tn10-locus/blob/main/tn10-storm-2026-10-09/build/RUN-REPORT.md).
- **Learned:** one step file and one holder; a sender must stop when its node dies; count the chain soon after the run.

## 10 Oct morning: take 2 (halted)

Details: [2026-10-10-take2.md](2026-10-10-take2.md).

- **Setup:** same desk nodes. Gate 06:15, T0 07:00, end 15:00.
- **Reported:** 06:15 gate passed (keel lag 1 s). Build's rehearsal row closed at 06:59:02: target 60, mean submit 58, clean.
- **What broke:** locus aborted at 06:52:56 and 07:26 with `0xc0000409` at the same offset; a watcher restarted it. stp halted the storm at 08:06 and retired both desk nodes (TN10 ops message, 10 Oct; not in git).
- **Source:** [INCIDENT-0652.md](https://github.com/STP-KAS/tn10-locus/blob/main/tn10-storm-2026-10-10/build/INCIDENT-0652.md), [go/take2](https://github.com/STP-KAS/tn10-locus/blob/main/go/take2/README.md).
- **Learned:** that kaspad build on the desk crashes at one offset; each side needs its own node on its own machine.

## 10 Oct, from T0: this run

- **Setup:** bot on n2 (box), Build on its own new desk node. Private, pruned, no tunnel, one miner per side. Plan: [tn10-private @ 517fb43](https://github.com/STP-KAS/tn10-private/tree/517fb43), refined in [go/](../go/README.md). Times: [go/README.md](../go/README.md#key-times).
- **Results:** pending. They go to [logs/](../logs/README.md).
