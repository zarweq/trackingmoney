import sqlite3

DB_PATH = "data/finance.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists transactions(
            id integer primary key autoincrement,
            date text not null,
            category text not null,
            amount real not null,
            type text not null check(type in('income','expense'))
            )
    """)
    conn.commit()
    conn.close()


def add_transaction(date, category, amount, type_):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        insert into transactions(date, category, amount, type)
        values (?, ?, ?, ?)
    """, (date, category, amount, type_))
    conn.commit()
    conn.close()


def get_transactions(category=None):
    conn = get_connection()
    cursor = conn.cursor()
    if category:
        cursor.execute("""
            select id, date, category, amount, type
            from transactions
            where category = ?
            order by date
        """, (category,))
    else:
        cursor.execute("""
            select id, date, category, amount, type
            from transactions
            order by date
        """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_summary_by_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        select category, sum(amount) as total
        from transactions
        where type = 'expense'
        group by category
        order by total desc
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_summary_by_month():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        select strftime('%Y-%m', date) as month, sum(amount) as total
        from transactions
        where type = 'expense'
        group by month
        order by month
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    print("База данных и таблица созданы (или уже существовали).")