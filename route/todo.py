from fastapi import FastAPI, APIRouter, Path, HTTPException, status, Request, Depends
from schemas import ToDo, TodoTask, TodoTasks
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory = "templates/")


todo_router = APIRouter(prefix = '/to-do', tags = ["TO-DO LIST"])

todo_list = []

@todo_router.post('/')
async def add_todo(request: Request, todo: ToDo = Depends(ToDo.as_form) ) -> dict:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",  {
        "request": request,
         "todos": todo_list 
    })
    
    return {"massage" : "successfully added"}


@todo_router.get('/')
async def get_todo(request: Request) -> dict:

    return templates.TemplateResponse("todo.html", {"request": request, "todos": todo_list })

    return {"todos": todo_list}

@todo_router.get('/{todo_id}')
async def get_by_id(todo_id: int = Path(..., title = "Getting todo by id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo" : todo
            }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"The task with id: {todo_id} is not available!")


@todo_router.put('/{todo_id}')
async def update_task(todo_data: TodoTask, todo_id: int = Path(..., title = "the id of the task you want to update.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.task = todo_data.task
            return {
                "message": f"Task with id: {todo_id} is updated successfully"
            }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Task with id: {todo_id} doesn't exist!!")

@todo_router.delete('/{todo_id}')
async def delete_by_id(todo_id:  int)  -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)

            return {
                "message": "Task deleted successfully."
            }
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =  f"Task with id: {todo_id} doesn't exist.")
    


@todo_router.delete('/')
async def Delete_all() -> dict:
    todo_list.clear()
    return {
        "message": "Tasks deleted successfuly!"
    }