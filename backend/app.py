# backend/app.py

import os
from flask import Flask
from flask_cors import CORS
from models import db, User
import routes.challenges as challenge_routes
import routes.auth as auth_routes
import routes.completion as completion_routes
import routes.admin as admin_routes
from flask_login import LoginManager


def create_app():
    """
    Factory function to create and configure the Flask app.
    Sets up database, CORS, and registers blueprints.
    """
    app = Flask(__name__)
    # Use environment variable for DB URI, fallback to SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///instance/challenges.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = '5553698f87140fcbc77a8192e1acce32'

    # Initialize DB
    db.init_app(app)
    # Flask-Login setup
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))


    # Use env var for CORS origins, fallback to localhost:3000
    cors_origins = os.environ.get("CORS_ORIGINS", "http://localhost:3000")
    CORS(app, origins=[cors_origins], supports_credentials=True)

    # Register blueprints / route groups
    app.register_blueprint(challenge_routes.bp, url_prefix="/api")
    app.register_blueprint(auth_routes.bp, url_prefix="/api")
    app.register_blueprint(completion_routes.bp, url_prefix="/api")
    app.register_blueprint(admin_routes.bp, url_prefix="/api/admin")

    return app

if __name__ == "__main__":
    app = create_app()
    # Always create tables if they don't exist - ensures users table is created
    with app.app_context():
        db.create_all()
        
        # Create the completed_challenges table if it doesn't exist
        from routes.completion import setup_completed_challenges_table
        setup_completed_challenges_table()
        
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app
    app.run(debug=False, host="0.0.0.0", port=port)
