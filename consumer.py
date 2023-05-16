import pika
import json


def consumer(queue, server='localhost', port=5672):
    try:
        connection_params = pika.ConnectionParameters(server, port)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
    except Exception:
        return f'Oops, something wet wrong with connection on server {server}:{port}'
    channel.queue_declare(queue=queue)
    method, properties, body = channel.basic_get(queue)
    if method:
        result = body.decode('utf-8')
        # channel.basic_ack(method.delivery_tag)
        try:
            result = json.loads(result)
        except:
            result = result
        return result
    else:
        return 'No messages returned'
