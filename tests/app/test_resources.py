import json
import pytest

from app.create_app import create_app
from app.controllers.rope import RopeController


@pytest.fixture
def test_client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_get_ropes(mocker, test_client):
    # arrange
    test_ropes = [
        {
            'test rope': 'test rope 1'
        },
        {
            'test rope': 'test rope 2'
        }
    ]
    mock_rope_controller = mocker.patch.object(RopeController, 'fetch_many', return_value=test_ropes)

    # act
    actual = test_client.get('/ropes')

    # assert
    assert json.loads(actual.data) == {'data': test_ropes}
    assert actual.status_code == 200
