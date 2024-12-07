FROM python:3.12.4

WORKDIR /TODO_project

COPY requirements.txt /TODO_project/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /TODO_project/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]