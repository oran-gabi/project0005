import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt_secret_key_here'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'media')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
