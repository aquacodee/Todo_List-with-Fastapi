from fastapi import FastAPI
from route import todo




app = FastAPI(title='To-do list', description='A to-do list Application running on FastAPI + uvicorn', version='0.1.0')

app.include_router(todo.todo_router)
