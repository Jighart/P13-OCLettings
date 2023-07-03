FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ARG DSN
ARG HOST_URL

RUN mkdir /p13_lettings
WORKDIR /p13_lettings
COPY . /p13_lettings/

RUN pip install -r requirements.txt && \
    python3 setup_env_file.py && \
    python3 manage.py create_env -dsn $DSN -host $HOST_URL
CMD python3 manage.py runserver 0.0.0.0:8000