from datetime import datetime, timedelta

def get_weekly_totals(data, weeks_ago=0):
    today = datetime.today()
    monday = today - timedelta(days=today.weekday()) - timedelta(weeks=weeks_ago)
    sunday = monday + timedelta(days=6)

    totals = {}
    for e in data:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if monday <= d <= sunday:
            cat = e["category"]
            totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals

def compare_weeks(data):
    this_w = sum(get_weekly_totals(data, 0).values())
    last_w = sum(get_weekly_totals(data, 1).values())
    print(f"\nThis week: {this_w:.2f}")
    print(f"Last week: {last_w:.2f}")
    if last_w > 0:
        change = ((this_w - last_w) / last_w) * 100
        print(f"Change: {change:+.1f}%")
        if change > 20:
            print("Warning! Spending up more than 20%!")