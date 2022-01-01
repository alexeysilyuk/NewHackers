from typing import Optional

from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "content": "This is new very cool topic",
            }
        }


class UpdatePostModel(BaseModel):
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "content": "This is new very cool topic",
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
