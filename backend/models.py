# backend/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Challenge(db.Model):
    __tablename__ = "challenges"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(100), nullable=False)

    # ─── NEW FIELDS ──────────────────────────────────────────────
    subject = db.Column(db.String(50), nullable=True)       # e.g. "AIDI1011"
    technology = db.Column(db.String(200), nullable=True)   # e.g. "Python,R,SQL"

    dataset_url = db.Column(db.String(500), nullable=True)
    overview = db.Column(db.Text, nullable=True)
    task = db.Column(db.Text, nullable=True)
    outcomes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty,
            "subcategory": self.subcategory,
            "subject": self.subject,
            "technology": self.technology,
            "dataset_url": self.dataset_url,
            "overview": self.overview,
            "task": self.task,
            "outcomes": self.outcomes,
        }
