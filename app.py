import streamlit as st
from utils import extract_text_from_pdf
from model import get_similarity, extract_skills

st.set_page_config(page_title="AI Resume Screener", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .sub-text {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🤖 AI Resume Screening System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Match your resume with job descriptions instantly</div>', unsafe_allow_html=True)

# Upload section
st.subheader("📄 Upload Resume")
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

st.subheader("📝 Job Description")
job_desc = st.text_area("Paste job description here")

# Analyze button
if st.button("🚀 Analyze Resume"):
    if resume_file and job_desc:
        
        with st.spinner("Analyzing... Please wait ⏳"):
            resume_text = extract_text_from_pdf(resume_file)
            score = get_similarity(resume_text, job_desc)
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_desc)
            missing = list(set(job_skills) - set(resume_skills))

        st.success("Analysis Complete ✅")

        # Score section
        st.subheader("📊 Match Score")
        st.progress(int(score))

        if score > 75:
            st.success(f"🔥 Excellent Match: {score}%")
        elif score > 50:
            st.warning(f"⚡ متوسط Match: {score}%")
        else:
            st.error(f"❌ Low Match: {score}%")

        # Skills section
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Your Skills")
            st.write(resume_skills)

        with col2:
            st.subheader("📌 Required Skills")
            st.write(job_skills)

        # Missing skills
        st.subheader("❌ Missing Skills")
        if missing:
            st.error(missing)
        else:
            st.success("No missing skills 🎉")

    else:
        st.warning("Please upload resume and enter job description")