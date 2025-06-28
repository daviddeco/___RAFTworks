### main.py (FastAPI backend)
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


#! from motor.motor_asyncio import AsyncIOMotorClient  # ASYNC - Sync will just use PyMongo

from contextlib import asynccontextmanager  # needed for lifespan event handler change
from decouple import config

DB_URL = config("DB_LOCAL_URL", cast=str)  # use local SQLite
DB_NAME = config("DB_LOCAL_NAME", cast=str)


# add in router(s)
# from .routes.cars import router as cars_router

import pandas as pd


# **********************
# **** Lifespan - Startup and Shutdown ****
# chatGPT advice for lifespan rewrite since advertised way is deprecated
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]
    yield
    # Shutdown
    app.mongodb_client.close()


# local needs
from utils.reporting_template import get_high_sales
from ___RAFTworks.backend.api.v1.crud import get_sales_data, sales


app = FastAPI(lifespan=lifespan)
df = pd.read_csv("data/stores.csv")

router = APIRouter()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Simple return the dat dataframe
@app.get("/sales")
def read_sales():
    return df


# Use Router - This should likely be moved
@app.get("/high-sales")
def read_high_sales(threshold: float = 1800):

    hs = get_high_sales(df, threshold)
    if hs.empty:
        return {"message": "NONE had high sales"}
    return hs.to_dict(orient="records")  #! LOOK AT THIS DD


# *** Self-Run
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082, reload=True)
