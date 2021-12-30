from typing import Optional

from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    title: str = Field(...)
    body: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "My cool news topic",
                "body": "This is new very cool topic"
            }
        }


class UpdatePostModel(BaseModel):
    title: Optional[str]
    body: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "My cool news topic",
                "body": "This is new very cool topic"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
