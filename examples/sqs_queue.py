import json


def put_on_queue(data_1, data_2, queue):
    queue_data = dict(
        first_data=data_1,
        second_data=data_2
    )
    queue.send_message(MessageBody=json.dumps(queue_data))
