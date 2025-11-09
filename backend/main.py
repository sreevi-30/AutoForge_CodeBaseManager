# backend/main.py
from backend.orchestrator import Orchestrator

if __name__ == "__main__":
    user_feature = input("Enter a feature request: ")
    orchestrator = Orchestrator()
    orchestrator.run(user_feature)
