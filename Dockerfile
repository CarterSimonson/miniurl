FROM python:3.10
MAINTAINER Carter Simonson

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /app

EXPOSE 5000

# Start gunicorn
CMD ["gunicorn", "--config", "/deploy/gunicorn_config.py", "main:app"]