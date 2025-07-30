# backend/app.py

import os
from flask import Flask
from flask_cors import CORS
from models import db
import routes.challenges as challenge_routes


def create_app():
    """
    Factory function to create and configure the Flask app.
    Sets up database, CORS, and registers blueprints.
    """
    app = Flask(__name__)
    # Use environment variable for DB URI, fallback to SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///challenges.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB
    db.init_app(app)

    # Use env var for CORS origins, fallback to localhost:3000
    cors_origins = os.environ.get("CORS_ORIGINS", "http://localhost:3000")
    CORS(app, origins=[cors_origins], supports_credentials=True)

    # Register blueprints / route groups
    app.register_blueprint(challenge_routes.bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    # Only auto-create tables if explicitly set (not recommended for prod)
    if os.environ.get("FLASK_AUTO_CREATE_TABLES", "false").lower() == "true":
        with app.app_context():
            db.create_all()
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app
    app.run(debug=False, host="0.0.0.0", port=port)
