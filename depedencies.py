from database import databd
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
from main import ouath2_schema, SECRET_KEY_V
from jose import jwt, JWTError, ExpiredSignatureError


def operating_session():
    try:
        Session = sessionmaker(bind=databd.db)

        session = Session()

        yield session
    
    finally:
        session.close()



def verify_token(tokenP: str = Depends(ouath2_schema), session: Session = Depends(operating_session)):
    try:
        dicionaty_informations_user = jwt.decode(token=tokenP, key=SECRET_KEY_V, algorithms="HS256" )
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token Expired')
    
    except JWTError:
        raise HTTPException(status_code=401, detail= 'Token invalid')

    id_user = int(dicionaty_informations_user.get('sub'))
    table_user = databd.User
    user = session.query(table_user).filter(table_user.idTable == id_user).first()

    if not user:
        raise HTTPException(status_code=401,detail= "User no already or access daniet" )
    
    else:
        return user
