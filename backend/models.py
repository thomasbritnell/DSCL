# backend/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
