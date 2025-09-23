from fastapi import APIRouter
from schemas import UserSchema


authentication_router = APIRouter(prefix="/auth", tags=["authentication"])


@authentication_router.get('/teste')
async def firstRouter():
    return {
        'mensagem': "Hello World"
    }


@authentication_router.post("/create_user")
async def create_user(user: UserSchema):
    return {
        'response': f'user { {user.name} } create with success! ' 
    }
