FROM python:3.9-slim

WORKDIR /app

COPY input.json /app/input.json
COPY test.py /app/test.py

CMD ["python", "test.py"]
