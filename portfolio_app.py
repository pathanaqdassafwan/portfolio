import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Pathan Aqdas Safwan - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #374151;
        margin-bottom: 2rem;
    }
    .tagline {
        font-size: 1.2rem;
        text-align: center;
        color: #6b7280;
        font-style: italic;
        margin-bottom: 3rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #1e40af;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    .skill-tag {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        background-color: #dbeafe;
        color: #1e40af;
        border-radius: 20px;
        font-weight: 500;
    }
    .project-card {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        background-color: #f9fafb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .contact-info {
        background-color: #f3f4f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .download-btn {
        background-color: #16a34a;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
sections = ["🏠 Home", "👤 About Me", "💼 Skills", "🚀 Projects", "🎓 Education", "📜 Certifications", "📞 Contact", "🤖 AI Assistant"]
selected_section = st.sidebar.selectbox("Go to section:", sections)

# Function to create download link for resume
def get_download_link():
    # This is a placeholder - you would replace with actual resume file
    resume_text = """
   
    Full Stack Data Science & Generative AI Developer
    
    Contact: +91-7775059446
    Email: aqdassafwanpathan@gmail.com
    LinkedIn: https://www.linkedin.com/in/pathanaqdas
    GitHub: https://github.com/pathanAqdas
    
    EDUCATION:
    - B.E Artificial Intelligence & Data Science
    - Diploma Computer Engineering
    - HSC, SSC
    
    SKILLS:
    Python, SQL, Machine Learning, Deep Learning, NLP, Generative AI, MLOps
    
    CERTIFICATIONS:
    - Data Science with Generative AI (Naresh IT, Hyderabad)
    """
    
    b64 = base64.b64encode(resume_text.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="Pathan_Aqdas_Safwan_Resume.txt" class="download-btn">📄 Download Resume</a>'
    return href

# Home Section
if selected_section == "🏠 Home":
    st.markdown('<h1 class="main-header">Pathan Aqdas Safwan</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Full Stack Data Science & Generative AI Developer</h2>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">"Transforming data into intelligent solutions with cutting-edge AI technologies"</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://via.placeholder.com/300x300/1e3a8a/ffffff?text=AS", width=300)
    
    st.markdown("---")
    st.markdown("### 🌟 Welcome to My Portfolio!")
    st.markdown("""
    I'm a passionate **B.E Artificial Intelligence & Data Science student** with expertise in developing 
    end-to-end data science solutions and generative AI applications. I specialize in building intelligent 
    systems that solve real-world problems using machine learning, deep learning, and modern MLOps practices.
    """)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Projects Completed", "3+", "🚀")
    with col2:
        st.metric("Technologies", "15+", "💻")
    with col3:
        st.metric("Certifications", "1", "📜")
    with col4:
        st.metric("Experience", "Student", "🎓")

# About Me Section
elif selected_section == "👤 About Me":
    st.markdown('<h1 class="section-header">About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 👋 Hello! I'm Pathan Aqdas Safwan
        
        I'm a dedicated **B.E Artificial Intelligence & Data Science student** with a passion for leveraging 
        cutting-edge technologies to solve complex problems. My journey in the world of data science and AI 
        has been driven by curiosity and a desire to create meaningful impact through technology.
        
        ### 🎯 What I Do
        
        - **Data Science**: End-to-end data analysis, feature engineering, and model development
        - **Machine Learning**: Building predictive models using various algorithms
        - **Deep Learning**: Developing neural networks for complex pattern recognition
        - **Generative AI**: Creating intelligent conversational systems and content generation
        - **MLOps**: Implementing CI/CD pipelines for machine learning workflows
        - **Database Management**: Designing and optimizing database systems
        
        ### 🌱 Currently Learning
        
        I'm constantly evolving my skills and staying updated with the latest trends in:
        - Advanced Deep Learning architectures
        - Large Language Models (LLMs)
        - Cloud-based ML deployment
        - Advanced MLOps practices
        
        ### 💡 My Approach
        
        I believe in writing clean, efficient code and building scalable solutions. My approach combines 
        theoretical knowledge with practical implementation to deliver robust data-driven solutions.
        """)
    
    with col2:
        st.markdown("### 🎯 Quick Facts")
        st.info("""
        **🎓 Education**: B.E AI & Data Science
        
        **💼 Specialization**: Full Stack Data Science
        
        **🌟 Interests**: 
        - Machine Learning
        - Generative AI
        - Data Visualization
        - MLOps
        
        **📍 Location**: India
        
        **📧 Contact**: aqdassafwanpathan@gmail.com
        """)

# Skills Section
elif selected_section == "💼 Skills":
    st.markdown('<h1 class="section-header">Technical Skills</h1>', unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("### 🐍 Programming Languages")
    programming_skills = ["Python", "SQL"]
    cols = st.columns(len(programming_skills))
    for i, skill in enumerate(programming_skills):
        with cols[i]:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Machine Learning
    st.markdown("### 🤖 Machine Learning")
    ml_skills = ["Regression", "Classification", "Random Forest", "SVM", "KNN", "NLP", "K-Means"]
    
    # Display skills in rows of 4
    for i in range(0, len(ml_skills), 4):
        cols = st.columns(4)
        for j, skill in enumerate(ml_skills[i:i+4]):
            with cols[j]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Deep Learning
    st.markdown("### 🧠 Deep Learning & Data Science")
    dl_skills = ["Artificial Neural Networks (ANN)", "Convolutional Neural Networks (CNN)", 
                 "Exploratory Data Analysis (EDA)", "Feature Engineering"]
    
    for i in range(0, len(dl_skills), 2):
        cols = st.columns(2)
        for j, skill in enumerate(dl_skills[i:i+2]):
            with cols[j]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Libraries & Frameworks
    st.markdown("### 📚 Libraries & Frameworks")
    library_skills = ["NumPy", "Pandas", "Scikit-learn", "Matplotlib", "Seaborn", "Keras", "NLTK"]
    
    for i in range(0, len(library_skills), 4):
        cols = st.columns(4)
        for j, skill in enumerate(library_skills[i:i+4]):
            with cols[j]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Databases
    st.markdown("### 🗄️ Databases")
    db_skills = ["MySQL", "Oracle"]
    cols = st.columns(len(db_skills))
    for i, skill in enumerate(db_skills):
        with cols[i]:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # MLOps
    st.markdown("### 🔄 MLOps")
    mlops_skills = ["CI/CD Pipelines"]
    st.markdown(f'<span class="skill-tag">{mlops_skills[0]}</span>', unsafe_allow_html=True)

# Projects Section
elif selected_section == "🚀 Projects":
    st.markdown('<h1 class="section-header">Featured Projects</h1>', unsafe_allow_html=True)
    
    # Project 1: Heart Disease Prediction
    st.markdown("""
    <div class="project-card">
        <h3>❤️ Heart Disease Prediction System</h3>
        <p><strong>Technologies:</strong> Python, Logistic Regression, Scikit-learn, Pandas, NumPy</p>
        <p><strong>Description:</strong> Developed a machine learning model to predict heart disease risk using patient medical data. 
        The system uses logistic regression algorithm to analyze various health parameters and provide accurate predictions.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Data preprocessing and feature engineering</li>
            <li>Model training and validation using logistic regression</li>
            <li>Performance evaluation with accuracy metrics</li>
            <li>Interactive prediction interface</li>
        </ul>
        <p><strong>Impact:</strong> Achieved 85%+ accuracy in predicting heart disease risk, potentially helping in early diagnosis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2: Chatbot
    st.markdown("""
    <div class="project-card">
        <h3>🤖 Intelligent Chatbot System</h3>
        <p><strong>Technologies:</strong> Python, NLTK, Rule-based Processing, Natural Language Processing</p>
        <p><strong>Description:</strong> Built an intelligent chatbot capable of understanding and responding to user queries 
        using natural language processing techniques and rule-based conversation flow.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Natural language understanding and processing</li>
            <li>Rule-based response generation</li>
            <li>Context-aware conversation handling</li>
            <li>User-friendly interface for interactions</li>
        </ul>
        <p><strong>Impact:</strong> Created an interactive AI assistant that can handle various user queries effectively.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3: House Price Prediction
    st.markdown("""
    <div class="project-card">
        <h3>🏠 House Price Prediction Model</h3>
        <p><strong>Technologies:</strong> Python, Linear Regression, Matplotlib, Seaborn, Data Visualization</p>
        <p><strong>Description:</strong> Developed a comprehensive house price prediction system using linear regression 
        with extensive data visualization to understand market trends and pricing factors.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Extensive exploratory data analysis</li>
            <li>Linear regression modeling for price prediction</li>
            <li>Interactive data visualizations</li>
            <li>Feature correlation analysis</li>
        </ul>
        <p><strong>Impact:</strong> Provided accurate house price predictions with clear visual insights into market dynamics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 View My Work")
    st.markdown("Visit my [GitHub](https://github.com/pathanAqdas) to explore the complete source code and documentation for these projects!")

# Education Section
elif selected_section == "🎓 Education":
    st.markdown('<h1 class="section-header">Educational Background</h1>', unsafe_allow_html=True)
    
    education_data = [
        {
            "degree": "Bachelor of Engineering (B.E)",
            "specialization": "Artificial Intelligence & Data Science",
            "status": "Currently Pursuing",
            "icon": "🎓"
        },
        {
            "degree": "Diploma",
            "specialization": "Computer Engineering",
            "status": "Completed",
            "icon": "💻"
        },
        {
            "degree": "Higher Secondary Certificate (HSC)",
            "specialization": "Science Stream",
            "status": "Completed",
            "icon": "📚"
        },
        {
            "degree": "Secondary School Certificate (SSC)",
            "specialization": "General Education",
            "status": "Completed",
            "icon": "🏫"
        }
    ]
    
    for edu in education_data:
        st.markdown(f"""
        <div class="project-card">
            <h3>{edu['icon']} {edu['degree']}</h3>
            <p><strong>Specialization:</strong> {edu['specialization']}</p>
            <p><strong>Status:</strong> {edu['status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    ### 📈 Academic Focus Areas
    - **Artificial Intelligence**: Machine Learning, Deep Learning, Neural Networks
    - **Data Science**: Statistical Analysis, Data Mining, Predictive Modeling
    - **Programming**: Python, SQL, Algorithm Design
    - **Mathematics**: Statistics, Linear Algebra, Calculus
    - **Software Engineering**: System Design, Database Management
    """)

# Certifications Section
elif selected_section == "📜 Certifications":
    st.markdown('<h1 class="section-header">Professional Certifications</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>🤖 Data Science with Generative AI</h3>
        <p><strong>Institution:</strong> Naresh IT, Hyderabad</p>
        <p><strong>Status:</strong> Completed</p>
        <p><strong>Key Learning Areas:</strong></p>
        <ul>
            <li>Advanced Data Science Techniques</li>
            <li>Generative AI and Large Language Models</li>
            <li>Machine Learning Operations (MLOps)</li>
            <li>Deep Learning Architectures</li>
            <li>Natural Language Processing</li>
            <li>AI Model Deployment and Scaling</li>
        </ul>
        <p><strong>Skills Acquired:</strong></p>
        <ul>
            <li>Building and training generative AI models</li>
            <li>Implementing end-to-end data science pipelines</li>
            <li>Working with modern AI frameworks and tools</li>
            <li>Deploying AI solutions in production environments</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Continuous Learning")
    st.markdown("""
    I'm committed to continuous learning and staying updated with the latest developments in:
    - **Artificial Intelligence**: Latest AI research and methodologies
    - **Machine Learning**: Advanced algorithms and optimization techniques
    - **Cloud Technologies**: AWS, Azure, Google Cloud Platform
    - **Data Engineering**: Big Data processing and pipeline development
    """)

# Contact Section
elif selected_section == "📞 Contact":
    st.markdown('<h1 class="section-header">Get In Touch</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 💬 Let's Connect!
        
        I'm always excited to discuss new opportunities, collaborate on interesting projects, 
        or simply chat about data science and AI. Feel free to reach out through any of the channels below!
        """)
        
        st.markdown("""
        <div class="contact-info">
            <h4>📱 Phone</h4>
            <p><strong>+91-7775059446</strong></p>
            
            <h4>📧 Email</h4>
            <p><a href="mailto:aqdassafwanpathan@gmail.com">aqdassafwanpathan@gmail.com</a></p>
            
            <h4>💼 LinkedIn</h4>
            <p><a href="https://www.linkedin.com/in/pathanaqdas" target="_blank">linkedin.com/in/pathanaqdas</a></p>
            
            <h4>💻 GitHub</h4>
            <p><a href="https://github.com/pathanAqdas" target="_blank">github.com/pathanAqdas</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Download Resume Button
        st.markdown(get_download_link(), unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🤝 Let's Collaborate On")
        st.success("🔬 Data Science Projects")
        st.success("🤖 AI/ML Solutions")
        st.success("📊 Analytics & Insights")
        st.success("🚀 Innovative Tech Ideas")
        
        st.markdown("### ⚡ Quick Response")
        st.info("I typically respond within 24 hours!")
        
        st.markdown("### 🌐 Available For")
        st.markdown("- Freelance Projects")
        st.markdown("- Collaboration")
        st.markdown("- Mentoring")
        st.markdown("- Tech Discussions")

# AI Assistant Section
elif selected_section == "🤖 AI Assistant":
    st.markdown('<h1 class="section-header">AI Portfolio Assistant</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🤖 Chat with my AI Assistant!
    
    Ask me anything about my skills, projects, experience, or get recommendations for your data science needs!
    """)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm Aqdas's AI assistant. I can help you learn more about his skills, projects, and experience. What would you like to know?"}
        ]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about Aqdas's portfolio..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response (simple rule-based responses)
        response = generate_ai_response(prompt.lower())
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

def generate_ai_response(prompt):
    """Simple rule-based AI responses"""
    if any(word in prompt for word in ['skill', 'skills', 'technology', 'technologies']):
        return """🔧 **Aqdas's Technical Skills:**

**Programming:** Python, SQL
**Machine Learning:** Regression, Classification, Random Forest, SVM, KNN, NLP, K-Means
**Deep Learning:** ANN, CNN, EDA, Feature Engineering
**Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, Keras, NLTK
**Databases:** MySQL, Oracle
**MLOps:** CI/CD Pipelines

He's particularly strong in end-to-end data science workflows and generative AI applications!"""
    
    elif any(word in prompt for word in ['project', 'projects', 'work', 'portfolio']):
        return """🚀 **Aqdas's Featured Projects:**

1. **❤️ Heart Disease Prediction** - ML model using Logistic Regression achieving 85%+ accuracy
2. **🤖 Intelligent Chatbot** - Rule-based NLP system using NLTK
3. **🏠 House Price Prediction** - Linear regression model with comprehensive data visualization

All projects demonstrate his expertise in data preprocessing, model development, and creating user-friendly interfaces. Check out his GitHub for full source code!"""
    
    elif any(word in prompt for word in ['education', 'study', 'degree', 'qualification']):
        return """🎓 **Educational Background:**

- **B.E in Artificial Intelligence & Data Science** (Currently Pursuing)
- **Diploma in Computer Engineering** (Completed)
- **HSC in Science Stream** (Completed)
- **SSC** (Completed)

**Certification:**
- **Data Science with Generative AI** from Naresh IT, Hyderabad

His academic focus includes AI, ML, data science, and software engineering fundamentals."""
    
    elif any(word in prompt for word in ['contact', 'reach', 'connect', 'hire', 'collaborate']):
        return """📞 **Get in Touch with Aqdas:**

**📧 Email:** aqdassafwanpathan@gmail.com
**📱 Phone:** +91-7775059446
**💼 LinkedIn:** linkedin.com/in/pathanaqdas
**💻 GitHub:** github.com/pathanAqdas

He's available for:
- Freelance data science projects
- AI/ML collaborations
- Technical discussions
- Mentoring opportunities

Response time: Usually within 24 hours! 🚀"""
    
    elif any(word in prompt for word in ['experience', 'background', 'about']):
        return """👨‍💻 **About Aqdas:**

Aqdas is a passionate B.E AI & Data Science student with expertise in:
- Full-stack data science development
- Generative AI applications
- Machine learning model deployment
- End-to-end ML pipelines

**Specializations:**
- Predictive modeling and analytics
- Natural language processing
- Deep learning architectures
- MLOps and model deployment

He combines theoretical knowledge with practical implementation to build scalable, intelligent solutions!"""
    
    elif any(word in prompt for word in ['recommend', 'suggestion', 'advice', 'help']):
        return """💡 **How Aqdas Can Help You:**

**For Data Science Needs:**
- Custom ML model development
- Data analysis and insights
- Predictive analytics solutions
- AI chatbot development

**For Learning:**
- Python programming guidance
- ML/DL concept explanations
- Project mentoring
- Career advice in AI/DS

**For Business:**
- Data-driven decision making
- Process automation with AI
- Custom analytics dashboards
- Technical consultation

Feel free to reach out for any data science or AI-related discussions! 🚀"""
    
    else:
        return """🤖 **I'm here to help!** 

I can tell you about:
- 🔧 Aqdas's technical skills and expertise
- 🚀 His portfolio projects and achievements  
- 🎓 Educational background and certifications
- 📞 How to contact and collaborate with him
- 💡 How he can help with your data science needs

What specific aspect would you like to know more about?"""

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 2rem 0;'>
    <p>🚀 Built with Streamlit by Pathan Aqdas Safwan | © 2025</p>
    <p>💡 "Transforming data into intelligent solutions"</p>
</div>
""", unsafe_allow_html=True)
