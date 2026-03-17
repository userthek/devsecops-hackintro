FROM python:3.9-slim

WORKDIR /app

RUN pip install flask==1.0 requests==2.19.0 numpy==1.18.0

CMD ["python", "-c", "print('Security scanner by userthek')"]