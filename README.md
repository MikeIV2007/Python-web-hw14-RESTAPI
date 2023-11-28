Домашнє завдання #13

Перша частина

У першій частині по  REST API зостасунку виконані усі пункти згідно завдання, окрім додаткового що до реалізації механізму скидання паролю. 

Обмеження кількості запитів було імплементовано у роутер орерації get_contacts в src\routes\contacts.py


Для роботи проекта необхідний файл `.env` зі змінними оточення.
Створіть його з таким вмістом і підставте свої значення (Дивись також .env_example ).

```dotenv
# Database PostgreSQL
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=

SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB}

# JWT authentication
SECRET_KEY=
ALGORITHM=

# Email service
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=
MAIL_SERVER=

# Redis
REDIS_HOST=
REDIS=

# Cloud Storage
CLOUDINARY_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

Запуск баз даних

```bash
docker-compose up -d
```

Запуск застосунку у корневому каталозі:

```
py main.py

Документація зостасунку знаходиться:
    docs\_build\html\index.html

Запуск тестів у корневому каталозі:
 
pytest tests/

