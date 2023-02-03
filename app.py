from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
  return fake_database

@app.post("/todos")
async def create_todo(request: Request):
  todo = await request.json()
  fake_database.append(todo)
  return todo

@app.delete("/todos/{todo_id}")
async def delete_todo_by_id(todo_id: int):
    for i, todo in enumerate(fake_database):
        if todo["id"] == todo_id:
            fake_database.pop(i)
            return {format(todo_id)}
    return {format(todo_id)}
