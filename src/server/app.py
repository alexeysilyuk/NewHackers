from fastapi import FastAPI
from server.routes.post import router as PostRouter

app = FastAPI()

app.include_router(PostRouter, tags=["NewHackers Posts"], prefix="/posts")
