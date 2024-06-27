from fast_zero.app import app

from http import HTTPStatus

from fastapi.testclient import TestClient


def test_read_root_retorna_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garantia)
    assert response.json() == {'message': 'Hello World!'}
