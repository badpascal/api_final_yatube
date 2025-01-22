# api_final
api final - CRUD для Yatube

## Стек технологий

* Python 3.9
* Django 3.2
* Django REST framework
* JWT + Djoser

## Установка

**Клонировать репозиторий и перейти в него в командной строке.**

```
git clone https://github.com/badpascal/api_final_yatube.git
```

**Cоздать и активировать виртуальное окружение:**

```
python -m venv venv
source venv/Scripts/activate
```

**Установить зависимости из файла requirements.txt:**

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python manage.py makemigrations
python manage.py migrate
```

**Создать суперюзера:**

```
python manage.py createsuperuser
```

**Запустить проект:**

```
python manage.py runserver
```
