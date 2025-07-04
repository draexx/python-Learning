import pytest
import sys
import os

# Add the project root to sys.path to allow imports from flaskProject
# when running pytest from the root directory or from flaskProject/tests
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

# Alternatively, if flaskProject is directly the parent of tests:
# FLASKPROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, FLASKPROJECT_DIR)


from flaskProject.app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Minimal configuration for testing
    # You might need to override more settings if your app uses them (e.g., DATABASE_URI)
    flask_app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,  # Disable CSRF for testing forms if needed
        "LOGIN_DISABLED": True, # If you use Flask-Login, disable it for most tests or mock login
        # Add other test-specific configurations here
    })

    # TODO: Add setup for database if you have one (e.g., create test DB, apply migrations)
    # For example, if using SQLAlchemy:
    # with flask_app.app_context():
    #     db.create_all()

    yield flask_app

    # TODO: Add cleanup for database if you have one (e.g., drop tables, remove test DB)
    # For example, if using SQLAlchemy:
    # with flask_app.app_context():
    #     db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()

# You can add more fixtures here, for example, to:
# - Create specific database records for tests
# - Mock external services
# - Authenticate users for certain tests
