from backend.database.db_functions import delete_table, get_all_yf_price_history
from backend.database.users_database import delete_user_table


def delete_any_table(table_name: str, system_db_path=None):
    try:
        delete_table(system_db_path, table_name)
        return f"System table '{table_name}' deleted."
    except Exception:
        try:
            delete_user_table(table_name)
            return f"User table '{table_name}' deleted."
        except Exception as e:
            raise RuntimeError(f"Delete failed: {e}")
        