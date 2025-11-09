# backend/agents/tester.py
import random

class TestingAgent:
    def __init__(self):
        self.role = "Testing Agent"

    @staticmethod
    def run_tests():
        """
        Simulate running test cases.
        """
        print("\n🧪 Running tests...")
        # For now, just simulate success/failure
        success = random.choice([True, True, True, False])
        if success:
            return "✅ All tests passed successfully!"
        else:
            return "❌ Some tests failed! Please check your code."
