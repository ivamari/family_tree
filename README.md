# family_tree

Технологии
* Python
* Django, Django REST Framework (DRF)
* PostgreSQL

  
Файл .env не убирала из публичного доступа, чтобы можно было быстро проверить работоспособность проекта.

## Как запустить проект (без докера):

### Клонировать репозиторий и перейти в него в командной строке:

`https://github.com/ivamari/family_tree.git`

`cd family_tree`

### Cоздать и активировать виртуальное окружение:

`python -m venv env`

`source venv/bin/activate`

### Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

### Выполнить миграции:

`python manage.py migrate`

### Команда для загрузки фикстур:

`python manage.py loaddata people.json`

### Для создания суперпользователя:

`python manage.py createsuperuser`

### Запустить проект:

`python manage.py runserver`

Для перехода в админку: http://127.0.0.1:8000/admin/

Для перехода в документацию: http://127.0.0.1:8000/v1/


## Как запустить проект (с докером):
В файле .env указываем DB_HOST=db_dev_family_tree

### Клонировать репозиторий и перейти в него в командной строке:

`https://github.com/ivamari/family_tree.git`

`cd family_tree`

### Запустить контейнеры:

`docker compose up -d --build`

### Выполнить миграции:

`python manage.py migrate`

### Команда для загрузки фикстур:

`python manage.py loaddata people.json`

### Для создания суперпользователя:

`python manage.py createsuperuser`

Для перехода в админку: http://127.0.0.1:8001/admin/

Для перехода в документацию: http://127.0.0.1:8001/v1/
