> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Rename map: every TN10 run repo gets a date

Back to [README](../README.md). **Written 10 Oct 2026, 18:53 CEST, by stp's order:** "label all githubs with dates, that's better … do it for all runs we have done, rename run: date".

**Nothing is renamed yet.** The renames happen **after run 2026-10-10 ends** (END 04:30 CEST Sun 11 Oct / 02:30 UTC, then the chain count and the log push), because that run's scheduler reads its plan from `tn10-storm-1010` and must not be disturbed mid-run. GitHub keeps a redirect from each old name, so old links keep working.

## The rule

- A repo that holds a **run**: `tn10-run-<YYYY-MM-DD>`, plus a short suffix when one date has more than one repo (for example `-public-nodes`).
- A TN10 repo that is **not a run** (questions, analysis, a stall, a review): `tn10-<YYYY-MM-DD>-<topic>`.
- The date is the run's start date in Brussels time (CEST). Where a repo spans days, it is the first run day. Where no run date is written in the repo, it is the day the repo was created (CEST), marked "created".
- This repo is already on the rule: **`tn10-run-2026-10-11`**.

## A. The storm runs (rename after run 2026-10-10)

| Current name | Visibility | What it holds | Run date (CEST) | New name |
|---|---|---|---|---|
| [tn10-storm-1010](https://github.com/STP-KAS/tn10-storm-2026-10-10) | private | The bot run + build run, T0 20:30 CEST Sat, END 04:30 CEST Sun | 2026-10-10 | **`tn10-run-2026-10-10`** |
| [tn10-storm-1010-public-nodes](https://github.com/STP-KAS/tn10-storm-2026-10-10-public-nodes) | private | Afternoon public-node test, 14:23–16:18 CEST | 2026-10-10 | **`tn10-run-2026-10-10-public-nodes`** |
| [tn10-private](https://github.com/STP-KAS/tn10-storm-2026-10-10-plan) | private | Plan for T0 15:00 CEST 10 Oct (each side its own node); superseded by the 17:00 run, halted 17:39 | 2026-10-10 | `tn10-run-2026-10-10-private-plan` |
| [tn10-locus](https://github.com/STP-KAS/tn10-storm-2026-10-09) | public | The Friday night run on locus/keel (9–10 Oct) and Saturday morning take 2 | 2026-10-09 | `tn10-run-2026-10-09-locus` |
| [grok-bot-build-combo](https://github.com/STP-KAS/tn10-storm-2026-10-08) | public | Bot + Build combo hub; the 8 Oct checkout, 20:00–22:00 CEST (18:00–20:00 UTC) | 2026-10-08 | `tn10-run-2026-10-08-combo` |
| [tn10-build-desk-tps-3500](https://github.com/STP-KAS/tn10-storm-2026-10-07) | public | Build desk try for over 3,500 tx/s included | 2026-10-07 (created) | `tn10-run-2026-10-07-build-desk-3500` |
| [tn10-build-desk-tps](https://github.com/STP-KAS/tn10-storm-2026-10-06) | public | Build desk runs, 6–7 Oct: short windows, long holds, fee-400 window | 2026-10-06 | `tn10-run-2026-10-06-build-desk` |
| [tn10-gusto-20261002](https://github.com/STP-KAS/tn10-storm-2026-10-02-ramp) | private | Full-gusto ramp findings | 2026-10-02 | `tn10-run-2026-10-02-gusto-ramp` |
| [tn10-gusto-ledger](https://github.com/STP-KAS/tn10-storm-2026-10-02-ledger) | private | Full-gusto spend ramp notes | 2026-10-02 | `tn10-run-2026-10-02-gusto-ledger` |
| [tn10-full-gusto](https://github.com/STP-KAS/tn10-storm-2026-10-02) | private | Operation full gusto findings | 2026-10-02 | `tn10-run-2026-10-02-full-gusto` |
| [full-gusto](https://github.com/STP-KAS/tn10-storm-2026-10-02-match) | private | Full gusto hosted tic-tac-toe match notes | 2026-10-02 | `tn10-run-2026-10-02-full-gusto-match` |
| [tn10-storm-2026-10-analysis](https://github.com/STP-KAS/tn10-storm-2026-10-01-analysis) | private | 24 h storm through n0, 1–2 Oct: raw data + analysis | 2026-10-01 | `tn10-run-2026-10-01-analysis` |
| [tn10-storm-2026-10-public-report](https://github.com/STP-KAS/tn10-storm-2026-10-01) | public | Public report of the 1–3 Oct storm | 2026-10-01 | `tn10-run-2026-10-01-public-report` |
| [tn10-stress-tests](https://github.com/STP-KAS/tn10-storm-2026-10-01-reports) | private | Box report and the 1 Oct desk storm prompt | 2026-10-01 | `tn10-run-2026-10-01-stress-reports` |

## B. TN10 repos that are not runs (rename after run 2026-10-10)

| Current name | Visibility | What it holds | Date (CEST) | New name |
|---|---|---|---|---|
| [tn10-storm-throughput-questions](https://github.com/STP-KAS/tn10-storm-2026-10-04-questions) | public | Kaspa Pulse's questions, method and the measurement plan, 4–9 Oct | 2026-10-04 | `tn10-2026-10-04-storm-questions` |
| [tn10-storm-build-bot-challenge](https://github.com/STP-KAS/tn10-storm-2026-10-09-challenge) | public | Bot/Build challenge for the 9 Oct storm; empty, never used | 2026-10-09 | `tn10-2026-10-09-build-bot-challenge` |
| [tn10-indexer-stall-2026-09](https://github.com/STP-KAS/tn10-storm-2026-09-25-indexer-stall) | private | api-tn10 indexer stall from 25 Sep 21:55 CEST, checked 29 Sep | 2026-09-25 | `tn10-2026-09-25-indexer-stall` |

## C. The September vprogs storms and older TN10 notes (proposed; stp to confirm)

Most of these are public and linked from outside. The rule applies, but stp confirms this group before it is renamed.

| Current name | Visibility | What it holds | Date (CEST) | New name |
|---|---|---|---|---|
| [tn10-vprogs-stress-findings](https://github.com/STP-KAS/tn10-storm-2026-09-25) | public | vprogs storm findings, 25–26 Sep | 2026-09-25 | `tn10-run-2026-09-25-vprogs-findings` |
| [grok-bot-vprogs](https://github.com/STP-KAS/tn10-storm-2026-09-25-r1-private) | private | Bot vprogs journal | 2026-09-25 | `tn10-run-2026-09-25-vprogs-bot` |
| [grok-build-vprogs](https://github.com/STP-KAS/tn10-storm-2026-09-25-build) | public | Build wallet load notes, 25 Sep | 2026-09-25 | `tn10-run-2026-09-25-vprogs-build` |
| [grok-bot-vprogs-round1-public](https://github.com/STP-KAS/tn10-storm-2026-09-25-r1) | public | Round 1 report (25 Sep), clean copy | 2026-09-25 | `tn10-run-2026-09-25-vprogs-round1` |
| [grok-bot-vprogs-round2](https://github.com/STP-KAS/tn10-storm-2026-09-25-r2) | public | Round 2, full-throttle storm | 2026-09-25 | `tn10-run-2026-09-25-vprogs-round2` |
| [grok-bot-vprogs-round3](https://github.com/STP-KAS/tn10-storm-2026-09-26-r3) | public | Round 3, vprogs under a storm | 2026-09-26 (created 01:10) | `tn10-run-2026-09-26-vprogs-round3` |
| [grok-bot-vprogs-round4](https://github.com/STP-KAS/tn10-storm-2026-09-26-r4) | public | Round 4, full-gusto windows, disk emergency | 2026-09-26 | `tn10-run-2026-09-26-vprogs-round4` |
| [grok-bot-vprogs-round5](https://github.com/STP-KAS/tn10-storm-2026-09-26-r5) | public | Round 5, own index-free runners | 2026-09-26 | `tn10-run-2026-09-26-vprogs-round5` |
| [grok-bot-vprogs-round6](https://github.com/STP-KAS/tn10-storm-2026-09-26-r6) | public | Round 6, full speed, stop 13:16 CEST | 2026-09-26 | `tn10-run-2026-09-26-vprogs-round6` |
| [tn10-vprogs-round7-ideas](https://github.com/STP-KAS/tn10-storm-2026-09-26-r7) | public | Round 7, L1 covenant tic-tac-toe | 2026-09-26 | `tn10-run-2026-09-26-vprogs-round7` |
| [tn10-vprogs-round8-covenants](https://github.com/STP-KAS/tn10-storm-2026-09-26-r8) | public | Round 8, covenants quiet vs storm | 2026-09-26 | `tn10-run-2026-09-26-vprogs-round8` |
| [tn10-vprogs-build-opinion](https://github.com/STP-KAS/tn10-storm-2026-09-26-build-opinion) | public | Build's read of the vprogs notes | 2026-09-26 | `tn10-2026-09-26-vprogs-build-opinion` |
| [tn10-vprogs-grokbot-opinion](https://github.com/STP-KAS/tn10-storm-2026-09-26-bot-opinion) | public | The bot's reply to it | 2026-09-26 | `tn10-2026-09-26-vprogs-bot-opinion` |
| [tn10-vprogs-final-verdict](https://github.com/STP-KAS/tn10-storm-2026-09-26-verdict) | public | Final verdict | 2026-09-26 | `tn10-2026-09-26-vprogs-final-verdict` |
| [vprogs-tn-desk](https://github.com/STP-KAS/tn10-storm-2026-09-25-vprogs-desk-private) | private | SilverScript/vprogs desk note, 25–26 Sep | 2026-09-25 | `tn10-2026-09-25-vprogs-desk` |
| [vprogs-tn-desk-public](https://github.com/STP-KAS/tn10-storm-2026-09-25-vprogs-desk) | public | Its public clean copy | 2026-09-25 | `tn10-2026-09-25-vprogs-desk-public` |
| [grok-bot-explorer-rewards-check](https://github.com/STP-KAS/tn10-storm-2026-09-26-explorer-check) | public | Explorer list frozen vs live mining rewards | 2026-09-26 | `tn10-2026-09-26-explorer-rewards-check` |
| [grok-desk-tn10](https://github.com/STP-KAS/tn10-storm-2026-09-27-desk-miners) | private | Desk CPU miner test | 2026-09-27 | `tn10-run-2026-09-27-desk-miners` |
| [tn10-grok](https://github.com/STP-KAS/tn10-storm-2026-09-18-mining) | private | TN10 stress journal from 18 Sep | 2026-09-18 (created) | `tn10-2026-09-18-journal` |
| [tn10-hard-test](https://github.com/STP-KAS/tn10-hard-test) | public | Build's 14 Sep catalog of STP-KAS repos | 2026-09-14 | `tn10-2026-09-14-hard-test` |

**Not in the map** (not TN10 run repos, names kept): the KNS repos (`kns-tn10-testing`, `kns-kasware-tn10-test`, `kns-kaspire-tn10-review`), `stillpay-tn10`, `vprog-runtime-test`, the kaspa-master, KCC, 1984 and site repos.

## How the renames are done (after run 2026-10-10)

1. Wait until run 2026-10-10 has ended, its chain count is done and its logs are pushed (PUSH by 07:30 CEST Sun 11 Oct), and the bot's scheduler for it is stopped.
2. Rename group A, then B, with `gh repo rename <new> -R STP-KAS/<old>`. Group C only after stp says yes.
3. Point the bot's and Build's local clones at the new names (the redirect works, but new names avoid surprises).
4. Update the links in this repo and in [history/README.md](../history/README.md) to the new names.
5. **Never create a new repo with an old name**: that kills the redirect.
6. No tags or releases; visibility does not change with a rename (making `tn10-run-2026-10-10` public after its logs land is a separate step).
