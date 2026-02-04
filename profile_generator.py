"""
Upwork About Me generator.
Uses data.json metrics, Industrial Engineering background, and automation experience.
"""

import json
from datetime import datetime
from pathlib import Path


def load_data():
    path = Path(__file__).parent / "data.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_metrics(data):
    total = data["toplam_kazanc"]
    records = data["gunluk_kayitlar"]
    if not records:
        return {"total": 0, "daily_avg": 0, "days_active": 0, "entries": 0}

    dates = sorted(set(r["tarih"] for r in records))
    start = datetime.strptime(min(dates), "%Y-%m-%d")
    end = datetime.strptime(max(dates), "%Y-%m-%d")
    days_active = max(1, (end - start).days + 1)
    daily_avg = round(total / days_active, 2) if days_active else 0

    return {
        "total": total,
        "daily_avg": daily_avg,
        "days_active": days_active,
        "entries": len(records),
    }


def generate_about_me(metrics):
    total = metrics["total"]
    daily_avg = metrics["daily_avg"]
    days_active = metrics["days_active"]
    entries = metrics["entries"]

    headline = "Data-Driven Industrial Engineer & Automation Specialist"

    # Speed/efficiency proof from data
    if daily_avg > 0 and total > 0:
        speed_line = (
            f"I track every project and every outcome - currently {days_active} days into a quantified journey "
            f"with a {total:,.0f} TL run rate and a {daily_avg:,.0f} TL/day average. "
            "That same discipline is what I bring to your workflows: measurable results and no wasted time."
        )
    else:
        speed_line = (
            "I run my own work by the numbers and bring that same discipline to every client: "
            "clear deliverables, on-time delivery, and workflows you can measure."
        )

    body = f"""
{headline}

I'm an Industrial Engineering student at Yasar University with a focus on turning data and processes into results. I don't just build scripts—I design systems that save hours and scale with your business.

{speed_line}

**What I do for you:**
• **Data automation** — Python-driven automation for Excel, JSON, and databases so your pipelines run 100% without manual steps.
• **Dynamic web dashboards** — Live charts and panels so you and your team see the numbers that matter, in real time.
• **Process efficiency** — An Industrial Engineering lens on your operations: digitization, bottlenecks removed, and time given back to you.

I promise efficiency: fewer repetitive tasks, clearer visibility into your data, and delivery you can count on. If you want a freelancer who treats your project like a system, not a one-off, let's talk.
""".strip()

    return body


def main():
    data = load_data()
    metrics = compute_metrics(data)
    about_me = generate_about_me(metrics)
    print(about_me)


if __name__ == "__main__":
    main()
