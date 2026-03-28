"""
Career Coach Pro - Streamlit Web App
=====================================
Your Personal Career Agency, now in the browser.
Built by Ayesha Shimu
"""

import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Career Coach Pro",
    page_icon="🚀",
    layout="wide"
)

# ============================================================
# CUSTOM STYLING
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global overrides */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #f1f5f9 !important;
    }
    section[data-testid="stSidebar"] label {
        color: #94a3b8 !important;
        font-weight: 500;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }
    section[data-testid="stSidebar"] .stCaption p {
        color: #64748b !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: #334155;
    }

    /* Hero section */
    .hero-container {
        text-align: center;
        padding: 3rem 1rem 1.5rem 1rem;
    }
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        padding: 6px 16px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0f172a, #334155);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        margin-top: 0;
        font-weight: 400;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 28px 24px;
        transition: all 0.25s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        height: 100%;
    }
    .feature-card:hover {
        border-color: #c7d2fe;
        box-shadow: 0 8px 24px rgba(99,102,241,0.1);
        transform: translateY(-2px);
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 12px;
        display: block;
    }
    .feature-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 0.88rem;
        color: #64748b;
        line-height: 1.6;
    }

    /* Result boxes */
    .result-box {
        background: linear-gradient(135deg, #f8faff, #eef2ff);
        border: 1px solid #c7d2fe;
        padding: 22px;
        border-radius: 14px;
        margin: 15px 0;
        font-size: 0.95rem;
        line-height: 1.75;
    }
    .tone-box {
        background-color: #f8fafc;
        border-left: 4px solid #6366f1;
        padding: 15px 20px;
        border-radius: 0 10px 10px 0;
        margin: 10px 0;
    }
    .tip-box {
        background: linear-gradient(135deg, #fffbeb, #fef3c7);
        border-left: 4px solid #f59e0b;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 12px 0;
        font-size: 0.9rem;
    }
    .copy-text {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 22px;
        border-radius: 12px;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 0.93rem;
        line-height: 1.85;
        white-space: pre-wrap;
    }
    .score-card {
        background: white;
        border: 1px solid #e2e8f0;
        padding: 18px;
        border-radius: 14px;
        margin: 8px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    /* CTA box */
    .cta-box {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        text-align: center;
        padding: 2rem;
        border-radius: 16px;
        margin-top: 2rem;
    }
    .cta-box h3 {
        color: white !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .cta-box p {
        color: #e0e7ff;
        font-size: 0.95rem;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #f1f5f9;
        padding: 4px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        font-weight: 500;
        font-size: 0.9rem;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background: white !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }

    /* Sidebar profile badge */
    .profile-badge {
        background: linear-gradient(135deg, #059669, #10b981);
        color: white;
        padding: 12px 16px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1rem;
    }
    .profile-badge .name {
        font-weight: 700;
        font-size: 1.05rem;
    }
    .profile-badge .detail {
        font-size: 0.8rem;
        opacity: 0.9;
        margin-top: 4px;
    }

    /* Footer */
    .app-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.78rem;
        padding: 2rem 0 1rem 0;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA
# ============================================================
CAREER_FIELDS = [
    "Data Analytics", "AI / Machine Learning", "Business Intelligence",
    "Digital Marketing", "Product Management", "UX Design / Research",
    "Software Development", "Project Management", "Finance / Accounting",
    "Supply Chain / Operations", "Human Resources", "Sales / Business Development"
]

TONES = {
    "Friendly & Warm": {
        "description": "Approachable, conversational, like talking to a supportive friend",
        "opening_words": ["I", "My journey", "What excites me", "I love"],
        "closers": ["Always happy to connect!", "Let's chat!", "Feel free to reach out!"],
        "power_words": ["passionate about", "genuinely excited", "love working with", "fascinated by"],
        "cv_tone": "warm but professional",
        "cover_letter_style": "enthusiastic and personable"
    },
    "Humanised & Real": {
        "description": "Honest, authentic, sounds like a real person wrote it (not AI)",
        "opening_words": ["Honestly", "Here's the thing", "I'll be real", "Truth is"],
        "closers": ["Hit me up if you relate.", "DMs always open.", "If this resonates, let's connect."],
        "power_words": ["figured out", "stumbled into", "taught myself", "actually enjoy"],
        "cv_tone": "authentic and grounded",
        "cover_letter_style": "honest and relatable"
    },
    "Professional & Polished": {
        "description": "Corporate-ready, structured, ideal for traditional industries",
        "opening_words": ["With a background in", "As a", "Having developed", "Drawing on"],
        "closers": ["I welcome the opportunity to connect.", "Open to professional discussions."],
        "power_words": ["demonstrated expertise in", "proven ability to", "proficient in"],
        "cv_tone": "formal and structured",
        "cover_letter_style": "formal and polished"
    },
    "Confident & Bold": {
        "description": "Strong, assertive, shows you know your worth",
        "opening_words": ["I build", "I turn", "I help", "I specialise in"],
        "closers": ["Ready to bring this energy to your team.", "Let's make things happen."],
        "power_words": ["expert at", "specialise in", "deliver results with", "drive impact through"],
        "cv_tone": "assertive and results-focused",
        "cover_letter_style": "bold and direct"
    },
    "Creative & Storytelling": {
        "description": "Narrative-driven, engaging, makes people want to keep reading",
        "opening_words": ["It started with", "Somewhere between", "Picture this", "Three years ago"],
        "closers": ["The next chapter? That's where you come in.", "The story continues..."],
        "power_words": ["discovered a passion for", "fell in love with", "found my calling in"],
        "cv_tone": "narrative and engaging",
        "cover_letter_style": "story-driven and compelling"
    }
}

FIELD_DATA = {
    "Data Analytics": {
        "technical_skills": ["Python", "SQL", "Excel", "Tableau", "Power BI", "R", "Statistics", "Google Sheets"],
        "soft_skills": ["Storytelling with data", "Problem solving", "Critical thinking", "Communication", "Attention to detail"],
        "certifications": ["Google Data Analytics Certificate", "IBM Data Analyst", "Microsoft Power BI", "Tableau Desktop Specialist"],
        "keywords": ["data-driven", "insights", "analytics", "visualization", "reporting", "KPIs", "dashboards"],
        "avg_salary_gbp": {"Entry Level": 28000, "Mid Level": 45000, "Senior": 65000},
        "job_titles": ["Data Analyst", "Junior Data Analyst", "Business Data Analyst", "Analytics Consultant", "Reporting Analyst"],
        "interview_topics": ["SQL queries", "Data cleaning scenarios", "Dashboard design", "Stakeholder communication", "A/B testing basics"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Birmingham", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Copenhagen", "Dublin", "Stockholm"],
        "demand_level": "Very High", "remote_friendly": "High"
    },
    "AI / Machine Learning": {
        "technical_skills": ["Python", "TensorFlow", "PyTorch", "SQL", "Machine Learning", "NLP", "Deep Learning", "Statistics"],
        "soft_skills": ["Research mindset", "Problem solving", "Adaptability", "Communication", "Curiosity"],
        "certifications": ["Google AI Essentials", "DeepLearning.AI Specialization", "Stanford ML Course", "AWS ML Specialty"],
        "keywords": ["AI", "machine learning", "automation", "neural networks", "models", "predictions", "NLP"],
        "avg_salary_gbp": {"Entry Level": 35000, "Mid Level": 55000, "Senior": 85000},
        "job_titles": ["ML Engineer", "AI Engineer", "Data Scientist", "NLP Engineer", "AI Research Analyst"],
        "interview_topics": ["Algorithm design", "Model evaluation metrics", "Feature engineering", "Bias in AI", "System design"],
        "top_cities_uk": ["London", "Cambridge", "Edinburgh", "Manchester", "Bristol"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Zurich", "Stockholm", "Copenhagen"],
        "demand_level": "Very High", "remote_friendly": "High"
    },
    "Business Intelligence": {
        "technical_skills": ["SQL", "Power BI", "Tableau", "Excel", "DAX", "ETL", "Data Warehousing", "SSRS"],
        "soft_skills": ["Business acumen", "Stakeholder management", "Presentation skills", "Analytical thinking"],
        "certifications": ["Microsoft PL-300", "Tableau Desktop Specialist", "Google BI Certificate"],
        "keywords": ["BI", "dashboards", "reporting", "data warehouse", "business insights", "KPIs", "ETL"],
        "avg_salary_gbp": {"Entry Level": 30000, "Mid Level": 48000, "Senior": 70000},
        "job_titles": ["BI Analyst", "BI Developer", "BI Consultant", "Reporting Analyst", "Data Engineer"],
        "interview_topics": ["Data modelling", "Dashboard best practices", "SQL optimization", "Business requirements gathering"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Leeds", "Edinburgh"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Dublin", "Copenhagen", "Munich"],
        "demand_level": "High", "remote_friendly": "Medium"
    },
    "Digital Marketing": {
        "technical_skills": ["Google Analytics", "SEO", "SEM", "Social Media Tools", "A/B Testing", "CRM", "Email Marketing"],
        "soft_skills": ["Creativity", "Communication", "Trend analysis", "Copywriting", "Strategic thinking"],
        "certifications": ["Google Digital Marketing", "HubSpot Inbound", "Meta Marketing Analytics", "Google Ads"],
        "keywords": ["campaigns", "conversion", "engagement", "ROI", "content strategy", "growth", "SEO"],
        "avg_salary_gbp": {"Entry Level": 24000, "Mid Level": 38000, "Senior": 55000},
        "job_titles": ["Digital Marketing Executive", "SEO Specialist", "Content Marketer", "Growth Marketer", "Marketing Analyst"],
        "interview_topics": ["Campaign strategy", "SEO fundamentals", "Analytics interpretation", "Content planning", "Budget allocation"],
        "top_cities_uk": ["London", "Manchester", "Bristol", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Barcelona", "Dublin", "Stockholm"],
        "demand_level": "High", "remote_friendly": "Very High"
    },
    "Product Management": {
        "technical_skills": ["Jira", "SQL", "A/B Testing", "Figma", "Roadmapping", "Analytics Tools", "Miro"],
        "soft_skills": ["Leadership", "Prioritization", "User empathy", "Cross-functional collaboration", "Decision making"],
        "certifications": ["Google PM Certificate", "Pragmatic Institute", "Product School", "Scrum Product Owner"],
        "keywords": ["product strategy", "user needs", "roadmap", "agile", "stakeholders", "MVP", "backlog"],
        "avg_salary_gbp": {"Entry Level": 35000, "Mid Level": 55000, "Senior": 80000},
        "job_titles": ["Associate PM", "Product Manager", "Product Owner", "Technical PM", "Senior PM"],
        "interview_topics": ["Product sense", "Prioritization frameworks", "Metrics definition", "User stories", "Go-to-market strategy"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Cambridge", "Bristol"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Stockholm", "Dublin", "Copenhagen"],
        "demand_level": "High", "remote_friendly": "High"
    },
    "UX Design / Research": {
        "technical_skills": ["Figma", "User Interviews", "Surveys", "Usability Testing", "Wireframing", "Prototyping"],
        "soft_skills": ["Empathy", "Active listening", "Communication", "Pattern recognition", "Visual thinking"],
        "certifications": ["Google UX Design", "Nielsen Norman Group", "Interaction Design Foundation"],
        "keywords": ["user experience", "research", "usability", "user needs", "design thinking", "wireframes"],
        "avg_salary_gbp": {"Entry Level": 28000, "Mid Level": 42000, "Senior": 60000},
        "job_titles": ["UX Researcher", "UX Designer", "UI/UX Designer", "Product Designer", "Design Researcher"],
        "interview_topics": ["Portfolio walkthrough", "Research methodology", "Design critique", "Accessibility", "User testing scenarios"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Bristol", "Brighton"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Copenhagen", "Stockholm", "Barcelona"],
        "demand_level": "Medium", "remote_friendly": "High"
    },
    "Software Development": {
        "technical_skills": ["Python", "JavaScript", "Git", "HTML/CSS", "APIs", "Databases", "React", "Node.js"],
        "soft_skills": ["Problem solving", "Debugging mindset", "Collaboration", "Continuous learning", "Communication"],
        "certifications": ["freeCodeCamp", "CS50", "AWS Cloud Practitioner", "Meta Front-End Developer"],
        "keywords": ["development", "code", "full-stack", "applications", "APIs", "deployment", "agile"],
        "avg_salary_gbp": {"Entry Level": 30000, "Mid Level": 50000, "Senior": 75000},
        "job_titles": ["Junior Developer", "Software Engineer", "Front-End Developer", "Full-Stack Developer", "Backend Developer"],
        "interview_topics": ["Coding challenges", "System design", "Data structures", "API design", "Version control"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Bristol", "Cambridge"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Stockholm", "Dublin", "Copenhagen"],
        "demand_level": "Very High", "remote_friendly": "Very High"
    },
    "Project Management": {
        "technical_skills": ["Jira", "Asana", "MS Project", "Excel", "Gantt Charts", "Agile", "Scrum", "Confluence"],
        "soft_skills": ["Leadership", "Communication", "Risk management", "Time management", "Negotiation"],
        "certifications": ["PMP", "PRINCE2", "Google PM Certificate", "Scrum Master", "Agile Certified"],
        "keywords": ["project delivery", "stakeholders", "timeline", "budget", "agile", "milestones", "risk"],
        "avg_salary_gbp": {"Entry Level": 28000, "Mid Level": 45000, "Senior": 65000},
        "job_titles": ["Project Coordinator", "Project Manager", "Scrum Master", "Programme Manager", "PMO Analyst"],
        "interview_topics": ["Conflict resolution", "Risk mitigation", "Stakeholder management", "Agile vs Waterfall", "Budget tracking"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Dublin", "Berlin", "Copenhagen", "Munich"],
        "demand_level": "High", "remote_friendly": "Medium"
    },
    "Finance / Accounting": {
        "technical_skills": ["Excel", "Financial Modelling", "SAP", "QuickBooks", "Power BI", "SQL", "VBA"],
        "soft_skills": ["Attention to detail", "Analytical thinking", "Ethics", "Communication", "Numeracy"],
        "certifications": ["ACCA", "CIMA", "CFA", "AAT", "Xero Advisor"],
        "keywords": ["financial analysis", "budgeting", "forecasting", "reporting", "audit", "compliance", "P&L"],
        "avg_salary_gbp": {"Entry Level": 26000, "Mid Level": 42000, "Senior": 65000},
        "job_titles": ["Financial Analyst", "Accountant", "Management Accountant", "Audit Associate", "Finance Manager"],
        "interview_topics": ["Financial statement analysis", "Budgeting scenarios", "Regulatory knowledge", "Excel proficiency", "Ethics"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Birmingham", "Bristol"],
        "top_cities_eu": ["Dublin", "Amsterdam", "Frankfurt", "Zurich", "Luxembourg"],
        "demand_level": "High", "remote_friendly": "Medium"
    },
    "Supply Chain / Operations": {
        "technical_skills": ["Excel", "SAP", "ERP Systems", "SQL", "Power BI", "Lean Six Sigma", "Forecasting"],
        "soft_skills": ["Problem solving", "Negotiation", "Process improvement", "Communication", "Adaptability"],
        "certifications": ["CSCP (APICS)", "Lean Six Sigma Green Belt", "CILT", "CIPS"],
        "keywords": ["logistics", "procurement", "inventory", "optimization", "supply chain", "operations", "efficiency"],
        "avg_salary_gbp": {"Entry Level": 26000, "Mid Level": 40000, "Senior": 60000},
        "job_titles": ["Supply Chain Analyst", "Operations Coordinator", "Procurement Specialist", "Logistics Manager", "Demand Planner"],
        "interview_topics": ["Process optimization", "Vendor management", "Inventory challenges", "ERP experience", "Cost reduction"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Leeds", "Liverpool"],
        "top_cities_eu": ["Amsterdam", "Copenhagen", "Hamburg", "Rotterdam", "Dublin"],
        "demand_level": "Medium", "remote_friendly": "Low"
    },
    "Human Resources": {
        "technical_skills": ["HRIS Systems", "Excel", "Workday", "BambooHR", "LinkedIn Recruiter", "ATS"],
        "soft_skills": ["Empathy", "Communication", "Conflict resolution", "Discretion", "Organisational skills"],
        "certifications": ["CIPD", "SHRM", "HRCI", "LinkedIn Talent Solutions"],
        "keywords": ["talent", "recruitment", "employee engagement", "people operations", "culture", "DEI", "onboarding"],
        "avg_salary_gbp": {"Entry Level": 24000, "Mid Level": 38000, "Senior": 55000},
        "job_titles": ["HR Coordinator", "Recruiter", "HR Business Partner", "People Operations", "Talent Acquisition"],
        "interview_topics": ["Employment law basics", "Handling difficult conversations", "DEI initiatives", "Recruitment strategies"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Dublin", "Berlin", "Copenhagen", "Stockholm"],
        "demand_level": "Medium", "remote_friendly": "Medium"
    },
    "Sales / Business Development": {
        "technical_skills": ["Salesforce", "HubSpot", "Excel", "LinkedIn Sales Navigator", "CRM Tools", "Cold Email Tools"],
        "soft_skills": ["Persuasion", "Relationship building", "Resilience", "Active listening", "Negotiation"],
        "certifications": ["HubSpot Sales", "Salesforce Administrator", "LinkedIn Sales Navigator"],
        "keywords": ["revenue", "pipeline", "B2B", "prospecting", "closing", "targets", "client relationships"],
        "avg_salary_gbp": {"Entry Level": 25000, "Mid Level": 40000, "Senior": 60000},
        "job_titles": ["Sales Executive", "BDR", "Account Executive", "Sales Manager", "Business Development Manager"],
        "interview_topics": ["Sales pitch practice", "Objection handling", "Pipeline management", "CRM proficiency", "Target achievement"],
        "top_cities_uk": ["London", "Manchester", "Bristol", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Dublin", "Amsterdam", "Berlin", "Stockholm", "Copenhagen"],
        "demand_level": "High", "remote_friendly": "Medium"
    }
}

EXPERIENCE_REFRAMES = {
    "Supply Chain": [
        ("Managed inventory", "Tracked and analysed inventory data to identify patterns and reduce waste"),
        ("Coordinated logistics", "Optimised logistics workflows using data-driven decision making"),
        ("Worked with vendors", "Managed vendor performance metrics and compliance dashboards"),
        ("Procurement tasks", "Analysed procurement data to forecast demand and negotiate better terms")
    ],
    "Finance": [
        ("Financial reporting", "Built financial models and analysed trends across large datasets"),
        ("Budgeting", "Created budget forecasts using quantitative analysis and reporting tools"),
        ("Accounting tasks", "Processed high-volume financial data with attention to accuracy"),
        ("Risk assessment", "Applied analytical frameworks to assess risk and forecast outcomes")
    ],
    "Marketing": [
        ("Social media", "Analysed social media performance metrics to optimise content strategy"),
        ("Campaigns", "Tracked campaign KPIs and used data insights to improve conversion rates"),
        ("Content creation", "Developed content informed by audience analytics and engagement data"),
        ("Brand management", "Monitored brand performance dashboards and competitive positioning")
    ],
    "Sales": [
        ("Hit targets", "Used data-driven strategies to consistently exceed revenue targets"),
        ("Client management", "Analysed customer behaviour patterns to improve retention"),
        ("Prospecting", "Built targeted prospect lists using data analysis and market research"),
        ("Closing deals", "Tracked pipeline metrics and optimised sales processes")
    ],
    "Retail": [
        ("Customer service", "Observed customer behaviour trends to inform service improvements"),
        ("Sales floor", "Monitored daily sales data and identified fast-moving product patterns"),
        ("Stock management", "Analysed stock levels and restocking patterns to optimise inventory"),
        ("Cash handling", "Handled end-of-day financial reconciliation and payment reporting")
    ],
    "Banking": [
        ("Transactions", "Processed and validated high-volume financial data with 100% accuracy"),
        ("Account management", "Managed client data across multiple systems ensuring data integrity"),
        ("Compliance", "Analysed transaction patterns for regulatory compliance and reporting"),
        ("Customer service", "Used CRM data to identify client needs and improve service delivery")
    ],
    "Admin / Office": [
        ("Data entry", "Maintained and organised large datasets with accuracy and consistency"),
        ("Scheduling", "Optimised scheduling processes to improve team efficiency"),
        ("Filing", "Created systematic information management workflows"),
        ("Correspondence", "Managed stakeholder communications and documentation")
    ]
}

# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================
if "profile_complete" not in st.session_state:
    st.session_state.profile_complete = False
if "tone" not in st.session_state:
    st.session_state.tone = "Humanised & Real"

# ============================================================
# SIDEBAR - PROFILE SETUP & NAVIGATION
# ============================================================
with st.sidebar:
    st.markdown("## Career Coach Pro")
    st.caption("Your Personal Career Agency")
    st.markdown("---")

    if not st.session_state.profile_complete:
        st.markdown("### Step 1: Tell me about yourself")

        name = st.text_input("Full name")
        city = st.text_input("City")
        country = st.text_input("Country")

        stage = st.selectbox("Where are you in your career?", [
            "Fresh graduate", "Student", "Working professional",
            "Job seeker", "Career pivoter", "Master's applicant"
        ])

        degree = st.text_input("Your degree (e.g. BBA in Finance)")
        university = st.text_input("University name")

        experience_level = st.selectbox("Work experience", [
            "None", "Internship only", "1-2 years", "3-5 years", "5+ years"
        ])

        current_role = ""
        current_company = ""
        previous_field = ""
        if experience_level != "None":
            current_role = st.text_input("Current/recent job title")
            current_company = st.text_input("Company name")
            previous_field = st.text_input("Your industry (e.g. Retail, Banking)")

        target_field = st.selectbox("What field do you want to work in?", CAREER_FIELDS)

        field_skills = FIELD_DATA[target_field]["technical_skills"] + FIELD_DATA[target_field]["soft_skills"]
        existing_skills = st.multiselect("Skills you already have", field_skills)

        has_projects = st.checkbox("I have projects or a portfolio")
        project_details = ""
        if has_projects:
            project_details = st.text_input("Briefly describe them")

        if st.button("✅ Save My Profile", use_container_width=True):
            st.session_state.profile = {
                "name": name or "Career Builder",
                "city": city,
                "country": country,
                "stage": stage,
                "degree": degree,
                "university": university,
                "experience_level": experience_level,
                "current_role": current_role,
                "current_company": current_company,
                "previous_field": previous_field,
                "target_field": target_field,
                "existing_skills": existing_skills,
                "has_projects": has_projects,
                "project_details": project_details
            }
            st.session_state.profile_complete = True
            st.rerun()

    else:
        profile = st.session_state.profile
        st.markdown(f"""
        <div class="profile-badge">
            <div class="name">{profile['name'].split()[0]}</div>
            <div class="detail">{profile['target_field']} &bull; {profile['stage']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Writing Tone")
        st.session_state.tone = st.selectbox(
            "Pick your vibe",
            list(TONES.keys()),
            index=list(TONES.keys()).index(st.session_state.tone)
        )
        st.caption(TONES[st.session_state.tone]["description"])

        st.markdown("---")
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.profile_complete = False
            st.rerun()

        st.markdown("---")
        st.caption("Built by Ayesha Shimu")

# ============================================================
# MAIN CONTENT
# ============================================================
if not st.session_state.profile_complete:
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">Free &bull; Private &bull; Powered by Python</div>
        <p class="main-header">Career Coach Pro</p>
        <p class="sub-header">Your personal career agency. Get expert guidance on LinkedIn, CVs, interviews, and more.</p>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("💼", "LinkedIn Optimizer", "Headlines, About section, experience rewriting, and post ideas in your chosen tone."),
        ("📄", "CV & Cover Letter", "Structure, examples, and tips tailored to your field and career stage."),
        ("📊", "Job Market Insights", "Salaries, top cities, demand levels, skills, and certifications."),
        ("🎯", "Interview Prep", "Common questions, STAR method, behavioural prep, and checklists."),
        ("🗺️", "Skills Roadmap", "Personalised 90-day learning plan with progress tracking."),
        ("💬", "Ask Coach", "Chat with your AI career coach. Ask anything about jobs, skills, or career planning.")
    ]

    # First row: 3 cards
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(features[:3]):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <span class="feature-icon">{icon}</span>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Second row: 3 cards
    cols2 = st.columns(3)
    for i, (icon, title, desc) in enumerate(features[3:6]):
        with cols2[i]:
            st.markdown(f"""
            <div class="feature-card">
                <span class="feature-icon">{icon}</span>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cta-box">
        <h3>Ready to get started?</h3>
        <p>Fill in your profile in the sidebar to unlock all features.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="app-footer">Built by Ayesha Shimu &bull; Python &bull; Streamlit &bull; Career Guidance</div>', unsafe_allow_html=True)

else:
    profile = st.session_state.profile
    tone_name = st.session_state.tone
    tone = TONES[tone_name]
    field = FIELD_DATA[profile["target_field"]]

    # TAB NAVIGATION
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "💼 LinkedIn", "📄 CV & Cover Letter", "📊 Job Market",
        "🎯 Interview Prep", "🗺️ Skills Roadmap", "📝 Post Ideas", "💬 Ask Coach"
    ])

    # ============================================================
    # TAB 1: LINKEDIN OPTIMIZER
    # ============================================================
    with tab1:
        st.header("LinkedIn Profile Optimizer")
        st.caption(f"Tone: {tone_name} — Optimised headlines get 40% more profile views and 5x more recruiter messages")

        # HEADLINES
        st.subheader("Your Headline Options (max 220 characters)")
        st.write("Your headline is the single most important line on LinkedIn. It appears in search results, comments, connection requests, and recruiter filters. A strong headline follows this formula: **Role + Key Skills + Value/Result + Differentiator**.")

        target = profile["target_field"]
        prev = profile["previous_field"]
        city = profile["city"]
        skills = profile["existing_skills"]
        top_skills = " | ".join(skills[:3]) if skills else target
        first_title = field["job_titles"][0]

        headlines = []

        # --- FORMULA 1: Role + Skills + Value (works for all tones) ---
        if "Friendly" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                headlines.append(f"{first_title} | {prev} background meets {target} skills | Turning business instinct into actionable insights | {city}")
                headlines.append(f"Aspiring {first_title} | {top_skills} | Bringing {prev.lower()} domain knowledge to every dataset | Open to connect")
            else:
                headlines.append(f"Aspiring {first_title} | {top_skills} | Building real projects and sharing the journey | {city}")
            headlines.append(f"{target} Enthusiast | {top_skills} | Making sense of messy data one project at a time")

        elif "Humanised" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                headlines.append(f"{prev} professional pivoting into {target.lower()} | Self-taught in {top_skills} | Real projects, no fluff")
                headlines.append(f"Career changer: {prev} to {target} | I ask the questions most analysts forget because I've sat on the business side")
            else:
                headlines.append(f"{first_title} in the making | {top_skills} | Learning in public, building in private")
            headlines.append(f"{target} | {top_skills} | The kind of person who opens a CSV before coffee")

        elif "Professional" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                headlines.append(f"{first_title} | {profile['degree']} | Leveraging {prev.lower()} domain expertise to deliver data-driven business outcomes")
                headlines.append(f"Transitioning {prev} Professional | {top_skills} | Bridging business acumen with technical analysis | {city}")
            else:
                headlines.append(f"{first_title} | {profile['degree']} | {top_skills} | Committed to data-driven decision making")
            headlines.append(f"Aspiring {first_title} | {top_skills} | {profile['university']} Graduate | {city}")

        elif "Confident" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                headlines.append(f"I translate {prev.lower()} complexity into {target.lower()} solutions | {top_skills} | Business mind, technical hands")
                headlines.append(f"{prev} expertise + {target} skills = insights pure-tech people miss | {city}")
            else:
                headlines.append(f"I build {target.lower()} projects that solve real problems | {top_skills} | Results over resumes")
            headlines.append(f"{first_title} | {top_skills} | I ship projects, not just certificates")

        else:  # Storytelling
            if profile["stage"] == "Career pivoter" and prev:
                headlines.append(f"From {prev.lower()} spreadsheets to {target.lower()} dashboards | The pivot that changed everything | {city}")
                headlines.append(f"{prev} taught me the 'why' behind business decisions. {target} taught me the 'how' | Building at the intersection")
            else:
                headlines.append(f"Turning raw curiosity into {target.lower()} projects | {top_skills} | Every dataset has a story")
            headlines.append(f"{first_title} | {top_skills} | Writing the next chapter of my career one commit at a time")

        # --- Stage-specific bonus headlines ---
        if profile["stage"] == "Fresh graduate":
            headlines.append(f"{profile['degree']} Graduate | {first_title} | {top_skills} | Ready to turn academic rigour into business impact")
        if profile["stage"] == "Master's applicant":
            headlines.append(f"MSc {target} Candidate | {profile['degree']} | Combining academic depth with hands-on {target.lower()} projects | {city}")
        if profile["stage"] == "Student":
            headlines.append(f"{target} Student | {top_skills} | Building portfolio projects before graduation | {city}")
        if profile["stage"] == "Job seeker":
            headlines.append(f"{first_title} | {top_skills} | Actively building and shipping {target.lower()} projects | {city}")
        if profile["has_projects"]:
            headlines.append(f"{first_title} | {top_skills} | Portfolio-driven | GitHub: real projects, real data, real results")

        for i, h in enumerate(headlines, 1):
            chars = len(h)
            status = "✅ Great length" if chars <= 220 else "⚠️ Trim to 220 chars"
            st.markdown(f'<div class="result-box"><strong>Option {i}</strong> ({chars}/220 chars) {status}<br><br>{h}</div>', unsafe_allow_html=True)

        st.markdown(f"""<div class="tip-box">
        💡 <strong>Recruiter Pro Tips:</strong><br>
        • Recruiters search by <strong>job title + skills</strong>. If those words aren't in your headline, you won't appear in their results.<br>
        • Never use "Seeking opportunities", "Open to work", or "Aspiring" alone. Lead with what you <strong>do</strong>, not what you want.<br>
        • Adding a number or measurable outcome can generate <strong>5x more recruiter messages</strong>.<br>
        • Your headline shows under your name on <strong>every comment, post, and connection request</strong>. Make every word count.
        </div>""", unsafe_allow_html=True)

        st.markdown("---")

        # ABOUT SECTION
        st.subheader("About Section (2,600 characters max)")
        st.write("Your About section is your elevator pitch. Structure: **Who you are → What led you here → What you bring → What you're building → Call to action + Keywords**. Write in first person. Every sentence should earn its place.")

        degree = profile["degree"]
        uni = profile["university"]

        if "Friendly" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                about = f"I spent my early career in {prev.lower()}, where I developed a sharp eye for identifying patterns, solving operational problems, and making sense of complex business processes. Somewhere along the way, I realised the part of my work I enjoyed most was the analytical side, the part where data told the real story."
                about += f"\n\nThat realisation led me to {target.lower()}. I have since been building practical skills in {', '.join(field['technical_skills'][:4])}, working on real projects, and learning what it takes to turn raw data into decisions that move the needle."
            else:
                about = f"I am a {degree} graduate from {uni} with a growing foundation in {target.lower()}. What draws me to this field is the ability to look at messy, real-world problems and find clarity through data."
                about += f"\n\nI have been actively building skills in {', '.join(field['technical_skills'][:4])} through structured courses and hands-on projects."
        elif "Humanised" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                about = f"I studied {degree} at {uni} and worked in {prev.lower()} after graduating. It was good work, but I kept gravitating toward the data side of things. The spreadsheets, the KPIs, the moments where a pattern suddenly made sense and changed how we made decisions."
                about += f"\n\nSo I made a deliberate choice to pivot. I started learning {', '.join(field['technical_skills'][:3])}, built projects to test what I was learning, and treated every dataset like a puzzle worth solving."
            else:
                about = f"I will be upfront: my path into {target.lower()} was not a straight line. I came from {prev.lower() if prev else 'a different background'}, and that detour gave me something a bootcamp alone never could: the ability to understand business context before touching a single dataset."
                about += f"\n\nI have since built hands-on skills in {', '.join(field['technical_skills'][:4])} through real projects, not just tutorials."
        elif "Professional" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                about = f"With a {degree} from {uni} and a professional background in {prev.lower()}, I bring a strong foundation in business operations, stakeholder management, and strategic problem-solving. I am now applying these competencies to {target.lower()}, where I see substantial opportunity to drive measurable impact through data-informed decision-making."
                about += f"\n\nI have developed proficiency in {', '.join(field['technical_skills'][:4])} through structured coursework and project-based learning, complemented by domain expertise that enables me to bridge the gap between technical analysis and business outcomes."
            else:
                about = f"As a {degree} graduate from {uni}, I have cultivated a strong analytical foundation and a demonstrated commitment to {target.lower()}. My approach combines academic rigour with practical application through project-based learning and industry-recognised certifications."
                about += f"\n\nCore competencies include {', '.join(field['technical_skills'][:4])}, with an emphasis on translating analytical findings into actionable business recommendations."
        elif "Confident" in tone_name:
            if profile["stage"] == "Career pivoter" and prev:
                about = f"Most people in {target.lower()} learned the tools first and the business later. I did the opposite. Years in {prev.lower()} taught me how businesses actually operate: the metrics that matter, the decisions that move revenue, the stakeholders who need convincing. Now I combine that operational instinct with {target.lower()} skills to deliver what most analysts cannot: insights that are technically sound and business-ready."
            else:
                about = f"I do not just study {target.lower()}. I build with it. While others collect certificates, I collect project repositories. My approach is simple: identify a real problem, build a solution, measure the result, and ship it."
            about += f"\n\nTechnical toolkit: {', '.join(field['technical_skills'][:5])}."
        else:  # Storytelling
            if profile["stage"] == "Career pivoter" and prev:
                about = f"It started with a question I could not answer. I was working in {prev.lower()}, staring at a report full of numbers, and I realised I had no idea whether those numbers were telling us to push forward or pull back. That gap between data and decision-making became an obsession."
                about += f"\n\nI walked away from a stable {prev.lower()} path to teach myself {', '.join(field['technical_skills'][:3])}. I built projects, broke things, rebuilt them, and slowly started to see the patterns hidden in the noise."
            else:
                about = f"My {target.lower()} journey did not start in a lecture hall. It started the moment I opened a dataset and realised I could spend hours exploring it without looking at the clock. That was the signal."
                about += f"\n\nSince then, I have been deliberately building my skillset in {', '.join(field['technical_skills'][:4])}, one project at a time."

        # Universal additions based on profile data
        if city:
            about += f"\n\nCurrently based in {city}."
        if skills:
            about += f" Working proficiency in {', '.join(skills[:5])}."
        if profile["has_projects"]:
            about += f"\n\n{profile['project_details']} I share my work publicly because a portfolio speaks louder than a bullet point."

        about += f"\n\nCurrently exploring opportunities in {target.lower()}. If you are building a team that values curiosity, ownership, and a willingness to figure things out, I would love to connect."
        about += f"\n\n{' | '.join(field['keywords'][:7])}"

        st.markdown(f'<div class="copy-text">{about}</div>', unsafe_allow_html=True)
        chars_used = len(about)
        remaining = 2600 - chars_used
        st.caption(f"{chars_used}/2,600 characters used ({remaining} remaining)")

        st.markdown(f"""<div class="tip-box">
        💡 <strong>About Section Pro Tips:</strong><br>
        • First 3 lines are visible before "See more". Lead with your strongest hook.<br>
        • Write in <strong>first person</strong> for authenticity. Third person reads like a press release.<br>
        • End with <strong>industry keywords</strong> separated by pipes. LinkedIn indexes these for search.<br>
        • Profiles with a complete About section get <strong>20x more views</strong> and 9x more connection requests.
        </div>""", unsafe_allow_html=True)

        st.markdown("---")

        # EXPERIENCE REWRITING
        st.subheader("Rewrite Your Experience (Action Verb + Task + Result)")
        st.write("Recruiters and ATS systems scan for **action verbs + measurable outcomes**. Never write duties. Write achievements. The formula: **[Action Verb] + [What You Did] + [Quantified Result]**.")

        matched = None
        if prev:
            for key in EXPERIENCE_REFRAMES:
                if key.lower() in prev.lower() or prev.lower() in key.lower():
                    matched = key
                    break

        if matched:
            st.write(f"Your background: **{prev}** → Target: **{target}**")
            for original, reframed in EXPERIENCE_REFRAMES[matched]:
                col_a, col_b = st.columns(2)
                with col_a:
                    st.error(f"**Weak:** \"{original}\"")
                with col_b:
                    st.success(f"**Strong:** \"{reframed}\"")
        else:
            st.info("Enter your industry in the sidebar to get specific reframing suggestions!")

        st.markdown("---")
        st.subheader("The Achievement Reframing Framework")
        st.write("For ANY past role, rewrite each bullet using this checklist:")
        st.write("1. **What action did you take?** (Use a power verb)")
        st.write("2. **What was the scope?** (How many users, records, transactions, team members?)")
        st.write("3. **What tool or method did you use?** (Excel, SQL, Tableau, Python?)")
        st.write("4. **What was the measurable outcome?** (Saved X hours, reduced Y%, improved Z)")
        st.write("5. **Who benefited?** (Team, department, clients, leadership)")
        st.write("")
        st.markdown("**Tier 1 Power Verbs (Achievement):** Accelerated, Delivered, Drove, Exceeded, Generated, Increased, Optimised, Reduced, Spearheaded, Transformed")
        st.markdown("**Tier 2 Power Verbs (Analytical):** Analysed, Automated, Built, Designed, Forecasted, Identified, Modelled, Streamlined, Tracked, Visualised")
        st.markdown("**Tier 3 Power Verbs (Collaborative):** Advised, Coordinated, Facilitated, Mentored, Partnered, Presented, Proposed, Resolved, Supported, Trained")
        st.write("")
        st.markdown(f"""<div class="tip-box">
        💡 <strong>Example transformation:</strong><br>
        ❌ <em>"Responsible for managing reports"</em><br>
        ✅ <em>"Built automated weekly reports using Excel and Power BI, reducing manual reporting time by 4 hours per week and enabling leadership to make faster inventory decisions"</em>
        </div>""")

    # ============================================================
    # TAB 2: CV & COVER LETTER
    # ============================================================
    with tab2:
        cv_tab, cl_tab = st.tabs(["📄 CV Guidance", "✉️ Cover Letter"])

        with cv_tab:
            st.header(f"CV Guidance ({tone_name} tone)")
            st.info(f"Your CV style: **{tone['cv_tone']}** — ATS-optimised, single-column, reverse chronological")

            st.subheader("ATS-Friendly CV Structure")
            st.write("Over 75% of CVs are filtered by ATS (Applicant Tracking Systems) before a human ever sees them. Use a **single-column layout**, **standard section headings**, and **keywords from the job description**.")

            st.markdown("**1. Header**")
            st.write("Full name (large, bold) | City, Country | Email | LinkedIn URL | GitHub/Portfolio. No photo, no date of birth, no marital status for UK/EU roles.")

            st.markdown("**2. Professional Summary (3-4 lines)**")
            st.write("This is your elevator pitch on paper. Formula: **[Who you are] + [Key skills] + [What you deliver] + [Target role]**.")
            if profile["stage"] == "Career pivoter" and prev:
                summary = f"{profile['degree']} graduate with {profile['experience_level']} experience in {prev.lower()}, transitioning into {target.lower()}. Combines domain expertise in business operations with newly developed proficiency in {', '.join(field['technical_skills'][:3])}. Proven ability to translate complex processes into actionable insights. Actively building a project portfolio demonstrating end-to-end {target.lower()} capabilities."
            elif profile["stage"] == "Fresh graduate":
                summary = f"Detail-oriented {profile['degree']} graduate from {uni} with a strong foundation in {target.lower()}. Proficient in {', '.join(field['technical_skills'][:3])} through coursework and independent projects. Combines analytical rigour with clear communication skills. Seeking a {field['job_titles'][0]} role to apply academic training to real business challenges."
            else:
                summary = f"Motivated {target.lower()} professional with hands-on experience in {', '.join(field['technical_skills'][:3])}. Demonstrated ability to turn raw data into clear, actionable recommendations through portfolio projects and self-directed learning. Brings a unique perspective from {prev.lower() + ' background' if prev else 'diverse experiences'} combined with technical skills."
            st.markdown(f'<div class="result-box">{summary}</div>', unsafe_allow_html=True)

            st.markdown("**3. Core Skills** (8-10, organised by category)")
            st.write("Place this section high on the page. ATS systems weight this heavily.")
            tech = field["technical_skills"][:5]
            soft = field["soft_skills"][:3]
            st.code(f"Technical: {' | '.join(tech)}\nAnalytical: {' | '.join(soft)}")

            st.markdown("**4. Experience** (reverse chronological, most recent first)")
            st.write("3-4 bullet points per role. Every bullet must follow: **[Action Verb] + [What] + [Measurable Result]**.")
            st.markdown(f"""<div class="result-box">
            <strong>Example bullets for your profile:</strong><br><br>
            • Analysed {prev.lower() if prev else 'operational'} data across multiple systems, identifying 3 key inefficiencies that informed process improvements<br>
            • Built interactive dashboards using {field['technical_skills'][0]} to visualise weekly performance metrics for stakeholder review<br>
            • Automated manual reporting workflows, reducing preparation time from 5 hours to 45 minutes per cycle<br>
            • Collaborated with cross-functional teams to define KPIs and establish data-driven decision-making frameworks
            </div>""", unsafe_allow_html=True)

            st.markdown("**5. Projects / Portfolio** (critical for career changers)")
            st.write("This section can **replace** lack of professional experience. For each project, include:")
            st.write("**Project Name** | One-line description | Tools: [Python, SQL, Tableau] | [GitHub Link]")
            st.markdown(f"""<div class="tip-box">💡 <strong>Portfolio tip:</strong> 2-3 quality projects with clean READMEs beat 10 tutorial follow-alongs. Include: the problem, your approach, tools used, key findings, and what you learned. Recruiters read READMEs.</div>""")

            st.markdown("**6. Education**")
            st.write(f"**{profile['degree']}** | {uni} | Graduation year. Include relevant modules, honours, and GPA if above 3.0/4.0.")

            st.markdown("**7. Certifications & Training**")
            for cert in field["certifications"]:
                st.write(f"🎓 {cert}")

            st.markdown("---")
            st.subheader("CV Red Flags (What Gets You Rejected)")
            mistakes = [
                ("Using the same CV for every application", "Tailor keywords to match each job description. Mirror their exact language."),
                ("Writing 'Responsible for...' or 'Duties included...'", "These describe tasks, not achievements. Use action verbs + results."),
                ("No numbers or metrics anywhere", "Even estimates help. 'Managed inventory' becomes 'Managed inventory of 500+ SKUs'."),
                ("Fancy two-column or graphic templates", "These break ATS parsing. Use a clean single-column layout."),
                ("Listing every tool you've touched once", "Only list tools you can confidently discuss in an interview."),
                ("CV longer than 2 pages", "1 page for under 5 years experience. 2 pages maximum for senior roles."),
                ("Including a photo, age, or marital status", "Not standard in UK/US. Can trigger unconscious bias."),
                ("Generic objective statement", "Replace with a targeted professional summary that mirrors the job posting.")
            ]
            for mistake, fix in mistakes:
                with st.expander(f"❌ {mistake}"):
                    st.write(f"**Fix:** {fix}")

        with cl_tab:
            st.header(f"Cover Letter Guidance ({tone_name} tone)")
            st.info(f"Your style: **{tone['cover_letter_style']}** — A cover letter is not a CV summary. It answers one question: Why you, why this role, why this company?")

            st.subheader("The 4-Paragraph Framework")

            st.markdown("**Paragraph 1: The Hook (Why This Role)**")
            st.write("Name the role. Show you have researched the company. Make it specific enough that it could only be sent to THIS company.")
            if "Friendly" in tone_name:
                example = f"I was drawn to the {field['job_titles'][0]} role at [Company] after reading about your recent work on [specific initiative]. Your team's approach to [specific value] aligns with exactly the kind of impact I want to create as I build my career in {target.lower()}."
            elif "Humanised" in tone_name:
                example = f"When I came across the {field['job_titles'][0]} position at [Company], something clicked. Your commitment to [specific mission or project] mirrors the exact reason I chose to pursue {target.lower()} in the first place: making data useful for real decisions, not just dashboards that collect dust."
            elif "Confident" in tone_name:
                example = f"I am applying for the {field['job_titles'][0]} role at [Company] because I bring something most candidates in this pipeline do not: {prev.lower() + ' domain expertise' if prev else 'a business-first mindset'} combined with hands-on {target.lower()} skills. Your work on [specific initiative] tells me this team values that combination."
            elif "Creative" in tone_name or "Storytelling" in tone_name:
                example = f"Before I knew what {target.lower()} was, I was already doing it. In my previous role, I spent hours dissecting reports, looking for the story behind the numbers. When I discovered that [Company] is building [specific thing], I knew this was where that instinct belongs."
            else:
                example = f"I am writing to express my strong interest in the {field['job_titles'][0]} position at [Company]. Your organisation's focus on [specific initiative] aligns directly with my professional development in {target.lower()} and my commitment to delivering data-driven business value."
            st.markdown(f'<div class="result-box">{example}</div>', unsafe_allow_html=True)

            st.markdown("**Paragraph 2: Evidence (Why You're Qualified)**")
            st.write("Match 2-3 of YOUR skills to THEIR listed requirements. Give a specific example with a measurable outcome. Do not restate your CV; tell a story your CV cannot.")
            st.markdown(f"""<div class="result-box">
            <strong>Example:</strong> In my previous role at [Company], I [action verb + specific task]. This resulted in [quantified outcome]. I have since expanded my toolkit to include {', '.join(field['technical_skills'][:3])}, which I applied in [project name], where I [specific result].
            </div>""", unsafe_allow_html=True)

            st.markdown("**Paragraph 3: Why This Company (Not Just Any Company)**")
            st.write("Demonstrate that you have done your homework. Reference their mission, recent news, a product you admire, or a value that resonates. Explain what YOU specifically bring that others might not.")

            st.markdown("**Paragraph 4: The Close**")
            st.write("Express genuine enthusiasm. State your availability. Do not beg or apologise. Be confident.")
            st.markdown(f"""<div class="result-box">
            <strong>Strong close:</strong> I would welcome the opportunity to discuss how my combination of {prev.lower() + ' experience and ' if prev else ''}{target.lower()} skills could contribute to [Company's] goals. I am available for an interview at your convenience and have attached my CV for your review.
            </div>""", unsafe_allow_html=True)

            st.markdown("---")
            col_do, col_dont = st.columns(2)
            with col_do:
                st.markdown("### ✅ Do")
                for d in [
                    "Address it to the hiring manager by name (check LinkedIn)",
                    "Keep it under one page, 3-4 paragraphs max",
                    "Mirror keywords from the job description exactly",
                    "Show you researched the company (mention something specific)",
                    "Include one specific achievement with numbers",
                    "Make sure your CV, LinkedIn, and cover letter tell the same story",
                    "Proofread twice, then read it out loud"
                ]:
                    st.write(f"+ {d}")
            with col_dont:
                st.markdown("### ❌ Don't")
                for d in [
                    "Start with 'To whom it may concern' or 'Dear Sir/Madam'",
                    "Repeat your CV bullet points verbatim",
                    "Apologise for lack of experience or being a career changer",
                    "Use the same letter for every application",
                    "Include salary expectations unless explicitly asked",
                    "Write more than one page",
                    "Use buzzwords without evidence (e.g., 'team player' with no example)"
                ]:
                    st.write(f"- {d}")

    # ============================================================
    # TAB 3: JOB MARKET INSIGHTS
    # ============================================================
    with tab3:
        st.header(f"Job Market Insights: {profile['target_field']}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Demand Level", field["demand_level"])
        with col2:
            st.metric("Remote Friendly", field["remote_friendly"])
        with col3:
            st.metric("Entry Salary", f"£{field['avg_salary_gbp']['Entry Level']:,}")

        st.markdown("---")

        st.subheader("Salary Ranges (GBP)")
        for level, salary in field["avg_salary_gbp"].items():
            max_sal = field["avg_salary_gbp"]["Senior"]
            pct = salary / max_sal
            st.write(f"**{level}:** £{salary:,}")
            st.progress(pct)

        st.markdown("---")

        col_titles, col_cities = st.columns(2)
        with col_titles:
            st.subheader("Common Job Titles")
            for title in field["job_titles"]:
                st.write(f"- {title}")
        with col_cities:
            st.subheader("Top Cities")
            st.write("**UK:**")
            for c in field["top_cities_uk"]:
                st.write(f"- {c}")
            st.write("**Europe:**")
            for c in field["top_cities_eu"]:
                st.write(f"- {c}")

        st.markdown("---")
        col_certs, col_skills = st.columns(2)
        with col_certs:
            st.subheader("Certifications Recruiters Want")
            for cert in field["certifications"]:
                st.write(f"🎓 {cert}")
        with col_skills:
            st.subheader("Most In-Demand Skills")
            for skill in field["technical_skills"]:
                if skill in profile["existing_skills"]:
                    st.write(f"✅ {skill} (you have this!)")
                else:
                    st.write(f"📌 {skill}")

    # ============================================================
    # TAB 4: INTERVIEW PREP
    # ============================================================
    with tab4:
        st.header(f"Interview Preparation: {profile['target_field']}")
        st.caption("Interviews are not about having perfect answers. They are about demonstrating how you think, communicate, and solve problems.")

        st.subheader(f"Technical Topics for {target}")
        for topic in field["interview_topics"]:
            st.write(f"📚 {topic}")

        st.markdown("---")
        st.subheader("The 10 Questions You Will Be Asked (with Expert Strategies)")

        pivoter = profile["stage"] == "Career pivoter" and prev

        questions = [
            ("Tell me about yourself",
             f"Use the **Present-Past-Future** framework in under 90 seconds:\n\n"
             f"**Present:** 'I am currently building my skills in {target.lower()}, focusing on {', '.join(field['technical_skills'][:2])}.'\n\n"
             f"**Past:** '{'I previously worked in ' + prev.lower() + ', where I developed strong analytical and problem-solving abilities.' if pivoter else 'I recently graduated with a ' + profile['degree'] + ' from ' + uni + '.'}'\n\n"
             f"**Future:** 'I am now looking for a {field['job_titles'][0]} role where I can apply these skills to drive real business impact.'\n\n"
             f"Keep it tight. End with why you are excited about THIS role."),

            ("Why are you changing careers?" if pivoter else "Why this field?",
             f"{'This question is an opportunity, not a threat. Frame your pivot as intentional and strategic:' if pivoter else 'Show this was a deliberate choice, not a fallback:'}\n\n"
             f"**Strong answer:** 'In my {prev.lower() if prev else 'previous'} work, I consistently found that the most impactful decisions were data-driven. I realised I wanted to be the person generating those insights, not just acting on them. That led me to invest in {target.lower()} through structured learning and hands-on projects.'\n\n"
             f"**Never say:** 'I was bored' or 'I couldn't find jobs in my old field.'"),

            ("What's your biggest weakness?",
             "Pick a real skill gap that is **not critical** to the role, then show how you are actively addressing it.\n\n"
             f"**Good example:** 'When I started learning {field['technical_skills'][0]}, I found myself spending too much time perfecting code instead of focusing on the business question. I have since adopted a practice of defining the goal first and setting time limits for exploration.'\n\n"
             "**Never say:** 'Perfectionism', 'I work too hard', or anything that sounds rehearsed."),

            ("Where do you see yourself in 5 years?",
             f"Show ambition aligned with the company's growth, not a plan to leave.\n\n"
             f"**Strong answer:** 'In five years, I want to be a trusted {target.lower()} professional who can independently take a business question, design the analysis, and present findings that influence strategy. I see this role as the foundation for that trajectory.'\n\n"
             f"**Avoid:** Mentioning competitor companies, saying 'your job', or being vague."),

            ("Why should we hire you?",
             f"This is your 30-second pitch. Combine three things: **unique background + relevant skills + attitude**.\n\n"
             f"**Strong answer:** 'I bring {'a ' + prev.lower() + ' background that gives me business context most analysts lack, ' if pivoter else ''}hands-on skills in {', '.join(field['technical_skills'][:3])}, and a track record of teaching myself complex topics quickly. I do not just analyse data; I think about what it means for the business.'\n\n"
             "Back this up with a specific project or achievement."),

            ("Tell me about a time you failed / faced a challenge",
             "Use the **STAR method** and always end on what you learned.\n\n"
             "**Framework:** Describe the **Situation** briefly, the **Task** you were responsible for, the **Action** you specifically took, and the **Result** including what you learned.\n\n"
             f"**Career changer example:** 'When I first started learning {field['technical_skills'][0]}, I built a project that completely fell apart because I skipped the data cleaning step. I had to redo the entire analysis from scratch. That failure taught me that 80% of good analysis is preparation, not visualisation.'"),

            ("What do you know about our company?",
             "This is a research test. Before every interview, find:\n\n"
             "• Their **mission statement** (About page)\n"
             "• One **recent news article** or press release\n"
             "• A **specific product, feature, or initiative** you admire\n"
             "• Who the **interviewer** is on LinkedIn\n\n"
             "**Template:** 'I was particularly interested in [specific initiative]. It aligns with my interest in [aspect of the role]. I also noticed [recent development] which suggests the team is growing in [direction].'"),

            ("Do you have any questions for us?",
             "**Always say yes.** Prepare 3-5 questions. Here are strong ones:\n\n"
             "• 'What does a typical day look like for someone in this role?'\n"
             "• 'What skills or qualities distinguish top performers on this team?'\n"
             "• 'How does the team approach [specific process relevant to the role]?'\n"
             "• 'What is the biggest challenge the team is currently facing?'\n"
             "• 'How do you measure success for this position in the first 6 months?'\n\n"
             "**Never ask** about salary in a first interview unless they bring it up."),

            ("Walk me through a project you've worked on",
             f"Pick your best project and structure it as:\n\n"
             f"**Problem:** 'I noticed that [problem or question].'\n"
             f"**Approach:** 'I used [tools: {', '.join(field['technical_skills'][:2])}] to [method].'\n"
             f"**Findings:** 'The analysis revealed [key insight].'\n"
             f"**Impact:** 'This could help a business [specific outcome].'\n\n"
             f"Practice this out loud until it takes under 2 minutes."),

            ("What are your salary expectations?",
             f"**Research first:** For {target} in the UK:\n"
             f"• Entry Level: £{field['avg_salary_gbp']['Entry Level']:,}\n"
             f"• Mid Level: £{field['avg_salary_gbp']['Mid Level']:,}\n"
             f"• Senior: £{field['avg_salary_gbp']['Senior']:,}\n\n"
             "**Strong answer:** 'Based on my research and the scope of this role, I would expect a salary in the range of £X to £Y. However, I am open to discussing this further based on the full compensation package.'\n\n"
             "**Pro tip:** Let them name a number first if possible. Say: 'I'd love to understand more about the role's scope before discussing numbers.'")
        ]

        for q, tip in questions:
            with st.expander(f"❓ {q}"):
                st.markdown(tip)

        st.markdown("---")
        st.subheader("STAR Method Deep Dive")
        st.write("For ANY behavioural question ('Tell me about a time when...'), use this structure:")
        col_s, col_t, col_a, col_r = st.columns(4)
        with col_s:
            st.markdown("**S — Situation**")
            st.write("Set the scene in 1-2 sentences. When, where, what was happening.")
        with col_t:
            st.markdown("**T — Task**")
            st.write("What was YOUR specific responsibility? Not the team's. Yours.")
        with col_a:
            st.markdown("**A — Action**")
            st.write("What did YOU do? Be specific. This is the longest part.")
        with col_r:
            st.markdown("**R — Result**")
            st.write("What happened? Use numbers. What did you learn?")

        st.markdown("---")
        st.subheader("48-Hour Interview Prep Checklist")
        checklist = [
            "Research the company: website, LinkedIn, Glassdoor reviews, recent news",
            "Read the job description 3 times and highlight keywords",
            "Prepare your 'Tell me about yourself' answer (under 90 seconds)",
            "Prepare 2-3 STAR stories from your experience or projects",
            "Practice walking through your best project (under 2 minutes)",
            "Prepare 3-5 questions to ask THEM",
            "Look up the interviewer on LinkedIn",
            "Test your camera, mic, and internet for video calls",
            "Have your CV and the job description open during the call",
            "Plan your outfit (one level above company culture)",
            "Arrive 10 minutes early (or log in 5 minutes early for video)",
            "Send a personalised thank-you email within 24 hours"
        ]
        for item in checklist:
            st.checkbox(item)

    # ============================================================
    # TAB 5: SKILLS ROADMAP
    # ============================================================
    with tab5:
        st.header(f"Your {profile['target_field']} Skills Roadmap")

        all_skills = field["technical_skills"] + field["soft_skills"]
        have = [s for s in all_skills if s in profile["existing_skills"]]
        missing = [s for s in all_skills if s not in profile["existing_skills"]]
        pct = len(have) / len(all_skills) if all_skills else 0

        st.subheader(f"Progress: {len(have)}/{len(all_skills)} skills ({pct*100:.0f}%)")
        st.progress(pct)

        col_have, col_need = st.columns(2)
        with col_have:
            st.markdown("### ✅ Skills You Have")
            for s in have:
                st.write(f"- {s}")
            if not have:
                st.write("Start building! Pick from the list on the right.")
        with col_need:
            st.markdown("### 📌 Skills to Learn")
            for i, s in enumerate(missing, 1):
                priority = "🔴 HIGH" if i <= 3 else "🟡 MEDIUM" if i <= 6 else "🟢 NICE TO HAVE"
                st.write(f"{i}. {s} [{priority}]")

        st.markdown("---")
        st.subheader("90-Day Learning Plan")

        if missing:
            month1 = missing[:2]
            month2 = missing[2:4] if len(missing) > 2 else []
            month3 = missing[4:6] if len(missing) > 4 else []

            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.markdown("### Month 1: Foundation")
                for s in month1:
                    st.write(f"📖 Learn {s}")
                st.write("📖 Complete 1 online course")
                st.write("🔨 Build 1 small project")
            with col_m2:
                st.markdown("### Month 2: Building")
                for s in month2:
                    st.write(f"📖 Learn {s}")
                st.write("🔨 Build 1 portfolio project")
                st.write("📱 Start posting on LinkedIn")
            with col_m3:
                st.markdown("### Month 3: Launching")
                for s in month3:
                    st.write(f"📖 Learn {s}")
                st.write("🎓 Get a certification")
                st.write("📧 Start applying to jobs")
                st.write("🤝 Network with 10 people")

        st.markdown("---")
        st.subheader("Certifications to Pursue")
        for cert in field["certifications"]:
            st.write(f"🎓 {cert}")

    # ============================================================
    # TAB 6: POST IDEAS
    # ============================================================
    with tab6:
        st.header(f"LinkedIn Post Ideas ({tone_name} tone)")

        if "Friendly" in tone_name:
            posts = [
                f"I started learning {target.lower()} [X] months ago and I'm honestly loving the journey! Here's what I've picked up so far...",
                f"Just built my first [project name] using Python and I'm so proud! Here's what the data told me...",
                f"One thing I wish someone told me when I started: you don't need to know everything to begin. Just start somewhere!",
                f"Quick question for anyone in {target.lower()}: what's the one skill you wish you'd learned sooner?",
                f"This week I learned: [1 thing]. Built: [1 thing]. Next week: [1 goal]. Small steps add up!"
            ]
        elif "Humanised" in tone_name:
            posts = [
                f"I'll be honest: {target.lower()} scared me at first. I had zero technical background. But [X] months in, here's where I am...",
                f"Nobody tells you this about learning {target.lower()}: the first project takes 10x longer than you think. But finishing it? That feeling is unmatched.",
                f"I came from {prev.lower() if prev else 'a completely different field'}. Everyone said I was crazy for switching. Here's what actually happened...",
                f"Broke my code 47 times today. Fixed it 47 times. That's basically what learning {target.lower()} looks like.",
                f"Real talk: imposter syndrome hit me hard this week. But then I looked back at where I was 3 months ago and..."
            ]
        elif "Professional" in tone_name:
            posts = [
                f"Key insight from my {target.lower()} studies this week: [insight]. Implications for businesses: [1-2 sentences].",
                f"I recently completed [certification/course] in {target.lower()}. Three key takeaways for professionals considering this field...",
                f"The gap between business acumen and technical proficiency is where the real value lies. Here's why...",
                f"This week's learning: [tool/concept]. How it applies to [industry/business problem].",
                f"Reflections on [X] months of systematic skill development in {target.lower()}: progress, challenges, and next steps."
            ]
        elif "Confident" in tone_name:
            posts = [
                f"I don't have a CS degree. I taught myself {target.lower()}. Here are the projects to prove it.",
                f"Everyone's talking about {target.lower()}. I'm actually building things with it. Big difference.",
                f"Stop consuming tutorials. Start building projects. That's it. That's the post.",
                f"My background in {prev.lower() if prev else 'business'} isn't a disadvantage in {target.lower()}. It's my superpower. Let me explain.",
                f"Hot take: you don't need permission to call yourself a {target.lower()} professional. You need projects."
            ]
        else:
            posts = [
                f"It started with a single CSV file and a question I couldn't stop thinking about...",
                f"Three months ago, I didn't know what Python was. Today I built [project]. Here's everything that happened in between...",
                f"Plot twist: the {prev.lower() if prev else 'business'} skills I thought were useless turned out to be my biggest advantage in {target.lower()}.",
                f"If my career was a movie, this chapter would be called: The Pivot. And it would start with...",
                f"Someone once told me I was too late to get into {target.lower()}. Here's what I built to prove them wrong."
            ]

        for i, post in enumerate(posts, 1):
            st.markdown(f'<div class="result-box"><strong>Post Idea {i}:</strong><br><br>"{post}"</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("Posting Strategy")
        st.write("📅 Aim for **2-3 posts per week**")
        st.write("🕐 Best times: **Tuesday to Thursday, 8-10 AM** your timezone")
        st.write("📸 Always add an **image or screenshot** (2x more engagement)")
        st.write("❓ End every post with a **question** to get comments")
        st.write("💬 Reply to **EVERY comment** within an hour")
        st.write("🤝 Engage with **5-10 other posts** before you publish yours")

    # ============================================================
    # TAB 7: ASK COACH (CHAT AGENT)
    # ============================================================
    with tab7:
        st.header("Ask Your Career Coach")
        st.caption("Ask me anything about your career, job search, skills, interviews, or LinkedIn!")

        # Initialize chat history
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = [
                {"role": "assistant", "content": f"Hey {profile['name'].split()[0]}! I'm your Career Coach. Ask me anything about {profile['target_field']}, job searching, LinkedIn, CVs, interviews, or career planning. What's on your mind?"}
            ]

        # Display chat history
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if user_question := st.chat_input("Ask me anything about your career..."):
            # Add user message
            st.session_state.chat_messages.append({"role": "user", "content": user_question})
            with st.chat_message("user"):
                st.markdown(user_question)

            # Generate response based on keywords
            q = user_question.lower()
            response = ""
            pivoter = profile["stage"] == "Career pivoter" and profile["previous_field"]

            # --- SALARY / NEGOTIATION ---
            if any(w in q for w in ["salary", "pay", "earn", "money", "income", "compensation", "wage", "negotiat"]):
                salaries = field["avg_salary_gbp"]
                response = f"**{profile['target_field']} Salary Landscape (UK, 2025):**\n\n"
                for level, amount in salaries.items():
                    response += f"- **{level}:** £{amount:,}/year\n"
                response += f"\n**Market context:** Demand is **{field['demand_level']}** with **{field['remote_friendly']}** remote flexibility. London typically pays 15-25% above these averages. European hubs like {', '.join(field['top_cities_eu'][:3])} offer comparable packages.\n\n"
                response += "**Negotiation strategy (from career coaches and r/jobs):**\n"
                response += "1. Never share your current salary. Say: 'I'd prefer to discuss what this role pays.'\n"
                response += "2. Let them name a number first. If pushed, give a researched range based on Glassdoor/Levels.fyi data.\n"
                response += "3. Once you get an offer, always negotiate. Even a 5-10% bump compounds over your career.\n"
                response += "4. Negotiate beyond salary: remote days, signing bonus, learning budget, review timeline.\n"
                response += "5. Frame it as: 'Based on my research and the scope of this role, I was expecting closer to £X.'"

            # --- SKILLS / LEARNING ---
            elif any(w in q for w in ["skill", "learn", "study", "course", "training", "upskill", "what should i"]):
                have = [s for s in field["technical_skills"] + field["soft_skills"] if s in profile["existing_skills"]]
                missing = [s for s in field["technical_skills"] if s not in profile["existing_skills"]]
                response = f"**Your {profile['target_field']} Skill Assessment:**\n\n"
                if have:
                    response += f"**You already have:** {', '.join(have)} — this is a solid foundation.\n\n"
                if missing:
                    top_3 = missing[:3]
                    response += f"**Priority #1 (learn these first):** {', '.join(top_3)}\n"
                    if len(missing) > 3:
                        response += f"**Priority #2 (next quarter):** {', '.join(missing[3:6])}\n"
                response += f"\n**Learning strategy (what actually works):**\n"
                response += f"1. Pick ONE skill. Spend 2-3 weeks on a structured course.\n"
                response += f"2. Immediately build a small project with it. This is non-negotiable. Tutorials without projects = wasted time.\n"
                response += f"3. Document what you built on GitHub with a proper README.\n"
                response += f"4. Post about it on LinkedIn. Then move to the next skill.\n\n"
                response += f"**Certifications recruiters actually value:** {', '.join(field['certifications'][:3])}\n\n"
                response += "**Where to learn for free/cheap:** Google Certificates (Coursera), freeCodeCamp, Khan Academy, YouTube (but be selective), Kaggle (for data projects)."

            # --- INTERVIEW ---
            elif any(w in q for w in ["interview", "question", "prepare", "nervous", "scared", "anxiety"]):
                response = f"**Interview Prep Blueprint for {profile['target_field']}:**\n\n"
                response += f"**Technical topics they will test:** {', '.join(field['interview_topics'])}\n\n"
                response += "**The 5 questions you WILL be asked:**\n\n"
                response += "1. **'Tell me about yourself'** — Use Present-Past-Future in 90 seconds. End with why you want THIS role.\n\n"
                if pivoter:
                    response += f"2. **'Why the career change?'** — Frame it as intentional: 'In {profile['previous_field'].lower()}, the most impactful work was data-driven. I wanted to be the person generating those insights.'\n\n"
                else:
                    response += f"2. **'Why {target}?'** — Show it was a deliberate choice backed by action, not a random interest.\n\n"
                response += "3. **'Walk me through a project'** — Structure: Problem → Approach → Tools → Findings → Impact. Under 2 minutes.\n\n"
                response += "4. **'What is your weakness?'** — Pick something real, not critical to the role, and show what you are doing about it.\n\n"
                response += "5. **'Do you have questions for us?'** — Always say yes. Ask about team structure, success metrics, or current challenges.\n\n"
                response += "**STAR method for behavioural questions:** Situation (2 sentences) → Task (your responsibility) → Action (what YOU did) → Result (with numbers).\n\n"
                response += "**Pro tips from hiring managers (Reddit r/jobs):**\n"
                response += "- Practice answers OUT LOUD, not just in your head\n"
                response += "- Research the interviewer on LinkedIn before the call\n"
                response += "- Send a personalised thank-you email within 24 hours\n"
                response += "- Silence is okay. Take a breath before answering."

            # --- CV / RESUME ---
            elif any(w in q for w in ["cv", "resume", "curriculum"]):
                response = f"**CV Strategy for {profile['target_field']} (ATS-Optimised):**\n\n"
                response += f"**Your CV tone:** {tone['cv_tone']}\n\n"
                response += "**Structure (single-column, reverse chronological):**\n"
                response += "1. **Header** — Name, city, email, LinkedIn, GitHub\n"
                response += "2. **Professional Summary** — 3-4 lines. Formula: Who you are + key skills + what you deliver + target role\n"
                response += f"3. **Core Skills** — {', '.join(field['technical_skills'][:6])}\n"
                response += "4. **Experience** — Each bullet: Action Verb + What + Measurable Result\n"
                response += "5. **Projects** — This replaces lack of experience. Include GitHub links.\n"
                response += "6. **Education** — Degree, university, relevant modules\n"
                response += f"7. **Certifications** — {', '.join(field['certifications'][:2])}\n\n"
                response += "**Rules that get you past ATS (from r/resumes):**\n"
                response += "- Single-column layout. No graphics, icons, or two-column designs.\n"
                response += "- Mirror exact keywords from the job description.\n"
                response += "- Never write 'Responsible for...' — write achievements with numbers.\n"
                response += "- 1 page for under 5 years experience. No exceptions.\n"
                response += "- Save as PDF unless they specifically ask for .docx.\n\n"
                response += "**Power verbs to use:** Accelerated, Analysed, Automated, Built, Delivered, Designed, Drove, Identified, Optimised, Reduced, Streamlined, Transformed."

            # --- COVER LETTER ---
            elif any(w in q for w in ["cover letter", "covering letter", "application letter"]):
                response = f"**Cover Letter Framework ({tone['cover_letter_style']} tone):**\n\n"
                response += "A cover letter answers one question: **Why you, why this role, why this company?**\n\n"
                response += "**Paragraph 1 — The Hook:** Name the role. Show you researched the company. Reference something specific (recent news, a product, a value).\n\n"
                response += "**Paragraph 2 — Evidence:** Match 2-3 of your skills to their requirements. Include ONE specific achievement with a number. Do not restate your CV.\n\n"
                response += "**Paragraph 3 — Why This Company:** Demonstrate homework. What makes them different from competitors? What do YOU bring that others cannot?\n\n"
                response += "**Paragraph 4 — The Close:** Express enthusiasm. State availability. Be confident, not desperate.\n\n"
                response += "**Critical rules (from hiring managers on r/jobs):**\n"
                response += "- Address it to the hiring manager by name. Check LinkedIn.\n"
                response += "- Never apologise for lack of experience. Frame your background as an asset.\n"
                response += "- Keep it under one page. 3-4 paragraphs maximum.\n"
                response += "- Your CV, LinkedIn, and cover letter must tell the same consistent story.\n"
                response += "- A generic cover letter is worse than no cover letter."

            # --- LINKEDIN ---
            elif any(w in q for w in ["linkedin", "profile", "headline", "post", "connection", "visibility"]):
                response = f"**LinkedIn Optimisation Strategy (based on 2025 best practices):**\n\n"
                response += "**Your headline** is the #1 factor. Recruiters search by job title + skills. If those words are not in your headline, you are invisible. Formula: **Role + Key Skills + Value + Differentiator**.\n\n"
                response += "**Your About section** — First 3 lines show before 'See more'. Lead with your strongest hook. End with pipe-separated keywords for search indexing.\n\n"
                response += "**Posting strategy (what actually moves the needle):**\n"
                response += "- Post 2-3x per week, Tue-Thu, 8-10 AM your timezone\n"
                response += "- Share your learning journey with screenshots of real work\n"
                response += "- Engage with 5-10 posts BEFORE you publish yours (the algorithm rewards active users)\n"
                response += "- Reply to every comment within an hour\n"
                response += "- Images and carousels get 2-3x more engagement than text-only posts\n\n"
                response += "**Profile completeness matters:** Profiles with all sections filled get 20x more views and 9x more connection requests.\n\n"
                response += f"**Keywords for your field:** {', '.join(field['keywords'][:7])}\n\n"
                response += "Check the **LinkedIn** and **Post Ideas** tabs for ready-to-paste content."

            # --- JOB SEARCH ---
            elif any(w in q for w in ["job", "apply", "application", "hire", "hiring", "recruit", "vacancy", "opening", "where to find"]):
                response = f"**Job Search Strategy for {profile['target_field']}:**\n\n"
                response += f"**Job titles to search:** {', '.join(field['job_titles'])}\n\n"
                response += f"**Top markets:** UK — {', '.join(field['top_cities_uk'][:3])} | EU — {', '.join(field['top_cities_eu'][:3])}\n\n"
                response += "**Where to look (ranked by effectiveness):**\n"
                response += "1. **Company career pages directly** — Many roles never make it to job boards\n"
                response += "2. **LinkedIn Jobs** — Set alerts for your target titles. Apply within 24 hours of posting.\n"
                response += "3. **Indeed / Glassdoor / Reed** (UK) — Cast a wider net\n"
                response += "4. **Networking** — 70% of jobs are filled through connections (LinkedIn data)\n"
                response += "5. **Recruiters** — Follow and engage with recruiters in your field on LinkedIn\n\n"
                response += "**The numbers game (from r/jobs):**\n"
                response += "- Apply to 5-10 targeted roles per week (quality over quantity)\n"
                response += "- Tailor your CV for each application. Mirror their exact keywords.\n"
                response += "- Track every application in a spreadsheet: company, role, date, status, follow-up\n"
                response += "- Follow up after 1 week if no response. A polite email can move you from 'maybe' to 'interview'.\n"
                response += "- Expect a 5-10% interview rate. This is normal. Keep going."

            # --- CERTIFICATION ---
            elif any(w in q for w in ["certif", "certificate", "credential", "badge"]):
                response = f"**Certifications That Actually Matter for {profile['target_field']}:**\n\n"
                for cert in field["certifications"]:
                    response += f"- **{cert}**\n"
                response += "\n**How to prioritise:**\n"
                response += "1. Start with Google or IBM certificates — they are affordable, widely recognised, and beginner-friendly.\n"
                response += "2. Check job postings in your target field. If 3+ listings mention a specific cert, get that one.\n"
                response += "3. One completed certification + one project using that skill is worth more than 5 certificates with no projects.\n\n"
                response += "**Where to get them:** Coursera, Google Career Certificates, edX, LinkedIn Learning, provider websites.\n\n"
                response += "**Pro tip from recruiters:** Certifications open doors, but projects close deals. Always pair a cert with a portfolio piece."

            # --- CAREER PIVOT ---
            elif any(w in q for w in ["pivot", "switch", "change career", "transition", "career change"]):
                prev_field = profile["previous_field"]
                response = f"**Career Pivot Playbook:**\n\n"
                if prev_field:
                    response += f"Your {prev_field.lower()} background is not a liability. It is your competitive advantage. Most {target.lower()} professionals lack business domain knowledge. You have it.\n\n"
                response += "**The 6-step pivot framework:**\n\n"
                response += f"**Step 1 — Skill foundation (Month 1-2):** Learn {', '.join(field['technical_skills'][:3])} through one structured course. Google Certificates or IBM on Coursera are ideal starting points.\n\n"
                response += "**Step 2 — Build proof (Month 2-3):** Create 2-3 portfolio projects on GitHub. Each project should solve a real problem using real (or realistic) data. Write proper READMEs.\n\n"
                response += f"**Step 3 — Get certified (Month 3):** Complete {field['certifications'][0]}. This signals commitment to hiring managers.\n\n"
                response += "**Step 4 — Reframe your story:** Rewrite your LinkedIn and CV to position your past experience as a strength, not a gap. Use the LinkedIn tab for specific rewrites.\n\n"
                response += "**Step 5 — Build visibility (Ongoing):** Post about your journey on LinkedIn 2-3x per week. Share what you are building. Engage with people in your target field.\n\n"
                response += "**Step 6 — Apply strategically:** Target roles that value your domain knowledge. A 'Data Analyst' role in a company from your previous industry is the perfect bridge.\n\n"
                response += "**Key insight from r/careerguidance:** The most successful career changers are the ones who treat the transition like a project with milestones, not a hope with a deadline."

            # --- PORTFOLIO / PROJECTS ---
            elif any(w in q for w in ["project", "portfolio", "github", "build", "showcase", "what should i build"]):
                response = f"**Portfolio Strategy for {profile['target_field']}:**\n\n"
                response += "A strong portfolio beats years of experience for entry-level roles. Hiring managers on r/resumes consistently say: 'Show me what you built.'\n\n"
                response += "**The 3-project portfolio:**\n\n"
                response += f"1. **Data cleaning + analysis project** — Take a messy real-world dataset (Kaggle, government data), clean it, analyse it, and present 3-5 actionable findings. Tools: {field['technical_skills'][0]}, {field['technical_skills'][1]}.\n\n"
                response += f"2. **Automation or tool project** — Build something useful. A tracker, a dashboard, a report generator. Show you can build things that save time. Tools: Python, {field['technical_skills'][2] if len(field['technical_skills']) > 2 else 'Excel'}.\n\n"
                response += f"3. **Visualisation or storytelling project** — Create an interactive dashboard or visual report that tells a story. Tools: {field['technical_skills'][3] if len(field['technical_skills']) > 3 else 'Tableau'}, {field['technical_skills'][4] if len(field['technical_skills']) > 4 else 'Excel'}.\n\n"
                response += "**README template for each project:**\n"
                response += "- **Problem:** What question are you answering?\n"
                response += "- **Data:** Where did it come from? How big?\n"
                response += "- **Approach:** What tools and methods did you use?\n"
                response += "- **Key Findings:** 3-5 bullet points with insights\n"
                response += "- **What I Learned:** Honest reflection\n\n"
                response += "**Where to share:** GitHub (primary), LinkedIn posts showing your process, personal portfolio website (Google Stitch, GitHub Pages, or Notion)."

            # --- REMOTE WORK ---
            elif any(w in q for w in ["remote", "work from home", "hybrid", "flexible"]):
                response = f"**Remote Work in {profile['target_field']}:**\n\n"
                response += f"Remote friendliness for your field: **{field['remote_friendly']}**\n\n"
                response += "**How to land remote roles:**\n"
                response += "1. Filter job searches specifically for 'remote' or 'hybrid'\n"
                response += "2. Highlight async communication skills on your CV and LinkedIn\n"
                response += "3. Mention experience with remote tools: Slack, Zoom, Jira, Notion, Confluence\n"
                response += "4. Consider time zone compatibility for international roles\n"
                response += "5. Build a strong online presence — remote hiring relies heavily on your digital footprint\n\n"
                response += "**Remote-friendly job boards:** LinkedIn (remote filter), We Work Remotely, Remote.co, FlexJobs, AngelList/Wellfound (startups).\n\n"
                response += "**Pro tip:** Remote roles get 3-5x more applications than on-site ones. Your CV needs to be exceptionally targeted."

            # --- MOTIVATION / IMPOSTER SYNDROME ---
            elif any(w in q for w in ["motivat", "imposter", "stuck", "overwhelm", "give up", "discourage", "doubt", "confiden", "burnout", "tired", "lost"]):
                response = "**Let me be direct with you:**\n\n"
                response += "What you are feeling is not a sign that you are failing. It is a sign that you are doing something hard. Every person who successfully pivoted or landed their first role in a new field went through exactly this.\n\n"
                response += "**What the research says:** Imposter syndrome affects 70% of professionals at some point. It is especially common among career changers and self-taught learners. It means you care about doing good work.\n\n"
                response += "**Practical steps (not just 'believe in yourself'):**\n\n"
                response += "1. **Track your progress.** Open a note and write down 3 things you can do today that you could not do 3 months ago. The list will surprise you.\n\n"
                response += "2. **Shrink the scope.** You do not need to learn everything. Pick ONE skill, ONE project, ONE application. Finish it. Then pick the next one.\n\n"
                response += "3. **Compare down, not up.** Stop comparing yourself to people with 5 years of experience. Compare yourself to where you were 90 days ago.\n\n"
                response += "4. **Ship something imperfect.** A finished project with flaws teaches you more than a perfect tutorial you never apply.\n\n"
                response += "5. **Talk to people on the same path.** Reddit communities like r/careerguidance and r/learnprogramming are full of people in your exact situation. You are not alone in this.\n\n"
                response += f"You chose **{profile['target_field']}** deliberately. That took courage. The hard part is already behind you. Now it is about consistency."

            # --- NETWORKING ---
            elif any(w in q for w in ["network", "connect", "mentor", "communit", "people"]):
                response = "**Networking Strategy (for people who hate networking):**\n\n"
                response += "Networking is not about asking strangers for jobs. It is about building relationships that naturally lead to opportunities. 70% of jobs are filled through connections.\n\n"
                response += "**LinkedIn networking (highest ROI):**\n"
                response += "- Comment genuinely on 5 posts per day from people in your target field\n"
                response += "- Send 3-5 connection requests per week with a personalised note\n"
                response += "- Never lead with 'Can you help me find a job?' Lead with curiosity.\n\n"
                response += "**Connection request template:**\n"
                response += "*'Hi [Name], I came across your post about [topic] and it resonated with me. I am currently building my skills in [field] and transitioning from [background]. Would love to follow your journey and learn from your experience.'*\n\n"
                response += "**Coffee chat request template:**\n"
                response += "*'Hi [Name], I have been following your work in [field] and really admire [specific thing]. I am making a career transition into this area and would love to hear about your experience. Would you have 15 minutes for a virtual coffee sometime?'*\n\n"
                response += "**Where to find communities:** r/careerguidance, r/datascience (Reddit), Meetup.com, local tech/data events on Eventbrite, Discord servers, LinkedIn groups.\n\n"
                response += "**Golden rule:** Give before you ask. Share resources, congratulate wins, add value to conversations."

            # --- ATS ---
            elif any(w in q for w in ["ats", "applicant tracking", "keyword", "filter", "screen"]):
                response = "**How ATS (Applicant Tracking Systems) Actually Work:**\n\n"
                response += "Over 75% of CVs are rejected by ATS before a human sees them. Here is how to beat it:\n\n"
                response += "**1. Keywords are everything.** Copy exact phrases from the job description into your CV. If they say 'data visualisation', use 'data visualisation' — not 'creating charts'.\n\n"
                response += "**2. Use a single-column layout.** Two-column, graphic-heavy, or creative templates break ATS parsing.\n\n"
                response += "**3. Standard section headings.** Use 'Experience', 'Education', 'Skills' — not 'My Journey' or 'What I Bring'.\n\n"
                response += "**4. Save as PDF** unless they specifically request .docx.\n\n"
                response += "**5. No headers/footers.** ATS often cannot read content in header/footer areas.\n\n"
                response += "**6. Spell out acronyms.** Write 'Search Engine Optimisation (SEO)' so the ATS catches both versions.\n\n"
                response += "**Quick test:** Copy your CV text into a plain text editor. If it reads cleanly in order, ATS can parse it. If it is jumbled, fix your template."

            # --- GENERAL / CATCH-ALL ---
            else:
                response = f"I am here to help, {profile['name'].split()[0]}. Based on your profile as a **{profile['stage'].lower()}** targeting **{profile['target_field']}**"
                if profile["city"]:
                    response += f" in **{profile['city']}**"
                response += ", here are the topics I can give you expert guidance on:\n\n"
                response += "- **'What salary can I expect?'** — Field-specific salary data + negotiation tactics\n"
                response += "- **'What should I learn next?'** — Personalised skill assessment + learning strategy\n"
                response += "- **'How do I prepare for interviews?'** — Question breakdowns + STAR method + practice tips\n"
                response += "- **'Help with my CV'** — ATS-optimised structure + power verbs + examples\n"
                response += "- **'Cover letter advice'** — 4-paragraph framework with tone-matched examples\n"
                response += "- **'How do I improve my LinkedIn?'** — Headline formulas + posting strategy + keyword optimisation\n"
                response += "- **'Where do I find jobs?'** — Platforms, search titles, application tracking\n"
                response += "- **'How do I switch careers?'** — 6-step pivot playbook\n"
                response += "- **'What should I build?'** — 3-project portfolio strategy with README templates\n"
                response += "- **'What is ATS?'** — How applicant tracking systems filter your CV\n"
                response += "- **'I feel stuck'** — Evidence-based strategies for imposter syndrome and motivation\n"
                response += "- **'How do I network?'** — Templates + communities + LinkedIn strategy\n\n"
                response += "Ask me anything. I will give you specific, actionable advice based on your situation."

            # Add assistant response
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
