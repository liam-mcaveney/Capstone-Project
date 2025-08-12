# Sentiment Analysis Web Application

## Overview

This project is a Flask-based sentiment analysis web application enhanced for the CS-499 Computer Science Capstone. It uses a trained Naive Bayes classifier with a CountVectorizer to predict whether user-submitted text has a positive or negative sentiment.

## Features

* Machine learning model trained on labeled sentiment data.
* Flask backend with SQLite database integration.
* User interface for submitting and viewing sentiment predictions.
* Persistent storage of user inputs and predictions.
* Model retraining capability.

## Technology Stack

* **Backend:** Python, Flask, SQLAlchemy
* **Machine Learning:** scikit-learn, joblib
* **Database:** SQLite
* **Frontend:** HTML, CSS (Flask templates)

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/liam-mcaveney/Capstone-Project.git
cd Capstone-Project
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Initialize the database:

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

5. Run the application:

```bash
python run.py
```

6. Open in browser at `http://127.0.0.1:5000`

## Usage

* Enter a sentence into the text box on the homepage.
* The system predicts sentiment and stores the result in the database.
* View stored predictions on the interface.

## Model Training

The ML model is trained using `sentiment_data.csv` and saved as `sentiment_model.pkl` and `vectorizer.pkl` in the `app` folder.

To retrain the model:

```bash
python retrain_model.py
```

## Author

Liam McAveney

