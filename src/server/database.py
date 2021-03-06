import motor.motor_asyncio
import os
from bson import ObjectId
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGO_CONNECTION_STRING"))
db = mongo_client.posts

posts_collection = db.get_collection("posts_collection")

def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "content": post["content"],
    }


# Retrieve all posts from database
async def retrieve_all_posts():
    posts = []
    async for post in posts_collection.find():
        posts.append(post_helper(post))
    return posts


# Add a new post into to the database
async def add_post(post_data: dict) -> dict:
    try:
        post = await posts_collection.insert_one(post_data)
        new_post = await posts_collection.find_one({"_id": ObjectId(post.inserted_id)})
        return post_helper(new_post)
    except:
        pass

# Retrieve a post with a matching ID
async def retrieve_post(id: str) -> dict:
    try:
        post = await posts_collection.find_one({"_id": ObjectId(id)})
        if post:
            return post_helper(post)
    except:
        pass



# Update a post with a matching ID
async def update_post(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    try:
        post = await posts_collection.find_one({"_id": ObjectId(id)})
        if post:
            updated_post = await posts_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_post:
                return True
            return False
    except:
        pass

# Delete a post from the database
async def delete_post(id: str):
    try:
        post = await posts_collection.find_one({"_id": ObjectId(id)})
        if post:
            await posts_collection.delete_one({"_id": ObjectId(id)})
            return True
    except:
        pass