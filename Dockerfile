FROM python:3.9-slim

WORKDIR /app
COPY app.py .

RUN pip install flask==2.0.0 requests==2.25.0 numpy==1.21.0 Pillow==8.3.0

CMD ["python", "app.py"]