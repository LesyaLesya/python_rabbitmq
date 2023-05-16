## Project description

Rabbitmq producer and consumer in Python3 with some test with pytest.

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management (for run rabbitmq in docker)
pip install -U pip
pip install -r requirements.txt
pytest -s -v tests/
```
