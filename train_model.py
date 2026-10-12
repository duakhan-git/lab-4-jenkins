import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump

# Sample historical build data
data = {
    "build_time": [120, 300, 90, 240],
    "tests_passed": [10, 5, 12, 7],
    "tests_failed": [0, 3, 0, 2],
    "build_success": [1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["build_time", "tests_passed", "tests_failed"]]
y = df["build_success"]

# Split data for training and evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42,
    stratify=y
)

# Train the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2f}")
print("Note: Accuracy is only illustrative because the dataset has 4 records.")

# Train final model using all available data
model.fit(X, y)

# Save the trained model
dump(model, "build_outcome_model.pkl")

print("Machine Learning model trained successfully!")
print("Model saved as build_outcome_model.pkl")
