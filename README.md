# Heart Disease Prediction

Heart Disease Prediction System using Logistic Regression, SVM, and Random Forest.

## Overview

This project is a comprehensive machine learning pipeline for predicting heart disease using the Cleveland Heart Disease dataset. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment.

## Features

- **Data Preprocessing**: Handles missing values, removes duplicates, and detects outliers.
- **Exploratory Data Analysis (EDA)**: Visualizes relationships between features and target variables using countplots, heatmaps, scatterplots, and more.
- **Machine Learning Models**: Implements Logistic Regression, Support Vector Machine (SVM), and Random Forest classifiers.
- **Hyperparameter Tuning**: Uses `GridSearchCV` to optimize model performance.
- **Evaluation Metrics**: Calculates accuracy, precision, recall, F1 score, false negative rate, and AUC scores.
- **Interactive Prediction System**: Allows users to input patient data and predict heart disease risk.
- **Model Deployment**: Saves trained models as `.pkl` files for future use.

## Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Scikit-learn
- Joblib

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the Jupyter Notebook for training and evaluation.
4. Use the interactive prediction system to test the models.

## Dataset

The project uses the Cleveland Heart Disease dataset, which contains 303 records with 14 features, including:
- Age
- Sex
- Chest pain type
- Cholesterol levels
- And more...

## Visualizations

The project includes various visualizations to analyze the dataset and model performance, such as:

- **Countplots** for categorical features
- **Pairwise plots** for numerical features
- **Correlation heatmaps**
- **ROC curves** and AUC comparisons

## Models

The following machine learning models are implemented:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

Each model is trained, tuned, and evaluated to identify the best-performing algorithm.

## Results

The project provides a detailed comparison of model performance, including metrics and visualizations, to help identify the most effective model for heart disease prediction.
