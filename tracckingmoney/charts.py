import matplotlib.pyplot as plt
from db import get_summary_by_category, get_summary_by_month


def plot_by_category():
    data = get_summary_by_category()
    if not data:
        print("Нет данных для графика.")
        return

    categories = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.figure(figsize=(7, 7))
    plt.pie(totals, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Расходы по категориям")
    plt.axis("equal")
    plt.show()


def plot_by_month():
    data = get_summary_by_month()
    if not data:
        print("Нет данных для графика.")
        return

    months = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.figure(figsize=(9, 5))
    plt.plot(months, totals, marker="o")
    plt.title("Динамика расходов по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Сумма расходов")
    plt.grid(True)
    plt.tight_layout()
    plt.show()