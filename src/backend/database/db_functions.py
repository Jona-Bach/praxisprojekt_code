import sqlite3
import os

def create_db(folder_name, db_name):
    try:
        current_dir = os.path.dirname(__file__)
        project_root = os.path.abspath(os.path.join(current_dir, "../../.."))
        data_folder = os.path.join(project_root, folder_name)
        os.makedirs(data_folder, exist_ok=True)
        db_path = os.path.join(data_folder, db_name)
        connection = sqlite3.connect(db_path)
        return connection
        print(f"Database successful created at: {db_path}")
    except Exception as e:
        print(f"Error while creating database: {e}")

def get_connection(db_folder_name, db_name):
    try:
        current_dir = os.path.dirname(__file__)
        project_root = os.path.abspath(os.path.join(current_dir, "../../.."))
        db_path = os.path.join(project_root, db_folder_name, db_name)
        return sqlite3.connect(db_path)
    except:
        print(f"Error with connecting to:{db_name}")
        return None

def create_finance_table(connection, tablename):
    query = f"""
    CREATE TABLE IF NOT EXISTS {tablename} (
    id INTEGER,
    price REAL,
    date TEXT
    )


    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Table created!")
    except Exception as e:
        print(f"Error while creating table: {e}")

def insert_finance_data(connection, table_name, id, price, date):
    query = f"INSERT INTO {table_name} (id, price, date) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (id, price, date))
        print(f"Eintrag erfolgreich hinzugefügt: id={id}, price={price}, date={date}")
    except Exception as e:
        print(f"Fehler beim Einfügen in {table_name}: {e}")

def fetch_data(connection, table):
    query = f"Select * FROM {table}"

    with connection:
        row = connection.execute(query).fetchall()
    return row