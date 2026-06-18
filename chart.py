def draw_chart(totals):
    if not totals:
        print("No data for this week.")
        return

    print("\n=== Weekly Spending Chart ===")
    max_val = max(totals.values())
    grand_total = sum(totals.values())

    for cat, total in sorted(totals.items(), key=lambda x: -x[1]):
        bar_len = int((total / max_val) * 30)
        bar = "█" * bar_len
        pct = (total / grand_total) * 100
        print(f"{cat:<12} {bar:<30} {total:>8.2f} ({pct:.1f}%)")

    print(f"\nTotal: {grand_total:.2f}")