from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

# Binds engine to create a new DB with todos table from models.py and database.py
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
