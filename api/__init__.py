# app/__init__.py

from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Load configuration (optional)
app.config.from_object('config.Config')

# Import routes after creating the app to ensure routes are registered
from app import routes
