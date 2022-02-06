from urllib import request
from httpx import get, post, delete

api_url = 'http://localhost:8000/posts/'

def test_posts_deve_retornar_200_quando_receber_um_get():
    request = get(api_url)
    assert request.status_code == 200

def test_tasks_deve_retornar_400_quando_receber_um_todo_invalido():
    not_task = {
        "title": "",
        "content": "",
        "author": ""
    }
    request = post(api_url, json=not_task)
    assert request.status_code == 400

def test_tasks_deve_retornar_400_quando_receber_um_todo():
    not_task = {
        "title": "teste 2",
        "content": "outro conteudo",
        "author": "desconhecido"
    }
    request = post(api_url, json=not_task)
    assert request.status_code == 201

def test_tasks_deve_retornar_400_quando_receber_um_todo():
  
    not_task = {
        "title": "teste 2",
        "content": "outro conteudo",
        "author": "desconhecido"
    }
    request = delete(api_url)
    assert request.status_code == 201

