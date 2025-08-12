from flask import Blueprint, render_template, request
from .models import db, SentimentEntry
from .forms import AnalyzeForm
import joblib
import os

main = Blueprint("main", __name__)

# Load model + vectorizer once
MODEL_PATH = os.path.join("app", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join("app", "vectorizer.pkl")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@main.route("/", methods=["GET", "POST"])
def index():
    form = AnalyzeForm()
    prediction = None

    if form.validate_on_submit():
        text = form.text.data.strip()
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]

        new_entry = SentimentEntry(text=text, sentiment=prediction)
        db.session.add(new_entry)
        db.session.commit()

        # Clear the textarea after save
        form.text.data = ""

    history = SentimentEntry.query.order_by(SentimentEntry.id.desc()).limit(10).all()
    return render_template("index.html", form=form, prediction=prediction, history=history)
