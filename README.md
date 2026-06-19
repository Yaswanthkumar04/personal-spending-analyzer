# 💰 Personal Spending Analyzer

A terminal-based Python application that helps you track, 
categorize, and analyze your daily expenses.

---

## 🚀 Features

- 📝 Log expenses with amount, category, and notes
- 💾 Auto-saves data using JSON (no database needed)
- 📊 Weekly spending summary with ASCII bar chart
- 📅 Week-over-week comparison
- ⚠️ Smart alerts if spending increases more than 20%

---

## 🛠️ Tech Stack

- Python 3.x
- JSON (data storage)
- datetime module
- File I/O
- No external libraries needed!

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| main.py | App menu and flow |
| tracker.py | Add and read expenses |
| analyzer.py | Calculate totals and trends |
| chart.py | Draw ASCII bar chart |
| expenses.json | Auto-created data storage |

---

## ▶️ How to Run

```bash
python main.py
📌 Menu Options
1. Add Expense   → Enter amount, category, note
2. View This Week → See ASCII bar chart
3. Compare Weeks → See % change from last week
4. Exit

💡 Concepts Used
Dictionaries
Loops and Functions
datetime manipulation
File I/O
List comprehensions
Modular programming

👨‍💻 Author
Yaswanth Kumar
github.com/Yaswanthkumar04
