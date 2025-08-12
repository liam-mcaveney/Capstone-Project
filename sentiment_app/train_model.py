import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load data
df = pd.read_csv("sentiment_data.csv")

X = df["sentence"]
y = df["label"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

# Save both
joblib.dump(model, os.path.join("app", "sentiment_model.pkl"))
joblib.dump(vectorizer, os.path.join("app", "vectorizer.pkl"))

print(" Model retrained and saved.")
