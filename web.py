from fastapi import FastAPI

from src.config import db_init, close_db
from src.models import PersonModel

app = FastAPI()


@app.on_event("startup")
async def init():
    # initialize database
    await db_init()


@app.on_event("shutdown")
async def close():
    # close db connections
    await close_db()


@app.post("/create-ammad")
async def create_ammd():
    ammad = PersonModel(
        first_name="Ammad",
        last_name="Khalid"
    )
    await ammad.save()

    return {
        "created": ammad,
    }
