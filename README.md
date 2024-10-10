# FirstDjango_07102024

## Инструкция по развертыванию проекта
1. `python3 -m venv django_venv`

2. `source django_venv/bin/activate`

3. `pip install -r requirements.txt`

4. `python manage.py migrate`

5. `python manage.py runserver`


## Запуск `ipython` в контексте `django` приложений
```
python manage.py shell_plus --ipython
```

## Дополнительно 
1. Полезное расширение для шаблонов `Django`
```
ext install batisteo.vscode-django
```

2. Добавить в `settings.json`
```
    "emmet.includeLanguages": {
    "django-html": "html"
    },
    "files.associations": {
    "*.html": "django-html"
    }
```