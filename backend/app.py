# backend/app.py
from flask import Flask
from flask_cors import CORS
from models import db
import routes.challenges as challenge_routes

def create_app():
    app = Flask(__name__)
    # Use SQLite for simplicity—this file will live next to app.py
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///challenges.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB
    db.init_app(app)

    # Enable CORS so that Next.js (localhost:3000) can talk to Flask (localhost:5000)
    CORS(app)

    # Register blueprints / route groups
    app.register_blueprint(challenge_routes.bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    # Create tables if they don’t exist
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
