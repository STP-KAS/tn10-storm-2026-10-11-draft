> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).** Written Sat 10 Oct 2026, 18:53 CEST, by stp's order, while run 2026-10-10 (T0 20:30 CEST) is still ahead. Nothing here is locked until that update lands. [Lessons so far](docs/LESSONS-from-2026-10-10.md)
>
> **Experimental. We are just trying this.** [Disclaimer](DISCLAIMER.md)
>
> **Archived on 11 Oct 2026 (read-only, nothing deleted):** draft for 11 Oct that was never run; replaced by the run repo. See [tn10-storm-2026-10-11](https://github.com/STP-KAS/tn10-storm-2026-10-11). Renamed from `tn10-run-2026-10-11`. Map of every storm: [tn-master](https://github.com/STP-KAS/tn-master).

# tn10-run-2026-10-11: the bot run and the build run

**Status:** DRAFT. T0 **12:00 CEST Sun 11 Oct 2026** (10:00 UTC), END **20:00 CEST** (18:00 UTC), same day. Private during the test; made public after the run, once the logs are on it. Kaspa Testnet-10 only; tKAS has no value.

## Map: where to find what

| Folder or file | What is in it |
|---|---|
| [README.md](README.md) | This page: map, intro, briefing, results |
| [DISCLAIMER.md](DISCLAIMER.md) | Experimental; what this repo is and is not |
| [docs/](docs/README.md) | Long pages behind the highlights below |
| [docs/TIMELINE.md](docs/TIMELINE.md) | The full timeline for 11 Oct, step by step, CEST first, UTC second |
| [docs/RESULTS.md](docs/RESULTS.md) | Results of this run in detail (filled after END) |
| [docs/LESSONS-from-2026-10-10.md](docs/LESSONS-from-2026-10-10.md) | What went wrong on 10 Oct and what changes; **TODO section filled after run 2026-10-10 ends** |
| [docs/LESSONS.md](docs/LESSONS.md) | Every older lesson behind this plan, with labels |
| [docs/RESULTS-public-nodes.md](docs/RESULTS-public-nodes.md) | The 10 Oct afternoon public-node test, in short |
| [docs/PLANS.md](docs/PLANS.md) | Plans old and new, and which repo holds each |
| [docs/RENAME-MAP.md](docs/RENAME-MAP.md) | Every TN10 run repo, its run date and its new dated name (renames happen after run 2026-10-10 ends) |
| [go/](go/README.md) | The plan: goals, timeline, targets, who sends where, gates, fees, node-dead rule, coins, disk, miners, kept and cut |
| [go/bot-run/](go/bot-run/GO-BOT-RUN.md) | The bot's prompt: `GO-BOT-RUN.md` |
| [go/build-run/](go/build-run/GO-BUILD-RUN.md) | Build's prompt: `GO-BUILD-RUN.md` |
| [go/LOGGING.md](go/LOGGING.md) | Every log file, every column with units, example rows, events, how to read the run in 5 minutes |
| [go/clock.py](go/clock.py) | The one source of all times; it writes every time table |
| [go/steps-utc.json](go/steps-utc.json) | The timeline, machine-readable (UTC) |
| [logs/](logs/README.md) | Where the results land |
| [logs/bot/](logs/bot/README.md) | Bot run logs; `SUMMARY.md` is the live summary, updated every 15 min during the run |
| [logs/build/](logs/build/README.md) | Build run logs, after the run |
| [history/](history/README.md) | All earlier runs, one file each, with dated repo names |
| [history/MASTER.md](history/MASTER.md) | The one master file: every TN10 storm, late Sep to 10 Oct 2026 |
| [credits/](credits/KASPA-PULSE.md) | Kaspa Pulse's inputs, with sources and what we changed |
| [credits/kaspa-pulse/](credits/kaspa-pulse/) | Kaspa Pulse's own counts |
| [credits/kaspa-pulse/2026-10-09-night/](credits/kaspa-pulse/2026-10-09-night/README.md) | His count of the 9 Oct night storm (CSV, notes) |
| [tn10-storm-1010](https://github.com/STP-KAS/tn10-storm-2026-10-10) (to become `tn10-run-2026-10-10`) | Run 2026-10-10, the bot run and the build run, T0 20:30 CEST (private) |
| [tn10-storm-1010-public-nodes](https://github.com/STP-KAS/tn10-storm-2026-10-10-public-nodes) (to become `tn10-run-2026-10-10-public-nodes`) | The 10 Oct afternoon public-node test, report and data (private) |
| [Kaspa Pulse (@gokugalax)](https://x.com/gokugalax) | The outside counter who shaped this plan |

## Intro

**What.** One TN10 storm on Sunday, 11 Oct 2026, 12:00 to 20:00 CEST, by two sides on one clock. The **bot run** (TN10 ops, with tn ops2, on the box) submits **only to the five public TN10 nodes**; its private node n2 is for reads, coins, the chain count and its miner. The **build run** (Grok Build on stp's desk) sends to **its own desk node**, with the five public nodes as **fallback only**. Split **25% bot, 75% Build**, with the bot's rates +10% since 19:03 CEST (Build unchanged); goal **over 3,000 tx/s combined**, network unique accepted, counted once.

**Why.** It is the same plan as run 2026-10-10 (T0 20:30 CEST Sat), moved to daylight and to a fresh day, so the lessons of 10 Oct can go in before it starts. On 10 Oct the bot alone reached about 3,168 tx/s submitted on the public nodes in the afternoon test, and Build pushed over 3,000 tx/s from its desk the week before. Details: [docs/LESSONS-from-2026-10-10.md](docs/LESSONS-from-2026-10-10.md).

**How.** One clock from [go/clock.py](go/clock.py), two gates with a **Build started?** check (BUILD-OK), a short ramp, MAX, then a long hold. Senders move away from a failing node instead of dying with it (Kaspa Pulse's node-dead rule). Count from the chain, once. Log everything in one format ([go/LOGGING.md](go/LOGGING.md)).

**Thank you first to Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)).** He counted our chain from outside, on his own two nodes, and shaped this plan with his questions, method and fixes ([credits/KASPA-PULSE.md](credits/KASPA-PULSE.md)).

## GO

**Not yet.** This repo is a DRAFT until it is updated after run 2026-10-10. Once that update is in and stp sends it, landing this repo (or `go/bot-run` / `go/build-run`) in the bot's or Build's chat is the GO: each side gets ready without questions and launches at the times in its file. Bot: [GO-BOT-RUN.md](go/bot-run/GO-BOT-RUN.md). Build: [GO-BUILD-RUN.md](go/build-run/GO-BUILD-RUN.md).

## Briefing

**Written 10 Oct 2026, 18:53 CEST, by stp's order** ("make already a new github and plan based on same structure, start run tomorrow local 12h, write now already but change after test run 1010"). Same step shape, rates and fees as run 2026-10-10; only the clock moved.

- **11:30 CEST G1**: each side reads its setup, logging starts. **11:45 CEST G2**: ready check, **Build started? (BUILD-OK)**, miners on. **12:00 CEST T0**.
- Ramp in 15-minute steps with 5-minute drains, MAX 13:50 CEST, long hold until 19:45 CEST, END 20:00 CEST. Full timeline: [docs/TIMELINE.md](docs/TIMELINE.md).
- Fees: half the lanes at 400, half at 600 sompi/gram. Node-dead rule per node. n2 lagging never zeros the bot. Rules: [go/README.md](go/README.md).

<!-- clock:key -->
| What | Brussels (CEST) | UTC |
|---|---|---|
| Gate 1 (G1), logging starts | 11:30 | 09:30 |
| Gate 2 (G2), ready check incl. **Build started? (BUILD-OK)**, miners on | 11:45 | 09:45 |
| **T0** (B0 starts) | **12:00** | **10:00** |
| First send step (X250) | 12:10 | 10:10 |
| MAX | 13:50–14:05 | 11:50–12:05 |
| Long hold (HOLD) | 14:20–19:45 | 12:20–17:45 |
| **END**, senders stop, miners off | **20:00** | **18:00** |
| Chain count (COUNT) | 20:00–22:00 | 18:00–20:00 |
| Logs pushed (PUSH) | by 23:00 | by 21:00 |
| Suggested window for Kaspa Pulse's counter | 11:40–20:05 | 09:40–18:05 |
<!-- /clock:key -->

**Change 10 Oct 2026, 19:03 CEST (stp): bot rates +10%.** Bot column ×1.1 (X250 60→66, C1000 250→275, C1500 375→413, C2000 500→550, C2500 625→688, MAX 900→990, HOLD 800→880; bot fallback hold 60→66). Build rates unchanged. Combined targets rise to 256, 1,025, 1,538, 2,050, 2,563, 3,590 and 3,280; step labels (X250, C1000 …) are kept as names.

<!-- clock:targets -->
| Step | Brussels (CEST) | UTC | Combined | Bot (25% base +10%) | Build (75% base) |
|---|---|---|---|---|---|
| X250 | 12:10–12:25 | 10:10–10:25 | 256 | 66 | 190 |
| C1000 | 12:30–12:45 | 10:30–10:45 | 1,025 | 275 | 750 |
| C1500 | 12:50–13:05 | 10:50–11:05 | 1,538 | 413 | 1,125 |
| C2000 | 13:10–13:25 | 11:10–11:25 | 2,050 | 550 | 1,500 |
| C2500 | 13:30–13:45 | 11:30–11:45 | 2,563 | 688 | 1,875 |
| MAX | 13:50–14:05 | 11:50–12:05 | 3,590 | 990 | 2,600 |
| HOLD | 14:20–19:45 | 12:20–17:45 | 3,280 | 880 | 2,400 |

Bot rates +10% (stp 10 Oct 19:03 CEST); Build unchanged; step labels kept as names. Fees, both sides: half the lanes at **400** and half at **600** sompi/gram, frozen per step. Floor 100, cap 600. Success line: network unique accepted at or above **3,000 tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data.
<!-- /clock:targets -->

### Highlights

- **Who sends where:** bot = five public nodes only; Build = own desk node, public nodes as fallback (lag over 60 s, DAA stall 30 s, not synced, dead, or desk RAM under 4 GB free), back after 2 minutes healthy. [go/README.md](go/README.md#who-sends-where)
- **Gates:** a failed G1 never blocks the public-node senders; G2 needs Build confirmed started (BUILD-OK). [go/README.md](go/README.md#gates)
- **Daylight run:** the whole run is on Sunday, 12:00 to 20:00 CEST, so stp can watch both sides and the chain count ends by 22:00 CEST.
- **10 Oct public-node test (Claim (measured on TN10)):** bot peak about 3,168 tx/s submitted (2,969 accepted); clean hold about 880 to 985 tx/s on 14 senders, zero rejects in the clean phase, fees 400. [docs/RESULTS-public-nodes.md](docs/RESULTS-public-nodes.md)
- **What broke on 10 Oct, and the fix:** n2's tip freeze, the launcher overspawn, the 0-count evaluation bug, the 17:00 run halted because Build had not started. [docs/LESSONS-from-2026-10-10.md](docs/LESSONS-from-2026-10-10.md)
- **Dated repo names:** every run repo gets a `tn10-run-<YYYY-MM-DD>` name after run 2026-10-10 ends. [docs/RENAME-MAP.md](docs/RENAME-MAP.md)
- **After the run:** once the logs are on GitHub, TN10 ops makes this repo public. [go/README.md](go/README.md#key-times)
- **Logs, easy to read:** one format for both sides, a live bot summary every 15 min, a 5-minute reading guide. [go/LOGGING.md](go/LOGGING.md#how-to-read-the-run-in-5-minutes)

## Results

**Filled after END (20:00 CEST / 18:00 UTC, Sun 11 Oct) and the chain count.** No numbers yet. **After the run, once the logs are on GitHub, TN10 ops makes this repo public.**

| Key number | Value | Detail |
|---|---|---|
| Network unique accepted, best step median (tx/s) | filled after END | [docs/RESULTS.md](docs/RESULTS.md) |
| HOLD median, network unique accepted (tx/s) | filled after END | [docs/RESULTS.md](docs/RESULTS.md) |
| Success line (3,000 tx/s) met? | filled after END | [docs/RESULTS.md](docs/RESULTS.md) |
| Bot: submitted / accepted per step | filled after END | [logs/bot/](logs/bot/README.md) |
| Build: submitted / accepted per step | filled after END | [logs/build/](logs/build/README.md) |
| Kaspa Pulse's outside count | filled after END | [credits/](credits/KASPA-PULSE.md) |

<details>
<summary><b>Certainty labels</b></summary>

| Label | Meaning |
|---|---|
| **Claim (measured on TN10)** | Seen on Testnet-10 by us, with a number and a source. |
| **Not sure / open for debate** | A reading that fits, but other readings fit too. |
| **Needs more testing** | One run is not enough to say. |

</details>

Counts only: no txid, key, seed, host IP, port or wallet address in this repo. The public TN10 node names are the community resolver nodes, not ours.

---

Intentions are good; thought process is questionable. STP remains delusional. Si vis pacem, para bellum.
