from db import init_db, add_transaction

def seed():
    init_db()

    transactions = [
        # Июнь
        ("2026-06-03", "продукты", 2200, "expense"),
        ("2026-06-05", "зарплата", 85000, "income"),
        ("2026-06-08", "транспорт", 450, "expense"),
        ("2026-06-12", "развлечения", 1800, "expense"),
        ("2026-06-15", "продукты", 1900, "expense"),
        ("2026-06-20", "коммуналка", 4200, "expense"),
        ("2026-06-25", "транспорт", 300, "expense"),

        # Июль
        ("2026-07-01", "продукты", 2500, "expense"),
        ("2026-07-05", "зарплата", 85000, "income"),
        ("2026-07-06", "транспорт", 500, "expense"),
        ("2026-07-10", "развлечения", 2200, "expense"),
        ("2026-07-14", "продукты", 1700, "expense"),
        ("2026-07-18", "подработка", 15000, "income"),
        ("2026-07-20", "коммуналка", 4300, "expense"),
        ("2026-07-22", "продукты", 2100, "expense"),
    ]

    for date, category, amount, type_ in transactions:
        add_transaction(date, category, amount, type_)

    print(f"Добавлено {len(transactions)} операций.")


if __name__ == "__main__":
    seed()