from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task Manager API")

tasks = {}
counter = 1

class Task(BaseModel):
    title: str
    done: Optional[bool] = False

@app.get("/tasks")
def get_tasks():
    return list(tasks.values())

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global counter
    new_task = {"id": counter, "title": task.title, "done": task.done}
    tasks[counter] = new_task
    counter += 1
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks.pop(task_id)

@app.get("/health")
def health():
    return {"status": "ok"}