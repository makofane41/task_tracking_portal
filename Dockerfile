FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /task_tracking
COPY requirements.txt /task_tracking/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /task_tracking/
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]