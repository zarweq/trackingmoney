# TrackingMoney — трекер личных финансов
Консольное приложение на Python для учёта доходов и расходов с хранением данных в SQLite и визуализацией через matplotlib
## Возможности
- Добавление операций (доходы/расходы) с категорией и датой
- Просмотр всех операций с фильтром по категории
- Сводка расходов по категориям
- Сводка расходов по месяцам
- Круговая диаграмма расходов по категориям
- Линейный график динамики расходов по месяцам
## Стек
- Python 3
- SQLite 
- matplotlib — для визуализации
## Структура проекта
tracckingmoney/
    main.py # консольное меню, точка входа
    db.py # работа с базой данных (создание таблицы, CRUD, сводки)
    charts.py # построение графиков
    seed_data.py # наполнение базы тестовыми данными
    data/
        finance.db # файл базы данных SQLite
    README.md
## Схема таблицы
sql
create table transactions(
    id integer primary key autoincrement,
    date text not null,
    category text not null,
    amount real not null,
    type text not null check(type in('income','expense'))
)
## Как запустить
1. Установить зависимости:
bash
pip3 install matplotlib
2. Наполнить базу тестовыми данными (опционально):
bash
python3 seed_data.py
3. Запустить приложение:
bash
python3 main.py
4. В меню выбрать нужный пункт, вводя номер:
Добавить операцию
Показать все операции
Сводка по категориям
Сводка по месяцам
График по категориям
График по месяцам
Выход
## Примеры SQL-запросов
Сумма расходов по категориям:
sql
select category, sum(amount) as total
from transactions
where type = 'expense'
group by category
order by total desc


Сумма расходов по месяцам:
sql
select strftime('%Y-%m', date) as month, sum(amount) as total
from transactions
where type = 'expense'
group by month
order by month
## Возможные улучшения
- Валидация ввода (проверка на пустые поля, некорректный формат даты)
- Редактирование и удаление существующих операций
- Экспорт отчётов в CSV
- Веб-интерфейс вместо консольного меню (например, через Streamlit)
