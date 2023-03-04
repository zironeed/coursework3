import pytest
import requests
from coursework3.utils.get_file import get_file, get_json
import json

@pytest.fixture
def url():
    return 'https://api.npoint.io/0942bffefc2b5fb8fc31'


@pytest.fixture
def json():
    return '{"done":"DONE!"}'


def test_get_file(url):
    """Берем инфу по ссылке"""
    assert get_file(url) == '{"done":"DONE!"}'


def test_get_json(json):
    """Преобразуем из json"""
    assert get_json(json) == {'done': 'DONE!'}
