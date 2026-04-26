from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(resume_text, job_desc):
    if not resume_text or not job_desc:
        return 0
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    
    similarity = cosine_similarity(vectors[0], vectors[1])
    
    return round(similarity[0][0] * 100, 2)


skills_list = [
    "python", "machine learning", "deep learning",
    "nlp", "data analysis", "sql", "pandas",
    "numpy", "tensorflow", "pytorch"
]

def extract_skills(text):
    found_skills = []
    text = text.lower()
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
            
    return found_skills