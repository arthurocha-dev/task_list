from fastapi import APIRouter


authentication_router = APIRouter(prefix="/auth", tags=["authentication"])


@authentication_router.get('/teste')
async def firstRouter():
    return {
        'mensagem': "Hello World"
    }