# backend/agents/coder.py
import os

class CodingAgent:
    def __init__(self):
        self.role = "Coding Agent"

    @staticmethod
    def write_code(plan: dict):
        """
        Takes a plan and creates simple code files.
        """
        feature = plan["feature"]
        files = plan["files_to_create"]

        os.makedirs("generated_code", exist_ok=True)
        for file in files:
            filepath = os.path.join("generated_code", file)
            with open(filepath, "w") as f:
                if file.startswith("test_"):
                    f.write(f"# Auto-generated test file for {feature}\n")
                    f.write("def test_example():\n    assert True\n")
                else:
                    f.write(f"# Auto-generated code for {feature}\n")
                    f.write("def main_feature():\n    print('Feature executed successfully!')\n")

        return f"✅ {len(files)} files created in /generated_code"
