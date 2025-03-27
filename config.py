import os

class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Protect against CSRF
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
    MYSQL_DB = os.getenv('MYSQL_DB', 'course_registration')
