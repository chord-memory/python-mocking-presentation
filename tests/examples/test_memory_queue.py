import json
from queue import Queue

import pytest

from examples.memory_queue import put_on_queue_1, put_on_queue_2


def test_put_on_queue_invaluable():
    # arrange
    test_queue = Queue()

    # act
    actual = put_on_queue_1(
        'some test data',
        'some more test data',
        test_queue
    )

    # assert
    assert actual == True


def test_put_on_queue_valuable():
    # arrange
    test_queue = Queue()
    test_data_1 = 'some test data'
    test_data_2 = 'some more test data'
    
    # act
    put_on_queue_2(
        test_data_1,
        test_data_2,
        test_queue
    )

    # assert
    expected = json.dumps(dict(
        first_data=test_data_1,
        second_data=test_data_2
    ))
    assert test_queue.get() == expected
