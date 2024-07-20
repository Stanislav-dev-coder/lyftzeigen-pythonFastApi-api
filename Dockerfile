FROM python:3.9-slim-buster

ENV MONGODB_URL="mongodb://mongoadmin:bdung@mongodb.lyftzeigen.ru:28017/"

COPY . .
WORKDIR /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]