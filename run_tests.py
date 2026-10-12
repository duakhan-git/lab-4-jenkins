import json
import sys
import unittest
from pathlib import Path

# Find and run all tests in the project
suite = unittest.defaultTestLoader.discover(
    start_dir=".",
    pattern="test_*.py"
)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Count actual test results
tests_failed = len(result.failures) + len(result.errors)
tests_passed = result.testsRun - tests_failed - len(result.skipped)

# Save results for Jenkins build-data collection
test_data = {
    "tests_passed": tests_passed,
    "tests_failed": tests_failed
}

Path("test_results.json").write_text(
    json.dumps(test_data, indent=4)
)

print("\nTest results saved to test_results.json")
print(json.dumps(test_data, indent=4))

# Fail the Jenkins stage if tests fail
if not result.wasSuccessful():
    sys.exit(1)
