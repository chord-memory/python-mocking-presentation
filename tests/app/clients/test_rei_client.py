import pytest

from app.clients.rei import ReiClient
from app.models.rope import RopeModel


def test_rei_client_fetch_ropes(mocker):
    # arrange
    test_rope_1 = dict(
        diameter=9.4,
        length=70,
        brand='mammut',
        color='blue',
        price=264.95
    )
    test_rope_2 = dict(
        diameter=9.9,
        length=60,
        brand='black diamond',
        color='green',
        price=199.95
    )
    test_response_dict = {
        'data': [
            test_rope_1,
            test_rope_2
        ]
    }
    mock_response = mocker.MagicMock()
    mocker.patch.object(mock_response, 'json', return_value=test_response_dict)
    mock_requests_get = mocker.patch('app.clients.rei.requests.get', return_value=mock_response)

    # act
    client = ReiClient('test-rei-url.com', 'random-rope-path')
    actual = client.fetch_ropes()

    # assert
    assert actual == [
        RopeModel(**test_rope_1),
        RopeModel(**test_rope_2)
    ]
    mock_requests_get.assert_called_once_with(
        'test-rei-url.com/random-rope-path'
    )
