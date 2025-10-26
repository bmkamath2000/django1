# Django Multi-App Project Demo

This project demonstrates how to create and manage multiple applications within a single Django project.

## Project Structure

```
project1/
├── app1/
├── app2/
├── project1/
├── manage.py
└── requirements.txt
```

## Features

- Multiple Django apps in one project
- Separate URL configurations for each app
- Shared database configuration
- Independent app functionalities

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```
    python manage.py migrate
    ```
5. Start the development server:
    ```
    python manage.py runserver
    ```

## Apps Description

- **App1**: Description of first app functionality
- **App2**: Description of second app functionality

## Technologies

- Django 4.x
- Python 3.x
- SQLite (default database)