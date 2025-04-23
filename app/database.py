import asyncpg
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://{}:{}@localhost/{}'.format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_DB')
))

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

