# backend/seed_data.py

from app import create_app
from models import db, Challenge, Pathway
import csv
import os
import requests

# URL to download seed data CSV from Google Sheets
# If download fails, fallback to local file

download_url = "https://docs.google.com/spreadsheets/d/1P1Q4_x8UJeU3yEiADp-JCBA6EexZJpPdpSPrEeasVNE/export?format=csv"
local_csv = os.path.join(os.path.dirname(__file__), "seed_data_real.csv")

# Try to download the CSV; if it fails, use the local file
try:
    response = requests.get(download_url, timeout=10)
    response.raise_for_status()
    with open(local_csv, "wb") as f:
        f.write(response.content)
    CSV_PATH = local_csv
    print("Downloaded CSV from Google Sheets.")
except Exception as e:
    print(f"Could not download CSV, using local file. Reason: {e}")
    CSV_PATH = local_csv

def load_challenges_from_csv(csv_path):
    """
    Load challenges from a CSV file and return a list of dicts.
    Each dict maps CSV columns to Challenge fields.
    """
    challenges = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Map CSV columns to Challenge fields, handle missing/empty values
            challenges.append({
                "title": row.get("title", "").strip(),
                "description": row.get("description", "").strip(),
                "difficulty": row.get("difficulty", "").strip(),
                "subcategory": row.get("subcategory", "").strip(),
                "technology": row.get("technology", "").strip(),
                "dataset_url": row.get("dataset_url", "").strip(),
                "dataset_description": row.get("dataset_description", "").strip(),
                "overview": row.get("overview", "").strip(),
                "task": row.get("task", "").strip(),
                "outcomes": row.get("outcomes", "").strip(),
                "image_1": row.get("image_1", "").strip(),
                "image_2": row.get("image_2", "").strip(),
                "sample_sol": row.get("sample_sol","").strip()
            })
    return challenges

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.drop_all()   # Remove old tables (so the new columns take effect)
        db.create_all() # Recreate tables with new schema

        challenges = load_challenges_from_csv(CSV_PATH)
        for entry in challenges:
            # Create and add Challenge objects to the DB
            c = Challenge(
                title=entry["title"],
                description=entry.get("description"),
                difficulty=entry.get("difficulty"),
                subcategory=entry.get("subcategory"),
                technology=entry.get("technology"),
                dataset_url=entry.get("dataset_url"),
                dataset_description=entry.get("dataset_description"),
                overview=entry.get("overview"),
                task=entry.get("task"),
                outcomes=entry.get("outcomes"),
                image_1=entry.get("image_1"),
                image_2=entry.get("image_2"),
                sample_sol=entry.get("sample_sol")
            )
            db.session.add(c)

        db.session.commit()

        # ── Seed Pathways Table ──────────────────────────────
        pathways = [
            {"name": "Learn the basics of data manipulation", "challenge_ids": "1,2,3,5,6"},
            {"name": "Learn machine learning basics", "challenge_ids": "7,8,9,10,11"},
            {"name": "Learn to detect outliers", "challenge_ids": "2,4,13"},
            {"name": "Build a recommender system with ML", "challenge_ids": "12,15"},
            {"name": "Work with images", "challenge_ids": "16,17,18"},
        ]
        for entry in pathways:
            p = Pathway(name=entry["name"], challenge_ids=entry["challenge_ids"])
            db.session.add(p)
        db.session.commit()
        print("Dropped old tables, recreated schema, and seeded from seed_data_real.csv and hardcoded pathways!")
        print("Database created/updated and seeded successfully!")
