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
python3 -m venv env
source env/bin/activate

*Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

*Выполнить миграции:
python3 manage.py migrate

*Запустить проект:
python3 manage.py runserver
