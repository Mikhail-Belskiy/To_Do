import asyncpg
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.database import DATABASE_URL
from typing import List, Optional

async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

async def create_task(task: TaskCreate) -> Task:
    conn = await get_connection()
    row = await conn.fetchrow(
        'INSERT INTO tasks(title, description, due_date) VALUES($1, $2, $3) RETURNING *',
        task.title, task.description, task.due_date
    )
    await conn.close()
    return Task(**row)

async def get_task(task_id: int) -> Optional[Task]:
    conn = await get_connection()
    row = await conn.fetchrow('SELECT * FROM tasks WHERE id = $1', task_id)
    await conn.close()
    return Task(**row) if row else None

async def get_tasks(completed: Optional[bool] = None) -> List[Task]:
    conn = await get_connection()
    if completed is not None:
        rows = await conn.fetch('SELECT * FROM tasks WHERE completed = $1', completed)
    else:
        rows = await conn.fetch('SELECT * FROM tasks')
    await conn.close()
    return [Task(**row) for row in rows]

async def update_task(task_id: int, task_update: TaskUpdate) -> Optional[Task]:
    conn = await get_connection()
    columns = []
    values = []
    if task_update.title is not None:
        columns.append("title = $1")
        values.append(task_update.title)
    if task_update.description is not None:
        columns.append("description = $2")
        values.append(task_update.description)
    if task_update.due_date is not None:
        columns.append("due_date = $3")
        values.append(task_update.due_date)
    if task_update.completed is not None:
        columns.append("completed = $4")
        values.append(task_update.completed)

    if columns:
        values.append(task_id)
        await conn.execute(f'UPDATE tasks SET {", ".join(columns)} WHERE id = ${len(values)}', *values)

    updated_row = await conn.fetchrow('SELECT * FROM tasks WHERE id = $1', task_id)
    await conn.close()
    return Task(**updated_row) if updated_row else None

async def delete_task(task_id: int) -> bool:
    conn = await get_connection()
    await conn.execute('DELETE FROM tasks WHERE id = $1', task_id)
    await conn.close()
    return True