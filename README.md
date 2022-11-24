# Проект «API для Yatube»
### Что это за проект:

Это API для соцсети Yatube. Этот интерфейс позволит расширить функциональность этого продукта с помощью представленных функций и связать его с другими продуктами.
С помощью него вы сможете регистрироваться в соцсети, создавать, изменять и удалять свои посты.
Оставлять, получать комментарии и редактировать их. Подписываться на любимых авторов и сообщества.
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Artek22/api_final_yatube.git
```

```
cd api_final_yatub
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры:
Создание публикации POST-метод:
```
http://127.0.0.1:8000/api/v1/posts/
```
Получение всех комментариев к публикации GET-метод:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Добавление комментария POST-метод:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Список сообществ GET-метод:
```
http://127.0.0.1:8000/api/v1/groups/
```