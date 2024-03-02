FROM python:3.11

COPY requirements.txt /api/requirements.txt

WORKDIR /api/

RUN pip3 install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0
