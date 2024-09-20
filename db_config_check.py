import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get('POSTGRES_URL')
engine = create_engine(DATABASE_URL)
try:
    with engine.connect() as connection:
        print("Database connection successful")
except Exception as e:
    print(f"Database connection failed: {str(e)}")