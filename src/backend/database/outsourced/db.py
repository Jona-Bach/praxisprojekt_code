from backend.database.outsourced.db_functions import create_db, get_connection, create_finance_table, insert_finance_data, fetch_data

#create_db("data","finance_data.db")
connection = get_connection("data","finance_data.db")
create_finance_table(connection, "finance")
insert_finance_data(connection, "finance", 1, 1.0,"Hello")
rows = fetch_data(connection, "finance")
print(rows)

#Python SQL Alchemy: Never Write SQL Syntax Again anschauen!