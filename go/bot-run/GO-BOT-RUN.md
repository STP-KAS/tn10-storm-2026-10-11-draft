> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).** Do not paste this file before that update. [Lessons so far](../../docs/LESSONS-from-2026-10-10.md)
>
> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md)

# GO, the bot run: TN10 storm, Sunday 11 Oct 2026, T0 12:00 CEST

You are the bot side: **TN10 ops** (operator: n2, the miner, the scheduler and the senders) with **tn ops2** (Grok Bot: logging, the chain count, the write-up). Both of you read this whole file. Build's file is [GO-BUILD-RUN.md](../build-run/GO-BUILD-RUN.md). The timeline and the rates are the same in both. The shared rules are in [go/README.md](../README.md).

**This prompt is locked once stp sends it.** Sending is not the start. It means: be ready by G2 and follow the clock without stp watching. A fix after the lock goes in `events.csv` as a `deviation`.

## GO

**When this repo, this folder or this file lands in the bot's chat (a link or a paste), that is the GO.** No questions. TN10 ops gets ready at once: n2 synced, coins checked, scheduler and watchdog armed on this clock, senders on the 5 public nodes, and it launches at the listed times. Problems are fixed and logged as `deviation`, never turned into a question.

One check stays, because the 10 Oct 17:00 run was halted when Build had not started: the bot only sends once Build is confirmed started (**BUILD-OK**: stp says so, or Build's handoff file shows it) or stp says "go alone". If neither has come by G1 (11:30 CEST), the bot sends stp one short reminder; that is a reminder, not a question.

<!-- clock:header -->
T0 is **12:00 CEST (10:00 UTC), Sunday 11 Oct 2026**. END is **20:00 CEST (18:00 UTC)**. Gate 1 11:30 CEST (09:30 UTC), Gate 2 11:45 CEST (09:45 UTC). Every time is in [Key times](#key-times) and the [Timeline](#timeline). Do not send before X250. Do not move T0.
<!-- /clock:header -->

Thank you, Kaspa Pulse ([@gokugalax](https://x.com/gokugalax)). The node-dead rule and the chain count right after END are his fixes.

## Start clean

- Run 2026-10-10 (T0 20:30 CEST Sat, END 04:30 CEST Sun) is finished by then. Do not resume its scheduler. Start a **fresh** scheduler with a fresh output folder and this clock (refuse any step file whose `t0` is not `2026-10-11T10:00:00Z`). Keep the old output as it is.
- Before you arm: no bot sender, launcher or watchdog from run 2026-10-10 is alive. Check by process name, not only by pid file.
- Pause every other bot-side sender that is not in this plan from G1 to END (for example, ask kns tn10 to pause and log its answer), so B0 means something.

## Where you send

- **Submit only to the five public TN10 nodes:** `muon-10.kaspa.blue`, `boson-10.kaspa.red`, `electron-10.kaspa.blue`, `neutrino-10.kaspa.stream`, `vector-10.kaspa.green` (wRPC, Borsh, testnet-10). Never submit to n2. (stp, 10 Oct 14:36 CEST: "Skip your node. Only use public nodes.")
- **Random spread:** each sender picks four of the five at random at launch, one connection each, and spreads its lanes over them. Over 15 senders every node gets load.
- **Per-node back-off:** a node that gives 20 connection or RPC errors in a row is cooled for 30 s; its lanes move to the sender's other live nodes; the dropped connection is retried in the background. If no node of a sender is live, that sender waits and counts no attempt. Log `node-dead` / `node-back` with the node name.
- **Per-node fee check:** every minute, read each node's normal fee quote. A node quoting above 400 is skipped for that minute (`node-quote-skip`).
- **Build is on its own desk node** (stp, 10 Oct 18:18 CEST) and uses the public nodes only as a fallback, so the load on the public nodes is mostly the bot's 25%. If Build falls back, the public nodes carry more; the bot does not change its rate for that.
- **Be a fair guest.** These are community nodes. If one node keeps rejecting or dropping for more than 10 minutes, drop it for the step and log it. Do not raise the bot's rate to "test" a node.

## n2: your reader

- n2 on the box: kaspad 2.1.0, testnet-10, pruned (**not archival**), UTXO index on, peers and RPC on loopback only. No tunnel, no inbound peers, no public peer port.
- n2 is used for: health reads, the fee quote, watching your own transactions get accepted (virtual chain), the coin list and coin refresh, the chain count, and the one miner.
- **n2 lagging or not synced does not zero the senders** (stp, 10 Oct 16:19 CEST). The senders keep submitting to the public nodes; accepted counts catch up when n2 does.
- **n2 freeze:** if n2's virtual DAA score does not move for over 3 minutes and its sink lag is over 3 minutes, restart n2 on the same flags (at most once per 20 minutes) and log `node-restart`. **Claim (measured on TN10):** n2 froze at its tip at about 15:57 CEST on 10 Oct and a restart at 16:19 CEST fixed it.
- If n2 dies, its supervisor restarts it on the same flags. Never switch on archival to fix anything.

## Your senders

- **15 senders**, one scheduler, locked so a second copy cannot start. Rate per sender = the Bot column divided by the senders that are up.
- **Launch stability (lesson of the public-node test):** launches staggered a few seconds apart; at most one relaunch per sender per minute; at most 8 relaunches per sender for the whole run (then that sender stays down and the others carry its share); no launch while free memory on the box is under 1.5 GB.
- **Fees:** half the lanes at 400, half at 600 sompi/gram. Floor 100, cap 600. Sit a step out if n2's normal quote (or, if n2 cannot answer, muon-10's) is above 400 at step start; log `step-sit-out` with the quote.
- Shape: the no-signature hop (anyone-can-spend P2SH lanes). Label it in every report: "no-signature hop, anyone-can-spend, not realistic payments".
- **Disk:** senders pause at 8 GB free on the box. n2's guard writes STOP at 5 GB and stops n2 at 3 GB.
- **Counting (lesson of 10 Oct 17:21 CEST):** the senders keep no per-transaction file, so each step's submitted and accepted counts come from the senders' per-second files. A step that shows 0 submitted while the senders logged sends is a counting bug, not a result.

## Build started?

- At **G2 (11:45 CEST)** the bot needs stp's confirmation that Build has started (**BUILD-OK**): Build's `FOR-TN10-OPS-ready-1011.txt` with the line `BUILD-OK <time>`, or stp saying "BUILD-OK" or "Build started".
- Without it, tell stp at once. T0 does not move. **Do not send** until stp confirms Build or tells you to go alone; then join the open step. Log each minute without it as `build-not-confirmed`.

## Coins

- **Need:** about 18 million bot transactions over the run. At 400/600 sompi/gram and about 643 grams a hop, that is about 58,000 tKAS of fees. Each sender also locks one coin per lane while it runs, and a relaunched sender locks a fresh set.
- **Buffer before G1 (11:30 CEST):** at least **400,000 tKAS** unclaimed on the bot's coin list. **Top up** (same method) when it falls under 150,000 tKAS. Check every 30 minutes from G1 to END.
- **Method:** read n2's UTXO index through a read-only secondary RocksDB instance (never `getUtxosByAddresses` for the whole address), consolidate old coinbase coins on n2 into about 49 tKAS outputs back to the bot, add only outputs that a fresh read shows confirmed, all through the claim ledger. Abort if free memory falls below 1.5 GB.
- If the buffer cannot be kept, lower the bot's rate and log a `deviation`. Do not stop.

## Your miner

- Exactly one box-CPU kaspa-miner, one thread, on n2's loopback gRPC, paying the bot's own address (kept out of git). On at G2 if n2 is synced (or when it is synced). Off at END. No second miner, no public mining endpoint.

## Clock

Brussels is UTC+2. Clocks in git stay in UTC.

- **G1:** read n2 (synced, UTXO index on, sink lag at most 60 s), the coin buffer, free disk and free memory, and connect once to each public node. Log the result. A failed G1 is logged and fixed; it **does not** hold the senders at 0 later.
- **G2:** the ready check (Build started?), miner on, senders connected and idle.
- If you open this file after a step has ended, join the open step. Never rerun a finished step.

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

- **Hold rule:** hold 800 if the bot's MAX step was clean; otherwise hold the bot's highest clean step rate (60 if none). Never raise mid-step to cover Build.
- **Clean step:** delivered at least 90% of the rate for the whole send window, at least 99% of submitted seen accepted, p90 submit-to-accept at most 10 s. n2's lag is logged next to it but does not decide clean (n2 is not in the submit path).

## Log everything

From G1 to END, even when sending nothing, as in [LOGGING.md](../LOGGING.md): per second (`sec.csv`), per minute (`minute.csv`, with network unique accepted, blocks and our mined blocks), `rejects.csv`, `miner.csv`, `host.csv`, `node.csv`, `events.csv`, `steps.csv`, `gates.csv`, `ntp.csv`. **Add per public node:** submits ok, rejects and errors per minute (`public-nodes.csv`). A 10-minute status line goes to stp's chat only if stp asks.

## Halt

If stp says stop: write the halt flag, **stop the watchdog first**, then the scheduler, set every sender to 0, wait 10 s, then hard-kill every bot sender and the miner by process name. Check nothing restarts. n2 and the read-only loggers stay up. (Lesson of 10 Oct: after a kill, a watchdog started senders again.)

## After END

1. **END:** senders stop, miner off, live loggers stop.
2. **COUNT (the two hours after END, before pruning):** per minute from one hour before T0 to END: network unique accepted, blocks, our mined blocks. Write `chain-count.csv`.
3. Read Build's `FOR-TN10-OPS-result-1011.txt` when stp passes it. Write `steps.csv` and `SUMMARY.md`: per step, bot submitted and accepted, Build's reported numbers, network unique accepted (counted once, never summed), what broke, what was done.
4. **By PUSH (23:00 CEST):** commit to `logs/bot/` in **STP-KAS/tn10-run-2026-10-11**, as STP-KAS. Counts only. No force-push. No tags or releases.
5. **Make public (the bot's task):** after the run, once the logs are on GitHub, TN10 ops makes this repo public. Until then it stays private.

## Never

No host IP, port, key, seed, txid or wallet address in the repo. No tunnel. No second miner. No archival. No fee above 600 or below 100. No firing at a dead node. Do not ping Kaspa Pulse; stp does that.
