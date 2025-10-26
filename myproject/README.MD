# Django MyProject

This is a Django web application project.

## Setup

1. Clone the repository
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```

2. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

3. Run the development server:
    ```bash
    python manage.py runserver
    ```

4. Access the application at `http://localhost:8000`

## Project Structure

- `myproject/` - Main project directory
  - `settings.py` - Project settings
  - `urls.py` - URL configurations
  - `wsgi.py` - WSGI configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.