"""Settings configuration - Configuration for environment variables can go in here."""

import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY', default='22d509acd65b930774ae53c8')
SQLALCHEMY_TRACK_MODIFICATIONS = False
G_API=os.getenv('G_API')
