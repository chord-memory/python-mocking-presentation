import json


def put_on_queue_1(data_1, data_2, queue):
    queue_data = dict(
        first_data=data_1,
        second_data=data_2
    )
    queue.put(json.dumps(queue_data))
    return True


def put_on_queue_2(data_1, data_2, queue):
    queue_data = dict(
        first_data=data_1,
        second_data=data_2
    )
    queue.put(json.dumps(queue_data))
