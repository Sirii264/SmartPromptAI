import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="🌸 SmartPrompt AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- LOAD API ----------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:#F8F9FC;
}

/* Title */

.title{
font-size:52px;
font-weight:700;
text-align:center;
color:#6C63FF;
margin-bottom:0;
}

.subtitle{
text-align:center;
font-size:18px;
color:#777;
margin-bottom:30px;
}

/* Card */

.card{
background:white;
padding:28px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
margin-bottom:20px;
}

/* Response */

.response{
background:white;
padding:30px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
border-left:8px solid #CDB4DB;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#EEF2FF;
}

/* Button */

.stButton>button{
width:100%;
background:#B8C0FF;
color:white;
border-radius:15px;
border:none;
padding:12px;
font-size:18px;
font-weight:bold;
transition:0.3s;
}

.stButton>button:hover{
background:#A0A8FF;
}

/* Selectbox */

div[data-baseweb="select"]{
border-radius:15px;
}

/* Text Area */

textarea{
border-radius:15px !important;
}

</style>
""",unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🌸 SmartPrompt AI")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👋 Welcome")

st.sidebar.success(
"""
Ask any question and receive responses in different styles.

✨ Simple

📚 Student

🧠 Detailed

📝 Exam

💼 Interview

⚡ Summary

👶 Explain Like I'm 10
"""
)

st.sidebar.markdown("---")

st.sidebar.info("💡 Prompt Engineering Project")

st.sidebar.markdown("---")

st.sidebar.caption("❤️ Developed by Sridevi Siri")

# ---------------- HEADER ----------------

st.markdown('<div class="title">🤖 SmartPrompt AI</div>',unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Ask Anything • Learn Better • Personalized AI Assistant</div>',
unsafe_allow_html=True)

# ---------------- INPUT ----------------

st.markdown('<div class="card">',unsafe_allow_html=True)

question = st.text_area(
"📝 Enter Your Question",
placeholder="""
Examples

• How is wool made?

• Explain Artificial Intelligence

• Write a leave letter

• Difference between RAM and ROM

• Tell me a joke
""",
height=180
)

mode = st.selectbox(
"🎯 Choose Response Style",
[
"😊 Simple",
"📚 Student",
"🧠 Detailed",
"📝 Exam",
"💼 Interview",
"⚡ Summary",
"👶 Explain Like I'm 10"
]
)

generate = st.button("✨ Generate Response", key="generate_btn")
st.markdown("</div>",unsafe_allow_html=True)

if generate:

    if question.strip() == "":
        st.warning("⚠ Please enter a question.")
        st.stop()

    # ---------------- PROMPTS ----------------

    if mode == "😊 Simple":

        prompt = f"""
You are a friendly AI assistant.

Question:
{question}

Instructions:
- Answer ONLY the user's question.
- Use simple English.
- Keep it concise.
- Use bullet points where appropriate.
- Use emojis naturally.
- Give a simple example if relevant.
- Do NOT add unnecessary sections.
- Format nicely using Markdown.
"""

    elif mode == "📚 Student":

        prompt = f"""
Question:
{question}

Explain for a college student.

Rules:
- Use headings if needed.
- Use bullet points.
- Include examples.
- Make it easy to understand.
- Only include relevant information.
"""

    elif mode == "🧠 Detailed":

        prompt = f"""
Question:
{question}

Give a detailed explanation.

Rules:
- Use Markdown.
- Use headings only if relevant.
- Use bullet points.
- Add examples wherever useful.
- If the topic has steps, show the steps.
- If advantages exist, include them.
- If they don't exist, don't invent them.
- Never force the same template for every question.
"""

    elif mode == "📝 Exam":

        prompt = f"""
Question:
{question}

Answer like a university exam.

Use:
- Definition (only if applicable)
- Point-wise explanation
- Key points
- Examples
- Conclusion

Easy to remember.
"""

    elif mode == "💼 Interview":

        prompt = f"""
Question:
{question}

Explain as if preparing someone for an interview.

Include:
- Main concept
- Important points
- Common interview questions if relevant.
"""

    elif mode == "⚡ Summary":

        prompt = f"""
Question:
{question}

Summarize in 5-6 bullet points.

Keep it short.
"""

    else:

        prompt = f"""
Question:
{question}

Explain like I'm 10 years old.

Use very easy English.

Give a fun example.

Use emojis.
"""

    # ---------------- GENERATE ----------------

    with st.spinner("🤖 SmartPrompt AI is thinking..."):

        response = model.generate_content(prompt)

    st.markdown('<div class="response">', unsafe_allow_html=True)

    st.markdown("## 💬 Response")

    st.markdown(response.text)

    st.markdown("</div>", unsafe_allow_html=True)
