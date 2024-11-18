# DjangoLogin

This project is a simple Django application that demonstrates user authentication, including login, logout, and registration functionalities.

## Features

- User registration
- User login and logout
- task management

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/DjangoLogin.git
    ```
2. Navigate to the project directory:
    ```bash
    cd DjangoLogin
    ```
3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Register a new user or log in with an existing account
