import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")

if not DB_URL:
    raise ValueError("DB_URL not found in .env file")


def get_connection():
    return psycopg.connect(DB_URL)