from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Challenge

bp = Blueprint("admin", __name__)

# Admin middleware to check if user is admin
def admin_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return {"error": "Authentication required"}, 401
        if current_user.user_type != "admin":
            return {"error": "Admin privileges required"}, 403
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# Get all challenges (admin view)
@bp.route("/challenges", methods=["GET"])
@admin_required
def get_all_challenges_admin():
    """
    Admin endpoint to get all challenges with full details
    """
    challenges = Challenge.query.all()
    return jsonify([c.to_dict() for c in challenges])

# Create a new challenge
@bp.route("/challenges", methods=["POST"])
@admin_required
def create_challenge():
    """
    Admin endpoint to create a new challenge
    """
    data = request.json
    
    # Validate required fields
    required_fields = ["title", "difficulty", "subcategory"]
    for field in required_fields:
        if field not in data or not data[field]:
            return {"error": f"Missing required field: {field}"}, 400
    
    # Create new challenge
    challenge = Challenge(
        title=data["title"],
        description=data.get("description"),
        difficulty=data["difficulty"],
        subcategory=data["subcategory"],
        technology=data.get("technology"),
        dataset_url=data.get("dataset_url"),
        dataset_description=data.get("dataset_description"),
        overview=data.get("overview"),
        task=data.get("task"),
        outcomes=data.get("outcomes"),
        image_1=data.get("image_1"),
        image_2=data.get("image_2"),
        sample_sol=data.get("sample_sol")
    )
    
    try:
        db.session.add(challenge)
        db.session.commit()
        return jsonify(challenge.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error creating challenge: {str(e)}")
        return {"error": "Failed to create challenge"}, 500

# Update a challenge
@bp.route("/challenges/<int:id>", methods=["PUT"])
@admin_required
def update_challenge(id):
    """
    Admin endpoint to update an existing challenge
    """
    challenge = Challenge.query.get_or_404(id)
    data = request.json
    
    # Update fields
    if "title" in data:
        challenge.title = data["title"]
    if "description" in data:
        challenge.description = data["description"]
    if "difficulty" in data:
        challenge.difficulty = data["difficulty"]
    if "subcategory" in data:
        challenge.subcategory = data["subcategory"]
    if "technology" in data:
        challenge.technology = data["technology"]
    if "dataset_url" in data:
        challenge.dataset_url = data["dataset_url"]
    if "dataset_description" in data:
        challenge.dataset_description = data["dataset_description"]
    if "overview" in data:
        challenge.overview = data["overview"]
    if "task" in data:
        challenge.task = data["task"]
    if "outcomes" in data:
        challenge.outcomes = data["outcomes"]
    if "image_1" in data:
        challenge.image_1 = data["image_1"]
    if "image_2" in data:
        challenge.image_2 = data["image_2"]
    if "sample_sol" in data:
        challenge.sample_sol = data["sample_sol"]
    
    try:
        db.session.commit()
        return jsonify(challenge.to_dict())
    except Exception as e:
        db.session.rollback()
        print(f"Error updating challenge: {str(e)}")
        return {"error": "Failed to update challenge"}, 500

# Delete a challenge
@bp.route("/challenges/<int:id>", methods=["DELETE"])
@admin_required
def delete_challenge(id):
    """
    Admin endpoint to delete a challenge
    """
    challenge = Challenge.query.get_or_404(id)
    
    try:
        db.session.delete(challenge)
        db.session.commit()
        return {"message": f"Challenge {id} deleted successfully"}
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting challenge: {str(e)}")
        return {"error": "Failed to delete challenge"}, 500
