Welcome to Data Science Challenge Library

We are a group of students at Georgian College completing our final project for AIDI- Artificial Intelligence Design and Implementation

This project aims to be a curated list of data science and machine learning challenges, created by us. 
Most of the datasets can be found on kaggle. If not they are linked in the challenge.


The project uses a flask backend with react frontend

Here is the project structure:

root
   backend
      instance
         challenges.db  # This is the sqlite database for challenges and pathways
      routes
         challenges.py  # This is the backend route for serving the challenge information
      venv # necessary for setting up the backend virtual environment
      app.py # the main backend app
      Dockerfile # docker information 
      models.py # flask models for challenge and pathways
      test_app.py # unit tests 
   frontend
      src   
         app   
            challenges/id/page.js  # the individual challenge details
            learning-pathway/page.js # the page for learning pathways
            page.js # the main page of the frontend app
         components # the jsx components used in the main page.js
         Dockerfile # docker information
   docker-compose.yml  # the docker file used for orchestrating the app's use

Requirements:
see requirements.txt in the backend and package.json in the frontend

Usage:

To run the app manually, perform the following steps:
1. **Backend Setup**
   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the backend Flask server:
     ```bash
     flask run
     ```
   - The backend will be available at `http://localhost:5000`.

2. **Frontend Setup**
   - Open a new terminal and navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```
   - The frontend will be available at `http://localhost:3000`.

3. **Access the Application**
   - Open your browser and go to `http://localhost:3000` to use the app.
