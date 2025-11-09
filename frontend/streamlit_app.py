# frontend/streamlit_app.py
import streamlit as st
import sys
import os

# Adjust path so Python can find backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.orchestrator import Orchestrator

st.set_page_config(page_title="Autonomous Codebase Manager 🤖", layout="centered")

st.title("🤖 Autonomous Codebase Manager")
st.write("An AI system that plans, codes, tests, reviews, and refactors your software automatically!")

# User input
feature_request = st.text_input("💡 Enter a feature request", placeholder="e.g., Add user login with JWT authentication")

if st.button("🚀 Run Agents"):
    if not feature_request.strip():
        st.warning("Please enter a feature request first.")
    else:
        st.info("Running autonomous workflow... please wait ⏳")

        orchestrator = Orchestrator()
        with st.spinner("AI Agents working..."):
            plan = orchestrator.planner.plan_feature(feature_request)
            st.subheader("🧠 PLAN GENERATED")
            for step in plan["milestones"]:
                st.write(f"- {step}")

            code_output = orchestrator.coder.write_code(plan)
            st.subheader("💻 CODE WRITTEN")
            st.success(code_output)

            test_results = orchestrator.tester.run_tests()
            st.subheader("🧪 TEST RESULTS")
            if "✅" in test_results:
                st.success(test_results)
            else:
                st.error(test_results)

            review_feedback = orchestrator.reviewer.review_code(test_results)
            st.subheader("🔎 REVIEW FEEDBACK")
            st.write(review_feedback)

            refactor_result = orchestrator.refactorer.refactor()
            st.subheader("🧹 REFACTOR RESULT")
            st.success(refactor_result)

        st.success("🎉 Workflow complete!")
        st.balloons()

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and GPT-powered AI Agents.")
