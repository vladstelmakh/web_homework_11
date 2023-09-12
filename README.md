<!DOCTYPE html>
<html>

<head>
    <title>FastAPI Contacts Management API</title>
</head>

<body>
    <h1>FastAPI Contacts Management API</h1>

<p>Це FastAPI додаток для керування контактами.</p>
.
<h2>Початок роботи</h2>

<p>Для запуску цього додатку вам потрібно:</p>

<ol>
        <li>Завантажити проект на свій локальний комп'ютер.</li>
        <li>Встановити всі необхідні залежності, використовуючи <code>pip install -r requirements.txt</code>.</li>
        <li>Встановити PostgreSQL та створити базу даних для проекту.</li>
        <li>Налаштувати з'єднання з базою даних, замінивши значення в <code>DATABASE_URL</code> у файлі <code>models.py</code>.</li>
        <li>Запустити сервер FastAPI, використовуючи <code>uvicorn main:app --host 127.0.0.1 --port 8001 --reload</code>.</li>
</ol>

<h2>Використання</h2>

<p>Додаток надає наступні ендпойнти:</p>

<ul>
        <li><code>POST /contacts/</code> - Створення нового контакту.</li>
        <li><code>GET /contacts/</code> - Отримання списку всіх контактів.</li>
        <li><code>GET /contacts/{contact_id}</code> - Отримання контакту за ідентифікатором.</li>
        <li><code>PUT /contacts/{contact_id}</code> - Оновлення контакту за ідентифікатором.</li>
        <li><code>DELETE /contacts/{contact_id}</code> - Видалення контакту за ідентифікатором.</li>
        <li><code>GET /search/?q={query}</code> - Пошук контактів за запитом.</li>
        <li><code>GET /upcoming_birthdays/</code> - Отримання контактів з майбутніми днями народження.</li>
    </ul>

<p>Замість <code>your_postgres_username</code>, <code>your_postgres_password</code>, і <code>your_database_name</code>, вам потрібно підставити свої дані підключення до бази даних PostgreSQL в файлі <code>models.py</code>.</p>
<h2>Керування контактами</h2>

<h3>Створити новий контакт</h3>

<p><strong>Запит</strong></p>

<pre><code>POST /contacts/
</code></pre>

<p><strong>Параметри</strong></p>

```json
{
  "first_name": "Іван",
  "last_name": "Петров",
  "email": "ivan@example.com",
  "phone_number": "+380991234567",
  "birthday": "1990-07-15",
  "additional_data": "Додаткові дані про контакт"
}
```
<p><strong>Відповідь</strong></p>


```json
{
  "id": 1,
  "first_name": "Іван",
  "last_name": "Петров",
  "email": "ivan@example.com",
  "phone_number": "+380991234567",
  "birthday": "1990-07-15",
  "additional_data": "Додаткові дані про контакт"
}
```


<h3>Отримати список всіх контактів</h3>
<p><strong>Запит</strong></p>
<pre><code>GET /contacts/
</code></pre>
<p><strong>Відповідь</strong></p>

```json
[
  {
    "id": 1,
    "first_name": "Іван",
    "last_name": "Петров",
    "email": "ivan@example.com",
    "phone_number": "+380991234567",
    "birthday": "1990-07-15",
    "additional_data": "Додаткові дані про контакт"
  },
  {
    "id": 2,
    "first_name": "Марія",
    "last_name": "Ковальчук",
    "email": "mary@example.com",
    "phone_number": "+380992345678",
    "birthday": "1985-05-20",
    "additional_data": null
  }
]

```

<h3>Отримати контакт за ідентифікатором</h3>
<p><strong>Запит</strong></p>
<pre><code>GET /contacts/{contact_id}
</code></pre>
<p><strong>Відповідь</strong></p>

```json
{
  "id": 1,
  "first_name": "Іван",
  "last_name": "Петров",
  "email": "ivan@example.com",
  "phone_number": "+380991234567",
  "birthday": "1990-07-15",
  "additional_data": "Додаткові дані про контакт"
}
```
<h3>Оновити існуючий контакт</h3>
<p><strong>Запит</strong></p>
<pre><code>PUT /contacts/{contact_id}
</code></pre>
<p><strong>Параметри</strong></p>

```json
{
  "first_name": "Іван",
  "last_name": "Сідоров",
  "email": "ivan@example.com",
  "phone_number": "+380991234567",
  "birthday": "1990-07-15",
  "additional_data": "Оновлені дані про контакт"
}
```
<p><strong>Відповідь</strong></p>

```json
{
  "id": 1,
  "first_name": "Іван",
  "last_name": "Сідоров",
  "email": "ivan@example.com",
  "phone_number": "+380991234567",
  "birthday": "1990-07-15",
  "additional_data": "Оновлені дані про контакт"
}
```

<h3>Видалити контакт</h3>
<p><strong>Запит</strong></p>
<pre><code>DELETE /contacts/{contact_id}
</code></pre>
<p><strong>Відповідь</strong></p>

```json
{
  "id": 1
}
```


</body>
</html>
