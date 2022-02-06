from urllib import request
from httpx import get, post, delete
import random
import string

random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

api_url = 'http://localhost:8000/user/'
delete_url = 'http://localhost:8000/user/delete/'


def test_posts_return_status_code_200_when_get():
    request = get(api_url)
    assert request.status_code == 200

def test_bad_tasks_return_400_when_invalid_task():
    task = {
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": "",
    "is_active": "true"
    }

    request = post(api_url, json=task)
    assert request.status_code == 400

def test_create_return_201_when_create():
    task = {
        "username": random_string,
        "first_name": random_string,
        "last_name": random_string,
        "email": random_string+"@example.com",
        "password": random_string,
        "is_active": "true"
    }
    request = post(api_url, json=task)
    assert request.status_code == 201

# TODO: to improve this test
def delete_return_400_when_not_find_delete():
      
    id = "2"

    request = delete(delete_url+id)
    assert request.status_code == 404
