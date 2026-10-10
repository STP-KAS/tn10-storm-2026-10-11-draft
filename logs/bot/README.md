> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).**
>
> **Experimental. We are just trying this.** [Disclaimer](../../DISCLAIMER.md)

# logs/bot

Written by TN10 ops and tn ops2 after the run. Submits: the five public TN10 nodes. Reads: n2 (the bot's private node on the box). Raw logs stay on the box; this folder gets the copy.

Status: **`SUMMARY.md` goes live from G1 (11:30 CEST Sun 11 Oct)**, updated every 15 minutes; the other files land after END.

| File | Every | What | Read it for |
|---|---|---|---|
| `sec.csv` | every second | One row per second per side: what the senders did and how the node looked. | [columns](../../go/LOGGING.md#seccsv) |
| `minute.csv` | every minute | One row per minute per side; the file to line up with Kaspa Pulse's count. | [columns](../../go/LOGGING.md#minutecsv) |
| `public-nodes.csv` | every minute, per public node | Which public node took, refused or failed. | [columns](../../go/LOGGING.md#public-nodescsv) |
| `rejects.csv` | every second with a reject | Why submits failed. | [columns](../../go/LOGGING.md#rejectscsv) |
| `miner.csv` | every 10 s | The side's one miner. | [columns](../../go/LOGGING.md#minercsv) |
| `host.csv` | every 10 s | The machine: is it the bottleneck? | [columns](../../go/LOGGING.md#hostcsv) |
| `node.csv` | every 10 s | The side's own node (bot: n2, the reader; Build: its desk node). | [columns](../../go/LOGGING.md#nodecsv) |
| `events.csv` | each event | Everything that happened, in order (list below). | [columns](../../go/LOGGING.md#eventscsv) |
| `steps.csv` | each step | The verdict per step. | [columns](../../go/LOGGING.md#stepscsv) |
| `gates.csv` | each gate read | G1 and G2. | [columns](../../go/LOGGING.md#gatescsv) |
| `ntp.csv` | start and end | Clock offset, so rows line up. | [columns](../../go/LOGGING.md#ntpcsv) |
| `chain-count.csv` | COUNT, per minute, one hour before T0 to END | The chain count right after END, before pruning (Kaspa Pulse's fix). | [columns](../../go/LOGGING.md#chain-countcsv) |
| `confirm.csv` | each step | How long a submit took to be accepted, by fee tier. | [columns](../../go/LOGGING.md#confirmcsv) |
| [`SUMMARY.md`](SUMMARY.md) | every 15 min during the run (live), final after END | Now, public nodes, n2 and box, steps so far, last events | the 5-minute read |

How to read the run in 5 minutes: [go/LOGGING.md](../../go/LOGGING.md#how-to-read-the-run-in-5-minutes).

Columns: [go/LOGGING.md](../../go/LOGGING.md). Counts only. Per-transaction logs and ids stay local.
