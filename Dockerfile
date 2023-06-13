FROM python:3.11-slim

CMD ["python3","main.py", "2", "5"]
COPY src/main.py .
