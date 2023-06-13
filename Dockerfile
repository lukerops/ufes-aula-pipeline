FROM python:3.11-slim

CMD ["main.py", "2", "5"]
COPY src/main.py .
