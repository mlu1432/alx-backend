#!/usr/bin/env python3
"""
2-app.py: A Flask application with Babel integration to support
language detection based on the request headers.

This module demonstrates how to detect the user's preferred language
using Flask-Babel's babel.localeselector decorator and the
request.accept_languages method.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class to set available languages, default locale, and timezone.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE = "en"
        BABEL_DEFAULT_TIMEZONE = "UTC"
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Initialize Flask app
app = Flask(__name__)

# Apply the configuration to the Flask app
app.config.from_object(Config)

# Initialize Babel for i18n support
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching language for the current request based
    on the Accept-Language headers sent by the client.

    Returns:
        str: The best matching language (either 'en' or 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html page with language localization support.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('2-index.html', current_locale=get_locale())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
