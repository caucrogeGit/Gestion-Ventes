from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST       = os.getenv("DB_HOST", "localhost")
DB_PORT       = int(os.getenv("DB_PORT", 3306))
DB_NAME       = os.getenv("DB_NAME", "Ventes")
DB_USER_LOGIN = os.getenv("DB_USER_LOGIN", "root")
DB_USER_PWD   = os.getenv("DB_USER_PWD", "")

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 8000))


