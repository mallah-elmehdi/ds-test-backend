from fastapi import APIRouter
from .dashboard import routes as dashboard
from .gen import routes as gen

# include all the app's routers

router = APIRouter()
router.include_router(gen.router, tags=["dashboard"], prefix="/_")
router.include_router(dashboard.router, tags=["dashboard"], prefix="/dashboard")