# 🎵 Тестовое задание: Разработчик Django / Django Rest Framework

## 📄 Описание тестового задания
Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями следующей структуры:

**Исполнитель**  
  - Название

**Альбом**  
  - Исполнитель  
  - Год выпуска

**Песня**  
  - Название  
  - Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.  
В качестве площадки для демонстрации API подключите Swagger, чтобы можно было проверить работу через Postman или браузер.

---

## 🛠 Используемые технологии
- **Python** 3.11.9  
- **Django** 4.2.20  
- **Django Rest Framework (DRF)**  
- **Pytest**  
- **Docker / Docker Compose**  
- **Swagger / drf-spectacular**
- **БД: PostgreSQL** 

---

## 🚀 Установка и запуск (Локально)
1. Скопировать `.env.example` в `.env` и настроить параметры БД и другие переменные окружения.
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
1. Скопировать `.env.example` в `.env` и настроить параметры БД и другие переменные окружения.
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Выполнить миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Запустите сервер Django:
   ```bash
   python manage.py runserver
   ```

## 🐳 Установка и запуск (Docker)
  ```bash
   docker compose up --build
   ```
### В Docker запускаются два сервиса: web (Django) и db (PostgreSQL)

### API будет доступен по: http://localhost:8080/api/v1/

### Swagger документация доступна по: http://localhost:8080/api/v1/docs/

---

## 🔧 Что реализовано
- CRUD API для Исполнителей, Альбомов и Песен через Django Rest Framework
- Swagger документация для API (/api/v1/docs)
- Использование Postgres через Docker или локальный сервер
- Тесты через Pytest
