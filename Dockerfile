
FROM python:alpine3.14

WORKDIR /app
COPY app/ /app

RUN pip3 install -r /app/requirements.txt
RUN python /app/init_dynamodb.py

ENTRYPOINT ["python", "router.py"]