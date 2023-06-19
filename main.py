from fastapi import FastAPI
from database.db_util import DbUtil
from routers import api_router

app = FastAPI()

### Set up database.
DbUtil.initialize_db()

app.include_router(api_router.api_router)

