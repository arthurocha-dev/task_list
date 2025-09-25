from fastapi import FastAPI
from passlib.context import CryptContext

#instância da aplicação + criação da aplicação
# a variavel tem que ser "app"
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


from authentication import authentication_router
from tasks import tasks_router

app.include_router(authentication_router)
app.include_router(tasks_router)