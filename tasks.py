from fastapi import APIRouter, HTTPException, Depends
from depedencies import operating_session
from schemas import TaskSchema 
from sqlalchemy.orm import Session
from database import databd


tasks_router = APIRouter(prefix='/tasks', tags='tasks')


@tasks_router.post('/create_list_tasks')
async def create_task(tasks: TaskSchema, session: Session = Depends(operating_session)):
    table = databd.Tasks
    task = session.query(table).filter(table)