> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).**
>
> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# Timeline, Sun 11 Oct 2026 (T0 12:00 CEST)

Back to [README](../README.md). Written by [go/clock.py](../go/clock.py); the same tables are in [go/README.md](../go/README.md#timeline) and both GO files. Machine-readable: [go/steps-utc.json](../go/steps-utc.json). Times: CEST first, UTC second.

## Key times

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

## Every step

<!-- clock:table -->
| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |
|---|---|---|---|---|---|
| PREP | until 11:30 | until 09:30 | Fresh scheduler armed. n2 synced (reads only). Coins topped up. No sends. Miner off. | Read this file. Desk node synced with UTXO index, coins, senders, public fallback. No sends. Miner off. | – |
| G1 | 11:30 | 09:30 | Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts. | Gate 1: desk node health, RAM >= 4 GB free, public fallback reachable, coins, disk. Logging starts. Stop every sender not in this plan. | – |
| G2 | 11:45 | 09:45 | Gate 2, **ready check**: BUILD-OK from stp (Build has started). Miner on. | Gate 2, **ready check**: write `FOR-TN10-OPS-ready-1011.txt` with `BUILD-OK`, stp passes it to the bot. Miner on. | – |
| **B0** | 12:00–12:10 | 10:00–10:10 | **T0.** No load. Miner on. | **T0.** No load. Miner on. | 0 |
| X250 | 12:10–12:25, drain to 12:30 | 10:10–10:25, drain to 10:30 | 60 | 190 | 250 |
| C1000 | 12:30–12:45, drain to 12:50 | 10:30–10:45, drain to 10:50 | 250 | 750 | 1,000 |
| C1500 | 12:50–13:05, drain to 13:10 | 10:50–11:05, drain to 11:10 | 375 | 1,125 | 1,500 |
| C2000 | 13:10–13:25, drain to 13:30 | 11:10–11:25, drain to 11:30 | 500 | 1,500 | 2,000 |
| C2500 | 13:30–13:45, drain to 13:50 | 11:30–11:45, drain to 11:50 | 625 | 1,875 | 2,500 |
| **MAX** | 13:50–14:05, drain to 14:10 | 11:50–12:05, drain to 12:10 | 900 | 2,600 (may go above, never below) | 3,500 |
| B1 | 14:10–14:20 | 12:10–12:20 | No load | No load | 0 |
| **HOLD** | 14:20–19:45 | 12:20–17:45 | 800 (see the hold rule) | 2,400 (see the hold rule) | 3,200 |
| DRAIN | 19:45–20:00 | 17:45–18:00 | Senders 0 | Senders 0 | 0 |
| **END** | 20:00 | 18:00 | Senders stop. Miner off. Live loggers stop. | Senders stop. Miner off. Live loggers stop. Node stays up. | – |
| COUNT | 20:00–22:00 | 18:00–20:00 | Chain count from n2, before pruning | Chain count from your desk node, before pruning | – |
| PUSH | by 23:00 | by 21:00 | Logs to `logs/bot/` | Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1011.txt` to stp | – |
<!-- /clock:table -->

## Targets

<!-- clock:targets -->
| Step | Brussels (CEST) | UTC | Combined | Bot (25%) | Build (75%) |
|---|---|---|---|---|---|
| X250 | 12:10–12:25 | 10:10–10:25 | 250 | 60 | 190 |
| C1000 | 12:30–12:45 | 10:30–10:45 | 1,000 | 250 | 750 |
| C1500 | 12:50–13:05 | 10:50–11:05 | 1,500 | 375 | 1,125 |
| C2000 | 13:10–13:25 | 11:10–11:25 | 2,000 | 500 | 1,500 |
| C2500 | 13:30–13:45 | 11:30–11:45 | 2,500 | 625 | 1,875 |
| MAX | 13:50–14:05 | 11:50–12:05 | 3,500 | 900 | 2,600 |
| HOLD | 14:20–19:45 | 12:20–17:45 | 3,200 | 800 | 2,400 |

Fees, both sides: half the lanes at **400** and half at **600** sompi/gram, frozen per step. Floor 100, cap 600. Success line: network unique accepted at or above **3,000 tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data.
<!-- /clock:targets -->

Rules for each step (gates, fees, node-dead rule, hold rule): [go/README.md](../go/README.md).
