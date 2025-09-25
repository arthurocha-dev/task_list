from fastapi import APIRouter, HTTPException, Depends
from schemas import UserSchema
from depedencies import operating_session
from sqlalchemy.orm import Session
from database import databd


authentication_router = APIRouter(prefix="/auth", tags=["authentication"])


@authentication_router.get('/teste')
async def firstRouter():
    return {
        'mensagem': "Hello World"
    }


@authentication_router.post("/create_user")
async def create_user(userR: UserSchema, session: Session = Depends(operating_session)):

    user = session.query(databd.User).filter(databd.User.emailTable == userR.email).first()

    if user:
        raise HTTPException(status_code= 400, detail= f'User { {userR.email} } already existent')
    
    else:
        new_user = databd.User(userR.name, userR.email, userR.password, userR.adm)
        session.add(new_user)
        session.commit()

    return {
        'response': 'user create with success! ',
        
        'user': {
            'name': userR.name,
            'email': userR.email,
            'adm': userR.adm

        }
    }
