import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


# === Custom CSS Styling ===
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Heading animation */
    h1 {
        text-align: center;
        color: white !important;
        font-size: 3rem !important;
        animation: fadeInDown 1s ease-in-out;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Glassmorphism effect for main blocks */
    .block-container {
        background: rgba(255, 255, 255, 0.15);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }

    /* Buttons */
    div.stButton > button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #ff4757;
        transform: scale(1.05);
    }

    /* Selectbox & Slider styling */
    .stSelectbox, .stSlider {
        font-size: 1.1rem !important;
    }

    /* Subheader text */
    h3 {
        color: #2c3e50 !important;
        font-weight: bold;
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
