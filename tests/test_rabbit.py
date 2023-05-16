import pytest
from producer import producer
from consumer import consumer


@pytest.mark.parametrize('msg, queue, exchange',
                         [('SuperCool', 'supertest', 'exp'),
                          ({'a': 1}, 'supertest_new', 'exp')])
def test_rabbit_messages(msg, queue, exchange):
    producer(msg, queue, exchange)
    result = consumer(queue)
    assert result == msg, f'Message - {result}'


@pytest.mark.parametrize('msg, queue, exchange, host, port',
                         [('SuperCool', 'supertest', 'ex', 'localhost', 9090)])
def test_rabbit_invalid_producer(msg, queue, exchange, host, port):
    message = producer(msg, queue, exchange, host, port)
    assert message == f'Oops, something wet wrong with connection on server {host}:{port}', \
        f'Message - {message}'


@pytest.mark.parametrize('msg, queue_1, queue_2, exchange',
                         [('', 'supertest1', 'supernew2', 'test')])
def test_rabbit_no_messages(msg, queue_1, queue_2, exchange):
    producer(msg, queue_1, exchange)
    result = consumer(queue_2)
    assert result == 'No messages returned', f'Message - {result}'
