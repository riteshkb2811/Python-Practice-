from fastapi import FastAPI, Request
from pydantic import BaseModel

app=FastAPI()


@app.middleware("http")
async def get_id(request:Request,call_next):
    print("Request Response")

    response=await call_next

    print("Response  sent")
    return response