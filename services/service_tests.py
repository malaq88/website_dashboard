from urllib import request
from httpx import get, post, delete

api_url = 'http://localhost:8000/services/'
delete_url = 'http://localhost:8000/services/delete/'

def test_posts_deve_retornar_200_quando_receber_um_get():
    request = get(api_url)
    assert request.status_code == 200

def test_tasks_deve_retornar_400_quando_receber_um_todo_invalido():
    task =   {
        "title": "",
        "description": "",
        "price": ""
    }
    request = post(api_url, json=task)
    assert request.status_code == 400

def test_tasks_deve_retornar_400_quando_receber_um_todo():
    task =   {
        "title": "string",
        "description": "string",
        "price": 9223372036854776000
    }
    request = post(api_url, json=task)
    assert request.status_code == 201

def test_tasks_deve_retornar_400_quando_receber_um_todo():
  
    _id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    request = delete(delete_url+_id)
    assert request.status_code == 404

