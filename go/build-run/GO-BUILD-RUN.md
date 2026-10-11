> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).** Do not paste this file before that update. [Lessons so far](../../docs/LESSONS-from-2026-10-10.md)
>
> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md)

# GO, the build run: TN10 storm, Sunday 11 Oct 2026, T0 12:00 CEST

You are **Grok Build** on stp's Windows desk. You carry **75% of the load**. The bot carries 25% from the box. The bot's file is [GO-BOT-RUN.md](../bot-run/GO-BOT-RUN.md). The timeline and the rates are the same in both. The shared rules are in [go/README.md](../README.md).

**This prompt is locked once stp sends it.** Sending is not the start. It means: **start now, be armed by G2 (11:45 CEST)**, and follow the clock without stp watching. A fix after the lock goes in your `events.csv` as a `deviation`.

## GO

**When this repo, this folder or this file lands in Build's chat (a link or a paste), that is the GO.** No questions. Build gets ready at once: node or public nodes checked, coins checked, senders armed on this clock, and it launches at the listed times. Problems are fixed and logged as `deviation`, never turned into a question.

As soon as Build is armed, it writes `FOR-TN10-OPS-ready-1011.txt` with the line `BUILD-OK <time CEST>` so stp can pass it to the bot. The bot does not send until Build is confirmed started (BUILD-OK).

<!-- clock:header -->
T0 is **12:00 CEST (10:00 UTC), Sunday 11 Oct 2026**. END is **20:00 CEST (18:00 UTC)**. Gate 1 11:30 CEST (09:30 UTC), Gate 2 11:45 CEST (09:45 UTC). Every time is in [Key times](#key-times) and the [Timeline](#timeline). Do not send before X250. Do not move T0.
<!-- /clock:header -->

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). The node-dead rule and the chain count right after END are his fixes.

## Why you must start now

On 10 Oct the 17:00 CEST run was halted by stp at 17:39 CEST because Build had not been started. In this run the bot **does not send** until stp confirms you have started (BUILD-OK). So: arm everything as soon as you read this, and write the ready file (below) by 11:45 CEST.

## Where you send: your own desk node first, the public nodes as fallback

**Set 10 Oct 2026, 18:18 CEST, by stp, and kept for 11 Oct:** Build uses its **own desk node as primary** for its whole 75% share (2,600 at MAX, 2,400 in the hold). The five public TN10 nodes are Build's **fallback only**.

- **Primary, your desk node:** kaspad 2.1.0, `--testnet --netsuffix=10 --utxoindex`, pruned (no `--archival`), peers and RPC on loopback only, no tunnel, no public peer port, a watcher that restarts it on the same flags. It must be **synced with the UTXO index on by G2 (11:45 CEST)**. Run 2026-10-10 ended at 04:30 CEST; if the desk node was stopped after it, start it again by 09:00 CEST.
- **If it is not synced by G2:** start on the public nodes at the listed times, log a `deviation`, and move to your node once it is synced and healthy for 2 minutes (log `node-back`).
- **Fallback, the five public TN10 nodes:** `muon-10.kaspa.blue`, `boson-10.kaspa.red`, `electron-10.kaspa.blue`, `neutrino-10.kaspa.stream`, `vector-10.kaspa.green` (wRPC, Borsh, testnet-10), random spread over all five, per-node back-off (below).
- **Move to the fallback** (only the affected senders) when your desk node: has a sink lag over 60 s, or its virtual DAA score stalls for 30 s, or stops being synced, or dies (RPC fails for 5 s). Log `node-fallback` and a `deviation` with the reason.
- **Move back** when your node has been healthy (synced, sink lag at most 60 s, DAA moving) for **2 minutes**. Log `node-back`.
- **Desk safety:** keep **at least 4 GB RAM free** on the desk. If memory gets tight, move senders to the public fallback (log `node-fallback`, reason `desk RAM`) instead of letting the node crash.
- **Never submit to the bot's node**, and **never fire at a dead node** (below).

### Desk lessons

- **Claim (measured on TN10):** Build pushed over 3,000 tx/s into blocks from the desk last week.
- **Claim (measured on TN10):** on 9 Oct the desk nodes keel and locus lagged and froze about every 10 minutes, and locus died at about 03:28 CEST on Saturday 10 Oct.
- **Not sure / open for debate:** node B most likely crashed because the desk's 32 GB of memory ran out while it was building its UTXO index on 9 Oct. Hence the 4 GB free-RAM rule and the public fallback.

## Your rates

Send the **Build** column. **Change 10 Oct 2026, 19:03 CEST (stp): bot rates +10%.** Bot column ×1.1 (X250 60→66, C1000 250→275, C1500 375→413, C2000 500→550, C2500 625→688, MAX 900→990, HOLD 800→880; bot fallback hold 60→66). Build rates unchanged. Combined targets rise to 256, 1,025, 1,538, 2,050, 2,563, 3,590 and 3,280; step labels (X250, C1000 …) are kept as names. Your column does not change. Never raise your rate mid-step to cover a bot shortfall. At MAX you may go above 2,600, never below. Use as many senders as you need; a fixed number, started once, not respawned in a loop.

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

- **Hold rule:** hold 2,400 if your MAX step was clean; otherwise hold your highest clean step rate (190 if none).
- **Clean step:** you delivered at least 90% of your rate for the whole send window, at least 99% of submitted were seen accepted, p90 submit-to-accept at most 10 s.

## Fees

- Half your lanes at **400**, half at **600** sompi/gram, frozen per step. **Floor 100, cap 600.** (stp asked for double fees at 14:25 CEST on 10 Oct; the old pair 200/300, doubled.)
- If the normal fee quote at step start is above 400, sit that step out and log `step-sit-out` with the quote.
- On public nodes: if one node quotes above 400, skip it for a minute and spread over the others.

## Node-dead rule (Kaspa Pulse)

- **Public nodes (fallback):** a node that gives about 20 connection or RPC errors in a row is cooled for 30 s and your load moves to the other live nodes. If none is live, wait and count no attempt. Log `node-dead` and `node-back` with the node name.
- **Your own node (primary):** a sender never fires at it when the node's RPC fails for 5 s, the node is not synced, its sink lag is over 60 s, or its virtual DAA score stops for 30 s. Instead it moves to the public fallback (`node-fallback`) and comes back after 2 minutes of good health (`node-back`), inside the open step.
- A failed submit is a reject, never "sent".

## Coins

- Build's own wallet and coins. Each sender has its own coins.
- **Work out your need before G1:** transactions × grams per transaction × fee. Example: your column adds up to about 54 million transactions over the run; × 1,000 grams × 500 sompi/gram that is about 270,000 tKAS of fees. Have at least 1.5 times your need ready before G1.
- **Coin-refresh rule (stp, 12:21 CEST):** check every 30 minutes; top up in small, memory-safe batches; never list a whole address in one call (that call once pushed a node to 9.4 GB and it was killed); never re-add a spent or claimed coin; log every refresh. If you cannot keep the buffer, lower your rate and log a `deviation`; do not stop.

## Your miner

- At most **one** miner, one thread, on **your own node only**, paying Build's own address (kept out of git). On at G2, off at END.

## Clock

Brussels is UTC+2. Clocks in git stay in UTC.

- **G1 (11:30 CEST):** stop every desk sender not in this plan (including anything left from run 2026-10-10). Read your setup: desk node synced with the UTXO index on, sink lag at most 60 s, at least 4 GB RAM free, each public fallback node reachable, coins ready, disk free. Logging starts. A failed read is retried for two minutes and fixed; it does not move T0.
- **G2 (11:45 CEST):** write `FOR-TN10-OPS-ready-1011.txt` with `BUILD-OK` (below). stp passes it to the bot. Miner on.
- **One step clock.** One holder process reads one copy of [go/steps-utc.json](../steps-utc.json) as it was when stp sent this prompt. Refuse any step file whose `t0` is not `2026-10-11T10:00:00Z`. Never start a second holder.
- If you open this file after a step has ended, join the open step. Never rerun a finished step.
- If stp has to paste anything, give him **one** PowerShell block that does all of it (node and watcher, senders with the public fallback, loggers, the step clock) and then needs nothing more from him. Put everything under `%USERPROFILE%\grok-build\tn10-run-2026-10-11\`.

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

## Timeline

<!-- clock:table -->
| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |
|---|---|---|---|---|---|
| PREP | until 11:30 | until 09:30 | Fresh scheduler armed. n2 synced (reads only). Coins topped up. No sends. Miner off. | Read this file. Desk node synced with UTXO index, coins, senders, public fallback. No sends. Miner off. | – |
| G1 | 11:30 | 09:30 | Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts. | Gate 1: desk node health, RAM >= 4 GB free, public fallback reachable, coins, disk. Logging starts. Stop every sender not in this plan. | – |
| G2 | 11:45 | 09:45 | Gate 2, **ready check**: BUILD-OK from stp (Build has started). Miner on. | Gate 2, **ready check**: write `FOR-TN10-OPS-ready-1011.txt` with `BUILD-OK`, stp passes it to the bot. Miner on. | – |
| **B0** | 12:00–12:10 | 10:00–10:10 | **T0.** No load. Miner on. | **T0.** No load. Miner on. | 0 |
| X250 | 12:10–12:25, drain to 12:30 | 10:10–10:25, drain to 10:30 | 66 | 190 | 256 |
| C1000 | 12:30–12:45, drain to 12:50 | 10:30–10:45, drain to 10:50 | 275 | 750 | 1,025 |
| C1500 | 12:50–13:05, drain to 13:10 | 10:50–11:05, drain to 11:10 | 413 | 1,125 | 1,538 |
| C2000 | 13:10–13:25, drain to 13:30 | 11:10–11:25, drain to 11:30 | 550 | 1,500 | 2,050 |
| C2500 | 13:30–13:45, drain to 13:50 | 11:30–11:45, drain to 11:50 | 688 | 1,875 | 2,563 |
| **MAX** | 13:50–14:05, drain to 14:10 | 11:50–12:05, drain to 12:10 | 990 | 2,600 (may go above, never below) | 3,590 |
| B1 | 14:10–14:20 | 12:10–12:20 | No load | No load | 0 |
| **HOLD** | 14:20–19:45 | 12:20–17:45 | 880 (see the hold rule) | 2,400 (see the hold rule) | 3,280 |
| DRAIN | 19:45–20:00 | 17:45–18:00 | Senders 0 | Senders 0 | 0 |
| **END** | 20:00 | 18:00 | Senders stop. Miner off. Live loggers stop. | Senders stop. Miner off. Live loggers stop. Node stays up. | – |
| COUNT | 20:00–22:00 | 18:00–20:00 | Chain count from n2, before pruning | Chain count from your desk node, before pruning | – |
| PUSH | by 23:00 | by 21:00 | Logs to `logs/bot/` | Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1011.txt` to stp | – |
<!-- /clock:table -->

## Log everything

From G1 to END, even when sending nothing, with the columns in [LOGGING.md](../LOGGING.md): `sec.csv`, `minute.csv`, `rejects.csv`, `host.csv`, `events.csv`, `steps.csv`, `gates.csv`, `ntp.csv`; plus `node.csv`, `miner.csv` and `chain-count.csv` from your node; plus `public-nodes.csv` (per minute, per public node: submits ok, rejects, errors) for any minute on the fallback; plus every `node-fallback` / `node-back` in `events.csv`. Per-transaction logs and ids stay on the desk.

## Handoff files for the bot

The bot cannot see your screen. stp carries two plain-text files from you to the bot. Formats are in [LOGGING.md](../LOGGING.md#handoff-files-build-to-the-bot).

1. **`FOR-TN10-OPS-ready-1011.txt` at G2 (11:45 CEST):** `BUILD-OK <time CEST>`, started yes, submit path (own node, or public fallback and why), senders, coins ready (tKAS), fee pair, desk node synced, desk RAM free, miner on/off, step file `t0`.
2. **`FOR-TN10-OPS-result-1011.txt` after END (by 22:00 CEST):** one line per step: target, mean submitted, mean accepted, rejects, clean yes/no and why; plus node deaths, restarts, every fallback to the public nodes (CEST from–to, reason), sit-outs and deviations.

## After END

1. **END (20:00 CEST):** senders stop, miner off, live loggers stop. Your desk node stays up.
2. **COUNT (20:00 to 22:00 CEST):** write `chain-count.csv` from your node per minute from one hour before T0 to END, before pruning.
3. Write `steps.csv`, `SUMMARY.md` and the result handoff file.
4. **By PUSH (23:00 CEST):** commit your files to `logs/build/` in **STP-KAS/tn10-storm-2026-10-11-draft**. Counts only. No force-push. No tags or releases.
5. **Make public (the bot's task):** after the run, once the logs are on GitHub, TN10 ops makes this repo public. Until then it stays private.

## Never

No host IP, port, key, seed, txid or wallet address in the repo. No tunnel. No second miner. No archival. No fee above 600 or below 100. No sending to the bot's node. No firing at a dead node.
