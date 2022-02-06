from urllib import request
from httpx import get, post, delete
import random
import string

random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

api_url = 'http://localhost:8000/user/'
delete_url = 'http://localhost:8000/user/delete/'


def test_posts_deve_retornar_200_quando_receber_um_get():
    request = get(api_url)
    assert request.status_code == 200

def test_tasks_deve_retornar_400_quando_receber_um_todo_invalido():
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

def test_tasks_deve_retornar_400_quando_receber_um_todo():
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

def test_tasks_deve_retornar_400_quando_receber_um_todo():
      
    id = "2"

    request = delete(delete_url+id)
    assert request.status_code == 404
