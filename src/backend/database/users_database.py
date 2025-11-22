from backend.database.db_functions import create_av_alchemy_db, get_table
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, DateTime, inspect, Date, text, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from sqlalchemy import UniqueConstraint
from datetime import datetime
import openpyxl
import pandas as pd
import json
import os

engine, Base, session, dbpath = create_av_alchemy_db("data", "users_database")

# Falls du direkt mit Sessions arbeiten willst:
SessionLocal = sessionmaker(bind=engine)


def _normalize_column_names(columns):
    """
    Spaltennamen etwas säubern:
    - Trim
    - Kleinbuchstaben
    - Leerzeichen -> Unterstrich
    """
    clean = []
    for c in columns:
        if not isinstance(c, str):
            c = str(c)
        c = c.strip().lower().replace(" ", "_")
        clean.append(c)
    return clean


def import_file_as_table(file_obj, filename: str, table_name: str, if_exists: str = "fail"):
    """
    Liest eine CSV- oder Excel-Datei in einen DataFrame und schreibt sie als Tabelle
    in die users_database.

    Parameters
    ----------
    file_obj : file-like (z.B. Streamlit uploaded_file)
    filename : str
        Wird benutzt, um die Dateiendung zu erkennen (.csv / .xlsx / .xls)
    table_name : str
        Name der Tabelle in der Datenbank
    if_exists : {"fail", "replace", "append"}
        Verhalten, wenn Tabelle bereits existiert
    """
    ext = os.path.splitext(filename)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_obj)
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_obj)
    else:
        raise ValueError(f"Unsupported file type: {ext}. Please upload CSV or Excel.")

    # Spaltennamen etwas säubern
    df.columns = _normalize_column_names(df.columns)

    # In DB schreiben
    df.to_sql(table_name, engine, index=False, if_exists=if_exists)

    return df  # kann für Preview im Frontend genutzt werden


def list_user_tables():
    """
    Gibt eine Liste aller Tabellen in der users_database zurück.
    """
    inspector = inspect(engine)
    return inspector.get_table_names()


def get_user_table(table_name: str) -> pd.DataFrame:
    """
    Lädt eine Tabelle aus users_database als DataFrame.
    """
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        raise ValueError(f"Tabelle '{table_name}' existiert nicht in users_database.")
    
    safe_name = f'"{table_name}"'

    query = f"SELECT * FROM {safe_name}"
    df = pd.read_sql(query, engine)
    return df