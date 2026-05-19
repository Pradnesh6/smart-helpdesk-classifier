import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
data = pd.read_csv("tickets.csv")

# Create machine learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train the model
model.fit(data["text"], data["category"])

# Save the trained model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")