from app import create_app, db
from app.models import SentimentEntry
import joblib
import os

# Load model and vectorizer using joblib
MODEL_PATH = os.path.join('app', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join('app', 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Sample inputs to classify and store
sample_texts = [
    "This app is amazing and really easy to use!",
    "I hate how slow the interface is sometimes.",
    "It's okay, not bad but not great either.",
    "Absolutely love the new features!",
    "The latest update broke everything.",
    "This tool saves me so much time at work.",
    "I don’t find this very helpful anymore."
]

def populate():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        for text in sample_texts:
            X = vectorizer.transform([text])
            prediction = model.predict(X)[0]
            entry = SentimentEntry(text=text, sentiment=prediction)
            db.session.add(entry)

        db.session.commit()
        print("Database has been populated.")

if __name__ == '__main__':
    populate()
