import math

SKILL_ALIASES = {
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",

    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "stats": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",

    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",
    "jest": "jest",
    "graphql": "graphql",

    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "springboot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",
    "microservices": "microservices",

    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",

    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",
    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",
    "aws": "aws",

    "android": "android",
    "firebase": "firebase",

    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "data structures": "data_structures",
    "competitive programming": "competitive_programming",

    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma",
}

RESUMES = {
    "Arjun Sharma": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
    "Priya Nair": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
    "Rahul Gupta": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
    "Sneha Patel": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib",
    "Vikram Singh": "C++, Algoritms, Data Structure, competitive programming, python",
    "Ananya Krishnan": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD",
    "Karan Mehta": "Python, Sklearn, XGboost, feature engineering, SQL, tableau",
    "Deepika Rao": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma",
    "Aditya Kumar": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest",
    "Meera Iyer": "python, R, statistics, ML, regression, clustering, Power-BI"
}

JDS = {
    "JD-1 — Kakao (ML Engineer)": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics",
    "JD-2 — Naver (Backend Engineer)": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis",
    "JD-3 — Line (Frontend Engineer)": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS"
}

def normalize_skills(skill_string):
    tokens = [x.strip().lower() for x in skill_string.split(",")]

    normalized = []

    for token in tokens:
        if token in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[token])

    return list(set(normalized))

normalized_resumes = {}

for name, skills in RESUMES.items():
    normalized_resumes[name] = normalize_skills(skills)

vocabulary = sorted(
    set(
        skill
        for skills in normalized_resumes.values()
        for skill in skills
    )
)

N = len(RESUMES)

df = {}

for skill in vocabulary:
    df[skill] = sum(
        1 for skills in normalized_resumes.values()
        if skill in skills
    )

idf = {}

for skill in vocabulary:
    idf[skill] = math.log(N / df[skill])

resume_vectors = {}

for name, skills in normalized_resumes.items():
    total_skills = len(skills)

    vector = []

    for skill in vocabulary:
        if skill in skills:
            tf = 1 / total_skills
            vector.append(tf * idf[skill])
        else:
            vector.append(0)

    resume_vectors[name] = vector

def build_jd_vector(jd_skills):
    normalized = normalize_skills(jd_skills)

    vector = []

    for skill in vocabulary:
        vector.append(1 if skill in normalized else 0)

    return vector

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))

    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))

    if mag_a == 0 or mag_b == 0:
        return 0

    return dot / (mag_a * mag_b)

for jd_name, jd_skills in JDS.items():

    jd_vector = build_jd_vector(jd_skills)

    scores = []

    for candidate, vector in resume_vectors.items():
        score = cosine_similarity(vector, jd_vector)
        scores.append((candidate, round(score, 2)))

    scores.sort(key=lambda x: (-x[1], x[0]))

    print(f"\n{jd_name}")

    for name, score in scores[:3]:
        print(f"{name} ({score})")
