import pika
import json


def producer(message, queue, exchange, server='localhost', port=5672):
    try:
        connection_params = pika.ConnectionParameters(server, port)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
    except Exception:
        return f'Oops, something wet wrong with connection on server {server}:{port}'
    channel.queue_declare(queue=queue)
    channel.exchange_declare(exchange=exchange)
    channel.queue_bind(queue=queue, exchange=exchange, routing_key=queue)
    if not isinstance(message, (dict, list)):
        message = bytes(message, encoding='utf-8')
    else:
        message = json.dumps(message).encode('utf-8')
    try:
        channel.basic_publish(exchange, queue, message)
        print(f'Sended message: {message}')
    except Exception:
        return 'Cannot send message'
    connection.close()
