import json
from queue import Queue

import pytest

from examples.sqs_queue import put_on_queue


def test_put_on_queue(mocker):
    # arrange
    mock_queue = mocker.MagicMock()
    mock_send_message = mocker.patch.object(mock_queue, 'send_message')

    test_data_1 = 'some test data'
    test_data_2 = 'some more test data'
    
    # act
    put_on_queue(
        test_data_1,
        test_data_2,
        mock_queue
    )

    # assert
    expected = json.dumps(dict(
        first_data=test_data_1,
        second_data=test_data_2
    ))
    mock_send_message.assert_called_once_with(
        MessageBody=expected
    )
