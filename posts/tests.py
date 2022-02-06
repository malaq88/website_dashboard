import pytest
from urllib import request
from httpx import get

api_url = 'http://localhost:8000/'

@pytest.mark.xfail
def test_posts_deve_retornar_200_quando_receber_um_get():
    request = get(api_url)
    assert request.status_code == 200