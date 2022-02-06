from urllib import request
from httpx import get, post, delete

api_url = 'http://localhost:8000/posts/'
delete_url = 'http://localhost:8000/posts/delete/'


def test_posts_return_status_code_200_when_get():
    request = get(api_url)
    assert request.status_code == 200

def test_bad_tasks_return_400_when_invalid_task():
    task = {
        "title": "",
        "content": "",
        "author": ""
    }
    request = post(api_url, json=task)
    assert request.status_code == 400

def test_create_return_201_when_create():
    task = {
        "title": "teste 2",
        "content": "outro conteudo",
        "author": "1"
    }
    request = post(api_url, json=task)
    assert request.status_code == 201

# TODO: to improve this test
def delete_return_400_when_not_find_delete():
      
    _id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    request = delete(delete_url+_id)
    assert request.status_code == 404
