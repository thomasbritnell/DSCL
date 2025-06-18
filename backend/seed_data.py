# backend/seed_data.py

from app import create_app
from models import db, Challenge
import csv
import os
import requests


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
                "subject": None,  # Not present in CSV
                "technology": row.get("technology", "").strip(),
                "dataset_url": row.get("dataset_url", "").strip(),
                "overview": row.get("overview", "").strip(),
                "task": row.get("task", "").strip(),
                "outcomes": row.get("outcomes", "").strip(),
            })
    return challenges

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.drop_all()   # Remove old tables (so the new columns take effect)
        db.create_all() # Recreate tables with new schema

        challenges = load_challenges_from_csv(CSV_PATH)
        for entry in challenges:
            c = Challenge(
                title=entry["title"],
                description=entry.get("description"),
                difficulty=entry.get("difficulty"),
                subcategory=entry.get("subcategory"),
                subject=entry.get("subject"),
                technology=entry.get("technology"),
                dataset_url=entry.get("dataset_url"),
                overview=entry.get("overview"),
                task=entry.get("task"),
                outcomes=entry.get("outcomes"),
            )
            db.session.add(c)

        db.session.commit()
        print("Dropped old tables, recreated schema, and seeded from seed_data_real.csv!")
        print("Database created/updated and seeded successfully!")
