FROM tiangolo/uwsgi-nginx-flask:python3.8

ARG CSRF_KEY="helloworld"

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
ENV UWSGI_INI  /var/www/app.ini
ENV PYTHONPATH=/var/www
ENV SECRET_KEY=$CSRF_KEY

COPY ./app.ini /etc/uwsgi/uwsgi.ini
COPY ./app /var/www/app
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app.ini /var/www/app.ini
COPY ./manage.py /var/www/manage.py
COPY ./wsgi.py /var/www/wsgi.py

RUN pip install -r /var/www/requirements.txt
