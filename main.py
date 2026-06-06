from fastapi import FastAPI
from routers.user_routers import user_router
app = FastAPI()


app.include_router(user_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}