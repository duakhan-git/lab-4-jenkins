import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Sample historical Jenkins build data
data = {
    "build_time": [120, 300, 90, 240],
    "tests_passed": [10, 5, 12, 7],
    "tests_failed": [0, 3, 0, 2],
    "build_success": [1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Features and target
X = df[["build_time", "tests_passed", "tests_failed"]]
y = df["build_success"]

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save trained model
dump(model, "build_outcome_model.pkl")

print("Machine Learning model trained successfully!")
print("Model saved as build_outcome_model.pkl")
