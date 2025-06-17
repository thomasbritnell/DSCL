# backend/routes/challenges.py

from flask import Blueprint, request, jsonify
from models import db, Challenge

bp = Blueprint("challenges", __name__)

@bp.route("/challenges", methods=["GET"])
def get_challenges():
    """
    Query parameters (all optional):
      - difficulty: "Easy", "Medium", "Hard"
      - subcategory: e.g. "AI-ML", "Data-Visualization", etc.
      - subject: e.g. "AIDI1011", "AIDI1012"
      - technology: e.g. "Python", "R" (matches if the challenge's technology field contains this substring)
    """
    difficulty = request.args.get("difficulty")
    subcategory = request.args.get("subcategory")
    subject = request.args.get("subject")
    tech = request.args.get("technology")

    query = Challenge.query

    if difficulty:
        query = query.filter(Challenge.difficulty == difficulty)
    if subcategory:
        query = query.filter(Challenge.subcategory == subcategory)
    if subject:
        query = query.filter(Challenge.subject == subject)
    if tech:
        # Here we do a simple “contains” match on the comma-separated string
        query = query.filter(Challenge.technology.ilike(f"%{tech}%"))

    results = query.all()
    return jsonify([c.to_dict() for c in results])

@bp.route("/challenges/<int:id>", methods=["GET"])
def get_challenge(id):
    c = Challenge.query.get_or_404(id)
    return jsonify(c.to_dict())