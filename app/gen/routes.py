from fastapi import APIRouter
from fastapi.requests import Request

from .handler import Handler
from .schema import UserModel

# creat a router + instantiate the handler class

router = APIRouter()
handler = Handler()

# GET


@router.get("/sign-in")
async def get(request: Request):
    return handler.get_signin(request)


@router.post("/sign-in")
async def post(request: Request, user: UserModel):
    return await handler.signin(request, user)
