import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.markdown("""
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
            background-color: #011147; /* rgb(1,17,71) */
        }

        /* Style the selectbox */
        .stSelectbox label {
            font-size: 18px !important;
            font-weight: 600 !important;
        }
        .stSelectbox div[data-baseweb="select"] {
            font-size: 16px !important;
            background-color: #0a1c5a !important;
            border-radius: 8px !important;
            border: 1px solid #4f7cff !important;
            padding: 6px !important;
        }

        /* Style the button */
        .stButton button {
            background-color: #1e40af !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            border: none !important;
            box-shadow: 0px 0px 10px rgba(79,124,255,0.9) !important; /* glowy effect */
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #2563eb !important;
            box-shadow: 0px 0px 20px rgba(79,124,255,1) !important;
            transform: scale(1.05);
        }

        /* Title Styling */
        .css-10trblm {
            font-size: 28px !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)


# === UI Setup ===
st.set_page_config(page_title="🎓 MentorMind")
st.title("🎓 MentorMind")
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
