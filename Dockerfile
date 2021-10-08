
FROM python:alpine3.14

WORKDIR /app
COPY app/ /app

RUN pip3 install -r /app/requirements.txt

ENTRYPOINT ["python", "router.py"]