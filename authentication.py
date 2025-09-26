from fastapi import APIRouter, HTTPException, Depends
from schemas import UserSchema, LoginSchema
from depedencies import operating_session
from sqlalchemy.orm import Session
from database import databd
from main import bcrypt_context, TOKEN_EXIPIRE_MINUTES_V, ouath2_schema
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError



authentication_router = APIRouter(prefix="/auth", tags=["authentication"])



def create_token(id_user, duration_token = timedelta(minutes=TOKEN_EXIPIRE_MINUTES_V)):

    date_expiration = datetime.now(timezone.utc) + duration_token

    #se quiser pode usar dentro do jwt.encode com uma variavel dic: dic_info = {'sub': id_user, 'exp': date_expiration}
    token = jwt.encode({'sub': id_user, 'exp': date_expiration}, key=SECRET_KEY_V)

    return token





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
        password_crypted = bcrypt_context.hash(userR.password)

        new_user = databd.User(userR.name, userR.email, password_crypted, userR.adm)
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


@authentication_router.post('/login')
async def login(loginS: LoginSchema, session: Session = Depends(operating_session)):
    user_table = databd.User
    user = session.query(user_table).filter(user_table.emailTable == loginS.email_login).first()

    if not user:
        raise HTTPException(status_code=400, detail= f'The user { {loginS.email_login} } no already existent')
    
    

    else:
        if not bcrypt_context.verify(loginS.password_login, user.passwordTable):
            raise HTTPException(status_code=401, detail=f'Password is wrong')
        
        else:
            access_token = create_token(user.idTable)

            return {
            'access_token': access_token,
            'bearer': 'bearer' 

            }
        
        
