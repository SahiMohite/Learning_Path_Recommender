import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI Setup ===
st.set_page_config(page_title="🎓 Learning Path Recommender")
st.title("🎓 Learning‑Path Recommender")
st.write("Select your preferences and get a personalized study roadmap.")

# === Input Sliders and Selects ===
field = st.selectbox("📘 Choose a Domain", ["Data Science", "Web Development", "AI/ML", "Finance", "Cybersecurity", "Blockchain", "Design"])

experience = st.selectbox("📊 Your Current Level", ["Beginner", "Intermediate", "Advanced"])

learning_style = st.selectbox("🧠 Preferred Style", ["Project-based", "Theory-focused", "Balanced"])

time_per_week = st.slider("🕒 Hours you can study per week", 1, 40, 8)

# === Generate Button ===
if st.button("Recommend My Learning Path"):
    with st.spinner("Building your learning roadmap..."):
        prompt = f"""
Act as a learning path engine.

Based on the following user profile:
- Domain: {field}
- Experience Level: {experience}
- Preferred Learning Style: {learning_style}
- Weekly Time Commitment: {time_per_week} hours

Generate a learning path with 4–6 progressive stages. Each stage should include the goal, key topics, and type of resources (e.g. video, course, hands-on). Keep the output easy to follow.
"""
        response = model.generate_content(prompt)
        st.subheader("🧭 Recommended Learning Path")
        st.markdown(response.text.strip())