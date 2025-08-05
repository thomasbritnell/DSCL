from models import Pathway

from flask import Blueprint, request
from models import db, User
from flask_login import login_user, logout_user, login_required, current_user


bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return {"error": "Username already exists"}, 400

    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully"}

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        login_user(user)  # <-- Flask-Login stores user in session
        return {"message": "Login successful"}
    return {"error": "Invalid credentials"}, 401

@bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return {"message": "Logged out"}

@bp.route("/me", methods=["GET"])
def me():
    if current_user.is_authenticated:
        return {"username": current_user.username}
    return {"username": None}, 401