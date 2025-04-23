from fastapi import APIRouter, HTTPException
from app.schemas import TaskCreate, TaskUpdate
from app.models import Task
from app import CRUD

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    return await CRUD.create_task(task)

@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: int):
    task = await CRUD.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=list[Task])
async def read_tasks(completed: bool = None):
    return await CRUD.get_tasks(completed)

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    task = await CRUD.update_task(task_id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    success = await CRUD.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "message": "Task deleted"}