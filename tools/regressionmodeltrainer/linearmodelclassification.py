import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
try:
    df = pd.read_csv("msa_clauses_dataset_v3.csv",encoding='windows-1252')
    df = df.dropna(subset=["label", "text"])
except FileNotFoundError:
    print("Error: The file 'msa_clauses_dataset_v3.csv' was not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: The file 'msa_clauses_dataset_v3.csv' is empty or malformed.")
    exit(1)
except PermissionError:
    print("Error: Permission denied when trying to read 'msa_clauses_dataset_v3.csv'.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred while loading the CSV: {e}")
    exit(1)

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=2000)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

pipeline.fit(X_train, y_train)

# Save the pipeline (vectorizer + model)
joblib.dump(pipeline, "clause_text_classifier.joblib")

# Optional: print test accuracy
print("Test accuracy:", pipeline.score(X_test, y_test))