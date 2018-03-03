FROM python:3.6.2

RUN mkdir /src
WORKDIR /src

ADD requirements.txt /src/
RUN pip install -r requirements.txt

ADD . /src/

EXPOSE 8000

CMD python manage.py collectstatic && \
	python manage.py makemigrations && \
	python manage.py migrate && \
	python manage.py runserver 0.0.0.0:8000
