# import uvicorn
from fastapi import FastAPI
from app.router import router as api_router

# create the application obj
app = FastAPI()

app.include_router(api_router, prefix="/api")

# run the application

# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0')