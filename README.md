# Laptop-Price-Predictor-A-Machine-Learning-Powered-Web-Application

## Machine Learning Concepts Applied:

- Supervised Learning – Predicting continuous laptop prices using regression
- Regression Algorithms – Including Multiple Linear Regression, Decision Tree, Random Forest, Lasso, and KNN
- Model Evaluation – Cross-validation and R² score to compare models
- Feature Engineering – One-hot encoding, binary flags for features like touchscreen and IPS
- Hyperparameter Tuning – Adjusting n_estimators, max_depth, and criterion in the Random Forest
- Model Selection – Based on performance metrics and assumption violations

## Technologies Used

#### Machine Learning & Data Science

- Python 3 – Core programming language
- Pandas – Data manipulation and preprocessing
- NumPy – Numerical operations
- Scikit-learn – Machine learning models and utilities

#### Web Development

- Flask – Lightweight Python web framework for backend
- HTML5 – Structure of the web page (form and layout)
- CSS3 – Styling of the web interface

#### Environment & Package Management

- Virtual Environment (env) – Isolated Python environment
- Requirements.txt – List of dependencies for deployment and reproducibility

#### Deployment & Version Control

- Git – Version control tool to track changes
- GitHub – Code hosting platform for source control
- Render.com – Cloud platform to deploy the web application


## Introduction
Laptop prices vary significantly based on hardware specifications, brand, and features. Consumers often face difficulty estimating a fair price for a laptop that fits their needs. This project aims to address that challenge by developing a machine learning-powered web application that predicts laptop prices based on user-defined inputs such as RAM, weight, brand, CPU, GPU, touchscreen availability, and operating system.

The application is built using Python and Flask, and it uses a machine learning model (Random Forest Regression) trained on real-world laptop data. The final application is deployed as a user-friendly web tool hosted on Render.com.

## Data Cleaning and Transformation
The original dataset contained 1303 rows and 12 columns with no missing values. The key data cleaning steps are outlined below:

| Column           | Transformation Applied                                                              |
|------------------|--------------------------------------------------------------------------------------|
| RAM              | Removed "GB", converted to float                                                    |
| Weight           | Removed "kg", converted to float                                                    |
| Company          | Grouped rare brands into "Other"                                                    |
| Product          | Kept as is (limited categories)                                                     |
| TypeName         | Dropped due to too many unique values                                               |
| CPU              | Grouped into main categories: Core i3, i5, i7, AMD, Other                           |
| GPU              | Grouped into Intel, NVIDIA, AMD (dropped ARM with 1 entry)                          |
| ScreenResolution | Created binary features: Touchscreen, IPS                                           |
| Operating System | Categorical encoding (e.g., Windows, macOS, etc.)                                   |


Feature Engineering
- After transformations and one-hot encoding, the final dataset had 31 features.
- Numerical columns were normalized when needed.

## Model Building and Evaluation

#### Models Tried
Five machine learning models were evaluated using cross-validation (CV) with R² as the performance metric:

| Model                   | R² Score (CV) |
|-------------------------|---------------|
| Multiple Linear Regression | 0.6801      |
| Decision Tree Regressor    | 0.6504      |
| Random Forest Regressor    | 0.7567      |
| Lasso Regression           | 0.6806      |
| K-Nearest Neighbors        | 0.6223      |


Final Model: Random Forest Regressor
Due to non-linear relationships in the data and poor assumption satisfaction for linear models, Random Forest was selected as the final model.

Final Model Parameters:
- n_estimators = 10
- max_depth = 19
- criterion = 'absolute_error'
- random_state = 42

Final R² Score (Test): 0.8167

## Deployment
The web application was developed with a Python Flask backend and HTML/CSS frontend. It accepts user inputs via a form and displays the predicted price dynamically.

Deployment Process:
- Virtual Environment Setup: All packages managed in env/ (excluded from GitHub).
- Requirements File: Created with pip freeze > requirements.txt
- GitHub Upload: Project pushed to a public GitHub repository.

Render Deployment:

- Connected GitHub repo to Render.com
- Provided build (pip install -r requirements.txt) and start (python app.py) commands
- Hosted with a custom link (e.g., https://laptop-price-predictor.onrender.com)








