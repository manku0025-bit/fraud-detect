import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("scam_dataset.csv")

# ✅ Remove missing values
df = df.dropna()

# Features & labels
X = df["message"]
y = df["label"]

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model
pickle.dump((model, vectorizer), open("scam_model.pkl", "wb"))

print("✅ Model trained successfully")