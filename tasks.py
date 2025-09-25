import json
from fastapi import APIRouter, HTTPException, Depends
from depedencies import operating_session
from schemas import TaskSchema, SearchListSchema
from sqlalchemy.orm import Session
from database import databd


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])


@tasks_router.post('/create_list_tasks')
async def create_task(tasksP: TaskSchema, session: Session = Depends(operating_session)):
    tableTask = databd.Tasks
    task_exists = session.query(tableTask).filter(tableTask.name_listT == tasksP.name_list).first()

    if task_exists:
        raise HTTPException(status_code=400, detail=f'The list task with the o name of { {tasksP.name_list} } already existent') 
    
    else:
        task = tableTask(tasksP.name_list, tasksP.tasks)
        session.add(task)
        session.commit()

        return{
            'mensager': f'List { {tasksP.name_list} } create with success!',

            'list name': tasksP.name_list,
            'tasks': tasksP.tasks

        }
    

@tasks_router.get('/get_list')
# requisições get não aceitam parametros do tipo pydantic(json)
async def getList(name_listP: str, session: Session = Depends(operating_session)):

    tableTask = databd.Tasks
    task_exists = session.query(tableTask).filter(tableTask.name_listT == name_listP).first()

    if not task_exists:
        raise HTTPException(status_code=400, detail= f"The { {name_listP} } no existent")
    
    else:

        return {
            'task': name_listP,
            'list': json.loads(task_exists.tasksT)

        }

    