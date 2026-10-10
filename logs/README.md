> **DRAFT — will be updated after run 2026-10-10 (what went wrong, improvements).**
>
> **Experimental. We are just trying this.** [Disclaimer](../DISCLAIMER.md)

# logs: where the results land

Empty until the run (T0 12:00 CEST, Sun 11 Oct 2026). Each side drops its files here after the chain count, by the PUSH time in [go/README.md](../go/README.md#key-times).

| Folder | Side | Submits to | Who writes it |
|---|---|---|---|
| [bot/](bot/README.md) | Bot run | The five public TN10 nodes (n2 for reads) | TN10 ops and tn ops2 |
| [build/](build/README.md) | Build run | Build's own desk node (public nodes as fallback) | Grok Build |

File names and columns are in [go/LOGGING.md](../go/LOGGING.md). Both folders use the same names, so files can be joined on `minute_utc` and lined up with Kaspa Pulse's count.

The headline, network unique accepted tx/s, is counted once from chain data, never summed across sides. A combined page, `COMBINED.md`, is written here after both folders are filled.

Live during the run: [bot/SUMMARY.md](bot/SUMMARY.md), every 15 minutes. How to read the run in 5 minutes: [go/LOGGING.md](../go/LOGGING.md#how-to-read-the-run-in-5-minutes).

After the run, once the logs are on GitHub, TN10 ops makes this repo public.

Counts only. No txid, key, seed, host IP, port or wallet address.
