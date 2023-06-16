from fastapi import FastAPI
from db_util import DbUtil
from models.models import User
from models.models import Pet
from routers import api_router

app = FastAPI()

### Set up database.
DbUtil.initialize_db()

app.include_router(api_router.api_router)

