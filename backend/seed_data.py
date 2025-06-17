# backend/seed_data.py

from app import create_app
from models import db, Challenge

sample_data = [
    # ───────────────────────────────────────────────────────────────────────────
    # 1) Easy, AI-ML
    {
        "title": "Iris Species Binary Classification (Easy)",
        "description": """
Use the UCI Iris dataset to build a binary classifier that predicts whether an iris is Setosa or not. 
The dataset contains 150 samples with 4 features each: sepal length, sepal width, petal length, petal width.
""",
        "difficulty": "Easy",
        "subcategory": "AI-ML",
        "subject": "AIDI1011",
        "technology": "Python,scikit-learn,pandas",
        "dataset_url": "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
        "overview": """
This challenge focuses on binary classification using the classic Iris dataset. You will preprocess data, 
train a simple classifier (e.g., Logistic Regression), and evaluate its performance.
""",
        "task": """
- Load the Iris CSV into a pandas DataFrame  
- Create a binary target column: 1 if species == 'Iris-setosa', else 0  
- Split the data into 80% train and 20% test sets  
- Scale features using StandardScaler  
- Train a Logistic Regression model to predict the binary target  
- Evaluate accuracy, precision, recall, and plot a confusion matrix
""",
        "outcomes": """
- Jupyter Notebook (.ipynb) with code for preprocessing, training, and evaluation  
- A saved model file named 'iris_binary_model.pkl'  
- A PNG of the confusion matrix named 'iris_confusion_matrix.png'  
- A short Markdown summary explaining classifier performance and feature impact
"""
    },

    # 2) Easy, AI-ML
    {
        "title": "MNIST Digit Visualization (Easy)",
        "description": """
Use the MNIST dataset to visualize a 5×5 grid of random handwritten digits. The dataset has 60,000 training images 
and 10,000 test images of 28×28 grayscale digits (0–9).
""",
        "difficulty": "Easy",
        "subcategory": "AI-ML",
        "subject": "AIDI1011",
        "technology": "Python,matplotlib,numpy",
        "dataset_url": "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
        "overview": """
In this challenge, you will load the MNIST dataset, select 25 random images, and display them in a 5×5 grid 
using matplotlib.
""",
        "task": """
- Download and extract the MNIST training images file  
- Load the first 60,000 images and their labels into NumPy arrays  
- Randomly select 25 images and their labels  
- Plot a 5×5 grid using matplotlib, showing each image with its true label as a title  
- Save the figure as 'mnist_grid.png'
""",
        "outcomes": """
- A Python script or Jupyter Notebook with code to load and visualize images  
- A PNG file named 'mnist_grid.png' showing the 5×5 grid  
- A brief Markdown explanation of how images were loaded and displayed
"""
    },

    # 3) Easy, Data-Visualization
    {
        "title": "COVID-19 Daily Cases Line Plot (Easy)",
        "description": """
Create a line plot of daily new COVID-19 cases for a selected country using the Johns Hopkins time-series data. 
Use the CSV that contains global confirmed cases by date.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1011",
        "technology": "Python,pandas,matplotlib",
        "dataset_url": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        "overview": """
This challenge asks you to parse the time-series CSV, extract daily new case counts for a given country, and plot 
them in a line chart.
""",
        "task": """
- Download the global confirmed cases CSV from Johns Hopkins repository  
- Load it into a pandas DataFrame  
- Filter rows to select a specific country (e.g., United States)  
- Compute daily new cases by differencing the cumulative counts  
- Plot daily new cases vs. date using matplotlib with appropriate labels and title  
- Save the figure as 'covid_daily_cases.png'
""",
        "outcomes": """
- Jupyter Notebook with code for data loading, preprocessing, and plotting  
- A PNG named 'covid_daily_cases.png'  
- A short description summarizing trends observed in the plot
"""
    },

    # 4) Easy, Data-Visualization
    {
        "title": "World Happiness Score Bar Chart (Easy)",
        "description": """
Visualize the top 10 happiest countries in 2022 from the World Happiness Report data by creating a horizontal 
bar chart.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1011",
        "technology": "Python,pandas,plotly",
        "dataset_url": "https://worldhappiness.report/ed/2022/Chapter2_Data.zip",
        "overview": """
In this challenge, you will extract 2022 happiness scores for all countries, sort them, and display a horizontal 
bar chart of the top 10 countries.
""",
        "task": """
- Download and unzip the Chapter2_Data.zip file to obtain the CSV  
- Load the CSV into pandas and select columns: Country, Happiness Score, Year  
- Filter for Year == 2022  
- Sort by Happiness Score descending and select the top 10 countries  
- Create a horizontal bar chart using Plotly Express with country names on the y-axis and scores on the x-axis  
- Save the result as 'happiness_top10.html' and export static PNG as 'happiness_top10.png'
""",
        "outcomes": """
- A Jupyter Notebook with data extraction and plotting code  
- An interactive HTML file 'happiness_top10.html'  
- A static PNG file 'happiness_top10.png'  
- A brief one-paragraph summary of findings (e.g., regional patterns)
"""
    },

    # 5) Easy, Data-Analytics
    {
        "title": "Sales Revenue Summary (Easy)",
        "description": """
Given a CSV of monthly sales transactions with fields: Month, Category, UnitsSold, UnitPrice, compute total 
revenue per month and average unit price per category.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1012",
        "technology": "Python,pandas",
        "dataset_url": "https://example.com/data/monthly_sales.csv",
        "overview": """
This challenge involves loading the transactions CSV, performing aggregation to compute monthly revenues and 
category-level average prices, and presenting the results.
""",
        "task": """
- Load 'monthly_sales.csv' into a pandas DataFrame  
- Compute total revenue per month by grouping on Month and summing (UnitsSold * UnitPrice)  
- Compute average UnitPrice per Category by grouping on Category  
- Create a DataFrame showing Month vs. TotalRevenue and save it as 'revenue_per_month.csv'  
- Create a DataFrame showing Category vs. AvgUnitPrice and save it as 'avg_price_per_category.csv'
""",
        "outcomes": """
- A Jupyter Notebook with aggregation code  
- Two CSV files: 'revenue_per_month.csv' and 'avg_price_per_category.csv'  
- A short Markdown summary highlighting which month had highest revenue and which category was most expensive on average
"""
    },

    # 6) Easy, Data-Analytics
    {
        "title": "Employee Demographics Pivot Table (Easy)",
        "description": """
Analyze employee survey data containing columns: EmployeeID, Department, Gender, Age, SatisfactionLevel. 
Create a pivot table showing average satisfaction by Department and Gender.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1012",
        "technology": "Python,pandas",
        "dataset_url": "https://example.com/data/employee_survey.csv",
        "overview": """
Load the employee survey CSV, then create and display a pivot table that shows average SatisfactionLevel for 
each Department-Gender combination.
""",
        "task": """
- Load 'employee_survey.csv' into pandas  
- Create a pivot table with index=Department, columns=Gender, values=SatisfactionLevel, aggfunc='mean'  
- Display or print the pivot table  
- Export the pivot table to an HTML file named 'employee_satisfaction_pivot.html'
""",
        "outcomes": """
- A Jupyter Notebook with code for pivot table creation  
- An HTML file 'employee_satisfaction_pivot.html' displaying the pivot table  
- A brief explanation of which department/gender group has the highest average satisfaction
"""
    },

    # 7) Easy, Case-Studies
    {
        "title": "Retail Foot Traffic Case Study (Easy)",
        "description": """
A retail chain provides daily foot traffic counts per store: columns: StoreID, Date, FootTraffic. Write a mini 
case study summarizing trends.
""",
        "difficulty": "Easy",
        "subcategory": "Case-Studies",
        "subject": "AIDI1012",
        "technology": "Python,pandas,matplotlib",
        "dataset_url": "https://example.com/data/retail_foot_traffic.csv",
        "overview": """
In this mini case study, you will load the foot traffic CSV, plot daily counts over time for a selected store, 
and provide a short summary.
""",
        "task": """
- Load 'retail_foot_traffic.csv' into pandas with parse_dates for Date  
- Filter data for a specific StoreID (e.g., StoreID == 101)  
- Plot daily FootTraffic vs. Date using matplotlib  
- Save the plot as 'store101_traffic.png'  
- Write a one-page Markdown report summarizing observed weekly or monthly trends
""",
        "outcomes": """
- A Jupyter Notebook (.ipynb) with data loading, filtering, and plotting code  
- A PNG 'store101_traffic.png' showing daily foot traffic  
- A one-page Markdown report with summary and recommendations (e.g., staffing suggestions)
"""
    },

    # 8) Easy, Case-Studies
    {
        "title": "Social Media Engagement Analysis (Easy)",
        "description": """
Analyze a CSV of Instagram posts: columns: PostID, Date, Likes, Comments, HasVideo (Yes/No). Provide a short 
case study comparing engagement for video vs. image posts.
""",
        "difficulty": "Easy",
        "subcategory": "Case-Studies",
        "subject": "AIDI1012",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "https://example.com/data/instagram_posts.csv",
        "overview": """
Load the Instagram posts CSV, compute average Likes and Comments for video vs. non-video posts, and visualize 
results.
""",
        "task": """
- Load 'instagram_posts.csv' into pandas  
- Group by HasVideo; compute average Likes and average Comments for Yes vs. No  
- Create a bar plot using seaborn comparing avg Likes and avg Comments for each group  
- Save the plot as 'video_vs_image_engagement.png'  
- Write a one-page case study summarizing the engagement differences and recommendations
""",
        "outcomes": """
- Jupyter Notebook with data loading, grouping, and plotting code  
- A PNG 'video_vs_image_engagement.png'  
- A one-page Markdown case study with insights and recommendations for social media strategy
"""
    },

    # ───────────────────────────────────────────────────────────────────────────
    # 9) Medium, AI-ML
    {
        "title": "Titanic Survival Prediction Comparison (Medium)",
        "description": """
Use the Kaggle Titanic dataset to build and compare two classifiers (Random Forest and Gradient Boosting) that 
predict passenger survival.
""",
        "difficulty": "Medium",
        "subcategory": "AI-ML",
        "subject": "AIDI1013",
        "technology": "Python,scikit-learn,xgboost,pandas",
        "dataset_url": "https://www.kaggle.com/c/titanic/data",
        "overview": """
In this challenge, you will preprocess Titanic data, engineer new features, train two models, and compare their 
performance using cross-validation and test metrics.
""",
        "task": """
- Load 'train.csv' and 'test.csv' from the Titanic dataset into pandas  
- Handle missing values (e.g., Age, Embarked) and encode categorical variables (Sex, Embarked)  
- Engineer at least two features (e.g., FamilySize, Title extracted from Name)  
- Split train.csv into train and validation sets (80/20)  
- Train a Random Forest classifier and a Gradient Boosting classifier (use XGBoost) with hyperparameter tuning via GridSearchCV  
- Evaluate both on validation set using accuracy, precision, recall, and ROC-AUC  
- Select the best model and make predictions on test.csv; save predictions to 'titanic_pred.csv'
""",
        "outcomes": """
- A Jupyter Notebook with preprocessing, feature engineering, training, and evaluation code  
- Two model files: 'titanic_rf_model.pkl' and 'titanic_xgb_model.json'  
- A CSV 'titanic_pred.csv' containing PassengerId and predicted Survived values  
- A Markdown summary comparing model performance and explaining feature importance
"""
    },

    # 10) Medium, AI-ML
    {
        "title": "Wine Quality Regression (Medium)",
        "description": """
Using the UCI Wine Quality dataset, build a regression model to predict wine quality score (0–10). Compare 
Random Forest and ElasticNet regressors.
""",
        "difficulty": "Medium",
        "subcategory": "AI-ML",
        "subject": "AIDI1013",
        "technology": "Python,scikit-learn,pandas",
        "dataset_url": "https://archive.ics.uci.edu/ml/datasets/Wine+Quality",
        "overview": """
In this challenge, you’ll preprocess both red and white wine CSVs, combine them, engineer features, train two 
regressors, and compare RMSE and R² scores.
""",
        "task": """
- Load 'winequality-red.csv' and 'winequality-white.csv' into pandas and add a 'type' column  
- Concatenate the two DataFrames  
- Handle missing values (if any) and scale numeric features using StandardScaler  
- Split data into train (70%), validation (15%), and test (15%) sets  
- Train a Random Forest Regressor and an ElasticNet Regressor with hyperparameter tuning  
- Evaluate each on validation set using RMSE and R²; select the best model  
- Evaluate the chosen model on the test set and plot predicted vs. actual quality scores
""",
        "outcomes": """
- Jupyter Notebook with end-to-end code for regression tasks  
- Two model files: 'wine_rf_model.pkl' and 'wine_elasticnet_model.pkl'  
- A PNG 'wine_pred_vs_actual.png' showing predicted vs. actual plots  
- A Markdown summary of regression performance and feature importance
"""
    },

    # 11) Medium, Data-Visualization
    {
        "title": "US Unemployment Rate Interactive Dashboard (Medium)",
        "description": """
Build an interactive dashboard using Plotly or Bokeh that shows monthly unemployment rates for US states from 
2000 to present. Allow multi-state comparison.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1013",
        "technology": "Python,plotly,pandas",
        "dataset_url": "https://www.bls.gov/web/laus/4799820.htm",
        "overview": """
In this challenge, you will fetch data (or load CSV) of monthly unemployment rates per state, then build an 
interactive dashboard for visual exploration.
""",
        "task": """
- Obtain monthly unemployment CSV with columns: State, Year, Month, UnemploymentRate  
- Load data into pandas and pivot so that each state is a column, index is date  
- Create a Plotly Dash or Bokeh dashboard with:  
  - A dropdown to select up to 3 states  
  - A line chart showing unemployment rate over time for selected states  
  - A choropleth map of current unemployment rates by state  
- Enable hover tooltips to display exact rate and date  
- Package as a single Python script 'dashboard.py'
""",
        "outcomes": """
- A Python dashboard file 'unemployment_dashboard.py' with instructions in comments  
- A requirements.txt listing dependencies (plotly, pandas, dash or bokeh)  
- Two static PNGs: 'unemployment_time_series.png' and 'unemployment_choropleth.png'  
- A README.md explaining how to run and use the dashboard
"""
    },

    # 12) Medium, Data-Visualization
    {
        "title": "Sales Heatmap for Retail Regions (Medium)",
        "description": """
Generate a sales heatmap by region and month using a CSV with columns: Region, Month, Revenue. Use seaborn's 
heatmap feature.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1013",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "https://example.com/data/retail_sales_region_month.csv",
        "overview": """
In this challenge, you will pivot the sales data so rows = Region, columns = Month, and values = Revenue, then 
visualize it as a heatmap with annotations.
""",
        "task": """
- Load 'retail_sales_region_month.csv' into pandas  
- Pivot data to create a matrix: index=Region, columns=Month, values=Revenue  
- Use seaborn.heatmap to visualize the matrix with annotation of revenue numbers  
- Add a title and axis labels, and save the figure as 'sales_heatmap.png'  
- Write a short summary interpreting which region-month combination had the highest revenue
""",
        "outcomes": """
- Jupyter Notebook with pivot table and heatmap code  
- A PNG 'sales_heatmap.png'  
- A one-paragraph summary of key findings from the heatmap
"""
    },

    # 13) Medium, Data-Analytics
    {
        "title": "Customer Segmentation via K-Means (Medium)",
        "description": """
Given a dataset of customers with features: AnnualIncome, SpendingScore, Age, and Tenure, perform K-Means 
clustering to segment customers. Determine optimal k using the elbow method and silhouette score.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1013",
        "technology": "Python,pandas,scikit-learn,matplotlib",
        "dataset_url": "https://example.com/data/customer_data.csv",
        "overview": """
In this challenge, you will scale features, determine the best k for K-Means clustering, fit the model, and 
visualize clusters in 2D using PCA.
""",
        "task": """
- Load 'customer_data.csv' into pandas  
- Scale numerical features with StandardScaler  
- Use the elbow method to plot within-cluster SSE for k in range 2 to 10  
- Compute silhouette scores for k in range 2 to 10 and plot them  
- Choose optimal k, fit K-Means, and assign cluster labels to customers  
- Reduce features to 2D using PCA and plot clusters with different colors  
- Save elbow plot as 'kmeans_elbow.png', silhouette plot as 'kmeans_silhouette.png', and cluster scatter as 'kmeans_clusters.png'
""",
        "outcomes": """
- Jupyter Notebook with clustering workflow code  
- Three PNGs: 'kmeans_elbow.png', 'kmeans_silhouette.png', 'kmeans_clusters.png'  
- A Markdown doc explaining chosen k and cluster characteristics with business recommendations
"""
    },

    # 14) Medium, Data-Analytics
    {
        "title": "Credit Card Fraud Detection (Medium)",
        "description": """
Using a credit card transactions CSV with anonymized features V1–V28, Time, Amount, and Class (0 = normal, 1 =
fraud), build models to detect fraudulent transactions. Handle class imbalance and evaluate performance.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1020",
        "technology": "Python,pandas,scikit-learn,imblearn",
        "dataset_url": "https://www.kaggle.com/mlg-ulb/creditcardfraud/download",
        "overview": """
In this challenge, you will preprocess imbalanced data, train at least two classifiers (Logistic Regression, 
Random Forest), and evaluate them using precision, recall, F1-score, and ROC-AUC.
""",
        "task": """
- Load 'creditcard.csv' into pandas  
- Separate features and target; apply SMOTE oversampling on the training data  
- Split data into train (70%) and test (30%) sets using stratified sampling  
- Train a Logistic Regression and a Random Forest classifier with hyperparameter tuning  
- Evaluate models on test set: precision, recall, F1-score, ROC-AUC  
- Plot ROC and Precision-Recall curves; save as 'fraud_roc_curve.png' and 'fraud_pr_curve.png'
""",
        "outcomes": """
- Jupyter Notebook with code for preprocessing, SMOTE, model training, and evaluation  
- Two PNGs: 'fraud_roc_curve.png' and 'fraud_pr_curve.png'  
- A Markdown report summarizing which model is best for minimizing false negatives in fraud detection
"""
    },

    # 15) Medium, Case-Studies
    {
        "title": "Telecom Churn Prediction Case Study (Medium)",
        "description": """
A telecom company provides customer usage data with features: tenure, MonthlyCharges, ContractType, 
InternetService, and Churn (Yes/No). Build a logistic regression model to predict churn and provide actionable insights.
""",
        "difficulty": "Medium",
        "subcategory": "Case-Studies",
        "subject": "AIDI1020",
        "technology": "Python,pandas,scikit-learn,matplotlib",
        "dataset_url": "https://example.com/data/telecom_churn.csv",
        "overview": """
In this case study, you will perform EDA to understand churn distribution, train a logistic regression model 
with interaction terms, and interpret coefficients to provide business recommendations.
""",
        "task": """
- Load 'telecom_churn.csv' into pandas; handle missing values and encode categorical features  
- Perform EDA: churn rates by ContractType and InternetService; visualize with bar charts  
- Create interaction features (e.g., ContractType × InternetService)  
- Split data into train (70%) and test (30%) sets  
- Train a logistic regression model; evaluate performance on test set using confusion matrix and ROC-AUC  
- Interpret coefficients to determine factors that increase or decrease churn probability  
- Write a 2-page case study with EDA findings, model results, and recommendations
""",
        "outcomes": """
- Jupyter Notebook with EDA, modeling, and interpretation code  
- A PNG 'churn_model_roc.png' showing ROC curve  
- A PDF or Markdown case study detailing insights and actionable recommendations (e.g., retention strategies)
"""
    },

    # 16) Medium, Case-Studies
    {
        "title": "E-Commerce Conversion Analysis (Medium)",
        "description": """
Analyze web session CSV with columns: SessionID, UserID, PageViews, TimeOnSite, DeviceType, TrafficSource, and 
Converted (1/0). Build a logistic regression model to predict conversion and write a case study.
""",
        "difficulty": "Medium",
        "subcategory": "Case-Studies",
        "subject": "AIDI1020",
        "technology": "Python,pandas,scikit-learn,seaborn",
        "dataset_url": "https://example.com/data/ecommerce_sessions.csv",
        "overview": """
You will analyze conversion rates by DeviceType and TrafficSource, train a logistic regression model, and summarize 
insights with recommendations for improving conversion rates.
""",
        "task": """
- Load 'ecommerce_sessions.csv' into pandas  
- Compute conversion rate by DeviceType and TrafficSource; visualize with seaborn bar plots  
- Encode categorical variables and split data into train (70%) and test (30%) sets  
- Train a logistic regression model; evaluate on test set (accuracy, precision, recall, ROC-AUC)  
- Interpret coefficients to identify factors impacting conversion  
- Write a 2-page case study with visualizations and recommendations (e.g., focus on mobile optimization)
""",
        "outcomes": """
- Jupyter Notebook with EDA, modeling, and visualization code  
- A PNG 'conversion_device_traffic.png' showing conversion rates  
- A PDF or Markdown case study outlining findings and recommendations
"""
    },

    # ───────────────────────────────────────────────────────────────────────────
    # 17) Hard, AI-ML
    {
        "title": "Sentiment Analysis with LSTM (Hard)",
        "description": """
Build an LSTM-based text classification model to analyze sentiment on the IMDb movie review dataset. Achieve 
at least 88% accuracy on the test set using pretrained word embeddings.
""",
        "difficulty": "Hard",
        "subcategory": "AI-ML",
        "subject": "AIDI1021",
        "technology": "Python,TensorFlow,Keras,numpy",
        "dataset_url": "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz",
        "overview": """
In this challenge, you will preprocess large text data, use GloVe embeddings, build LSTM models, and evaluate 
accuracy and loss curves.
""",
        "task": """
- Download and extract the IMDb dataset; load train and test directories into pandas DataFrames  
- Clean and tokenize text (lowercase, remove punctuation)  
- Load GloVe 100-dimensional embeddings and create an embedding matrix  
- Build two LSTM architectures:  
  1) Single-layer LSTM with dropout  
  2) Bidirectional LSTM with attention  
- Train both models with early stopping; compare validation accuracy and loss  
- Evaluate best model on test set; compute accuracy and plot confusion matrix  
- Save the model as 'imdb_lstm_model.h5' and the tokenizer as 'imdb_tokenizer.pkl'
""",
        "outcomes": """
- A Jupyter Notebook detailing data loading, preprocessing, embedding, and model training  
- Two model files: 'imdb_lstm_model.h5' and 'imdb_attention_model.h5'  
- A PNG 'imdb_training_curves.png' showing loss and accuracy over epochs  
- A confusion matrix PNG 'imdb_confusion_matrix.png'  
- A Markdown report summarizing model architectures, tuning, and final performance
"""
    },

    # 18) Hard, AI-ML
    {
        "title": "Image Segmentation with U-Net (Hard)",
        "description": """
Using the Oxford-IIIT Pet Dataset, train a U-Net model to perform pet segmentation (pixel-wise classification). 
Achieve at least 0.75 mean IoU on the validation set.
""",
        "difficulty": "Hard",
        "subcategory": "AI-ML",
        "subject": "AIDI1021",
        "technology": "Python,TensorFlow,Keras,OpenCV",
        "dataset_url": "https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz",
        "overview": """
This challenge requires building a U-Net architecture from scratch, applying data augmentation, training, and 
validating for semantic segmentation of pet images.
""",
        "task": """
- Download and extract the Oxford-IIIT Pet Dataset (images + annotations)  
- Preprocess images: resize to 128×128, normalize pixel values, and load corresponding masks  
- Implement a U-Net model with encoder-decoder and skip connections using Keras  
- Apply data augmentation (random flips, rotations) during training  
- Train the model for 50 epochs with validation split (80/20); monitor IoU metric  
- Save predicted masks on 10 sample test images and overlay them on original images  
- Save the model as 'pet_unet_model.h5'
""",
        "outcomes": """
- A Jupyter Notebook with preprocessing, U-Net implementation, and training code  
- A model file 'pet_unet_model.h5'  
- A GIF or HTML 'pet_segmentation_samples.html' showing original vs. predicted masks for sample images  
- A Markdown report with architecture details, hyperparameter choices, and final IoU scores
"""
    },

    # 19) Hard, Data-Visualization
    {
        "title": "Geospatial Air Quality Mapping (Hard)",
        "description": """
Create animated choropleth maps showing daily PM2.5 levels by neighborhood for a major city using GeoPandas 
and Plotly. Animate data over one month.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1021",
        "technology": "Python,GeoPandas,Plotly,folium",
        "dataset_url": "https://example.com/data/air_quality_pm25.csv",
        "overview": """
Load hourly air quality readings with latitude/longitude, aggregate to daily averages per monitoring station, 
and map these values onto a neighborhood shapefile.
""",
        "task": """
- Load 'air_quality_pm25.csv' into pandas; parse timestamps and group by station and date to compute daily averages  
- Load a city neighborhoods shapefile into GeoPandas  
- Merge station coordinates with neighborhood polygons using spatial join to compute daily average PM2.5 per neighborhood  
- For each day of a chosen month, create a Plotly choropleth map showing PM2.5 levels per neighborhood  
- Combine daily maps into an animated GIF 'pm25_animation.gif'  
- Save an interactive HTML Plotly animation 'pm25_animation.html'
""",
        "outcomes": """
- A Jupyter Notebook with EDA, aggregation, and mapping code  
- A GIF 'pm25_animation.gif' and HTML 'pm25_animation.html'  
- A PNG 'pm25_static_map.png' for the monthly average  
- A one-page Markdown summary interpreting spatial pollution hotspots
"""
    },

    # 20) Hard, Data-Visualization
    {
        "title": "COVID-19 Vaccine Uptake Animation (Hard)",
        "description": """
Animate global COVID-19 vaccination rates over time (monthly) using Plotly to create a time-lapse choropleth map 
showing 'people_fully_vaccinated_per_hundred'.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1021",
        "technology": "Python,Plotly,pandas,imageio",
        "dataset_url": "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv",
        "overview": """
In this challenge, you will process OWID vaccination data to show how the global vaccination rate evolves month by 
month in 2021 using animated choropleth maps.
""",
        "task": """
- Load the OWID vaccination CSV into pandas; parse the 'date' column as datetime  
- Filter data for 'people_fully_vaccinated_per_hundred' and group by month and location (country) to get the last 
  available value each month  
- Create a sequence of Plotly choropleth figures (one for each month from Jan 2021 to Dec 2021)  
- Export each frame as a static PNG and combine into an animated GIF using imageio  
- Also create a Plotly animation and save as 'vaccine_animation.html'
""",
        "outcomes": """
- A Jupyter Notebook with data cleaning, frame generation, and animation code  
- An animated GIF 'vaccine_animation_2021.gif'  
- A Plotly HTML 'vaccine_animation_2021.html'  
- A PNG 'vaccine_static_map.png' showing one representative month (e.g., June 2021)
"""
    },

    # 21) Hard, Data-Analytics
    {
        "title": "Electricity Demand Forecasting (Hard)",
        "description": """
Forecast hourly electricity demand using historical demand and temperature data. Compare SARIMA and XGBoost 
models for one-year ahead forecasting.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1021",
        "technology": "Python,pandas,statsmodels,xgboost,matplotlib",
        "dataset_url": "https://example.com/data/electricity_demand_temp.csv",
        "overview": """
You will decompose the time series, engineer lag features, train SARIMA and XGBoost models, and compare forecast 
accuracy over a test period.
""",
        "task": """
- Load 'electricity_demand_temp.csv' into pandas with parse_dates for 'Datetime'  
- Plot demand vs. time and demand vs. temperature scatter plots  
- Decompose the demand series into trend, seasonality, and residual using statsmodels  
- Create lag features (lag1, lag24, lag168) of demand for machine learning model  
- Split data: first 80% for training, next 10% for validation, last 10% for testing  
- Train a SARIMA model with exogenous variable = temperature; tune (p,d,q) parameters  
- Train an XGBoost regressor using lag features and temperature; tune via grid search  
- Evaluate on test set: MAE and RMSE; plot actual vs. forecast for both models over test period  
- Save forecasts and errors to 'demand_forecast_results.csv'
""",
        "outcomes": """
- A Jupyter Notebook with time series decomposition, SARIMA, and XGBoost code  
- A CSV 'demand_forecast_results.csv' with columns: Datetime, Actual, SARIMA_Forecast, XGBoost_Forecast  
- A PNG 'forecast_comparison.png' showing actual vs. predicted demand curves  
- A Markdown report summarizing model performance and recommendations for operational use
"""
    },

    # 22) Hard, Data-Analytics
    {
        "title": "Retail Chain Hierarchical Forecasting (Hard)",
        "description": """
Perform hierarchical forecasting on daily sales data across multiple product categories and stores. Use SARIMAX 
for total sales and LightGBM for category-level disaggregation.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1021",
        "technology": "Python,pandas,statsmodels,lightgbm",
        "dataset_url": "https://example.com/data/retail_daily_sales.csv",
        "overview": """
This challenge requires aggregate sales, decompose time series, forecast total sales using SARIMAX with promotions 
as exogenous variables, and use LightGBM to disaggregate forecasts to category-level.
""",
        "task": """
- Load 'retail_daily_sales.csv'; columns: Date, StoreID, CategoryID, UnitsSold, Price, Promotion  
- Aggregate total daily UnitsSold across all stores and categories  
- Decompose total series into trend, seasonal, and residual components  
- Train a SARIMAX model for total daily sales with Promotion as exogenous variable; tune parameters via grid search  
- Create features for LightGBM: lagged UnitsSold, Price, Promotion for each category  
- Train LightGBM models to predict daily sales per category using aggregated forecast as input  
- Evaluate hierarchical forecasts on a 3-month hold-out using MASE  
- Save final forecasts to 'hierarchical_forecasts.csv'
""",
        "outcomes": """
- Jupyter Notebook with hierarchical forecasting steps and evaluation code  
- A CSV 'hierarchical_forecasts.csv' containing Date, CategoryID, ActualSales, ForecastedSales  
- A PNG 'total_sales_decomposition.png' showing trend/seasonal/residual of total sales  
- A Markdown analysis summarizing hierarchical forecast accuracy and insights
"""
    },

    # 23) Hard, Case-Studies
    {
        "title": "Healthcare Cost Prediction Case Study (Hard)",
        "description": """
Using a patient dataset with features: Age, Gender, BMI, Children, Smoker, Region, and MedicalCost, build a 
model to predict costs and interpret results with SHAP.
""",
        "difficulty": "Hard",
        "subcategory": "Case-Studies",
        "subject": "AIDI1022",
        "technology": "Python,pandas,scikit-learn,shap,matplotlib",
        "dataset_url": "https://example.com/data/healthcare_costs.csv",
        "overview": """
This case study involves regression modeling, feature engineering, SHAP explainability, and actionable 
recommendations for healthcare cost management.
""",
        "task": """
- Load 'healthcare_costs.csv' into pandas; handle missing values and encode categorical variables (One-Hot for Region, binary for Smoker)  
- Split data into train (70%) and test (30%) sets  
- Train an ElasticNet regressor and a Gradient Boosting regressor (LightGBM), tuning hyperparameters  
- Evaluate on test set: MAE, MSE, R²; compare models  
- Compute SHAP values for the best model and plot the summary bar plot of top 10 features  
- Write a 5-page case study: data description, EDA, model comparison, SHAP interpretations, and recommendations (e.g., wellness programs)
""",
        "outcomes": """
- Jupyter Notebook with EDA, modeling, and SHAP analysis code  
- Two model files: 'cost_elasticnet_model.pkl' and 'cost_lgbm_model.txt'  
- A PNG 'shap_summary.png' showing feature importance via SHAP  
- A PDF/Markdown case study with detailed findings and policy recommendations
"""
    },

    # 24) Hard, Case-Studies
    {
        "title": "Credit Risk Assessment Case Study (Hard)",
        "description": """
Using a bank loan applicant dataset, build classification models to predict loan default and provide interpretability 
with SHAP. Dataset includes: Gender, Married, Dependents, Education, SelfEmployed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Loan_Status.
""",
        "difficulty": "Hard",
        "subcategory": "Case-Studies",
        "subject": "AIDI1022",
        "technology": "Python,pandas,scikit-learn,lightgbm,shap",
        "dataset_url": "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls",
        "overview": """
Perform end-to-end credit scoring: EDA, feature engineering (TotalIncome), model training (LightGBM & XGBoost), 
and SHAP analysis for interpretability. Provide policy recommendations.
""",
        "task": """
- Load the Excel file into pandas; rename 'default payment next month' to 'default'  
- Perform EDA: distributions of ApplicantIncome, LoanAmount, and correlation heatmap  
- Impute missing values for LoanAmount and Credit_History  
- Engineer feature TotalIncome = ApplicantIncome + CoapplicantIncome  
- One-Hot encode categorical variables: Gender, Education, Property_Area  
- Split data into train (70%) and test (30%) sets with stratification on 'default'  
- Train a LightGBM classifier and an XGBoost classifier with hyperparameter tuning via cross-validation  
- Evaluate models on test set: accuracy, precision, recall, F1-score, ROC-AUC  
- Compute SHAP values for the best model; create summary and dependence plots for top features  
- Write a 6-page case study with EDA, model results, SHAP interpretations, and policy recommendations (e.g., stricter criteria for self-employed applicants)
""",
        "outcomes": """
- Jupyter Notebook with complete workflow including SHAP analysis  
- Two model files: 'credit_lgbm_model.txt' and 'credit_xgb_model.json'  
- Two PNGs: 'shap_summary_credit.png' and 'shap_dependence_credit.png'  
- A PDF or Markdown case study detailing all findings and recommended credit policies
"""
    },

    # 25) Easy, AI-ML
    {
        "title": "Pima Indians Diabetes Prediction (Easy)",
        "description": """
Use the Pima Indians Diabetes Dataset to build a logistic regression classifier that predicts whether a patient 
has diabetes. The dataset has 768 samples and 8 input features.
""",
        "difficulty": "Easy",
        "subcategory": "AI-ML",
        "subject": "AIDI1011",
        "technology": "Python,pandas,scikit-learn",
        "dataset_url": "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv",
        "overview": """
Build a logistic regression model on the Pima Indians dataset, evaluate with accuracy and confusion matrix.
""",
        "task": """
- Load the diabetes CSV into pandas  
- Handle any zero or missing values in Glucose, BloodPressure, BMI features (replace zeros with median)  
- Split data into 70% train and 30% test sets  
- Scale features using StandardScaler  
- Train a Logistic Regression classifier and evaluate accuracy on test set  
- Plot and save the confusion matrix as 'diabetes_confusion_matrix.png'
""",
        "outcomes": """
- Jupyter Notebook containing data cleaning, model training, and evaluation code  
- A model file 'diabetes_lr_model.pkl'  
- A PNG 'diabetes_confusion_matrix.png'  
- A Markdown summary discussing model performance and potential feature improvements
"""
    },

    # 26) Easy, AI-ML
    {
        "title": "Titanic Age Imputation (Easy)",
        "description": """
Impute missing 'Age' values in the Titanic dataset using mean or median by group (e.g., median age by Pclass and Gender). 
Show before and after distributions.
""",
        "difficulty": "Easy",
        "subcategory": "AI-ML",
        "subject": "AIDI1011",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
        "overview": """
Focus on handling missing values for Age in the Titanic dataset by imputing median age based on passenger class 
and gender, and compare distributions using plots.
""",
        "task": """
- Load 'titanic.csv' into pandas  
- Identify missing Age values and compute median age grouped by Pclass and Sex  
- Fill missing Age with group-specific median values  
- Plot age distributions before and after imputation using seaborn histograms  
- Save plots as 'age_before_imputation.png' and 'age_after_imputation.png'
""",
        "outcomes": """
- Jupyter Notebook with data loading, imputation, and plotting code  
- Two PNGs: 'age_before_imputation.png' and 'age_after_imputation.png'  
- A brief Markdown explanation of the imputation strategy and its impact on distributions
"""
    },

    # 27) Easy, Data-Visualization
    {
        "title": "Global Population Growth Line Chart (Easy)",
        "description": """
Visualize world population data from 1960 to 2020 using a line chart. Use World Bank data with columns: Year, 
Population.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1011",
        "technology": "Python,pandas,matplotlib",
        "dataset_url": "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv",
        "overview": """
Plot global population growth from 1960 to 2020 using a line chart, annotate major milestones (e.g., 5 billion mark).
""",
        "task": """
- Download and extract the World Bank population CSV  
- Load data into pandas and filter for global total population by year  
- Plot Year vs. Population using matplotlib with proper labels and title  
- Annotate the year when population crossed 5 billion  
- Save the figure as 'global_population_growth.png'
""",
        "outcomes": """
- Jupyter Notebook with data loading and plotting code  
- A PNG 'global_population_growth.png'  
- A short Markdown summary describing population growth trends
"""
    },

    # 28) Easy, Data-Visualization
    {
        "title": "Airbnb Price Distribution (Easy)",
        "description": """
Visualize the distribution of Airbnb listing prices in a city using a histogram and box plot. The dataset includes 
columns: id, name, neighborhood_group, neighborhood, room_type, price, minimum_nights, number_of_reviews.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1011",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "http://data.insideairbnb.com/united-states/ny/new-york-city/2021-09-01/data/listings.csv.gz",
        "overview": """
Load the Airbnb dataset for New York City, then create a histogram and box plot of the 'price' column to visualize 
distribution and outliers.
""",
        "task": """
- Download and load 'listings.csv.gz' into pandas  
- Filter out prices > $1000 to reduce extreme outliers  
- Create a histogram of the 'price' column using seaborn with 50 bins  
- Create a box plot of 'price' using seaborn  
- Save figures as 'airbnb_price_histogram.png' and 'airbnb_price_boxplot.png'
""",
        "outcomes": """
- Jupyter Notebook with data loading, filtering, and plotting code  
- Two PNGs: 'airbnb_price_histogram.png' and 'airbnb_price_boxplot.png'  
- A brief Markdown note summarizing price distribution and outlier handling
"""
    },

    # 29) Easy, Data-Analytics
    {
        "title": "Netflix Genre Count (Easy)",
        "description": """
Count the number of movies and TV shows per genre in a Netflix titles dataset. The CSV includes: show_id, type, 
title, director, country, date_added, release_year, rating, duration, listed_in, description.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1011",
        "technology": "Python,pandas",
        "dataset_url": "https://www.kaggle.com/datasets/shivamb/netflix-shows/download?datasetVersionNumber=1",
        "overview": """
Analyze the Netflix dataset to count how many titles belong to each genre (genre list in 'listed_in' column, 
comma-separated).
""",
        "task": """
- Load the Netflix CSV into pandas  
- Split the 'listed_in' column by comma to get individual genres  
- Explode the DataFrame so each row has one genre per title  
- Group by genre and count number of titles; sort descending  
- Save results to 'netflix_genre_count.csv'
""",
        "outcomes": """
- Jupyter Notebook with data loading and genre counting code  
- CSV 'netflix_genre_count.csv' with columns: Genre, Count  
- A brief Markdown summary listing the top 5 genres by count
"""
    },

    # 30) Easy, Data-Analytics
    {
        "title": "Restaurant Tip Analysis (Easy)",
        "description": """
Analyze the tipping behavior in the 'tips' dataset from seaborn. The CSV includes: total_bill, tip, sex, smoker, 
day, time, size.
""",
        "difficulty": "Easy",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1011",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
        "overview": """
Compute average tip percentage by gender and by day of the week, and provide a brief summary.
""",
        "task": """
- Load 'tips.csv' into pandas  
- Create a new column 'tip_pct' = tip / total_bill * 100  
- Group by sex and compute average 'tip_pct'; group by day and compute average 'tip_pct'  
- Print results as DataFrames and save to 'avg_tip_by_sex.csv' and 'avg_tip_by_day.csv'  
- Create a bar plot showing average tip percentage by day and save as 'tip_pct_by_day.png'
""",
        "outcomes": """
- Jupyter Notebook with column creation, grouping, and plotting code  
- CSVs: 'avg_tip_by_sex.csv' and 'avg_tip_by_day.csv'  
- A PNG 'tip_pct_by_day.png'  
- A one-paragraph summary of tipping patterns by gender and day
"""
    },

    # 31) Easy, Case-Studies
    {
        "title": "Marketing Campaign ROI Case Study (Easy)",
        "description": """
A company ran two marketing campaigns (A and B). You have CSV with columns: CustomerID, Campaign, Spend, Revenue. 
Write a mini case study comparing ROI for each campaign.
""",
        "difficulty": "Easy",
        "subcategory": "Case-Studies",
        "subject": "AIDI1011",
        "technology": "Python,pandas,matplotlib",
        "dataset_url": "https://example.com/data/marketing_campaign.csv",
        "overview": """
Compute total spend and revenue per campaign, calculate ROI = (Revenue - Spend) / Spend, and provide visual 
comparisons and recommendations.
""",
        "task": """
- Load 'marketing_campaign.csv' into pandas  
- Group by Campaign; sum Spend and sum Revenue  
- Compute ROI for each campaign and display in a DataFrame  
- Create a bar plot comparing ROI for Campaign A vs. Campaign B and save as 'campaign_roi.png'  
- Write a 1-page Markdown summary recommending which campaign to scale
""",
        "outcomes": """
- Jupyter Notebook with grouping, ROI computation, and plotting code  
- A PNG 'campaign_roi.png'  
- A one-page Markdown document summarizing findings and recommendations
"""
    },

    # 32) Easy, Case-Studies
    {
        "title": "Customer Satisfaction Survey (Easy)",
        "description": """
Analyze a customer satisfaction survey CSV with columns: RespondentID, Age, Gender, SatisfactionScore (1–10), 
Recommend (Yes/No). Provide a case study with insights.
""",
        "difficulty": "Easy",
        "subcategory": "Case-Studies",
        "subject": "AIDI1011",
        "technology": "Python,pandas,seaborn",
        "dataset_url": "https://example.com/data/customer_survey.csv",
        "overview": """
In this case study, you will summarize satisfaction scores by age group and gender, plot distributions, and 
make recommendations.
""",
        "task": """
- Load 'customer_survey.csv' into pandas  
- Create age groups: <25, 25–40, 41–60, >60  
- Compute average SatisfactionScore by age group and by gender; visualize with seaborn bar plots  
- Compute percent of 'Recommend' == 'Yes' by age group and plot as a bar chart  
- Save plots as 'satisfaction_by_age.png' and 'recommend_by_age.png'  
- Write a 2-page case study summarizing findings and recommendations for improving satisfaction
""",
        "outcomes": """
- Jupyter Notebook with EDA and plotting code  
- Two PNGs: 'satisfaction_by_age.png' and 'recommend_by_age.png'  
- A PDF or Markdown case study with insights and recommendations
"""
    },

    # ───────────────────────────────────────────────────────────────────────────
    # 33) Medium, AI-ML
    {
        "title": "House Price Regression Comparison (Medium)",
        "description": """
Use the California Housing dataset to predict median house values. Compare Linear Regression, Random Forest, 
and Gradient Boosting models.
""",
        "difficulty": "Medium",
        "subcategory": "AI-ML",
        "subject": "AIDI1013",
        "technology": "Python,scikit-learn,pandas,matplotlib",
        "dataset_url": "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv",
        "overview": """
You will load the housing data, engineer features (e.g., RoomsPerHousehold), train three regressors, and compare 
performance using MAE, MSE, and R².
""",
        "task": """
- Load the housing CSV into pandas  
- Create new features: RoomsPerHousehold = total_rooms / households, BedroomsPerRoom = total_bedrooms / total_rooms  
- Split data into train (60%), validation (20%), and test (20%) sets  
- Train a Linear Regression model, a Random Forest Regressor, and a Gradient Boosting Regressor with hyperparameter tuning  
- Evaluate each on validation set; select best model and evaluate on test set  
- Plot predicted vs. actual values for the test set and save as 'housing_pred_vs_actual.png'
""",
        "outcomes": """
- Jupyter Notebook with data preparation, feature engineering, and modeling code  
- Three model files: 'housing_lr.pkl', 'housing_rf.pkl', 'housing_gb.pkl'  
- A PNG 'housing_pred_vs_actual.png'  
- A Markdown summary comparing model performance and justifying the chosen model
"""
    },

    # 34) Medium, AI-ML
    {
        "title": "Customer Lifetime Value Prediction (Medium)",
        "description": """
Using an e-commerce customer dataset with columns: CustomerID, Age, Gender, AnnualIncome, SpendingScore, 
build a model to predict Customer Lifetime Value (CLV) for next year.
""",
        "difficulty": "Medium",
        "subcategory": "AI-ML",
        "subject": "AIDI1013",
        "technology": "Python,pandas,scikit-learn,xgboost",
        "dataset_url": "https://example.com/data/ecommerce_customers.csv",
        "overview": """
In this challenge, you will predict CLV as a regression problem using features describing customer demographics 
and spending behavior.
""",
        "task": """
- Load 'ecommerce_customers.csv' into pandas  
- Handle missing values and encode categorical variables  
- Split data into train (70%), validation (15%), and test (15%) sets  
- Train a Random Forest Regressor and an XGBoost Regressor with hyperparameter tuning via GridSearchCV  
- Evaluate on validation set using MAE and RMSE; select best model  
- Evaluate the final model on the test set and plot residuals vs. predicted values; save as 'clv_residuals.png'
""",
        "outcomes": """
- Jupyter Notebook with regression modeling workflow  
- Two model files: 'clv_rf.pkl' and 'clv_xgb.json'  
- A PNG 'clv_residuals.png'  
- A Markdown summary describing model performance and business implications for targeting customers
"""
    },

    # 35) Medium, Data-Visualization
    {
        "title": "Interactive Stock Price Dashboard (Medium)",
        "description": """
Build an interactive dashboard using Dash that displays candlestick charts and moving averages for a user-entered 
stock ticker from the past 5 years.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1013",
        "technology": "Python,plotly,dash,yfinance",
        "dataset_url": "https://pypi.org/project/yfinance/",
        "overview": """
Create a Dash app where users input a stock ticker (e.g., AAPL), and the app fetches historical data using yfinance, 
plots candlestick chart with 50-day and 200-day moving averages, and displays volume.
""",
        "task": """
- Set up a Dash app with a text input for the stock ticker and a 'Submit' button  
- On submit, fetch 5 years of daily data for the ticker using yfinance  
- Compute 50-day and 200-day moving averages  
- Plot a Plotly candlestick chart with moving averages overlaid and volume bars below  
- Deploy locally and save two static PNGs: 'candlestick_chart.png' and 'moving_average.png'
""",
        "outcomes": """
- A Python file 'stock_dashboard.py' implementing the Dash app  
- Static PNGs: 'candlestick_chart.png' and 'moving_average.png'  
- A requirements.txt listing dependencies (dash, plotly, yfinance)  
- A README.md with instructions to run the dashboard (e.g., 'python stock_dashboard.py')
"""
    },

    # 36) Medium, Data-Visualization
    {
        "title": "Sales Forecast Visualization (Medium)",
        "description": """
Visualize sales forecasts and actuals for the next 12 months using Plotly: shaded area showing confidence 
interval from a provided CSV containing forecasted mean, lower, and upper bounds.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1013",
        "technology": "Python,pandas,plotly",
        "dataset_url": "https://example.com/data/sales_forecast.csv",
        "overview": """
Load a CSV containing columns: Date, ActualSales, ForecastMean, ForecastLower, ForecastUpper. Create an interactive 
Plotly line chart with an area fill between lower and upper forecasts.
""",
        "task": """
- Load 'sales_forecast.csv' into pandas with parse_dates for Date  
- Plot ActualSales and ForecastMean as lines using Plotly  
- Add a shaded area (fill) between ForecastLower and ForecastUpper  
- Customize hover tooltips to show all values  
- Save the figure as 'sales_forecast_visualization.html' and export a static PNG 'sales_forecast.png'
""",
        "outcomes": """
- Jupyter Notebook with data loading and Plotly code  
- An interactive HTML 'sales_forecast_visualization.html'  
- A static PNG 'sales_forecast.png'  
- A short summary describing forecast accuracy and uncertainty bounds
"""
    },

    # 37) Medium, Data-Analytics
    {
        "title": "Retail Basket Analysis with Apriori (Medium)",
        "description": """
Perform market-basket analysis on a retail transactions dataset using the Apriori algorithm to find frequent 
itemsets and generate association rules.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1013",
        "technology": "Python,pandas,mlxtend,networkx",
        "dataset_url": "https://example.com/data/retail_transactions.csv",
        "overview": """
You will pivot transactional data into basket format, find frequent itemsets with support ≥ 0.02, generate rules 
with confidence ≥ 0.5 and lift ≥ 1.2, and visualize top rules.
""",
        "task": """
- Load 'retail_transactions.csv' into pandas  
- Pivot data: rows=TransactionID, columns=Item, values=True/False indicating purchase  
- Use mlxtend.frequent_patterns.apriori to find frequent itemsets (support ≥ 0.02)  
- Generate association rules with mlxtend.frequent_patterns.association_rules (min_threshold=0.5)  
- Filter rules with lift ≥ 1.2 and sort by descending lift; select top 5  
- Visualize the top 5 rules as a directed network graph using NetworkX and save as 'basket_rules_network.png'
""",
        "outcomes": """
- Jupyter Notebook with basket transformation, Apriori, and rule generation code  
- A CSV 'top5_association_rules.csv' listing antecedents, consequents, support, confidence, lift  
- A PNG 'basket_rules_network.png'  
- A one-paragraph interpretation of the top association rule
"""
    },

    # 38) Medium, Data-Analytics
    {
        "title": "Credit Scoring Model Development (Medium)",
        "description": """
Develop a credit scoring model using the UCI Credit Card Default dataset. Use logistic regression and random 
forest, compare ROC curves, and choose a cutoff threshold.
""",
        "difficulty": "Medium",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1020",
        "technology": "Python,pandas,scikit-learn,matplotlib",
        "dataset_url": "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls",
        "overview": """
You will preprocess the credit dataset, train two classifiers, evaluate ROC curves, and choose a probability cutoff 
for predicting defaults.
""",
        "task": """
- Load the Excel file into pandas and rename the target column to 'default'  
- Split data into train (70%) and test (30%) sets stratified by 'default'  
- Train a Logistic Regression and a Random Forest classifier with hyperparameter tuning  
- Compute predicted probabilities on the test set and plot ROC curves for both models; save as 'credit_roc.png'  
- Determine optimal cutoff threshold by maximizing Youden’s J statistic and report it  
- Save test set predictions to 'credit_default_predictions.csv'
""",
        "outcomes": """
- Jupyter Notebook with preprocessing, model training, and evaluation code  
- A PNG 'credit_roc.png' showing ROC curves for both models  
- A CSV 'credit_default_predictions.csv' containing actual labels, predicted probabilities, and predicted labels  
- A Markdown summary explaining cutoff choice and model comparison
"""
    },

    # 39) Medium, Case-Studies
    {
        "title": "Sales Conversion Funnel Case Study (Medium)",
        "description": """
Analyze e-commerce funnel data with columns: Stage (Visited, AddedToCart, Purchased), Count. Create a case 
study explaining conversion drop-offs and recommendations.
""",
        "difficulty": "Medium",
        "subcategory": "Case-Studies",
        "subject": "AIDI1020",
        "technology": "Python,pandas,matplotlib",
        "dataset_url": "https://example.com/data/conversion_funnel.csv",
        "overview": """
Load conversion funnel data, plot funnel chart, compute conversion rates between stages, and provide business 
recommendations to improve funnel performance.
""",
        "task": """
- Load 'conversion_funnel.csv' into pandas  
- Compute conversion rates: AddedToCart/Visited, Purchased/AddedToCart  
- Create a funnel chart using matplotlib (horizontal bar chart with decreasing widths)  
- Save the chart as 'conversion_funnel.png'  
- Write a two-page case study summarizing drop-off points and recommending optimizations (e.g., improved UX)
""",
        "outcomes": """
- Jupyter Notebook with data analysis and funnel chart code  
- A PNG 'conversion_funnel.png'  
- A PDF or Markdown case study with analysis and recommendations
"""
    },

    # 40) Medium, Case-Studies
    {
        "title": "Customer Lifetime Value Segmentation (Medium)",
        "description": """
Segment customers based on predicted CLV from an e-commerce dataset and write a case study describing each 
segment’s characteristics.
""",
        "difficulty": "Medium",
        "subcategory": "Case-Studies",
        "subject": "AIDI1020",
        "technology": "Python,pandas,scikit-learn,matplotlib",
        "dataset_url": "https://example.com/data/ecommerce_customers.csv",
        "overview": """
You will predict CLV, then segment customers into quartiles, analyze each quartile’s demographics and purchasing 
behavior, and provide marketing strategies.
""",
        "task": """
- Load 'ecommerce_customers.csv' and predict CLV using a pre-trained model (or train a simple regressor)  
- Add a CLV column to the DataFrame  
- Segment customers into four quartiles based on CLV  
- For each quartile, compute average Age, AnnualIncome, and SpendingScore; visualize as bar charts  
- Save charts as 'clv_quartile_profiles.png'  
- Write a two-page case study describing each segment and recommending targeted marketing strategies
""",
        "outcomes": """
- Jupyter Notebook with CLV prediction, segmentation, and analysis code  
- A PNG 'clv_quartile_profiles.png'  
- A PDF or Markdown case study detailing segment characteristics and marketing recommendations
"""
    },

    # ───────────────────────────────────────────────────────────────────────────
    # 41) Hard, AI-ML
    {
        "title": "Neural Machine Translation (English→French) (Hard)",
        "description": """
Build a seq2seq model with attention to translate English sentences to French using the Tatoeba 'fra-eng' dataset. 
Evaluate using BLEU scores.
""",
        "difficulty": "Hard",
        "subcategory": "AI-ML",
        "subject": "AIDI1022",
        "technology": "Python,TensorFlow,Keras,nltk",
        "dataset_url": "https://www.manythings.org/anki/fra-eng.zip",
        "overview": """
You will preprocess English-French sentence pairs, build an LSTM encoder-decoder with attention, train for multiple 
epochs, and compute BLEU scores on a test set.
""",
        "task": """
- Download and extract 'fra-eng.zip'; load 'fra.txt' into pandas with columns: English, French  
- Clean text by lowercasing and removing punctuation; tokenize sentences using NLTK  
- Build vocabularies for English and French with a max size of 20,000 tokens  
- Implement a seq2seq model with LSTM encoder-decoder and Bahdanau attention in Keras  
- Train the model for 30 epochs with batch_size=64; monitor validation loss  
- After training, use the model to translate 500 test English sentences and compute BLEU scores  
- Save translations and reference sentences to 'nmt_translations.txt'
""",
        "outcomes": """
- A Jupyter Notebook with data preprocessing, model building, training, and evaluation code  
- A model file 'nmt_fra_eng_model.h5' and tokenizer files 'eng_tokenizer.pkl', 'fra_tokenizer.pkl'  
- A text file 'nmt_translations.txt' listing English, reference French, and predicted French sentences  
- A Markdown report summarizing BLEU scores and model observations
"""
    },

    # 42) Hard, AI-ML
    {
        "title": "Image Captioning with CNN-RNN (Hard)",
        "description": """
Build an image captioning model using a pre-trained CNN (e.g., InceptionV3) and an LSTM decoder. Use the Flickr8k 
dataset to train and evaluate the model.
""",
        "difficulty": "Hard",
        "subcategory": "AI-ML",
        "subject": "AIDI1022",
        "technology": "Python,TensorFlow,Keras,numpy,matplotlib",
        "dataset_url": "https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip",
        "overview": """
In this challenge, you will extract image features using a pre-trained CNN, preprocess captions, train an LSTM 
decoder, and generate captions for unseen images.
""",
        "task": """
- Download and extract Flickr8k images and caption file 'Flickr8k.token.txt'  
- Load images and extract features using InceptionV3 without top layer; save features to disk  
- Preprocess captions: lowercase, remove punctuation, add startseq and endseq tokens, and build tokenizer  
- Define an encoder-decoder architecture: CNN feature extractor + LSTM decoder with embedding layer  
- Train for 20 epochs with batch_size=64; monitor validation loss  
- Generate captions for 10 random test images and save results to 'image_captions.txt'  
- Save trained model as 'image_captioning_model.h5'
""",
        "outcomes": """
- A Jupyter Notebook detailing feature extraction, preprocessing, model building, and training  
- A model file 'image_captioning_model.h5' and tokenizer file 'caption_tokenizer.pkl'  
- A text file 'image_captions.txt' listing image filenames and generated captions  
- A Markdown report discussing challenges, BLEU scores for generated captions, and future improvements
"""
    },

    # 43) Hard, Data-Visualization
    {
        "title": "Stock Market Animation with Moving Averages (Hard)",
        "description": """
Create an animation of a stock’s candlestick chart with 50-day and 200-day moving averages over time using 
matplotlib and imageio.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1022",
        "technology": "Python,pandas,matplotlib,imageio,yfinance",
        "dataset_url": "https://pypi.org/project/yfinance/",
        "overview": """
Fetch 5 years of daily OHLCV data for a given stock ticker, compute moving averages, and generate frame-by-frame 
charts to animate price movements alongside moving averages.
""",
        "task": """
- Use yfinance to download 5 years of daily data for a stock ticker (e.g., 'AAPL') into pandas  
- Compute 50-day and 200-day moving averages; add as new columns  
- For each trading day, create a candlestick chart with matplotlib and overlay moving averages; save each frame as PNG  
- Combine all PNG frames into an animated GIF 'stock_animation.gif' using imageio  
- Save a sample frame as 'stock_sample_frame.png'
""",
        "outcomes": """
- A Python script 'stock_animation.py' with data fetching, plotting, and animation code  
- An animated GIF 'stock_animation.gif'  
- A sample PNG 'stock_sample_frame.png'  
- A README.md explaining how to run the script and generate the animation
"""
    },

    # 44) Hard, Data-Visualization
    {
        "title": "Global CO2 Emissions Interactive Map (Hard)",
        "description": """
Build an interactive choropleth map that shows CO2 emissions per country for multiple years, allowing users to 
select the year slider.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1022",
        "technology": "Python,plotly,pandas",
        "dataset_url": "https://datahub.io/core/co2-fossil-global/r/fossil-fuels-co2.csv",
        "overview": """
Load the global fossil fuel CO2 emissions CSV, pivot data to have countries vs. years, and create a Plotly Express 
choropleth with a year slider.
""",
        "task": """
- Load 'fossil-fuels-co2.csv' into pandas  
- Pivot data so each row is a country and columns are years with CO2 values  
- Melt or restructure the DataFrame to long format: columns: Country, Year, CO2  
- Create a Plotly Express choropleth with animation_frame='Year' and color='CO2'  
- Customize the layout with title and colorbar, and save the HTML as 'co2_emissions_map.html'  
- Export a static PNG of one frame (e.g., 2020) as 'co2_emissions_2020.png'
""",
        "outcomes": """
- Jupyter Notebook with data reshaping and Plotly animation code  
- An interactive HTML 'co2_emissions_map.html'  
- A PNG 'co2_emissions_2020.png'  
- A short Markdown summary describing emission trends and hotspots
"""
    },

    # 45) Hard, Data-Analytics
    {
        "title": "Turbofan Engine RUL Prediction (Hard)",
        "description": """
Use the NASA Turbofan Engine Degradation Simulation dataset to predict Remaining Useful Life (RUL) of engines. 
Compare Random Forest and LSTM models.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1022",
        "technology": "Python,pandas,scikit-learn,TensorFlow",
        "dataset_url": "https://ti.arc.nasa.gov/c/6/",
        "overview": """
Load CMAPSS data files, compute RUL labels, engineer features, train a Random Forest regressor and an LSTM model, 
and compare performance using RMSE.
""",
        "task": """
- Download and parse 'train_FD001.txt' and 'test_FD001.txt' into pandas with appropriate column names  
- Compute RUL for each training cycle: max cycle number per engine minus current cycle  
- Engineer features: rolling mean and std of sensor readings over last 5 cycles  
- Split train data into train (80%) and validation (20%) by engine ID  
- Train a Random Forest regressor with hyperparameter tuning on validation set  
- Build a simple LSTM model for regression using TensorFlow; train with early stopping  
- Evaluate both models on the official test set using RMSE; plot predicted vs. actual RUL for 5 engines and save as 'rul_comparison.png'
""",
        "outcomes": """
- Jupyter Notebook with feature engineering, Random Forest, and LSTM code  
- Two model files: 'rul_rf_model.pkl' and 'rul_lstm_model.h5'  
- A PNG 'rul_comparison.png' showing predicted vs. actual RUL  
- A Markdown report comparing model performance and recommending the best approach
"""
    },

    # 46) Hard, Data-Analytics
    {
        "title": "Retail Demand Forecasting with Prophet (Hard)",
        "description": """
Forecast daily retail sales using Facebook Prophet. Compare Prophet forecasts to an ARIMA model for one-year ahead forecasting.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Analytics",
        "subject": "AIDI1022",
        "technology": "Python,pandas,fbprophet,statsmodels,matplotlib",
        "dataset_url": "https://example.com/data/retail_daily_sales.csv",
        "overview": """
You will use Prophet to forecast daily sales for the next year and compare its performance against an ARIMA model 
using past 5 years of data.
""",
        "task": """
- Load 'retail_daily_sales.csv' into pandas with parse_dates for Date; aggregate sales to daily total  
- Prepare data for Prophet (columns 'ds' and 'y')  
- Fit a Prophet model and forecast one year ahead; plot and save as 'prophet_forecast.png'  
- Fit an ARIMA model on the same training data; forecast one year ahead; plot and save as 'arima_forecast.png'  
- Compute forecast accuracy metrics (MAE, RMSE) for both models on a hold-out test set (last year)  
- Save forecast results to 'prophet_vs_arima.csv'
""",
        "outcomes": """
- Jupyter Notebook with Prophet and ARIMA forecasting code  
- Two PNGs: 'prophet_forecast.png' and 'arima_forecast.png'  
- A CSV 'prophet_vs_arima.csv' comparing actual vs. predicted sales for both models  
- A Markdown summary discussing which model performed better and why
"""
    },

    # 47) Hard, Case-Studies
    {
        "title": "Fraud Detection in Financial Transactions Case Study (Hard)",
        "description": """
Analyze a credit card transactions dataset (highly imbalanced) to build a fraud detection system. Use Logistic 
Regression, Random Forest, and XGBoost, and compare using ROC-AUC and Precision-Recall curves.
""",
        "difficulty": "Hard",
        "subcategory": "Case-Studies",
        "subject": "AIDI1022",
        "technology": "Python,pandas,scikit-learn,xgboost,imblearn",
        "dataset_url": "https://www.kaggle.com/mlg-ulb/creditcardfraud/download",
        "overview": """
Perform end-to-end analysis: handle class imbalance with SMOTE, train three classifiers, evaluate and interpret using 
SHAP, and present a detailed case study with recommendations.
""",
        "task": """
- Load 'creditcard.csv' into pandas; separate features and target  
- Apply SMOTE oversampling on the training data to handle imbalance  
- Split data into train (60%), validation (20%), and test (20%) sets using stratified sampling  
- Train a Logistic Regression, Random Forest, and XGBoost classifier with hyperparameter tuning  
- Evaluate on validation set using ROC-AUC and Precision-Recall curves; select best model  
- Compute SHAP values for the best model and display summary and dependence plots for top features  
- Evaluate final model on test set and save metrics and curves as 'fraud_case_study_results.csv'
""",
        "outcomes": """
- Jupyter Notebook with data handling, model training, SHAP analysis, and evaluation code  
- SHAP summary PNG 'fraud_shap_summary.png' and dependence PNG 'fraud_shap_dependence.png'  
- A CSV 'fraud_case_study_results.csv' with model metrics on test set  
- A 6-page PDF or Markdown case study covering methodology, results, SHAP interpretations, and recommendations for real-time fraud prevention
"""
    },

    # 48) Hard, Case-Studies
    {
        "title": "Manufacturing Defect Prediction Case Study (Hard)",
        "description": """
Using sensor data from a manufacturing line, predict product defects before production completes. The dataset 
includes Sensor1...Sensorn readings and DefectLabel (0/1). Build Random Forest and Neural Network models.
""",
        "difficulty": "Hard",
        "subcategory": "Case-Studies",
        "subject": "AIDI1022",
        "technology": "Python,pandas,scikit-learn,TensorFlow,matplotlib",
        "dataset_url": "https://example.com/data/manufacturing_sensors.csv",
        "overview": """
You will aggregate sensor readings, build classification models, compare performance, and propose preventive 
maintenance strategies based on model outputs.
""",
        "task": """
- Load 'manufacturing_sensors.csv' into pandas; parse Timestamp column  
- Aggregate sensor readings by product batch: compute mean, median, std for each sensor over last 10 cycles  
- Merge aggregated features with DefectLabel  
- Split data into train (70%), validation (15%), and test (15%) sets stratified by DefectLabel  
- Train a Random Forest classifier with hyperparameter tuning; evaluate on validation set  
- Train a Neural Network binary classifier (2 hidden layers) in TensorFlow; evaluate and compare with Random Forest  
- Plot ROC curves for both models and save as 'defect_detection_roc.png'  
- Identify top 10 high-risk product batches and suggest maintenance actions
""",
        "outcomes": """
- Jupyter Notebook with feature aggregation, model training, and evaluation code  
- Two model files: 'defect_rf_model.pkl' and 'defect_nn_model.h5'  
- A PNG 'defect_detection_roc.png' comparing ROC curves  
- A two-page case study PDF or Markdown with analysis, model comparisons, and maintenance recommendations
"""
    },

    # 49) Hard, AI-ML
    {
        "title": "Time Series Anomaly Detection with LSTM (Hard)",
        "description": """
Detect anomalies in a multivariate time series dataset (e.g., IoT sensor data) using an LSTM autoencoder. 
Reconstruct input and compute anomaly scores.
""",
        "difficulty": "Hard",
        "subcategory": "AI-ML",
        "subject": "AIDI1022",
        "technology": "Python,TensorFlow,Keras,pandas,matplotlib",
        "dataset_url": "https://example.com/data/iot_sensor_timeseries.csv",
        "overview": """
Load multivariate sensor data, build an LSTM autoencoder for reconstruction, compute reconstruction error 
as anomaly score, and evaluate detection performance.
""",
        "task": """
- Load 'iot_sensor_timeseries.csv' into pandas with parse_dates for Timestamp  
- Normalize features using MinMaxScaler  
- Split data into train (normal data only) and test (with injected anomalies)  
- Build an LSTM autoencoder: encoder with LSTM layers and decoder symmetric; compile with MSE loss  
- Train on train set and compute reconstruction error for each sample in test set  
- Determine anomaly threshold (e.g., 95th percentile of train reconstruction errors)  
- Label test samples as anomalies if error > threshold; compute precision, recall, F1, and plot error distribution as 'anomaly_error_dist.png'
""",
        "outcomes": """
- Jupyter Notebook with data loading, autoencoder implementation, and anomaly detection code  
- A model file 'lstm_autoencoder.h5'  
- A PNG 'anomaly_error_dist.png' showing reconstruction error distribution  
- A Markdown report summarizing anomaly detection performance and threshold selection
"""
    },

    # 50) Hard, Data-Visualization
    {
        "title": "3D Protein Structure Visualization (Hard)",
        "description": """
Visualize a protein’s 3D structure using data from the Protein Data Bank (PDB) file. Render an interactive 3D 
plot using Plotly.
""",
        "difficulty": "Hard",
        "subcategory": "Data-Visualization",
        "subject": "AIDI1022",
        "technology": "Python,biopython,plotly",
        "dataset_url": "https://files.rcsb.org/download/1AKE.pdb",
        "overview": """
Load a PDB file (e.g., 1AKE), extract atomic coordinates, and create an interactive 3D scatter plot of C-alpha 
atoms colored by residue type.
""",
        "task": """
- Use Biopython’s PDB parser to load '1AKE.pdb' and extract atom coordinates and residue types for C-alpha atoms  
- Create a DataFrame with columns: x, y, z, residue_name  
- Map each residue to a distinct color (e.g., hydrophobic vs. polar)  
- Use Plotly to plot a 3D scatter of C-alpha atoms with color based on residue_name; add hover text showing residue ID  
- Save the plot as an interactive HTML 'protein_3d.html' and a static PNG 'protein_3d.png'
""",
        "outcomes": """
- Jupyter Notebook with PDB parsing and Plotly visualization code  
- An interactive HTML 'protein_3d.html'  
- A PNG 'protein_3d.png'  
- A Markdown description explaining which regions correspond to alpha-helices, beta-sheets, and loops
"""
    }
]

# ────────────────────────────────────────────────────────────────────────────────
# After pasting, you can extend your existing `sample_data` like:
#
# sample_data = [
#     … (existing entries) …,
#     *extra_mock_data
# ]
#
# Then run `python seed_data.py` (with drop_all / create_all logic) to recreate the table
# and insert all records, including these 12 new ones.
# ────────────────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.drop_all()   # Remove old tables (so the new columns take effect)
        db.create_all() # Recreate tables with new schema

        for entry in sample_data:
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
        print("Dropped old tables, recreated schema, and seeded sample_data with new fields.")        
        print("Database created/updated and seeded successfully!")
