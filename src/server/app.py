from fastapi import FastAPI
from server.routes.post import router as PostRouter

app = FastAPI()

app.include_router(PostRouter, tags=["Post"], prefix="/posts")
