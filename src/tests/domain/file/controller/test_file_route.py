import os
os.environ["PROFILE"] = "test"
from fastapi.testclient import TestClient
from main import app
from common.env import settings
client = TestClient(app)

def test_upload_file():
    with open("src/tests/resources/sample.jpg", "rb") as f:
        files = {"file": ("sample.png", f, "image/jpeg")}
        response = client.post(
            "/file/upload",
            files=files,
        )
        assert response.status_code == 200
        body = response.json()
        assert body["file_name"] != "sample.png"
        assert body["size"] == 6268505
        assert body["type"] == "image/jpeg"
        assert body["width"] == 11375
        assert body["height"] == 8992
