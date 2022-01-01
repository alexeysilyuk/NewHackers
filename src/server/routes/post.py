from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
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

@router.get("/", response_description="Posts retrieved")
async def get_posts_api():
    posts = await retrieve_all_posts()
    if posts:
        return JSONResponse(
            content={"result": ResponseModel(posts, "Posts data retrieved successfully.")},
            status_code=status.HTTP_200_OK
            )
    return JSONResponse(
        content={"result": ResponseModel(posts, "No posts found.")},
        status_code=status.HTTP_404_NOT_FOUND
        )

@router.get("/{id}", response_description="Post data retrieved")
async def get_post_api(id: str):
    post = await retrieve_post(id)
    if post:
        return JSONResponse(
            content={"result": ResponseModel(post, "Post data retrieved successfully.")},
            status_code=status.HTTP_200_OK
            )
    return JSONResponse(
        content={"result": ErrorResponseModel("An error occurred.", 404, "Post doesn't exist.")},
        status_code=status.HTTP_404_NOT_FOUND
        )
    

@router.post("/", response_description="Post added to database")
async def add_post_api(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    if new_post:
        return JSONResponse(
            content={"result": ResponseModel(new_post, "Post added successfully.")},
            status_code=status.HTTP_200_OK
            )
    return JSONResponse(
        content={"result": ErrorResponseModel("An error occurred.", 500, "Post creation failed.")},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.put("/{id}")
async def update_post_api(id: str, req: UpdatePostModel = Body(...)):
    req = { k: v for k, v in req.dict().items() if v is not None }
    updated_post = await update_post(id, req)
    if updated_post:
        return JSONResponse(
            content={"result": ResponseModel("Updated successfully", "Post with ID: {} updated successfully".format(id))},
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content={"result": ErrorResponseModel("An error occurred", 404, "There was an error updating the post.")},
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.delete("/{id}", response_description="Post data deleted from the database")
async def delete_post_api(id: str):
    deleted_post = await delete_post(id)
    if deleted_post:
        return JSONResponse(
            content={"result": ResponseModel("Removed successfully", "Post with ID: {} removed".format(id))},
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content={"result": ErrorResponseModel("An error occurred", 404, "Post with id {0} doesn't exist".format(id))},
        status_code=status.HTTP_404_NOT_FOUND
    )

