# backend/agents/planner.py

class PlanningAgent:
    def __init__(self):
        self.role = "Planner Agent"

    @staticmethod
    def plan_feature(feature_request: str) -> dict:
        """
        Takes user input and returns a development plan.
        """
        plan = {
            "feature": feature_request,
            "milestones": [
                f"Analyze requirements for: {feature_request}",
                f"Design architecture for: {feature_request}",
                f"Implement core functionality for: {feature_request}",
                f"Write test cases for: {feature_request}",
                f"Review and refactor code for: {feature_request}"
            ],
            "files_to_create": ["main_feature.py", "test_main_feature.py"]
        }
        return plan
