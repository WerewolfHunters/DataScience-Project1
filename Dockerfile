FROM python:3.8-alpine

RUN apk add --no-cache gcc musl-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py"]