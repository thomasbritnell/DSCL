from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(200),nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Pathway(db.Model):
    """
    SQLAlchemy model for a Learning Pathway.
    Each pathway has a name and a list of challenge IDs (stored as a comma-separated string).
    """
    __tablename__ = "pathways"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    challenge_ids = db.Column(db.String(500), nullable=False)  # Comma-separated list of challenge IDs

    def to_dict(self):
        """
        Serialize the Pathway object to a dictionary for API responses.
        """
        return {
            "id": self.id,
            "name": self.name,
            "challengeIds": [int(cid) for cid in self.challenge_ids.split(",") if cid.strip()]
        }
# backend/models.py


class Challenge(db.Model):
    """
    SQLAlchemy model for a Challenge.
    Represents a challenge with metadata, dataset info, and solution.
    """
    __tablename__ = "challenges"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(100), nullable=False)
    technology = db.Column(db.String(200), nullable=True)  
    dataset_url = db.Column(db.String(500), nullable=True)
    dataset_description = db.Column(db.String(500), nullable=True)
    overview = db.Column(db.Text, nullable=True)
    task = db.Column(db.Text, nullable=True)
    outcomes = db.Column(db.Text, nullable=True)
    image_1 = db.Column(db.Text, nullable=True)
    image_2 = db.Column(db.Text, nullable=True)
    sample_sol = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """
        Serialize the Challenge object to a dictionary for API responses.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty,
            "subcategory": self.subcategory,
            "technology": self.technology,
            "dataset_url": self.dataset_url,
            "dataset_description" : self.dataset_description,
            "overview": self.overview,
            "task": self.task,
            "outcomes": self.outcomes,
            "image_1" : self.image_1,
            "image_2" : self.image_2,
            "sample_sol" : self.sample_sol 
        }
