FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8765

CMD ["python3", "server.py"]