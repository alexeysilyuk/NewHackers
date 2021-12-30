from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_post,
    delete_post,
    retrieve_post,
    retrieve_all_posts,
    update_post,
)
from server.models.post import (
    ErrorResponseModel,
    ResponseModel,
    PostSchema,
    UpdatePostModel,
)

router = APIRouter()

@router.post("/", response_description="Post added to database")
async def add_post_api(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    return ResponseModel(new_post, "Post added successfully.")


@router.get("/", response_description="Posts retrieved")
async def get_posts_api():
    posts = await retrieve_all_posts()
    if posts:
        return ResponseModel(posts, "Posts data retrieved successfully")
    return ResponseModel(posts, "Empty list returned")


@router.get("/{id}", response_description="Post data retrieved")
async def get_post_api(id):
    post = await retrieve_post(id)
    if post:
        return ResponseModel(post, "Post data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Post doesn't exist.")


@router.put("/{id}")
async def update_post_api(id: str, req: UpdatePostModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_post = await update_post(id, req)
    if updated_post:
        return ResponseModel(
            "Post with ID: {} updated successfully".format(id),
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the post.",
    )


@router.delete("/{id}", response_description="Post data deleted from the database")
async def delete_post_api(id: str):
    deleted_post = await delete_post(id)
    if deleted_post:
        return ResponseModel(
            "Post with ID: {} removed".format(id)
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Post with id {0} doesn't exist".format(id)
    )
