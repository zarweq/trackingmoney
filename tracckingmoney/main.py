from db import init_db, add_transaction, get_transactions, get_summary_by_category, get_summary_by_month
from charts import plot_by_category, plot_by_month


def print_menu():
    print("\n=== Трекер финансов ===")
    print("1. Добавить операцию")
    print("2. Показать все операции")
    print("3. Сводка по категориям")
    print("4. Сводка по месяцам")
    print("5. График по категориям")
    print("6. График по месяцам")
    print("0. Выход")


def handle_add_transaction():
    date = input("Дата (ГГГГ-ММ-ДД): ")
    category = input("Категория: ")
    amount = float(input("Сумма: "))
    type_ = input("Тип (income/expense): ")
    add_transaction(date, category, amount, type_)
    print("Операция добавлена.")


def handle_show_transactions():
    category = input("Фильтр по категории (Enter — все): ").strip()
    category = category if category else None
    transactions = get_transactions(category)
    if not transactions:
        print("Операций не найдено.")
        return
    for t in transactions:
        print(t)


def handle_summary_by_category():
    summary = get_summary_by_category()
    for category, total in summary:
        print(f"{category}: {total:.2f}")


def handle_summary_by_month():
    summary = get_summary_by_month()
    for month, total in summary:
        print(f"{month}: {total:.2f}")


def main():
    init_db()

    actions = {
        "1": handle_add_transaction,
        "2": handle_show_transactions,
        "3": handle_summary_by_category,
        "4": handle_summary_by_month,
        "5": plot_by_category,
        "6": plot_by_month,
    }

    while True:
        print_menu()
        choice = input("Выбор: ").strip()

        if choice == "0":
            print("Выход.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Неверный выбор, попробуй снова.")


if __name__ == "__main__":
    main()