import json
import pandas as pd
from joblib import load
from pathlib import Path

# Load the trained model
model = load("build_outcome_model.pkl")

# Read actual Jenkins build information
data_file = Path("current_build_data.json")

if not data_file.exists():
    raise SystemExit("Current Jenkins build data not found.")

build_data = json.loads(data_file.read_text())

# Prepare features for prediction
new_build = pd.DataFrame({
    "build_time": [build_data["build_time"]],
    "tests_passed": [build_data["tests_passed"]],
    "tests_failed": [build_data["tests_failed"]]
})

# Predict build outcome
prediction = model.predict(new_build)

print("Jenkins Build Number:", build_data["build_number"])
print("Git Commit:", build_data["commit"])
print("Build Duration:", build_data["build_time"], "seconds")
print("Tests Passed:", build_data["tests_passed"])
print("Tests Failed:", build_data["tests_failed"])

if prediction[0] == 1:
    print("Predicted Build Outcome: SUCCESS")
else:
    print("Predicted Build Outcome: FAILURE")
