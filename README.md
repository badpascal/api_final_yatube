# api_final
api final - CRUD для Yatube

## Стек технологий

* Python 3.9
* Django 3.2
* Django REST framework
* JWT + Djoser

Как запустить проект:
*Клонировать репозиторий и перейти в него в командной строке.

*Cоздать и активировать виртуальное окружение:
python -m venv venv
source venv/Scripts/activate

*Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

*Выполнить миграции:
python manage.py migrate

*Запустить проект:
python manage.py runserver
