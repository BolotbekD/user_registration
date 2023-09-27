1. Нужно создать вертуальное окружение с помощью команды python3 -m venv название окружения
2. Нужно активировать виртуальное окружение с помощью команды source/окружение/bin/activate
3. В settings.py прописываем настройки БД

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4. Для запуска мигрaции запускаем комaнды: 
    - python3 manage.py makemigrations 
    - python3 manage.py migrate

5. Установка зависимостей - pip freeze > requirements.txt
 
6. Запуск проекта - python3 manage.py runserver

7. Пока что ссылка на сброс пароля приходит на консоль проекта 