from fastapi.testclient import TestClient
from fastapi import Form, status
import json

client = TestClient(app)

def get_all_posts_empty():
    response = client.get("/posts")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
