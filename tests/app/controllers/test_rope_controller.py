from dataclasses import asdict

import pytest

from app import app_settings
from app.clients.rei import ReiClient
from app.controllers.rope import RopeController
from app.models.rope import RopeModel


def test_rope_controller_fetch_many_1(mocker):
    # arrange
    test_rei_client = ReiClient(**app_settings['rei'])
    test_rope_model_1 = RopeModel(
        diameter=9.4,
        length=70,
        brand='mammut',
        color='blue',
        price=264.95
    )
    test_rope_model_2 = RopeModel(
        diameter=9.9,
        length=60,
        brand='black diamond',
        color='green',
        price=199.95
    )
    mock_fetch_ropes = mocker.patch.object(test_rei_client, 'fetch_ropes', return_value=[
        test_rope_model_1,
        test_rope_model_2
    ])

    # act
    actual = RopeController().fetch_many([test_rei_client])

    # assert
    assert actual == [
        asdict(test_rope_model_1),
        asdict(test_rope_model_2)
    ]
    mock_fetch_ropes.assert_called_once_with()


def test_rope_controller_fetch_many_2(mocker):
    # arrange
    test_client_with_rope_1 = mocker.MagicMock()
    test_client_with_rope_2 = mocker.MagicMock()
    test_rope_model_1 = RopeModel(
        diameter=9.4,
        length=70,
        brand='mammut',
        color='blue',
        price=264.95
    )
    test_rope_model_2 = RopeModel(
        diameter=9.9,
        length=60,
        brand='black diamond',
        color='green',
        price=199.95
    )
    test_rope_model_3 = RopeModel(
        diameter=9.4,
        length=40,
        brand='edelrid',
        color='pink',
        price=199.95
    )
    test_rope_model_4 = RopeModel(
        diameter=9.9,
        length=60,
        brand='mammut',
        color='yellow',
        price=264.95
    )
    mock_fetch_ropes_1 = mocker.patch.object(test_client_with_rope_1, 'fetch_ropes', return_value=[
        test_rope_model_1,
        test_rope_model_2
    ])
    mock_fetch_ropes_2 = mocker.patch.object(test_client_with_rope_2, 'fetch_ropes', return_value=[
        test_rope_model_3,
        test_rope_model_4
    ])

    # act
    actual = RopeController().fetch_many([test_client_with_rope_1, test_client_with_rope_2])

    # assert
    assert actual == [
        asdict(test_rope_model_1),
        asdict(test_rope_model_2),
        asdict(test_rope_model_3),
        asdict(test_rope_model_4)
    ]
    mock_fetch_ropes_1.assert_called_once_with()
    mock_fetch_ropes_2.assert_called_once_with()
