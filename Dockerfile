FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY}
ARG SENTRY_DSN
ENV SENTRY_DSN ${SENTRY_DSN}
ARG HOST_URL
ENV HOST_URL ${HOST_URL}
RUN mkdir /p13_lettings
WORKDIR /p13_lettings
COPY requirements.txt /p13_lettings/
RUN pip install -r requirements.txt
COPY . /p13_lettings/
CMD python3 manage.py runserver 0.0.0.0:8000