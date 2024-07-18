FROM python:3.9-slim-buster
COPY . .
WORKDIR /
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "8081"]
