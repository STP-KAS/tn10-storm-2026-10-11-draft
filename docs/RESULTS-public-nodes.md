> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# The afternoon public-node test, Sat 10 Oct 2026, 14:23 to 16:18 CEST

Back to [README](../README.md). Full report and data: [tn10-storm-1010-public-nodes](https://github.com/STP-KAS/tn10-storm-1010-public-nodes) (private, [REPORT.md](https://github.com/STP-KAS/tn10-storm-1010-public-nodes/blob/main/REPORT.md)). Bot senders only; Build sent to the same five public nodes at the same time, so network counts were combined.

| What | Value | Label |
|---|---|---|
| Window | about 14:23 to 15:57 CEST (12:23 to 13:57 UTC); senders torn down 16:18 CEST | Claim (measured on TN10) |
| Peak bot submitted | about **3,168 tx/s** at 14:38 CEST (22 senders), about 2,969 accepted | Claim (measured on TN10) |
| Earlier highs | about **2,415 tx/s** at 14:27 CEST (21 senders); about **2,430 tx/s** at about 14:35 CEST (19 senders, fees 400) | Claim (measured on TN10) |
| Clean hold | about **880 to 985 tx/s** submitted on **14 senders**; last row 15:57 CEST: 984.7 submitted, 976.4 accepted, 0 rejects | Claim (measured on TN10) |
| Fees | 200, then **400** sompi/gram from 14:26 CEST (stp) | Claim (measured on TN10) |
| Rejects | 0 in the clean phase; spikes only during the launcher overspawn | Claim (measured on TN10) |
| Box limit | RAM: the out-of-memory killer took n2 at about 14:51 CEST above about 20 senders | Claim (measured on TN10) |
| n2 tip freeze | about 15:57 to 16:20 CEST; fixed by a restart | Claim (measured on TN10) |
| Launcher overspawn | two launchers, senders past 20, rate fell from about 2,850 to about 200 tx/s; fixed with one locked launcher and a hard cap | Claim (measured on TN10) |
| Per-node behaviour | muon-10 and vector-10 took most ok submits; boson-10, electron-10 and neutrino-10 often refused connections when many senders booted at once | Claim; the cause is Not sure / open for debate |

What this plan took from it: [LESSONS.md](LESSONS.md) and [LESSONS-from-2026-10-10.md](LESSONS-from-2026-10-10.md).
