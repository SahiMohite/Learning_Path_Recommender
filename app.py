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
      background-color: #1e3a8a; /* Navy blue */
      border-radius: 100px;
      box-shadow: rgba(30, 58, 138, .2) 0 -25px 18px -14px inset,
                  rgba(30, 58, 138, .15) 0 1px 2px,
                  rgba(30, 58, 138, .15) 0 2px 4px,
                  rgba(30, 58, 138, .15) 0 4px 8px,
                  rgba(30, 58, 138, .15) 0 8px 16px,
                  rgba(30, 58, 138, .15) 0 16px 32px;
      color: white;
      cursor: pointer;
      display: inline-block;
      font-family: 'Poppins', -apple-system, system-ui, Roboto, sans-serif;
      padding: 10px 24px;
      text-align: center;
      text-decoration: none;
      transition: all 250ms;
      border: 0;
      font-size: 16px;
      font-weight: 600;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }

    .stButton button:hover {
      box-shadow: rgba(30, 58, 138, .35) 0 -25px 18px -14px inset,
                  rgba(30, 58, 138, .25) 0 1px 2px,
                  rgba(30, 58, 138, .25) 0 2px 4px,
                  rgba(30, 58, 138, .25) 0 4px 8px,
                  rgba(30, 58, 138, .25) 0 8px 16px,
                  rgba(30, 58, 138, .25) 0 16px 32px;
      transform: scale(1.05) rotate(-1deg);
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
