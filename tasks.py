import json
from fastapi import APIRouter, HTTPException, Depends
from depedencies import operating_session, Depends, verify_token
from schemas import TaskSchema, PathListSchema
from sqlalchemy.orm import Session
from database import databd


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'], dependencies=[Depends(verify_token)])







@tasks_router.post('/create_list_tasks')
async def create_task(tasksR: TaskSchema, session: Session = Depends(operating_session), userToken: databd.User = Depends(verify_token)):
    tableTask = databd.Tasks

    task_exists = session.query(tableTask).filter(tableTask.name_listT == tasksR.name_list).first()

    if task_exists:
        raise HTTPException(status_code=400, detail=f'The list task with the o name of { {tasksR.name_list} } already existent') 
    
    else:
        task = tableTask(
        user_idP=  userToken.idTable,
        name_listP = tasksR.name_list,
        tasksP =  tasksR.tasks_list,
        )
        session.add(task)
        session.commit()

        return{
            'mensager': f'List { {tasksR.name_list} } create with success!',

            'list name': tasksR.name_list,
            'tasks': tasksR.tasks_list

        }
    

@tasks_router.get('/get_list')
# requisições get não aceitam parametros do tipo pydantic(json)
async def getList(name_listP: str, session: Session = Depends(operating_session), token_user: databd.User = Depends(verify_token)):

    tableTask = databd.Tasks
    task_exists = session.query(tableTask).filter(tableTask.name_listT == name_listP, tableTask.user_idT == token_user.idTable).first()

    if not task_exists:
        raise HTTPException(status_code=400, detail= f"The { {name_listP} } no existent or you no have see this is list")
    
    else:
         return {
            'task': name_listP,
            'list': json.loads(task_exists.tasksT)

         }
    

@tasks_router.delete('/delete_list_of_task')
async def delete_list(name_list: str, session: Session = Depends(operating_session), user: databd.User = Depends(verify_token)):

    table_task = databd.Tasks

    task = session.query(table_task).filter(table_task.name_listT == name_list, table_task.user_idT == user.idTable).first()

    if not task:
        raise HTTPException(status_code= 401, detail= 'error! You no have permission or list no existent')
    
    else:
        session.delete(task)
        session.commit()

        return{
            'mensager': f'list { {name_list} } deleted with success'
        }


@tasks_router.patch("/edit_list")
async def edit_list(name_listE: str, edit_listSchema: PathListSchema, user: databd.User = Depends(verify_token), session: Session = Depends(operating_session)):

    tableTask = databd.Tasks
    list_exist = session.query(tableTask).filter(tableTask.name_listT == name_listE, tableTask.user_idT == user.idTable).first()

    if not list_exist:
        raise HTTPException(status_code=401, detail=f'The { {name_listE} } no existent or you no have access this is list')
    
    else:
        
        list_exist.name_listT = json.dumps(edit_listSchema.name_edited)
        list_exist.tasksT = json.dumps(edit_listSchema.list_edited)


        session.commit()

        return{
            'mensager': f'Lits { {name_listE} } update with success!'
        }

        

    