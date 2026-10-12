import json
import os
import time
from pathlib import Path

# Collect information about the current Jenkins build
build_number = os.environ.get("BUILD_NUMBER", "unknown")
commit = os.environ.get("GIT_COMMIT", "unknown")

# Build duration measured from the start of our pipeline
start_time = float(os.environ.get("PIPELINE_START_TIME", time.time()))
build_time = round(time.time() - start_time, 2)

# Read test results recorded by the pipeline
results_file = Path("test_results.json")

if results_file.exists():
    results = json.loads(results_file.read_text())
    tests_passed = results.get("tests_passed", 0)
    tests_failed = results.get("tests_failed", 0)
else:
    raise SystemExit("Test results file not found.")

# Collect current build features
build_data = {
    "build_number": build_number,
    "commit": commit,
    "build_time": build_time,
    "tests_passed": tests_passed,
    "tests_failed": tests_failed
}

# Save for the prediction script
Path("current_build_data.json").write_text(
    json.dumps(build_data, indent=4)
)

print("Current Jenkins build data:")
print(json.dumps(build_data, indent=4))
