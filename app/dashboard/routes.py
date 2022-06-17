from fastapi import APIRouter
from fastapi.requests import Request

from .handler import Handler

# creat a router + instantiate the handler class 

router = APIRouter()
handler = Handler()

# GET

@router.get("/")
async def get(request: Request):
    return await handler.get_dashboard(request)