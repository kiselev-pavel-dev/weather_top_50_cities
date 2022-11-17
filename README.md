# Погода в 50 крупнейших городах мира
Тестовое задание (Получение данных о погоде 50 крупнейших городов мира по населению с занесением в БД и обновлением раз в час)

# Технологии:
    Python 3.8
    Django 4.1.3
    PostgreSQL
    Celery 4.4.7
    Redis 4.3.4
    Docker (docker-compose)
    
# Запуск и работа с проектом

1. Клонировать репозиторий к себе на локальную машину:

```git clone git@github.com:kiselev-pavel-dev/weather_top_50_cities.git```

2. Перейти в директорию с проектом:

```cd weather_top_50_cities```

3. Создать и активировать виртуальное окружение:

```python -m venv venv```
```source venv/scripts/activate```

4. Перейти в категорию weather:

```cd weather```

5. Запустить контейнеры:

```docker compose up --build```

6. После запуска перейти в контейнер с Django:

```docker exec -it weather_django bash```

7. Создать миграции, применить их, создать суперпользователя и загрузить города(подготовлен csv c 50 крупнейшими городами):

```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py createsuperuser```
```python manage.py load_cities```

После этого создадутся города в базе, и выполнится обновление погоды для этих городов.

Теперь можно зайти в админку http://127.0.0.1:8000/admin/ под вашим логином администратора.



