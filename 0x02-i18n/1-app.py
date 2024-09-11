#!/usr/bin/env python3
"""
1-app.py: A basic Flask application with Babel integration for
internationalization and localization support.
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration class to set available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)

# Apply the configuration to the Flask app
app.config.from_object(Config)

# Instantiate Babel for i18n support
babel = Babel(app)

@app.route('/')
def index():
    """
    Renders the index.html page with language support.
    """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
