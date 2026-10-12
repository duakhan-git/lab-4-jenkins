import pandas as pd
from joblib import load

# Load the trained Machine Learning model
model = load("build_outcome_model.pkl")

# Example Jenkins build data
new_build = pd.DataFrame({
    "build_time": [150],
    "tests_passed": [10],
    "tests_failed": [0]
})

# Predict build outcome
prediction = model.predict(new_build)

if prediction[0] == 1:
    print("Prediction: Build will be SUCCESSFUL")
else:
    print("Prediction: Build may FAIL")
