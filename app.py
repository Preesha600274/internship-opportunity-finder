import streamlit as st
from agent import run_agent
from judge import run_judge

st.set_page_config(
    page_title="Internship Opportunity Finder",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Internship Opportunity Finder")
st.markdown("Find real internship opportunities using AI-powered search")
st.divider()

col1, col2 = st.columns(2)
with col1:
    role = st.text_input("Role / Skill", placeholder="e.g. Python developer, UI/UX designer")
with col2:
    location = st.selectbox("Location", ["remote", "India", "Pune", "Bangalore", "Mumbai", "USA"])

search_btn = st.button("🔍 Find Internships", type="primary", use_container_width=True)

if search_btn:
    if not role.strip():
        st.warning("Please enter a role or skill!")
    else:
        with st.spinner("🔍 Searching for internships..."):
            result = run_agent(role.strip(), location)

        st.success("✅ Search complete!")
        st.subheader("📋 Internship Opportunities")
        st.markdown(result["formatted_output"])
        
        with st.expander("🔗 Raw Sources"):
            for r in result["raw_results"]:
                st.markdown(f"- [{r.get('title','Link')}]({r.get('url','')})")
        
        st.divider()

        with st.spinner("⚖️ Evaluating quality..."):
            judge_result = run_judge(role, location, result["formatted_output"])

        st.subheader("⚖️ LLM-as-Judge Evaluation")
        
        overall = judge_result.get("overall_score", "N/A")
        st.metric("Overall Quality Score", f"{overall} / 5")
        st.info(judge_result.get("summary", ""))

        scores = judge_result.get("scores", {})
        if scores:
            for criterion, data in scores.items():
                label = criterion.replace("_", " ").title()
                score = data.get("score", 0)
                reasoning = data.get("reasoning", "")
                st.markdown(f"**{label}:** {score}/5")
                st.progress(score / 5)
                st.caption(reasoning)

        col1, col2 = st.columns(2)
        with col1:
            st.success(f"✦ **Strength:** {judge_result.get('top_strength', 'N/A')}")
        with col2:
            st.warning(f"△ **Improve:** {judge_result.get('top_improvement', 'N/A')}")

st.divider()
st.caption("Built with Streamlit · Gemini API · Tavily Search")