> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Credits: Kaspa Pulse

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)), for the guidance and the input from 4 Oct 2026 on. He stays out of the setup. He counts what the chain accepted, on his own two nodes, and sends us the comparison first. The 7 Oct wording stays: sign-and-send processes are **senders**, **runner** is the setup, **bot** is reserved for the operator.

All of his inputs came by X DM. Below: every input, where it is recorded, and what we changed because of it.

## Every input

| # | Date | Input | Source | What we changed |
|---|---|---|---|---|
| 1 | 4–5 Oct | **Five questions:** accepted vs submitted and where it flattens; confirmation time per step, 1× vs 1.5× fee; indexer freeze; mempool depth over time; send order vs accept order (headline tx/s is not the metric) | [PULSE-README.md §Questions](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/PULSE-README.md#questions), commits [`db7a1a2`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/db7a1a2), [`6ccc208`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/6ccc208), [`a75e44d`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/a75e44d) | They became the measured goals of the plan. Today: `confirm.csv` by fee tier, `order.csv`, mempool every second ([LOGGING](../go/LOGGING.md)). |
| 2 | 5 Oct | **Six method points:** write the plan first and publish it with its commit SHA and deviations; 10-minute baseline first; fixed steps, not one blast (his example 1×, 2×, 5×, 10×); submitted and accepted per second in UTC, with order; mining share up front; raw data next to the summary | [PULSE-README.md §Method](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/PULSE-README.md#method-before-the-run), [`bc45938`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/bc45938) | Locked prompts and a deviations list; B0 at T0; fixed step table; per-second UTC logs; raw CSV in [logs/](../logs/README.md). |
| 3 | 5 Oct | **Four tightenings:** miners-off control in the main run at low load, matched, and called imperfect; label a plateau box-bound or network-bound (node CPU, cap hits, reject reasons); NTP offsets at start and end; saturation defined before T0 (accepted < 95% of submitted for 60 s), reorder rates with n, ~90 probes per tier is thin | [NEXT-STORM-PLAN.md](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/NEXT-STORM-PLAN.md#kaspa-pulses-four-tightenings-review-of-5-oct-before-the-lock), [`4dbe14c`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/4dbe14c) | Miners-off rows OFF0 to ON; `host.csv` and `rejects.csv`; `ntp.csv`. |
| 4 | 7 Oct | **The 7 Oct window check:** line up one window, sent vs accepted, which node, sample ids; name the 2,750 figure and the ~9.7k pool chain or node before calling either a ceiling | [PULSE-WINDOW-7-OCT.md](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/PULSE-WINDOW-7-OCT.md), [`1335faf`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/1335faf) | One UTC minute format, the same as his CSV. No figure is called a ceiling. |
| 5 | 7 Oct | **Cadence:** "I'd rather see one clean run first and go through those numbers properly before we stack more." | [NEXT-STORM-PLAN.md header](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/NEXT-STORM-PLAN.md), [`8c62d92`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/8c62d92) | Today is that one clean run, again. No weekly repeats before it is read. |
| 6 | 7 Oct | **Wording:** senders, runner, bot | [`c62cb97`](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/commit/c62cb97) | Used on every page here. |
| 7 | 4–7 Oct | **Scope:** load stays on TN10; no mainnet comparisons or costing | [NEXT-STORM-PLAN.md header](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/NEXT-STORM-PLAN.md) | TN10 only. |
| 8 | 7 Oct | **Offer:** to be the independent side of a later open builder leg (not planned) | [NEXT-STORM-PLAN.md §10](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions/blob/main/plan/NEXT-STORM-PLAN.md#10-later-leg-idea-not-planned-yet) | Not planned. Kept on record. |
| 9 | 8 Oct | **Checkout read:** per minute, tx sent, the node each sender talks to, five ids per minute kept local; the hours after 00:25Z had no named phase (name them or end at 00:25) | [tonight-8-oct/PULSE.md](https://github.com/STP-KAS/tn10-storm-2026-10-08/blob/main/tonight-8-oct/PULSE.md#later-note), [`4198003`](https://github.com/STP-KAS/tn10-storm-2026-10-08/commit/4198003) | `minute.csv` has sent per minute and the node by side. The hours are named: MAX, B1, HOLD, DRAIN. |
| 10 | 9 Oct | **First look at the checkout:** our rounds line up with his minutes; keep the desk node's accept and his block count apart | [tonight-8-oct/PULSE.md](https://github.com/STP-KAS/tn10-storm-2026-10-08/blob/main/tonight-8-oct/PULSE.md#9-oct-2026-after-the-checkout-was-opened), [`b2eed2c`](https://github.com/STP-KAS/tn10-storm-2026-10-08/commit/b2eed2c) | `node_accepted` and `network_unique_accepted` are separate columns. |
| 11 | 10 Oct | **Night count, 9–10 Oct, 21:25–05:35Z**, on two nodes, all 490 minutes confirmed by both: see below | [kaspa-pulse/2026-10-09-night/](kaspa-pulse/2026-10-09-night/README.md) | It is the reference for Friday in [history/MASTER.md](../history/MASTER.md). |
| 12 | 10 Oct | **Senders fired at a dead locus:** from 01:28Z our sent column read about 1 million per minute while the chain showed base load | [notes, "Two things for you to check" 1](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt) | **Node-dead rule** in both prompts: a sender stops itself, logs `node-dead`, never fires at a dead node; a failed submit is a reject, never sent. |
| 13 | 10 Oct | **The max step shows no senders at all** | [notes, step table "max"](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt) | `steps.csv` marks every step clean, not clean or not run, with a reason; `not-run` events. |
| 14 | 10 Oct | **Count soon after the run on non-archival nodes**, before older blocks are pruned | today's message (below) | A **COUNT** row, the two hours after END, on both sides: `chain-count.csv`. |
| 15 | 10 Oct | **The mining address in the plan produced blocks only 21:27–21:31Z; send the actual payout address privately** so he can show mining share per step | [notes, point 2](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt) | A to-do for stp, privately. **No payout address goes in this repo.** |
| 16 | 10 Oct | **Give T0 a few hours ahead, and he counts again** | today's message (below) | A to-do for stp: T0 and a suggested window are in [go/README.md](../go/README.md#key-times). The bots do not send it. |
| 17 | 10 Oct | Mempool numbers disagree between nodes after 01:30Z (about 2,880 vs about 200), so he uses none for conclusions | [notes, "Limits of this count"](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt) | Mempool is logged per node and labelled as that node's view. |

## His message, 10 Oct 2026

From stp's screenshot, quoted as given. Ellipses mark text not on the screen.

> "Our count runs on our own two nodes, so nothing changes on our side. The night run is done... Everything you pushed until 01:28 landed, 7.54 million tx in blocks. The peak of 1,223 tx/s at 00:47 is what arrived, not a network limit. The chain never stalled. Miners-off is confirmed minute by minute. Your chain count is within 1.2 % of ours. Three things that may help with the new plan: From 01:28 your sent column reads about 1 million per minute while the chain shows base load only. Looks like the senders kept firing at the dead locus. The max step shows no senders at all. With non-archival nodes, do your chain count soon after the run, older blocks get pruned. ... send me your actual miner payout address privately. Then we can show your mining share per step. ... when the new plan is ready, give us T0 a few hours ahead and we count again."

## His night count, 9–10 Oct

Source: [notes](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-notes.txt), [accepted CSV](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-accepted.csv), [side-by-side CSV](kaspa-pulse/2026-10-09-night/tn10-2026-10-09-2125-0535-side-by-side.csv). Published with his yes.

- **7,541,103** tx accepted in blocks over the night, 21:25–05:35Z.
- **6,607,409** in the load window 22:00–01:28Z, mean **526.9 tx/s**.
- Peak minute **00:47Z, 1,223 tx/s**. What arrived, not a network limit.
- **493–716** blocks per minute, **9.92** blocks/s on average, longest gap between blocks **1.13 s**. The chain never stalled.
- Miners-off **22:01–22:24Z** confirmed: 0 of our blocks, network at **9.2** blocks/s.
- Our chain count is **1.2 %** higher in sum over 238 valid minutes (median **3.5 %** per minute).
- Locus stopped at **01:28Z**. Base load about **55 tx/s** after that.

The step-by-step table is in [history/2026-10-09-night.md](../history/2026-10-09-night.md).

---

Si vis pacem, para bellum.
