import os
from dotenv import load_dotenv

load_dotenv()

def _as_bool(v, default=False):
    if v is None:
        return default
    return str(v).strip().lower() in {"1", "true", "yes", "y", "on"}

class Config:

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or os.getenv("DATABASE_URI")
        or "postgresql+psycopg2://postgres:postgres@localhost:5432/crud_db_fresh"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = _as_bool(os.getenv("TRACK_MODIFICATIONS"), False)

  
