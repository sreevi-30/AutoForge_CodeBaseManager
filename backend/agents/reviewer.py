# backend/agents/reviewer.py

class ReviewerAgent:
    def __init__(self):
        self.role = "Reviewer Agent"

    @staticmethod
    def review_code(test_results: str):
        """
        Reviews code quality based on test results.
        """
        print("\n🔎 Reviewing code...")
        if "✅" in test_results:
            return "👍 Code looks clean and tests passed. Approved for refactoring."
        else:
            return "⚠️ Code needs improvements before merging."
