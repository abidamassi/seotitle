import streamlit as st
from openai import OpenAI

# 🔐 Load OpenAI key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🧠 Generate SEO output
def generate_seo(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ using accessible model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=120
    )
    return response.choices[0].message.content.strip()

# 🖼️ Streamlit config
st.set_page_config(page_title="Meta Optimizer AI", page_icon="🔍", layout="centered")

# 🎨 Inline Tailwind-style CSS (white title)
st.markdown("""
    <style>
    body {
        background-color: #F9FAFB;
    }
    .big-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    .subhead {
        font-size: 1.125rem;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    .stTextArea > label, .stRadio > label {
        font-weight: 600;
        color: #374151;
    }
    .footer {
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #9CA3AF;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 📌 Header
st.markdown('<div class="big-title">🔍 Meta Optimizer AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subhead">Learn from competitors and generate SEO-friendly meta titles or descriptions</div>', unsafe_allow_html=True)

# 🧾 Inputs
meta_type = st.radio("What do you want to generate?", ["Meta Title", "Meta Description"])
examples = st.text_area("Paste at least 5 competitor examples (one per line):", height=200)

# 🔁 Generate button
if st.button("Generate Recommendation"):
    lines = [line.strip() for line in examples.split("\n") if line.strip()]
    if len(lines) < 5:
        st.warning("Please input at least 5 examples.")
    else:
        example_summary = "\n".join(f"- {line}" for line in lines)
        limit = "60" if meta_type == "Meta Title" else "160"
        prompt = f"""Based on the following {meta_type.lower()} examples:\n{example_summary}

Analyze the common pattern, length, structure, and keywords. Now generate 1 unique, SEO-friendly {meta_type.lower()} 
that is different from the rest but still follows best SEO practices. Keep it under {limit} characters."""

        with st.spinner("Analyzing and generating..."):
            output = generate_seo(prompt)
            st.success("✅ Here’s your optimized output:")
            st.markdown(f"```text\n{output}\n```")

# 📦 Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit and GPT • © 2025 Meta Optimizer AI</div>', unsafe_allow_html=True)
