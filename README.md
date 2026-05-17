# Weather Forecast ML System

An end-to-end machine learning project focused on real-time weather forecasting, automated data collection, and full-stack deployment.

The main goal of this project is to understand how real-world machine learning systems are built beyond just model training. The project covers the complete workflow — from collecting live weather data and performing analysis to building forecasting models, creating a web dashboard, and exploring deployment and MLOps practices.

Live weather data is collected continuously using the OpenWeatherMap API for multiple Indian cities and stored for analysis and forecasting.

---

## Project Status

### Completed
- Automated weather data collection using OpenWeatherMap API
- Hourly cron-based data pipeline on Linux
- Historical weather dataset generation
- Exploratory Data Analysis (EDA)
- Profiling reports and visual analysis
- Time-series feature engineering
- Lag and rolling window feature creation
- Feature importance analysis
- Baseline Random Forest forecasting model
- Hyperparameter tuning using GridSearchCV
- Model evaluation and prediction analysis

### Currently Working On
- Improving forecasting performance with larger datasets
- Experimenting with additional features and model optimization
- Saving and versioning trained models

### Planned
- PostgreSQL database integration
- Django-based weather dashboard
- Forecast visualization interface
- Model deployment pipeline
- Automated retraining workflow
- Introductory MLOps integration

---

## Features

- Real-time weather data collection
- Multi-city weather monitoring
- Automated hourly data updates
- Historical weather tracking
- Time-series forecasting pipeline
- Feature engineering for forecasting
- Model training and evaluation
- Data visualization and profiling
- Modular project structure for scalability

---

## Tech Stack

### Machine Learning & Data Processing
- Python
- Pandas
- NumPy
- Scikit-learn

### Data Visualization
- Matplotlib
- Seaborn
- ydata-profiling

### Backend & Automation
- Django
- Linux Cron Jobs
- Conda Environment
- Git & GitHub

### APIs & Data Sources
- OpenWeatherMap API

---

## Project Structure

```bash
weather_forecast/
│
├── data/
├── live_data/
├── models/
├── notebooks/
├── reports/
├── scripts/
├── environment.yml
├── README.md
└── .gitignore