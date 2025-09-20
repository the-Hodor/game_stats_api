# Game Stats API

**Django API** для работы с играми и отзывами. Проект упакован в **Docker** с базой **PostgreSQL**, есть админка, Swagger-документация и команда для наполнения тестовыми данными.

---

## 🔹 Что делает проект

- Хранит список игр (`title`, `genre`, `release_date`).  
- Хранит отзывы к играм (`game`, `text`, `rating`).  
- Отдаёт данные через API в формате JSON.  
- Веб-админка для управления записями.  
- Можно запускать через Docker на любой машине.

---

## 🔹 Как запустить проект

1. Перейти в папку с `manage.py`.

2. Собрать и запустить контейнеры:

```bash
docker compose up --build
````

3. Применить миграции:

```bash
docker compose exec web python manage.py migrate
```

4. Создать суперпользователя:

```bash
docker compose exec web python manage.py createsuperuser
```

5. (Опционально) Наполнить тестовыми данными:

```bash
docker compose exec web python manage.py seed
```

6. Открыть в браузере:

* API: `http://127.0.0.1:8000/api/`
* Админка: `http://127.0.0.1:8000/admin/`
* Swagger: `http://127.0.0.1:8000/swagger/`

---

## 🔹 Примеры работы с API

* Получить все игры:

```
GET http://127.0.0.1:8000/api/games/
```

* Создать игру:

```http
POST /api/games/ HTTP/1.1
Content-Type: application/json

{
  "title": "New Game",
  "genre": "Action",
  "release_date": "2024-01-01"
}
```

* Аналогично для `/api/reviews/`.

---

## 🔹 Структура проекта

```
manage.py
Dockerfile
docker-compose.yml
requirements.txt
gamestatus/
games/
```

---

## 🔹 Частые команды Docker

* `docker compose up --build` — собрать и запустить контейнеры.
* `docker compose up -d` — поднять в фоне.
* `docker compose logs -f web` — смотреть логи.
* `docker compose exec web bash` — открыть shell в контейнере.
* `docker compose exec web python manage.py migrate` — применить миграции.
* `docker compose exec web python manage.py seed` — добавить тестовые данные.
* `docker compose down -v` — остановить и удалить контейнеры + volumes.

```