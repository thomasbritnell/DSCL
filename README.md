# Data Science Challenge Library (DSCL)

A web app for browsing, completing, and tracking progress on data science challenges. Built with Next.js (frontend) and Flask (backend).

## Project Structure

```
DSCL/
├── backend/                # Flask API, models, seed scripts
│   ├── app.py
│   ├── models.py
│   ├── seed_data.py
│   ├── test_app.py
│   └── ...
├── frontend/               # Next.js frontend app
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.js
│   │   │   ├── layout.js
│   │   │   └── challenges/[id]/page.js
│   │   ├── components/
│   │   │   ├── ChallengeCard.jsx
│   │   │   ├── DifficultySelector.jsx
│   │   │   ├── SubcategoryTabs.jsx
│   │   │   └── TechnologySelector.jsx
│   └── ...
├── docker-compose.yml      # Docker orchestration for frontend/backend
└── README.md
```

## Getting Started

### Manual Setup

#### Backend (Flask)
1. Install Python 3.9+ and pip.
2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Seed the database (optional):
   ```bash
   python seed_data.py
   ```
4. Start the Flask API:
   ```bash
   python app.py
   ```

#### Frontend (Next.js)
1. Install Node.js (18+ recommended).
2. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
3. Start the frontend:
   ```bash
   npm run dev
   ```
4. Visit [http://localhost:3000](http://localhost:3000) in your browser.

### Docker Setup

1. Make sure Docker and Docker Compose are installed.
2. From the project root, run:
   ```bash
   docker-compose up --build
   ```
3. The frontend will be available at [http://localhost:3000](http://localhost:3000), backend at [http://localhost:5000](http://localhost:5000).

## Running Tests

- **Backend:**
  ```bash
  cd backend
  python -m unittest test_app.py
  ```
- **Frontend:**
  ```bash
  cd frontend
  npm test
  ```

## Features
- Browse challenges by difficulty, subcategory, and technology
- View challenge details, datasets, and sample solutions
- Learning pathways and leaderboards (prototype)

## Contributing
Pull requests and issues are welcome!

## License
MIT
