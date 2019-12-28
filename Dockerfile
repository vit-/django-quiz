FROM python:3.8
MAINTAINER Vitalii Vokhmin <vitaliy.vokhmin@gmail.com>

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY src/ .

RUN mkdir -p /opt/data/static \
    && ./manage.py collectstatic

ENV DJANGO_SECRET_KEY=''
ENV DJANGO_DEBUG=false
ENV DJANGO_ALLOWED_HOSTS=localhost
ENV DJANGO_DB_NAME=quiz
ENV DJANGO_DB_USER=quiz
ENV DJANGO_DB_PASSWORD=''
ENV DJANGO_DB_HOST=''
ENV DJANGO_DB_PORT=5432

VOLUME /opt/data/static
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "quiz.wsgi"]
