FROM python:3

WORKDIR /code

COPY ./reqirement.txt .
RUN pip install -r /code/reqirement.txt
COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]