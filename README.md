# Weather Forecast ML System

A real-time weather forecasting and analytics project built using machine learning and automated data pipelines.

This project started as an attempt to understand how real-world ML systems are built beyond just training a model. The goal is to build a complete end-to-end weather forecasting platform that handles data collection, analysis, feature engineering, model training, deployment, and automation.

The system continuously collects live weather data from multiple Indian cities using the OpenWeatherMap API and stores it for forecasting and analysis.

---

## Current Progress

### Completed
- Automated weather data collection using OpenWeatherMap API
- Hourly cron-based data pipeline on Linux
- Historical dataset creation and storage
- Exploratory Data Analysis (EDA)
- Profiling reports and visualization
- Time-series feature engineering
- Lag and rolling window features
- Feature importance analysis using Random Forest

### In Progress
- Forecast model training and evaluation
- Hyperparameter tuning
- Prediction pipeline

### Planned
- Django-based weather dashboard
- Forecast visualization UI
- Database integration
- Model deployment
- MLOps workflow and automated retraining

---

## Features

- Live weather data collection
- Multi-city weather monitoring
- Automated hourly updates using cron jobs
- Historical weather tracking
- Time-series forecasting pipeline
- Feature engineering for weather prediction
- Data visualization and profiling
- Modular project structure for deployment

---

## Tech Stack

### Data & Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn

### Visualization & Analysis
- Matplotlib
- Seaborn
- ydata-profiling

### Backend & Deployment
- Django
- Linux Cron Jobs
- Conda Environment
- Git & GitHub

### APIs
- OpenWeatherMap API

---

## Project Structure

```bash
weather_forecast/
│
├── data/
├── notebooks/
├── reports/
├── scripts/
├── environment.yml
├── README.md
└── .gitignore