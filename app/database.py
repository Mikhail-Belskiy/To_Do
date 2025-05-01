import asyncpg
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

async def create_database():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute(
        '''CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            deadline TIMESTAMPTZ NOT NULL,
            completed BOOLEAN DEFAULT FALSE
            )'''
    )
    await conn.close()

