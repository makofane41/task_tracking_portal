FROM python:3.10-slim

RUN mkdir /task_tracking
WORKDIR /task_tracking

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /task_tracking/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /task_tracking/

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

