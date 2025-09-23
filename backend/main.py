from fastapi import FastAPI

#instância da aplicação + criação da aplicação
# a variavel tem que ser "app"
app = FastAPI()


from authentication import authentication_router

app.include_router(authentication_router)