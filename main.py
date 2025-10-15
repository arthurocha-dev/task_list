from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

TOKEN_EXIPIRE_MINUTES_V = int(os.getenv('TOKEN_EXIPIRE_MINUTES'))
SECRET_KEY_V = os.getenv('SECRET_KEY')










#instância da aplicação + criação da aplicação
# a variavel tem que ser "app"
app = FastAPI()

origins = [
    "http://localhost:5173"
]


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

ouath2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login_athorize")


from authentication import authentication_router
from tasks import tasks_router

app.include_router(authentication_router)
app.include_router(tasks_router)


# 🔥 Permite que o front se conecte ao back
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"] se quiser deixar mais seguro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)