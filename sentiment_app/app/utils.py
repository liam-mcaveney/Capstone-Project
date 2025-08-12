import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "sentiment_model.pkl")
vec_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vec_path)

def analyze_sentiment(text):
    X_input = vectorizer.transform([text])
    prediction = model.predict(X_input)[0]

    if isinstance(prediction, (int, float)):
        sentiment = "Positive" if prediction == 1 else "Negative"
    else:
        sentiment = str(prediction).capitalize()

    return sentiment, "Custom AI"
