from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Challenge, User
from sqlalchemy import text

bp = Blueprint("completion", __name__)

# Create a completed_challenges table if it doesn't exist
def setup_completed_challenges_table():
    """Create the completed_challenges table if it doesn't exist"""
    db.engine.execute(text("""
    CREATE TABLE IF NOT EXISTS completed_challenges (
        user_id INTEGER,
        challenge_id INTEGER,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id, challenge_id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (challenge_id) REFERENCES challenges(id) ON DELETE CASCADE
    )
    """))

# Get completed challenges for the current user
@bp.route("/completed-challenges", methods=["GET"])
@login_required
def get_completed_challenges():
    """
    Get all challenges completed by the current user
    """
    try:
        # Query the completed_challenges table for the current user
        result = db.engine.execute(text(
            """
            SELECT c.* FROM challenges c
            JOIN completed_challenges cc ON c.id = cc.challenge_id
            WHERE cc.user_id = :user_id
            """), 
            {"user_id": current_user.id}
        )
        
        # Convert to list of dictionaries
        completed_challenges = [dict(row) for row in result]
        
        return jsonify(completed_challenges)
    except Exception as e:
        print(f"Error retrieving completed challenges: {str(e)}")
        return {"error": "Failed to retrieve completed challenges"}, 500

# Mark a challenge as completed
@bp.route("/completed-challenges/<int:challenge_id>", methods=["POST"])
@login_required
def mark_challenge_completed(challenge_id):
    """
    Mark a challenge as completed for the current user
    """
    # Check if challenge exists
    challenge = Challenge.query.get_or_404(challenge_id)
    
    try:
        # Add entry to completed_challenges table
        db.engine.execute(text(
            """
            INSERT OR IGNORE INTO completed_challenges (user_id, challenge_id)
            VALUES (:user_id, :challenge_id)
            """),
            {"user_id": current_user.id, "challenge_id": challenge_id}
        )
        
        return {"message": f"Challenge {challenge_id} marked as completed"}, 201
    except Exception as e:
        print(f"Error marking challenge as completed: {str(e)}")
        return {"error": "Failed to mark challenge as completed"}, 500

# Remove a challenge from completed list
@bp.route("/completed-challenges/<int:challenge_id>", methods=["DELETE"])
@login_required
def unmark_challenge_completed(challenge_id):
    """
    Remove a challenge from the user's completed list
    """
    # Check if challenge exists
    challenge = Challenge.query.get_or_404(challenge_id)
    
    try:
        # Remove entry from completed_challenges table
        db.engine.execute(text(
            """
            DELETE FROM completed_challenges
            WHERE user_id = :user_id AND challenge_id = :challenge_id
            """),
            {"user_id": current_user.id, "challenge_id": challenge_id}
        )
        
        return {"message": f"Challenge {challenge_id} unmarked as completed"}, 200
    except Exception as e:
        print(f"Error unmarking challenge: {str(e)}")
        return {"error": "Failed to unmark challenge"}, 500
