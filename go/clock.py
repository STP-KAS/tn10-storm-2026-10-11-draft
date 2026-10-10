#!/usr/bin/env python3
"""The one place for times and rates of the bot run and the build run. Edit T0 below, run `python3 go/clock.py`, commit.

It rewrites the blocks between <!-- clock:NAME --> and <!-- /clock:NAME --> in README.md, go/README.md,
go/bot-run/GO-BOT-RUN.md, go/build-run/GO-BUILD-RUN.md and docs/TIMELINE.md, and writes go/steps-utc.json.
Every step is an offset in minutes from T0. Do not change times or rates by hand anywhere else.
Do not run this after stp has sent the prompts (they are locked then).
DRAFT: written 10 Oct 2026 18:53 CEST; to be updated after run 2026-10-10 (what went wrong, improvements).
"""
import json, re, pathlib
from datetime import datetime, timedelta, timezone

T0 = datetime(2026, 10, 11, 10, 0, tzinfo=timezone.utc)    # <- the only time to edit (12:00 CEST Sun 11 Oct, stp 10 Oct 18:53 CEST)
LOCAL = timezone(timedelta(hours=2), "CEST")               # Brussels, UTC+2
FEE_LOW, FEE_HIGH, FEE_CAP, FEE_FLOOR = 400, 600, 600, 100  # sompi/gram, both sides
SUCCESS_TX_S = 3000

# id, kind, start, end, drain_end, bot tx/s, build tx/s, bot text, build text   (minutes from T0; None = a point in time)
STEPS = [
    ("PREP", "prep", None, -30, None, 0, 0, "Fresh scheduler armed. n2 synced (reads only). Coins topped up. No sends. Miner off.", "Read this file. Desk node synced with UTXO index, coins, senders, public fallback. No sends. Miner off."),
    ("G1", "gate", -30, None, None, 0, 0, "Gate 1: n2 health, coin buffer, the five public nodes reachable. Logging starts.", "Gate 1: desk node health, RAM >= 4 GB free, public fallback reachable, coins, disk. Logging starts. Stop every sender not in this plan."),
    ("G2", "gate", -15, None, None, 0, 0, "Gate 2, **ready check**: BUILD-OK from stp (Build has started). Miner on.", "Gate 2, **ready check**: write `FOR-TN10-OPS-ready-1011.txt` with `BUILD-OK`, stp passes it to the bot. Miner on."),
    ("B0", "baseline", 0, 10, None, 0, 0, "**T0.** No load. Miner on.", "**T0.** No load. Miner on."),
    ("X250", "step", 10, 25, 30, 60, 190, "60", "190"),
    ("C1000", "step", 30, 45, 50, 250, 750, "250", "750"),
    ("C1500", "step", 50, 65, 70, 375, 1125, "375", "1,125"),
    ("C2000", "step", 70, 85, 90, 500, 1500, "500", "1,500"),
    ("C2500", "step", 90, 105, 110, 625, 1875, "625", "1,875"),
    ("MAX", "step", 110, 125, 130, 900, 2600, "900", "2,600 (may go above, never below)"),
    ("B1", "baseline", 130, 140, None, 0, 0, "No load", "No load"),
    ("HOLD", "hold", 140, 465, None, 800, 2400, "800 (see the hold rule)", "2,400 (see the hold rule)"),
    ("DRAIN", "drain", 465, 480, None, 0, 0, "Senders 0", "Senders 0"),
    ("END", "end", 480, None, None, 0, 0, "Senders stop. Miner off. Live loggers stop.", "Senders stop. Miner off. Live loggers stop. Node stays up."),
    ("COUNT", "count", 480, 600, None, 0, 0, "Chain count from n2, before pruning", "Chain count from your desk node, before pruning"),
    ("PUSH", "push", None, 660, None, 0, 0, "Logs to `logs/bot/`", "Logs to `logs/build/`, plus `FOR-TN10-OPS-result-1011.txt` to stp"),
]
G1, G2, END = -30, -15, 480

def at(m, tz=timezone.utc):
    d = (T0 + timedelta(minutes=m)).astimezone(tz)
    s = d.strftime("%H:%M")
    return s + (" " + d.strftime("%a") if d.date() != T0.astimezone(tz).date() else "")

def span(s, e, dr, tz):
    if s is None: return ("by " if e > 0 else "until ") + at(e, tz)
    if e is None: return at(s, tz)
    return f"{at(s, tz)}–{at(e, tz)}" + (f", drain to {at(dr, tz)}" if dr is not None else "")

def table():
    rows = ["| Step | Brussels (CEST) | UTC | Bot tx/s | Build tx/s | Combined tx/s |", "|---|---|---|---|---|---|"]
    for sid, kind, s, e, dr, bot, build, bt, bdt in STEPS:
        comb = f"{bot + build:,}" if kind in ("step", "hold") else "0" if kind in ("baseline", "drain") else "–"
        b = f"**{sid}**" if sid in ("B0", "MAX", "HOLD", "END") else sid
        rows.append(f"| {b} | {span(s, e, dr, LOCAL)} | {span(s, e, dr, timezone.utc)} | {bt} | {bdt} | {comb} |")
    return "\n".join(rows)

def key():
    return "\n".join([
        "| What | Brussels (CEST) | UTC |", "|---|---|---|",
        f"| Gate 1 (G1), logging starts | {at(G1, LOCAL)} | {at(G1)} |",
        f"| Gate 2 (G2), ready check incl. **Build started? (BUILD-OK)**, miners on | {at(G2, LOCAL)} | {at(G2)} |",
        f"| **T0** (B0 starts) | **{at(0, LOCAL)}** | **{at(0)}** |",
        f"| First send step (X250) | {at(10, LOCAL)} | {at(10)} |",
        f"| MAX | {at(110, LOCAL)}–{at(125, LOCAL)} | {at(110)}–{at(125)} |",
        f"| Long hold (HOLD) | {at(140, LOCAL)}–{at(465, LOCAL)} | {at(140)}–{at(465)} |",
        f"| **END**, senders stop, miners off | **{at(END, LOCAL)}** | **{at(END)}** |",
        f"| Chain count (COUNT) | {at(480, LOCAL)}–{at(600, LOCAL)} | {at(480)}–{at(600)} |",
        f"| Logs pushed (PUSH) | by {at(660, LOCAL)} | by {at(660)} |",
        f"| Suggested window for Kaspa Pulse's counter | {at(G2 - 5, LOCAL)}–{at(END + 5, LOCAL)} | {at(G2 - 5)}–{at(END + 5)} |",
    ])

def header():
    d = T0.astimezone(LOCAL)
    return (f"T0 is **{at(0, LOCAL)} CEST ({at(0)} UTC), {d.strftime('%A')} {d.day} Oct 2026**. END is **{at(END, LOCAL)} CEST ({at(END)} UTC)**. "
            f"Gate 1 {at(G1, LOCAL)} CEST ({at(G1)} UTC), Gate 2 {at(G2, LOCAL)} CEST ({at(G2)} UTC). "
            "Every time is in [Key times](#key-times) and the [Timeline](#timeline). Do not send before X250. Do not move T0.")

def targets():
    rows = ["| Step | Brussels (CEST) | UTC | Combined | Bot (25%) | Build (75%) |", "|---|---|---|---|---|---|"]
    for sid, kind, s, e, dr, bot, build, bt, bdt in STEPS:
        if kind in ("step", "hold"):
            rows.append(f"| {sid} | {at(s, LOCAL)}–{at(e, LOCAL)} | {at(s)}–{at(e)} | {bot + build:,} | {bot:,} | {build:,} |")
    return "\n".join(rows + ["",
        f"Fees, both sides: half the lanes at **{FEE_LOW}** and half at **{FEE_HIGH}** sompi/gram, frozen per step. Floor {FEE_FLOOR}, cap {FEE_CAP}. "
        f"Success line: network unique accepted at or above **{SUCCESS_TX_S:,} tx/s**, median of a step's valid minutes, at least 10 valid minutes, counted once from chain data."])

BLOCKS = {"table": table(), "key": key(), "header": header(), "targets": targets()}
root = pathlib.Path(__file__).resolve().parent.parent
for f in ["README.md", "go/README.md", "go/bot-run/GO-BOT-RUN.md", "go/build-run/GO-BUILD-RUN.md", "docs/TIMELINE.md"]:
    p = root / f; s = p.read_text()
    for name, body in BLOCKS.items():
        s = re.sub(rf"(<!-- clock:{name} -->\n)(?:.*?\n)?(<!-- /clock:{name} -->)", lambda m: m.group(1) + body + "\n" + m.group(2), s, flags=re.S)
    p.write_text(s)

iso = lambda m: None if m is None else (T0 + timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ")
steps = [{"step": sid, "kind": kind, "start": iso(s), "end": iso(e), "drain_end": iso(dr), "bot_tx_s": bot, "build_tx_s": build,
          "combined_tx_s": bot + build, "bot": bt, "build": bdt} for sid, kind, s, e, dr, bot, build, bt, bdt in STEPS]
(root / "go/steps-utc.json").write_text(json.dumps({
    "name": "tn10-run-2026-10-11 bot run + build run (DRAFT)", "t0": iso(0), "end": iso(END), "gate1": iso(G1), "gate2": iso(G2),
    "miners": {"on": iso(G2), "off": iso(END)},
    "fees": {"low": FEE_LOW, "high": FEE_HIGH, "cap": FEE_CAP, "floor": FEE_FLOOR},
    "split": {"bot": 0.25, "build": 0.75}, "success_network_unique_accepted_tx_s": SUCCESS_TX_S,
    "hold_rule": "Each side holds its HOLD rate if its MAX step was clean; otherwise its highest clean step rate (bot: 60 if none; Build: 190 if none).",
    "steps": steps}, indent=1, ensure_ascii=False) + "\n")
print("T0", iso(0), "END", iso(END))
