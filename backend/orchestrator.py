# backend/orchestrator.py
from backend.agents.planner import PlanningAgent
from backend.agents.coder import CodingAgent
from backend.agents.tester import TestingAgent
from backend.agents.reviewer import ReviewerAgent
from backend.agents.refactorer import RefactorerAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlanningAgent()
        self.coder = CodingAgent()
        self.tester = TestingAgent()
        self.reviewer = ReviewerAgent()
        self.refactorer = RefactorerAgent()

    def run(self, user_input: str):
        print("🤖 Starting AI Workflow...\n")

        # Step 1: Plan feature
        plan = self.planner.plan_feature(user_input)
        print("🧠 PLAN GENERATED:")
        for step in plan["milestones"]:
            print(f"   - {step}")

        # Step 2: Code
        code_output = self.coder.write_code(plan)
        print(f"\n💻 CODE WRITTEN: {code_output}")

        # Step 3: Test
        test_results = self.tester.run_tests()
        print(test_results)

        # Step 4: Review
        review_feedback = self.reviewer.review_code(test_results)
        print(review_feedback)

        # Step 5: Refactor
        refactor_result = self.refactorer.refactor()
        print(refactor_result)

        print("\n✅ Process complete.")
