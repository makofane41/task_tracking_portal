# FROM python:3.10-slim

# RUN mkdir /task_tracking
# WORKDIR /task_tracking
# COPY . /task_tracking/

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# EXPOSE 8000
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]


FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /task_tracking

# Copy project files
COPY . /task_tracking/

# Install virtualenv
RUN pip install --upgrade pip
RUN pip install virtualenv

# Create and activate virtual environment
RUN virtualenv /task_tracking/venv
ENV PATH="/task_tracking/venv/bin:$PATH"

# Install dependencies in the virtual environment
RUN /task_tracking/venv/bin/pip install -r requirements.txt

# Run Django commands within the virtual environment
RUN /task_tracking/venv/bin/python manage.py makemigrations
RUN /task_tracking/venv/bin/python manage.py migrate

# Expose port
EXPOSE 8000

# Start server using the virtual environment's Python
CMD ["/task_tracking/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

