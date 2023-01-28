from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class ToDo(BaseModel):
    id: Optional[int]
    task: str

    @classmethod
    def as_form( cls, task: str = Form(...) ):
        
        return cls(task=task)
    
    class Config:
        schema_extra = {
            "Example" : {
                "task": "How is it?"
            }
        }

class TodoTask(BaseModel):
    task: str

    class Config:
        schema_extra = {
            "examples": {
                "task": "read your next task"
            }
        }



class TodoTasks(BaseModel):
    task: List[TodoTask]

    class Config:
        schema_extra = {
            "examples": {
                "todos": [
                    {
                        "task": "task 1"
                    },
                    {
                        "task": "task 2"
                    }
                ]
            }
        }