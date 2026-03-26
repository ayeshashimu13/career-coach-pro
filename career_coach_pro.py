"""
Career Coach Pro - Your Personal Career Agency
==============================================================
A Python tool that acts as your personal career agency. Whether
you're just starting out, pivoting careers, or levelling up,
this tool helps you with everything: LinkedIn optimization,
CV tips, cover letter writing, job market insights, interview
prep, skill recommendations, and career planning.

Built for anyone who wants professional guidance without paying
for a career consultant.

Built by: Ayesha Shimu
Skills demonstrated: String manipulation, dictionaries, lists, loops,
                     input handling, f-strings, functions, data-driven
                     content generation, file I/O, datetime, try/except
"""

import csv
import os
from datetime import datetime

# ============================================================
# STEP 1: CONFIGURATION
# ============================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "generated_content")

# Writing tones
TONES = {
    "1": {
        "name": "Friendly & Warm",
        "description": "Approachable, conversational, like talking to a supportive friend",
        "opening_words": ["I", "My journey", "What excites me", "I love", "Growing up"],
        "connectors": ["and honestly", "which is why", "the cool thing is", "what really got me was"],
        "closers": ["Always happy to connect!", "Let's chat!", "Feel free to reach out!", "Would love to hear your story too!"],
        "power_words": ["passionate about", "genuinely excited", "love working with", "fascinated by", "drawn to"],
        "cv_tone": "warm but professional",
        "cover_letter_style": "enthusiastic and personable"
    },
    "2": {
        "name": "Humanised & Real",
        "description": "Honest, authentic, sounds like a real person wrote it (not AI)",
        "opening_words": ["Honestly", "Here's the thing", "I'll be real", "Not going to lie", "Truth is"],
        "connectors": ["and that's when", "turns out", "the thing nobody tells you is", "what actually happened was"],
        "closers": ["Hit me up if you relate.", "DMs always open.", "If this resonates, let's connect.", "Still figuring it out, but enjoying the ride."],
        "power_words": ["figured out", "stumbled into", "taught myself", "actually enjoy", "hands-on experience with"],
        "cv_tone": "authentic and grounded",
        "cover_letter_style": "honest and relatable"
    },
    "3": {
        "name": "Professional & Polished",
        "description": "Corporate-ready, structured, ideal for traditional industries",
        "opening_words": ["With a background in", "As a", "Having developed", "Drawing on", "Throughout my career"],
        "connectors": ["consequently", "this experience has equipped me", "building upon this", "in addition to"],
        "closers": ["I welcome the opportunity to connect.", "I look forward to contributing.", "Open to professional discussions.", "Seeking to collaborate with like-minded professionals."],
        "power_words": ["demonstrated expertise in", "proven ability to", "extensive experience with", "proficient in", "committed to"],
        "cv_tone": "formal and structured",
        "cover_letter_style": "formal and polished"
    },
    "4": {
        "name": "Confident & Bold",
        "description": "Strong, assertive, shows you know your worth",
        "opening_words": ["I build", "I turn", "I help", "I specialise in", "I make"],
        "connectors": ["and here's the proof", "the result?", "what sets me apart is", "I don't just talk about it"],
        "closers": ["Ready to bring this energy to your team.", "Let's make things happen.", "If you need results, let's talk.", "I deliver. Simple as that."],
        "power_words": ["expert at", "specialise in", "deliver results with", "drive impact through", "known for"],
        "cv_tone": "assertive and results-focused",
        "cover_letter_style": "bold and direct"
    },
    "5": {
        "name": "Creative & Storytelling",
        "description": "Narrative-driven, engaging, makes people want to keep reading",
        "opening_words": ["It started with", "Somewhere between", "Picture this", "There's a moment when", "Three years ago"],
        "connectors": ["that's when everything changed", "and I haven't looked back since", "fast forward to today", "little did I know"],
        "closers": ["The next chapter? That's where you come in.", "This is just the beginning.", "The story continues...", "Every chapter leads somewhere new."],
        "power_words": ["discovered a passion for", "fell in love with", "found my calling in", "transformed my approach to", "unlocked potential in"],
        "cv_tone": "narrative and engaging",
        "cover_letter_style": "story-driven and compelling"
    }
}


def choose_tone():
    """Let the user pick their preferred writing tone."""
    print("\n" + "=" * 55)
    print("  CHOOSE YOUR WRITING TONE")
    print("  This will shape how all your content sounds!")
    print("=" * 55)

    for key, tone in TONES.items():
        print(f"\n  {key}. {tone['name']}")
        print(f"     {tone['description']}")
        print(f"     Example opener: \"{tone['opening_words'][0]}...\"")
        print(f"     Example closer: \"{tone['closers'][0]}\"")

    while True:
        choice = input("\n  Pick your tone (1-5): ").strip()
        if choice in TONES:
            tone = TONES[choice]
            print(f"\n  Great choice! All your content will be written in a")
            print(f"  '{tone['name']}' tone. You can change this anytime from the menu.")
            return tone
        print("  Please pick a number between 1 and 5!")

# Career fields and their data
CAREER_FIELDS = {
    "1": "Data Analytics",
    "2": "AI / Machine Learning",
    "3": "Business Intelligence",
    "4": "Digital Marketing",
    "5": "Product Management",
    "6": "UX Design / Research",
    "7": "Software Development",
    "8": "Project Management",
    "9": "Finance / Accounting",
    "10": "Supply Chain / Operations",
    "11": "Human Resources",
    "12": "Sales / Business Development"
}

# Comprehensive field data
FIELD_DATA = {
    "Data Analytics": {
        "technical_skills": ["Python", "SQL", "Excel", "Tableau", "Power BI", "R", "Statistics", "Google Sheets"],
        "soft_skills": ["Storytelling with data", "Problem solving", "Critical thinking", "Communication", "Attention to detail"],
        "certifications": ["Google Data Analytics Certificate", "IBM Data Analyst", "Microsoft Power BI", "Tableau Desktop Specialist"],
        "keywords": ["data-driven", "insights", "analytics", "visualization", "reporting", "KPIs", "dashboards", "trends"],
        "avg_salary_gbp": {"entry": 28000, "mid": 45000, "senior": 65000},
        "job_titles": ["Data Analyst", "Junior Data Analyst", "Business Data Analyst", "Analytics Consultant", "Reporting Analyst"],
        "interview_topics": ["SQL queries", "Data cleaning scenarios", "Dashboard design", "Stakeholder communication", "A/B testing basics"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Birmingham", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Copenhagen", "Dublin", "Stockholm"],
        "demand_level": "Very High",
        "remote_friendly": "High"
    },
    "AI / Machine Learning": {
        "technical_skills": ["Python", "TensorFlow", "PyTorch", "SQL", "Machine Learning", "NLP", "Deep Learning", "Statistics"],
        "soft_skills": ["Research mindset", "Problem solving", "Adaptability", "Communication", "Curiosity"],
        "certifications": ["Google AI Essentials", "DeepLearning.AI Specialization", "Stanford ML Course", "AWS ML Specialty"],
        "keywords": ["AI", "machine learning", "automation", "neural networks", "models", "predictions", "NLP"],
        "avg_salary_gbp": {"entry": 35000, "mid": 55000, "senior": 85000},
        "job_titles": ["ML Engineer", "AI Engineer", "Data Scientist", "NLP Engineer", "AI Research Analyst"],
        "interview_topics": ["Algorithm design", "Model evaluation metrics", "Feature engineering", "Bias in AI", "System design"],
        "top_cities_uk": ["London", "Cambridge", "Edinburgh", "Manchester", "Bristol"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Zurich", "Stockholm", "Copenhagen"],
        "demand_level": "Very High",
        "remote_friendly": "High"
    },
    "Business Intelligence": {
        "technical_skills": ["SQL", "Power BI", "Tableau", "Excel", "DAX", "ETL", "Data Warehousing", "SSRS"],
        "soft_skills": ["Business acumen", "Stakeholder management", "Presentation skills", "Analytical thinking"],
        "certifications": ["Microsoft PL-300", "Tableau Desktop Specialist", "Google BI Certificate"],
        "keywords": ["BI", "dashboards", "reporting", "data warehouse", "business insights", "KPIs", "ETL"],
        "avg_salary_gbp": {"entry": 30000, "mid": 48000, "senior": 70000},
        "job_titles": ["BI Analyst", "BI Developer", "BI Consultant", "Reporting Analyst", "Data Engineer"],
        "interview_topics": ["Data modelling", "Dashboard best practices", "SQL optimization", "Business requirements gathering"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Leeds", "Edinburgh"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Dublin", "Copenhagen", "Munich"],
        "demand_level": "High",
        "remote_friendly": "Medium"
    },
    "Digital Marketing": {
        "technical_skills": ["Google Analytics", "SEO", "SEM", "Social Media Tools", "A/B Testing", "CRM", "Email Marketing"],
        "soft_skills": ["Creativity", "Communication", "Trend analysis", "Copywriting", "Strategic thinking"],
        "certifications": ["Google Digital Marketing", "HubSpot Inbound", "Meta Marketing Analytics", "Google Ads"],
        "keywords": ["campaigns", "conversion", "engagement", "ROI", "content strategy", "growth", "SEO"],
        "avg_salary_gbp": {"entry": 24000, "mid": 38000, "senior": 55000},
        "job_titles": ["Digital Marketing Executive", "SEO Specialist", "Content Marketer", "Growth Marketer", "Marketing Analyst"],
        "interview_topics": ["Campaign strategy", "SEO fundamentals", "Analytics interpretation", "Content planning", "Budget allocation"],
        "top_cities_uk": ["London", "Manchester", "Bristol", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Barcelona", "Dublin", "Stockholm"],
        "demand_level": "High",
        "remote_friendly": "Very High"
    },
    "Product Management": {
        "technical_skills": ["Jira", "SQL", "A/B Testing", "Figma", "Roadmapping", "Analytics Tools", "Miro"],
        "soft_skills": ["Leadership", "Prioritization", "User empathy", "Cross-functional collaboration", "Decision making"],
        "certifications": ["Google PM Certificate", "Pragmatic Institute", "Product School", "Scrum Product Owner"],
        "keywords": ["product strategy", "user needs", "roadmap", "agile", "stakeholders", "MVP", "backlog"],
        "avg_salary_gbp": {"entry": 35000, "mid": 55000, "senior": 80000},
        "job_titles": ["Associate PM", "Product Manager", "Product Owner", "Technical PM", "Senior PM"],
        "interview_topics": ["Product sense", "Prioritization frameworks", "Metrics definition", "User stories", "Go-to-market strategy"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Cambridge", "Bristol"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Stockholm", "Dublin", "Copenhagen"],
        "demand_level": "High",
        "remote_friendly": "High"
    },
    "UX Design / Research": {
        "technical_skills": ["Figma", "User Interviews", "Surveys", "Usability Testing", "Wireframing", "Prototyping"],
        "soft_skills": ["Empathy", "Active listening", "Communication", "Pattern recognition", "Visual thinking"],
        "certifications": ["Google UX Design", "Nielsen Norman Group", "Interaction Design Foundation"],
        "keywords": ["user experience", "research", "usability", "user needs", "design thinking", "wireframes"],
        "avg_salary_gbp": {"entry": 28000, "mid": 42000, "senior": 60000},
        "job_titles": ["UX Researcher", "UX Designer", "UI/UX Designer", "Product Designer", "Design Researcher"],
        "interview_topics": ["Portfolio walkthrough", "Research methodology", "Design critique", "Accessibility", "User testing scenarios"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Bristol", "Brighton"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Copenhagen", "Stockholm", "Barcelona"],
        "demand_level": "Medium",
        "remote_friendly": "High"
    },
    "Software Development": {
        "technical_skills": ["Python", "JavaScript", "Git", "HTML/CSS", "APIs", "Databases", "React", "Node.js"],
        "soft_skills": ["Problem solving", "Debugging mindset", "Collaboration", "Continuous learning", "Communication"],
        "certifications": ["freeCodeCamp", "CS50", "AWS Cloud Practitioner", "Meta Front-End Developer"],
        "keywords": ["development", "code", "full-stack", "applications", "APIs", "deployment", "agile"],
        "avg_salary_gbp": {"entry": 30000, "mid": 50000, "senior": 75000},
        "job_titles": ["Junior Developer", "Software Engineer", "Front-End Developer", "Full-Stack Developer", "Backend Developer"],
        "interview_topics": ["Coding challenges", "System design", "Data structures", "API design", "Version control"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Bristol", "Cambridge"],
        "top_cities_eu": ["Amsterdam", "Berlin", "Stockholm", "Dublin", "Copenhagen"],
        "demand_level": "Very High",
        "remote_friendly": "Very High"
    },
    "Project Management": {
        "technical_skills": ["Jira", "Asana", "MS Project", "Excel", "Gantt Charts", "Agile", "Scrum", "Confluence"],
        "soft_skills": ["Leadership", "Communication", "Risk management", "Time management", "Negotiation"],
        "certifications": ["PMP", "PRINCE2", "Google PM Certificate", "Scrum Master", "Agile Certified"],
        "keywords": ["project delivery", "stakeholders", "timeline", "budget", "agile", "milestones", "risk"],
        "avg_salary_gbp": {"entry": 28000, "mid": 45000, "senior": 65000},
        "job_titles": ["Project Coordinator", "Project Manager", "Scrum Master", "Programme Manager", "PMO Analyst"],
        "interview_topics": ["Conflict resolution", "Risk mitigation", "Stakeholder management", "Agile vs Waterfall", "Budget tracking"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Dublin", "Berlin", "Copenhagen", "Munich"],
        "demand_level": "High",
        "remote_friendly": "Medium"
    },
    "Finance / Accounting": {
        "technical_skills": ["Excel", "Financial Modelling", "SAP", "QuickBooks", "Power BI", "SQL", "VBA"],
        "soft_skills": ["Attention to detail", "Analytical thinking", "Ethics", "Communication", "Numeracy"],
        "certifications": ["ACCA", "CIMA", "CFA", "AAT", "Xero Advisor"],
        "keywords": ["financial analysis", "budgeting", "forecasting", "reporting", "audit", "compliance", "P&L"],
        "avg_salary_gbp": {"entry": 26000, "mid": 42000, "senior": 65000},
        "job_titles": ["Financial Analyst", "Accountant", "Management Accountant", "Audit Associate", "Finance Manager"],
        "interview_topics": ["Financial statement analysis", "Budgeting scenarios", "Regulatory knowledge", "Excel proficiency", "Ethics"],
        "top_cities_uk": ["London", "Manchester", "Edinburgh", "Birmingham", "Bristol"],
        "top_cities_eu": ["Dublin", "Amsterdam", "Frankfurt", "Zurich", "Luxembourg"],
        "demand_level": "High",
        "remote_friendly": "Medium"
    },
    "Supply Chain / Operations": {
        "technical_skills": ["Excel", "SAP", "ERP Systems", "SQL", "Power BI", "Lean Six Sigma", "Forecasting"],
        "soft_skills": ["Problem solving", "Negotiation", "Process improvement", "Communication", "Adaptability"],
        "certifications": ["CSCP (APICS)", "Lean Six Sigma Green Belt", "CILT", "CIPS"],
        "keywords": ["logistics", "procurement", "inventory", "optimization", "supply chain", "operations", "efficiency"],
        "avg_salary_gbp": {"entry": 26000, "mid": 40000, "senior": 60000},
        "job_titles": ["Supply Chain Analyst", "Operations Coordinator", "Procurement Specialist", "Logistics Manager", "Demand Planner"],
        "interview_topics": ["Process optimization", "Vendor management", "Inventory challenges", "ERP experience", "Cost reduction"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Leeds", "Liverpool"],
        "top_cities_eu": ["Amsterdam", "Copenhagen", "Hamburg", "Rotterdam", "Dublin"],
        "demand_level": "Medium",
        "remote_friendly": "Low"
    },
    "Human Resources": {
        "technical_skills": ["HRIS Systems", "Excel", "Workday", "BambooHR", "LinkedIn Recruiter", "ATS"],
        "soft_skills": ["Empathy", "Communication", "Conflict resolution", "Discretion", "Organisational skills"],
        "certifications": ["CIPD", "SHRM", "HRCI", "LinkedIn Talent Solutions"],
        "keywords": ["talent", "recruitment", "employee engagement", "people operations", "culture", "DEI", "onboarding"],
        "avg_salary_gbp": {"entry": 24000, "mid": 38000, "senior": 55000},
        "job_titles": ["HR Coordinator", "Recruiter", "HR Business Partner", "People Operations", "Talent Acquisition"],
        "interview_topics": ["Employment law basics", "Handling difficult conversations", "DEI initiatives", "Recruitment strategies"],
        "top_cities_uk": ["London", "Manchester", "Birmingham", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Amsterdam", "Dublin", "Berlin", "Copenhagen", "Stockholm"],
        "demand_level": "Medium",
        "remote_friendly": "Medium"
    },
    "Sales / Business Development": {
        "technical_skills": ["Salesforce", "HubSpot", "Excel", "LinkedIn Sales Navigator", "CRM Tools", "Cold Email Tools"],
        "soft_skills": ["Persuasion", "Relationship building", "Resilience", "Active listening", "Negotiation"],
        "certifications": ["HubSpot Sales", "Salesforce Administrator", "LinkedIn Sales Navigator"],
        "keywords": ["revenue", "pipeline", "B2B", "prospecting", "closing", "targets", "client relationships"],
        "avg_salary_gbp": {"entry": 25000, "mid": 40000, "senior": 60000},
        "job_titles": ["Sales Executive", "BDR", "Account Executive", "Sales Manager", "Business Development Manager"],
        "interview_topics": ["Sales pitch practice", "Objection handling", "Pipeline management", "CRM proficiency", "Target achievement"],
        "top_cities_uk": ["London", "Manchester", "Bristol", "Edinburgh", "Leeds"],
        "top_cities_eu": ["Dublin", "Amsterdam", "Berlin", "Stockholm", "Copenhagen"],
        "demand_level": "High",
        "remote_friendly": "Medium"
    }
}

# Experience reframing templates for different backgrounds
EXPERIENCE_REFRAMES = {
    "Supply Chain": [
        ("managed inventory", "Tracked and analysed inventory data to identify patterns and reduce waste"),
        ("coordinated logistics", "Optimised logistics workflows using data-driven decision making"),
        ("worked with vendors", "Managed vendor performance metrics and compliance dashboards"),
        ("procurement tasks", "Analysed procurement data to forecast demand and negotiate better terms")
    ],
    "Finance": [
        ("financial reporting", "Built financial models and analysed trends across large datasets"),
        ("budgeting", "Created budget forecasts using quantitative analysis and reporting tools"),
        ("accounting tasks", "Processed high-volume financial data with attention to accuracy"),
        ("risk assessment", "Applied analytical frameworks to assess risk and forecast outcomes")
    ],
    "Marketing": [
        ("social media", "Analysed social media performance metrics to optimise content strategy"),
        ("campaigns", "Tracked campaign KPIs and used data insights to improve conversion rates"),
        ("content creation", "Developed content informed by audience analytics and engagement data"),
        ("brand management", "Monitored brand performance dashboards and competitive positioning")
    ],
    "Sales": [
        ("hit targets", "Used data-driven strategies to consistently exceed revenue targets"),
        ("client management", "Analysed customer behaviour patterns to improve retention and conversion"),
        ("prospecting", "Built targeted prospect lists using data analysis and market research"),
        ("closing deals", "Tracked pipeline metrics and optimised sales processes based on performance data")
    ],
    "Retail": [
        ("customer service", "Observed customer behaviour trends to inform service improvements"),
        ("sales floor", "Monitored daily sales data and identified fast-moving product patterns"),
        ("stock management", "Analysed stock levels and restocking patterns to optimise inventory"),
        ("cash handling", "Handled end-of-day financial reconciliation and payment reporting")
    ],
    "Banking": [
        ("transactions", "Processed and validated high-volume financial data with 100% accuracy"),
        ("account management", "Managed client data across multiple banking systems ensuring data integrity"),
        ("compliance", "Analysed transaction patterns for regulatory compliance and reporting"),
        ("customer service", "Used CRM data to identify client needs and improve service delivery")
    ],
    "Admin / Office": [
        ("data entry", "Maintained and organised large datasets with attention to accuracy and consistency"),
        ("scheduling", "Optimised scheduling processes to improve team efficiency"),
        ("filing", "Created systematic information management workflows"),
        ("correspondence", "Managed stakeholder communications and documentation")
    ]
}


# ============================================================
# STEP 2: USER PROFILE
# ============================================================

def collect_user_profile():
    """Gather information about the user."""
    print("\n" + "=" * 55)
    print("  LET'S GET TO KNOW YOU")
    print("  Answer a few questions so I can help you properly!")
    print("=" * 55)

    profile = {}

    profile["name"] = input("\n  Your full name: ").strip() or "Career Builder"
    profile["city"] = input("  City you're based in: ").strip()
    profile["country"] = input("  Country: ").strip()

    # Career stage
    print("\n  Where are you in your career?")
    print("    1. Fresh graduate (just finished uni)")
    print("    2. Student (currently studying)")
    print("    3. Working (want to grow or switch)")
    print("    4. Between jobs (looking for work)")
    print("    5. Career pivoter (switching to a new field)")
    print("    6. Applying to master's programmes")

    stage_choice = input("\n  Pick (1-6): ").strip()
    stages = {
        "1": "Fresh graduate", "2": "Student", "3": "Working professional",
        "4": "Job seeker", "5": "Career pivoter", "6": "Master's applicant"
    }
    profile["stage"] = stages.get(stage_choice, "Job seeker")

    # Education
    profile["degree"] = input("\n  Your degree (e.g. BBA in Finance, BSc Computer Science): ").strip()
    profile["university"] = input("  University name: ").strip()
    profile["grad_year"] = input("  Graduation year: ").strip()

    # Work experience
    print("\n  How much work experience do you have?")
    print("    1. None (student / fresh grad)")
    print("    2. Internship experience only")
    print("    3. 1-2 years")
    print("    4. 3-5 years")
    print("    5. 5+ years")

    exp_choice = input("\n  Pick (1-5): ").strip()
    exp_map = {"1": "none", "2": "internship", "3": "1-2 years", "4": "3-5 years", "5": "5+ years"}
    profile["experience_level"] = exp_map.get(exp_choice, "none")

    if profile["experience_level"] != "none":
        profile["current_role"] = input("  Current/most recent job title: ").strip()
        profile["current_company"] = input("  Company name: ").strip()
        profile["previous_field"] = input("  Your industry/field (e.g. Retail, Banking, Marketing): ").strip()
    else:
        profile["current_role"] = ""
        profile["current_company"] = ""
        profile["previous_field"] = ""

    # Target field
    print("\n  What field do you want to work in (or grow in)?")
    for key, value in CAREER_FIELDS.items():
        print(f"    {key:>2}. {value}")

    field_choice = input("\n  Pick (1-12): ").strip()
    profile["target_field"] = CAREER_FIELDS.get(field_choice, "Data Analytics")

    # Skills check
    field = FIELD_DATA[profile["target_field"]]
    all_skills = field["technical_skills"] + field["soft_skills"]

    print(f"\n  Which of these {profile['target_field']} skills do you already have?")
    print("  (Type numbers separated by commas, or 'none')")
    for i, skill in enumerate(all_skills, 1):
        print(f"    {i:>2}. {skill}")

    skill_input = input("\n  Your skills: ").strip()
    if skill_input.lower() == "none" or not skill_input:
        profile["existing_skills"] = []
    else:
        try:
            indices = [int(x.strip()) - 1 for x in skill_input.split(",")]
            profile["existing_skills"] = [all_skills[i] for i in indices if 0 <= i < len(all_skills)]
        except (ValueError, IndexError):
            profile["existing_skills"] = []

    # Projects and portfolio
    profile["has_projects"] = input("\n  Do you have projects or a portfolio? (yes/no): ").strip().lower() == "yes"
    if profile["has_projects"]:
        profile["project_details"] = input("  Briefly describe them: ").strip()
    else:
        profile["project_details"] = ""

    # LinkedIn status
    print("\n  How's your LinkedIn right now?")
    print("    1. Don't have one yet")
    print("    2. Have one but it's empty/basic")
    print("    3. Decent but could be better")
    print("    4. Pretty good, just need fine-tuning")

    li_choice = input("\n  Pick (1-4): ").strip()
    li_map = {"1": "none", "2": "basic", "3": "decent", "4": "good"}
    profile["linkedin_status"] = li_map.get(li_choice, "basic")

    return profile


# ============================================================
# STEP 3: LINKEDIN PROFILE OPTIMIZER
# ============================================================

def linkedin_optimizer(profile, tone):
    """Full LinkedIn profile optimization."""
    print("\n" + "=" * 55)
    print(f"  LINKEDIN PROFILE OPTIMIZER ({tone['name']} tone)")
    print("=" * 55)

    print("\n  What do you need help with?")
    print("    1. Headline options")
    print("    2. About section")
    print("    3. Experience rewriting")
    print("    4. Skills to add")
    print("    5. Post ideas to get noticed")
    print("    6. ALL of the above")

    choice = input("\n  Pick (1-6): ").strip()

    if choice in ["1", "6"]:
        generate_headlines(profile, tone)
    if choice in ["2", "6"]:
        generate_about(profile, tone)
    if choice in ["3", "6"]:
        rewrite_experience(profile)
    if choice in ["4", "6"]:
        linkedin_skills(profile)
    if choice in ["5", "6"]:
        post_ideas(profile, tone)

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("  Invalid choice!")


def generate_headlines(profile, tone):
    """Generate LinkedIn headline options based on chosen tone."""
    print(f"\n  --- HEADLINE OPTIONS ({tone['name']} tone) ---")
    print("  (Pick the one that feels most like you)\n")

    target = profile["target_field"]
    prev = profile["previous_field"]
    city = profile["city"]
    skills = profile["existing_skills"]
    stage = profile["stage"]
    tone_name = tone["name"]
    top_skills = " | ".join(skills[:3]) if skills else target

    headlines = []

    # Tone-specific headlines
    if "Friendly" in tone_name:
        if stage == "Career pivoter" and prev:
            headlines.append(f"{prev} grad who fell in love with {target.lower()} | Building projects and learning every day | {city}")
            headlines.append(f"From {prev} to {target} | Loving the journey | Always happy to connect")
        headlines.append(f"Aspiring {target} professional | {top_skills} | Learning, building, growing | {city}")
        if profile["has_projects"]:
            headlines.append(f"Self-taught {target} enthusiast | Real projects on GitHub | Let's connect!")

    elif "Humanised" in tone_name:
        if stage == "Career pivoter" and prev:
            headlines.append(f"Studied {prev}, realised I'd rather play with data | Now building {target.lower()} skills from scratch")
            headlines.append(f"Not your typical {target.lower()} person | {prev} background, self-taught coder, figuring it out")
        headlines.append(f"{target} | Taught myself {top_skills} | Still learning, still building | {city}")
        if profile["has_projects"]:
            headlines.append(f"Built real projects before getting a degree in it | {target} | {city}")

    elif "Professional" in tone_name:
        if stage == "Career pivoter" and prev:
            headlines.append(f"{prev} Professional Transitioning to {target} | {top_skills} | {profile['degree']}")
            headlines.append(f"Aspiring {target} Specialist | {profile['degree']} | {profile['university']}")
        headlines.append(f"{target} | {top_skills} | {profile['degree']} Graduate | {city}")
        if profile["has_projects"]:
            headlines.append(f"{target} Professional | Portfolio on GitHub | {profile['experience_level']} Experience")

    elif "Confident" in tone_name:
        if stage == "Career pivoter" and prev:
            headlines.append(f"I turn {prev.lower()} problems into {target.lower()} solutions | {top_skills} | {city}")
            headlines.append(f"{prev} brain, {target.lower()} skills | I bring both to the table")
        headlines.append(f"I build things with data | {target} | {top_skills} | Results over resumes")
        if profile["has_projects"]:
            headlines.append(f"Self-taught. Project-proven. Ready to deliver | {target} | {city}")

    elif "Creative" in tone_name or "Storytelling" in tone_name:
        if stage == "Career pivoter" and prev:
            headlines.append(f"Once upon a {prev.lower()} career, I discovered {target.lower()} | Now writing a new chapter from {city}")
            headlines.append(f"From spreadsheets to scripts | My {prev} to {target} story is just getting started")
        headlines.append(f"Turning curiosity into code | {target} journey in progress | {city}")
        if profile["has_projects"]:
            headlines.append(f"Every project teaches me something new | {target} | Building my story one commit at a time")

    # Universal options for all tones
    if stage == "Fresh graduate":
        headlines.append(f"{profile['degree']} Graduate | Aspiring {target} Professional | {profile['university']}")
    if stage == "Master's applicant":
        headlines.append(f"MSc {target} Applicant | {profile['degree']} Background | {city}")
    if stage == "Working professional":
        headlines.append(f"{profile['current_role']} at {profile['current_company']} | Growing into {target}")

    for i, h in enumerate(headlines, 1):
        chars = len(h)
        fit = "good" if chars <= 120 else "trim a bit" if chars <= 180 else "too long"
        print(f"  Option {i} ({chars} chars, {fit}):")
        print(f"  \"{h}\"\n")

    print(f"  TIP: Your headline appears everywhere on LinkedIn: search results,")
    print(f"  comments, connection requests. Make every word count!")
    print(f"  Avoid: 'Seeking opportunities', 'Open to work', 'Unemployed'")


def generate_about(profile, tone):
    """Generate About section based on chosen tone."""
    print(f"\n  --- YOUR ABOUT SECTION ({tone['name']} tone) ---")
    print("  (Copy and paste this into LinkedIn)\n")

    name = profile["name"].split()[0]
    target = profile["target_field"]
    stage = profile["stage"]
    degree = profile["degree"]
    uni = profile["university"]
    city = profile["city"]
    skills = profile["existing_skills"]
    prev = profile["previous_field"]
    field = FIELD_DATA[target]
    tone_name = tone["name"]

    # ---- OPENING based on tone + career stage ----
    if "Friendly" in tone_name:
        if stage == "Career pivoter" and prev:
            about = f"  Hi! I come from a {prev.lower()} background, and while I really valued what I learned there,"
            about += f" I kept finding myself more excited about the data side of things."
            about += f" That curiosity eventually turned into a full career decision, and here I am!"
        elif stage == "Fresh graduate":
            about = f"  Hi there! I recently graduated with a {degree} from {uni},"
            about += f" and I am so excited to be starting my journey in {target.lower()}."
        else:
            about = f"  Hey! I am a {degree} graduate with a genuine love for {target.lower()}."
            about += f" I believe the best things happen when curiosity meets action."

    elif "Humanised" in tone_name:
        if stage == "Career pivoter" and prev:
            about = f"  I studied {degree} at {uni}, and honestly, it took me a while to figure out"
            about += f" that {prev.lower()} wasn't where I wanted to be long-term. What I kept coming back to"
            about += f" was the data, the patterns, the 'aha' moments when numbers start telling a story."
        elif stage == "Fresh graduate":
            about = f"  I just finished my {degree} at {uni}, and I'll be real, the most interesting"
            about += f" part of my studies was always when we got to work with actual data."
        else:
            about = f"  Here's the thing about me: I did not follow a straight path into {target.lower()}."
            about += f" I came from {prev.lower() if prev else 'a completely different background'}, and honestly,"
            about += f" that detour taught me things a textbook never could."

    elif "Professional" in tone_name:
        if stage == "Career pivoter" and prev:
            about = f"  With a {degree} from {uni} and experience in {prev.lower()},"
            about += f" I bring a strong foundation in business operations and strategic thinking."
            about += f" I am now channelling these competencies into {target.lower()},"
            about += f" where I see significant opportunity to create impact."
        elif stage == "Fresh graduate":
            about = f"  A recent {degree} graduate from {uni}, I am eager to apply my"
            about += f" analytical skills and academic foundation to a career in {target.lower()}."
        else:
            about = f"  As a {degree} graduate with a demonstrated interest in {target.lower()},"
            about += f" I am committed to building expertise through continuous learning"
            about += f" and practical application."

    elif "Confident" in tone_name:
        if stage == "Career pivoter" and prev:
            about = f"  I spent years in {prev.lower()} learning how businesses actually work."
            about += f" Now I am taking that knowledge and combining it with {target.lower()} skills"
            about += f" to deliver something most pure-tech people can't: real business understanding"
            about += f" backed by technical ability."
        elif stage == "Fresh graduate":
            about = f"  I graduated with a {degree} from {uni}, and I did not wait around"
            about += f" for someone to hand me a {target.lower()} career. I started building one myself."
        else:
            about = f"  I don't just talk about {target.lower()}. I build things, I learn fast,"
            about += f" and I bring a {prev.lower() + ' ' if prev else ''}perspective that most people in this field don't have."

    elif "Creative" in tone_name or "Storytelling" in tone_name:
        if stage == "Career pivoter" and prev:
            about = f"  Somewhere between my {prev.lower()} lectures and my first Excel spreadsheet,"
            about += f" I realised I was more interested in what the numbers were saying"
            about += f" than in the processes they were tracking. That was the moment everything shifted."
        elif stage == "Fresh graduate":
            about = f"  It started in a university lecture hall. While everyone else was taking notes,"
            about += f" I was the one wondering what patterns were hiding in the data we were studying."
            about += f" That curiosity led me to {target.lower()}."
        else:
            about = f"  Every career has a turning point. Mine was the day I realised that"
            about += f" {target.lower()} was not just a skill to learn, it was how my brain"
            about += f" already worked. I just needed to give it a name."
    else:
        about = f"  I am a {degree} graduate building a career in {target.lower()}."

    # ---- MIDDLE section (tone-adapted) ----
    if "Friendly" in tone_name:
        if city:
            about += f"\n\n  Since moving to {city}, I have been having a great time building"
        else:
            about += f"\n\n  Lately, I have been having a great time building"
        about += f" practical skills in this space."
    elif "Humanised" in tone_name:
        if city:
            about += f"\n\n  Since moving to {city}, I started teaching myself."
        else:
            about += f"\n\n  So I started teaching myself."
        about += f" No fancy bootcamp, no hand-holding. Just me, a laptop, and a lot of trial and error."
    elif "Professional" in tone_name:
        if city:
            about += f"\n\n  Based in {city}, I have been systematically developing"
        else:
            about += f"\n\n  I have been systematically developing"
        about += f" my capabilities in this domain through structured learning and practical application."
    elif "Confident" in tone_name:
        if city:
            about += f"\n\n  From {city}, I have been actively building the skills that matter."
        else:
            about += f"\n\n  I have been actively building the skills that matter."
        about += f" Not just watching tutorials. Actually building things."
    else:
        if city:
            about += f"\n\n  The next chapter brought me to {city}, where every day"
        else:
            about += f"\n\n  Every day"
        about += f" became an opportunity to learn something new."

    # Skills mention
    if skills:
        skill_list = ", ".join(skills[:4])
        if "Humanised" in tone_name:
            about += f" I picked up {skill_list} along the way,"
            about += f" mostly through online courses and building things that actually work."
        elif "Confident" in tone_name:
            about += f" I now work with {skill_list},"
            about += f" and I am adding to that list every week."
        elif "Professional" in tone_name:
            about += f" Key competencies developed include {skill_list},"
            about += f" acquired through rigorous self-directed learning and hands-on projects."
        else:
            about += f" So far I have learned {skill_list}"
            about += f" through courses and hands-on practice."

    # Projects mention
    if profile["has_projects"]:
        if "Humanised" in tone_name:
            about += f"\n\n  I believe showing beats telling. {profile['project_details']}"
            about += f" They are on my GitHub because talk is cheap but working code is not."
        elif "Confident" in tone_name:
            about += f"\n\n  Don't just take my word for it. {profile['project_details']}"
            about += f" It's all on my GitHub. Real projects, real code, real results."
        elif "Creative" in tone_name or "Storytelling" in tone_name:
            about += f"\n\n  Each project taught me something new. {profile['project_details']}"
            about += f" I share them publicly because I believe every project is a chapter in a bigger story."
        elif "Professional" in tone_name:
            about += f"\n\n  I am a strong proponent of applied learning. {profile['project_details']}"
            about += f" These projects are available on my GitHub profile, demonstrating practical capability."
        else:
            about += f"\n\n  I believe in learning by doing! {profile['project_details']}"
            about += f" I share my work publicly because showing your skills matters more than just listing them."
    else:
        about += f"\n\n  I am currently working on building practical projects to demonstrate"
        about += f" my skills in action."

    # ---- CLOSING (tone-specific) ----
    closer = tone["closers"][0]
    about += f"\n\n  {closer}"

    # Keywords
    keywords = " | ".join(field["keywords"][:6])
    about += f"\n\n  {keywords}"

    print(about)
    char_count = len(about.replace("  ", ""))
    print(f"\n  [{char_count} characters out of 2,600 allowed]")
    print(f"\n  TIP: Want a different vibe? Change your tone from the main menu (option 11)!")


def rewrite_experience(profile):
    """Rewrite past experience for target field."""
    print("\n  --- REWRITE YOUR EXPERIENCE ---\n")

    prev = profile["previous_field"]
    target = profile["target_field"]

    # Find matching reframe
    matched = None
    for key in EXPERIENCE_REFRAMES:
        if key.lower() in prev.lower() or prev.lower() in key.lower():
            matched = key
            break

    if matched:
        print(f"  Your background: {prev}")
        print(f"  Your target: {target}\n")

        reframes = EXPERIENCE_REFRAMES[matched]
        for i, (original, reframed) in enumerate(reframes, 1):
            print(f"  {i}. Instead of: \"{original}\"")
            print(f"     Write this: \"{reframed}\"\n")
    else:
        print(f"  I don't have specific reframes for '{prev}', but here's the trick:\n")

    print(f"  THE UNIVERSAL REFRAMING FORMULA:")
    print(f"  {'=' * 42}")
    print(f"  For ANY past role, ask yourself:")
    print(f"    1. Did I work with any data or numbers?")
    print(f"    2. Did I notice patterns or trends?")
    print(f"    3. Did I help make or inform decisions?")
    print(f"    4. Did I communicate findings to anyone?")
    print(f"    5. Did I improve or optimise any process?")
    print(f"\n  If yes to ANY of these, frame it using these power verbs:")
    verbs = ["Analysed", "Tracked", "Optimised", "Automated", "Identified",
             "Streamlined", "Forecasted", "Reported", "Visualised", "Improved"]
    print(f"    {', '.join(verbs)}")


def linkedin_skills(profile):
    """Show skills to add to LinkedIn."""
    print("\n  --- SKILLS TO ADD TO YOUR PROFILE ---\n")

    target = profile["target_field"]
    field = FIELD_DATA[target]
    existing = [s.lower() for s in profile["existing_skills"]]

    print(f"  TECHNICAL SKILLS for {target}:")
    for skill in field["technical_skills"]:
        status = "[x] " if skill.lower() in existing else "[ ] "
        note = "(you have this!)" if skill.lower() in existing else "(add this)"
        print(f"    {status}{skill} {note}")

    print(f"\n  SOFT SKILLS:")
    for skill in field["soft_skills"]:
        status = "[x] " if skill.lower() in existing else "[ ] "
        note = "(you have this!)" if skill.lower() in existing else "(add this)"
        print(f"    {status}{skill} {note}")

    have = len([s for s in field["technical_skills"] + field["soft_skills"] if s.lower() in existing])
    total = len(field["technical_skills"]) + len(field["soft_skills"])
    pct = (have / total * 100) if total else 0

    print(f"\n  Your coverage: {have}/{total} ({pct:.0f}%)")
    bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
    print(f"  [{bar}]")

    print(f"\n  TIP: Add ALL relevant skills to LinkedIn, even ones you're still learning.")
    print(f"  Recruiters search by skills, so more skills = more visibility!")


def post_ideas(profile, tone):
    """Generate LinkedIn post ideas based on tone."""
    print(f"\n  --- LINKEDIN POST IDEAS ({tone['name']} tone) ---")
    print("  (Posting consistently is the #1 way to get noticed)\n")

    target = profile["target_field"]
    prev = profile["previous_field"]
    tone_name = tone["name"]

    if "Friendly" in tone_name:
        ideas = [
            f"'I started learning {target.lower()} [X] months ago and I'm honestly loving the journey! Here's what I've picked up so far...'",
            f"'Just built my first [project name] using Python and I'm so proud! Here's what the data told me...' (add a screenshot!)",
            f"'One thing I wish someone told me when I started: you don't need to know everything to begin. Just start somewhere!'",
            f"'Happy to share the free resources that helped me get into {target.lower()}! Hope they help someone else too.'",
            f"'Just completed [course/certification]! The 3 things that surprised me most...'",
            f"'Quick question for anyone in {target.lower()}: what's the one skill you wish you'd learned sooner? I'm all ears!'",
            f"'For anyone thinking about getting into {target.lower()}: here are 3 things I'd do differently if I started over today.'",
            f"'This week I learned: [1 thing]. Built: [1 thing]. Next week: [1 goal]. Small steps add up!'"
        ]
    elif "Humanised" in tone_name:
        ideas = [
            f"'I'll be honest: {target.lower()} scared me at first. I had zero technical background. But [X] months in, here's where I am...'",
            f"'Nobody tells you this about learning {target.lower()}: the first project takes 10x longer than you think. But finishing it? That feeling is unmatched.'",
            f"'I came from {prev.lower() if prev else 'a completely different field'}. Everyone said I was crazy for switching. Here's what actually happened...'",
            f"'Broke my code 47 times today. Fixed it 47 times. That's basically what learning {target.lower()} looks like.'",
            f"'The most useful thing I've learned this month isn't a tool or framework. It's that asking for help is not a weakness. It's a skill.'",
            f"'Real talk: imposter syndrome hit me hard this week. But then I looked back at where I was 3 months ago and...'",
            f"'Here's my messy, unfiltered learning process this week. No polished insights, just the reality of switching careers.'",
            f"'To everyone who thinks they're too late to start: I started from zero [X] months ago. Here's the proof.'"
        ]
    elif "Professional" in tone_name:
        ideas = [
            f"'Key insight from my {target.lower()} studies this week: [insight]. Implications for businesses: [1-2 sentences].'",
            f"'I recently completed [certification/course] in {target.lower()}. Three key takeaways for professionals considering this field...'",
            f"'Having transitioned from {prev.lower() if prev else 'a traditional business role'} into {target.lower()}, I've identified the skills that matter most at the intersection of both.'",
            f"'An analysis of current {target.lower()} job postings reveals interesting trends in skills demand. Here's what I found...'",
            f"'The gap between business acumen and technical proficiency is where the real value lies. Here's why...'",
            f"'For professionals exploring a transition into {target.lower()}: a structured approach I would recommend based on my experience.'",
            f"'This week's learning: [tool/concept]. How it applies to [industry/business problem]. Practical application notes below.'",
            f"'Reflections on [X] months of systematic skill development in {target.lower()}: progress, challenges, and next steps.'"
        ]
    elif "Confident" in tone_name:
        ideas = [
            f"'I don't have a CS degree. I taught myself {target.lower()}. Here are the projects to prove it.'",
            f"'Everyone's talking about {target.lower()}. I'm actually building things with it. Big difference.'",
            f"'Switched from {prev.lower() if prev else 'a non-tech career'} to {target.lower()}. Best decision I ever made. Here's why.'",
            f"'Stop consuming tutorials. Start building projects. That's it. That's the post.'",
            f"'3 things that actually move the needle when learning {target.lower()} (hint: courses aren't one of them).'",
            f"'My background in {prev.lower() if prev else 'business'} isn't a disadvantage in {target.lower()}. It's my superpower. Let me explain.'",
            f"'Week [X] of building in public. Here's what I shipped this week.'",
            f"'Hot take: you don't need permission to call yourself a {target.lower()} professional. You need projects.'"
        ]
    else:  # Creative / Storytelling
        ideas = [
            f"'It started with a single CSV file and a question I couldn't stop thinking about. That's how my {target.lower()} journey began...'",
            f"'Three months ago, I didn't know what Python was. Today I built [project]. Here's the story of everything that happened in between...'",
            f"'There's a moment in every career change when you think: what am I doing? For me, that moment was [story]. But then...'",
            f"'The best thing about learning {target.lower()} isn't the skills. It's the moment your data tells you something nobody else has seen yet.'",
            f"'Plot twist: the {prev.lower() if prev else 'business'} skills I thought were useless turned out to be my biggest advantage in {target.lower()}.'",
            f"'Day 1 vs Day 90 of learning {target.lower()}. A thread about fails, wins, and the messy middle.'",
            f"'If my career was a movie, this chapter would be called: The Pivot. And it would start with...'",
            f"'Someone once told me I was too late to get into {target.lower()}. Here's what I built to prove them wrong.'"
        ]

    for i, idea in enumerate(ideas, 1):
        print(f"  {i:>2}. {idea}\n")

    print(f"  POSTING STRATEGY:")
    print(f"  - Aim for 2-3 posts per week")
    print(f"  - Best times: Tuesday to Thursday, 8-10 AM your timezone")
    print(f"  - Always add an image or screenshot (2x more engagement)")
    print(f"  - End every post with a question to get comments")
    print(f"  - Reply to EVERY comment within an hour")
    print(f"  - Engage with 5-10 other people's posts before you publish yours")


# ============================================================
# STEP 4: CV / RESUME TIPS
# ============================================================

def cv_guidance(profile, tone):
    """Provide CV writing tips and structure with tone-adapted examples."""
    print("\n" + "=" * 55)
    print(f"  CV / RESUME GUIDANCE ({tone['name']} tone)")
    print("=" * 55)

    target = profile["target_field"]
    field = FIELD_DATA[target]
    stage = profile["stage"]
    tone_name = tone["name"]

    print(f"\n  Your CV will be written in a {tone['cv_tone']} style.")

    print(f"\n  IDEAL CV STRUCTURE for {target}:")
    print(f"  {'=' * 42}")

    print(f"\n  1. HEADER")
    print(f"     Your name, city, email, LinkedIn URL, GitHub/portfolio link")
    print(f"     TIP: No photo needed for UK jobs. Include phone number.")

    print(f"\n  2. PERSONAL SUMMARY (3-4 lines)")
    print(f"     Who you are + what you bring + what you want")

    # Tone-adapted CV summary examples
    if "Friendly" in tone_name:
        if stage == "Career pivoter":
            print(f"     Example: 'A {profile['degree']} graduate who discovered a real passion for")
            print(f"     {target.lower()} after working in {profile['previous_field'].lower()}. Now combining")
            print(f"     business understanding with hands-on skills in {', '.join(field['technical_skills'][:3])}")
            print(f"     to bring a fresh perspective to data-driven teams.'")
        else:
            print(f"     Example: 'Enthusiastic {profile['degree']} graduate from {profile['university']}")
            print(f"     with a genuine interest in {target.lower()} and a knack for")
            print(f"     turning numbers into stories that make sense.'")

    elif "Humanised" in tone_name:
        if stage == "Career pivoter":
            print(f"     Example: '{profile['degree']} graduate with {profile['experience_level']} experience")
            print(f"     in {profile['previous_field'].lower()}, now channelling that business instinct into")
            print(f"     {target.lower()}. Self-taught in {', '.join(field['technical_skills'][:3])}")
            print(f"     with real projects to show for it.'")
        else:
            print(f"     Example: 'Recent {profile['degree']} graduate who learns by doing.")
            print(f"     Built practical {target.lower()} projects using {', '.join(field['technical_skills'][:2])}")
            print(f"     and looking for a team where curiosity is valued.'")

    elif "Confident" in tone_name:
        if stage == "Career pivoter":
            print(f"     Example: '{profile['previous_field']} professional turned {target.lower()} practitioner.")
            print(f"     {profile['experience_level'].capitalize()} experience understanding how businesses work.")
            print(f"     Now delivering that insight through {', '.join(field['technical_skills'][:3])}.'")
        else:
            print(f"     Example: '{profile['degree']} graduate with proven self-learning ability.")
            print(f"     Skilled in {', '.join(field['technical_skills'][:3])}. Portfolio of real projects.")
            print(f"     Ready to deliver value from day one.'")

    elif "Creative" in tone_name or "Storytelling" in tone_name:
        if stage == "Career pivoter":
            print(f"     Example: 'From {profile['previous_field'].lower()} to {target.lower()}: a {profile['degree']}")
            print(f"     graduate who found their calling in data. Combining business intuition")
            print(f"     with growing expertise in {', '.join(field['technical_skills'][:3])}")
            print(f"     to uncover stories hidden in the numbers.'")
        else:
            print(f"     Example: 'A curious {profile['degree']} graduate who sees patterns where others")
            print(f"     see spreadsheets. Building a career in {target.lower()} one project at a time.'")

    else:  # Professional
        if stage == "Career pivoter":
            print(f"     Example: '{profile['degree']} graduate with {profile['experience_level']} experience")
            print(f"     in {profile['previous_field'].lower()}, now transitioning into {target.lower()}.")
            print(f"     Combining business understanding with growing technical skills")
            print(f"     in {', '.join(field['technical_skills'][:3])}.'")
        else:
            print(f"     Example: 'Recent {profile['degree']} graduate from {profile['university']}")
            print(f"     with a strong interest in {target.lower()}. Eager to apply")
            print(f"     analytical skills and fresh perspective to a {field['job_titles'][0]} role.'")

    print(f"\n  3. KEY SKILLS")
    print(f"     List 6-8 relevant skills in a clean row:")
    skill_row = " | ".join(field["technical_skills"][:6])
    print(f"     {skill_row}")

    print(f"\n  4. EXPERIENCE")
    print(f"     Most recent first. For each role:")
    print(f"     - Job title | Company | Dates")
    print(f"     - 3-4 bullet points starting with ACTION VERBS")
    print(f"     - Include numbers where possible (e.g. 'Analysed 500+ records')")

    print(f"\n  5. EDUCATION")
    print(f"     Degree | University | Year")
    print(f"     Mention relevant modules or dissertation if applicable")

    print(f"\n  6. PROJECTS / PORTFOLIO (especially if experience is limited)")
    print(f"     Project name | What it does | Tools used | Link")
    print(f"     This section can REPLACE lack of experience for entry-level roles!")

    print(f"\n  7. CERTIFICATIONS")
    print(f"     Relevant ones for {target}:")
    for cert in field["certifications"]:
        print(f"       - {cert}")

    # Common mistakes
    print(f"\n  COMMON CV MISTAKES TO AVOID:")
    print(f"  {'=' * 42}")
    mistakes = [
        "Using a generic CV for every job (tailor it each time!)",
        "Writing duties instead of achievements ('Responsible for...' is weak)",
        "Including a photo (not standard in UK/US)",
        "Making it longer than 2 pages",
        "Using fancy fonts, colours, or templates that break ATS systems",
        "Not including keywords from the job description",
        "Putting education first when you have work experience",
        "Listing every job you've ever had (only relevant ones!)",
        "No numbers or metrics (always quantify your impact)",
        "Typos and grammar errors (get someone to proofread!)"
    ]
    for i, mistake in enumerate(mistakes, 1):
        print(f"    {i:>2}. {mistake}")


# ============================================================
# STEP 5: COVER LETTER TIPS
# ============================================================

def cover_letter_guidance(profile, tone):
    """Provide cover letter writing tips and template with tone."""
    print("\n" + "=" * 55)
    print(f"  COVER LETTER GUIDANCE ({tone['name']} tone)")
    print("=" * 55)

    target = profile["target_field"]
    name = profile["name"].split()[0]
    field = FIELD_DATA[target]
    tone_name = tone["name"]

    print(f"\n  Your cover letter style: {tone['cover_letter_style']}")
    print(f"\n  THE 4-PARAGRAPH FORMULA:")
    print(f"  (Works for almost any job application)\n")

    print(f"  PARAGRAPH 1: The Hook")
    print(f"  {'=' * 42}")
    print(f"  - State the role you're applying for")
    print(f"  - One sentence about why THIS company excites you")
    print(f"  - Show you've researched them (mention something specific)")
    print(f"  - Keep it to 2-3 sentences max")

    # Tone-specific opening examples
    if "Friendly" in tone_name:
        print(f"\n  Example:")
        print(f"  'I was really excited to see the {field['job_titles'][0]} role at [Company].")
        print(f"  Your work on [specific thing] genuinely resonated with me, and I would")
        print(f"  love the chance to bring my {target.lower()} skills to your team.'")
    elif "Humanised" in tone_name:
        print(f"\n  Example:")
        print(f"  'When I saw the {field['job_titles'][0]} role at [Company], it felt like it")
        print(f"  was written for someone on exactly my path. Your focus on [specific thing]")
        print(f"  is exactly the kind of work I have been building towards.'")
    elif "Confident" in tone_name:
        print(f"\n  Example:")
        print(f"  'I am applying for the {field['job_titles'][0]} role at [Company] because")
        print(f"  I believe my combination of {target.lower()} skills and real-world business")
        print(f"  understanding is exactly what this role demands.'")
    elif "Creative" in tone_name or "Storytelling" in tone_name:
        print(f"\n  Example:")
        print(f"  'The first time I came across [Company's] work on [specific thing],")
        print(f"  I knew this was the kind of team I wanted to be part of. That is why")
        print(f"  the {field['job_titles'][0]} role immediately caught my attention.'")
    else:
        print(f"\n  Example:")
        print(f"  'I am writing to express my interest in the {field['job_titles'][0]} position")
        print(f"  at [Company]. Your organisation's commitment to [specific thing] aligns")
        print(f"  closely with my professional aspirations in {target.lower()}.'")


    print(f"\n  PARAGRAPH 2: Why You're Qualified")
    print(f"  {'=' * 42}")
    print(f"  - Match YOUR skills to THEIR requirements")
    print(f"  - Give a specific example of something you've done")
    print(f"  - Use numbers if possible")
    print(f"  - This is where projects and experience shine")

    print(f"\n  PARAGRAPH 3: Why This Company")
    print(f"  {'=' * 42}")
    print(f"  - Show you understand their mission/values")
    print(f"  - Explain what you'd bring that others might not")
    print(f"  - Connect your background to their needs")
    if profile["stage"] == "Career pivoter":
        print(f"  - Your {profile['previous_field'].lower()} background IS a strength here")

    print(f"\n  PARAGRAPH 4: The Close")
    print(f"  {'=' * 42}")
    print(f"  - Express enthusiasm")
    print(f"  - Mention availability for interview")
    print(f"  - Keep it confident but not arrogant")
    print(f"  - 'I would welcome the opportunity to discuss how my skills")
    print(f"    can contribute to [Company's] goals.'")

    print(f"\n  COVER LETTER DO'S AND DON'TS:")
    print(f"  {'=' * 42}")
    dos = [
        "Address it to a real person if possible",
        "Keep it under one page",
        "Match keywords from the job description",
        "Show enthusiasm for the company specifically",
        "Proofread at least twice"
    ]
    donts = [
        "Don't repeat your entire CV",
        "Don't start with 'To whom it may concern'",
        "Don't use the same letter for every application",
        "Don't apologise for lack of experience",
        "Don't include salary expectations unless asked"
    ]

    print(f"\n  DO:")
    for d in dos:
        print(f"    + {d}")
    print(f"\n  DON'T:")
    for d in donts:
        print(f"    - {d}")


# ============================================================
# STEP 6: JOB MARKET INSIGHTS
# ============================================================

def job_market_insights(profile):
    """Show job market data for the target field."""
    print("\n" + "=" * 55)
    print(f"  JOB MARKET INSIGHTS: {profile['target_field'].upper()}")
    print("=" * 55)

    target = profile["target_field"]
    field = FIELD_DATA[target]

    # Salary info
    print(f"\n  SALARY RANGES (GBP, full-time):")
    print(f"  {'=' * 42}")
    levels = {"entry": "Entry Level", "mid": "Mid Level", "senior": "Senior"}
    max_sal = field["avg_salary_gbp"]["senior"]

    for key, label in levels.items():
        salary = field["avg_salary_gbp"][key]
        bar_len = int((salary / max_sal) * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {label:<14} £{salary:>6,}  {bar}")

    # Job titles
    print(f"\n  COMMON JOB TITLES:")
    print(f"  {'=' * 42}")
    for title in field["job_titles"]:
        print(f"    - {title}")

    # Demand and remote
    print(f"\n  MARKET OVERVIEW:")
    print(f"  {'=' * 42}")
    print(f"  Demand level: {field['demand_level']}")
    print(f"  Remote friendliness: {field['remote_friendly']}")

    # Top cities
    print(f"\n  TOP CITIES (UK):")
    for city in field["top_cities_uk"]:
        print(f"    - {city}")

    print(f"\n  TOP CITIES (Europe):")
    for city in field["top_cities_eu"]:
        print(f"    - {city}")

    # Skills in demand
    print(f"\n  MOST IN-DEMAND SKILLS:")
    print(f"  {'=' * 42}")
    existing = [s.lower() for s in profile["existing_skills"]]
    for i, skill in enumerate(field["technical_skills"], 1):
        have = " (you have this!)" if skill.lower() in existing else ""
        print(f"    {i}. {skill}{have}")

    # Certifications that boost your CV
    print(f"\n  CERTIFICATIONS RECRUITERS LOOK FOR:")
    print(f"  {'=' * 42}")
    for cert in field["certifications"]:
        print(f"    - {cert}")

    print(f"\n  KEY INSIGHT:")
    if field["demand_level"] == "Very High":
        print(f"  {target} is one of the hottest fields right now. Companies are")
        print(f"  actively hiring and there aren't enough qualified candidates.")
        print(f"  This is the perfect time to break in!")
    elif field["demand_level"] == "High":
        print(f"  {target} has strong demand across the UK and Europe.")
        print(f"  Building the right skills and having a solid portfolio")
        print(f"  will put you ahead of most applicants.")
    else:
        print(f"  {target} has steady demand. To stand out, focus on")
        print(f"  getting certified and building practical experience")
        print(f"  through projects and internships.")


# ============================================================
# STEP 7: INTERVIEW PREPARATION
# ============================================================

def interview_prep(profile):
    """Interview preparation guidance."""
    print("\n" + "=" * 55)
    print(f"  INTERVIEW PREP: {profile['target_field'].upper()}")
    print("=" * 55)

    target = profile["target_field"]
    field = FIELD_DATA[target]

    print(f"\n  TOPICS YOU SHOULD PREPARE FOR:")
    print(f"  {'=' * 42}")
    for i, topic in enumerate(field["interview_topics"], 1):
        print(f"    {i}. {topic}")

    print(f"\n  COMMON INTERVIEW QUESTIONS (and how to answer them):")
    print(f"  {'=' * 42}")

    questions = [
        {
            "q": "Tell me about yourself",
            "tip": "Use the Present-Past-Future formula: What you do now, what led you here, what you want next. Keep it under 2 minutes.",
            "example": f"'I am currently [your situation]. I studied {profile['degree']} at {profile['university']}, which gave me [relevant skill]. I have since been building my {target.lower()} skills through [courses/projects], and I am excited about the opportunity to [what this role offers].'"
        },
        {
            "q": "Why are you interested in this role?",
            "tip": "Connect YOUR goals to THEIR needs. Show you've researched the company.",
            "example": "'What drew me to this role is [specific thing about the company]. My background in [your background] and my growing skills in [target skills] mean I can bring [specific value].'"
        },
        {
            "q": "What's your biggest weakness?",
            "tip": "Pick something real but show how you're actively working on it. Never say 'perfectionism'.",
            "example": f"'I am still building my {field['technical_skills'][-1]} skills, but I have been taking courses on it and practicing through personal projects. I believe in being honest about gaps and actively closing them.'"
        },
        {
            "q": "Where do you see yourself in 5 years?",
            "tip": "Show ambition but keep it realistic and relevant to the role.",
            "example": f"'In 5 years, I see myself as a solid {target.lower()} professional who has contributed meaningfully to the team and taken on more responsibility. I want to be the person others come to for {target.lower()} advice.'"
        },
        {
            "q": "Why should we hire you?",
            "tip": "Summarise your unique combination: background + new skills + attitude.",
            "example": f"'I bring a unique combination of {profile['previous_field'].lower() if profile['previous_field'] else 'business'} understanding and {target.lower()} skills. I have shown initiative by teaching myself and building real projects. I am someone who doesn't wait to be told what to learn.'"
        }
    ]

    for qa in questions:
        print(f"\n  Q: \"{qa['q']}\"")
        print(f"  Strategy: {qa['tip']}")
        print(f"  Template: {qa['example']}")

    # Behavioural questions
    print(f"\n  BEHAVIOURAL QUESTIONS (use the STAR method):")
    print(f"  {'=' * 42}")
    print(f"  S = Situation (set the scene)")
    print(f"  T = Task (what was your responsibility)")
    print(f"  A = Action (what YOU did)")
    print(f"  R = Result (what happened because of your action)\n")

    behavioural = [
        "Tell me about a time you solved a difficult problem",
        "Describe a situation where you had to learn something quickly",
        "Give an example of when you worked in a team",
        "Tell me about a time you made a mistake and how you handled it",
        "Describe a situation where you had to communicate complex information simply"
    ]

    for i, q in enumerate(behavioural, 1):
        print(f"    {i}. {q}")

    print(f"\n  PRE-INTERVIEW CHECKLIST:")
    print(f"  {'=' * 42}")
    checklist = [
        "Research the company (website, news, LinkedIn, Glassdoor)",
        "Read the job description 3 times and match your skills to each requirement",
        "Prepare 2-3 questions to ask THEM",
        "Test your camera and microphone if it's a video call",
        "Have a copy of your CV open in front of you",
        "Dress one level above what the company normally wears",
        "Arrive 10 minutes early (or log in 5 minutes early for video)",
        "Bring a notebook and pen to take notes",
        "Follow up with a thank-you email within 24 hours"
    ]
    for item in checklist:
        print(f"    [ ] {item}")


# ============================================================
# STEP 8: SKILLS ROADMAP
# ============================================================

def skills_roadmap(profile):
    """Personalized skills learning roadmap."""
    print("\n" + "=" * 55)
    print(f"  YOUR {profile['target_field'].upper()} SKILLS ROADMAP")
    print("=" * 55)

    target = profile["target_field"]
    field = FIELD_DATA[target]
    existing = [s.lower() for s in profile["existing_skills"]]

    # Progress
    all_skills = field["technical_skills"] + field["soft_skills"]
    have = [s for s in all_skills if s.lower() in existing]
    missing = [s for s in all_skills if s.lower() not in existing]
    pct = (len(have) / len(all_skills) * 100) if all_skills else 0

    print(f"\n  CURRENT PROGRESS: {len(have)}/{len(all_skills)} skills ({pct:.0f}%)")
    bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
    print(f"  [{bar}]")

    if have:
        print(f"\n  SKILLS YOU HAVE:")
        for s in have:
            print(f"    [x] {s}")

    if missing:
        print(f"\n  SKILLS TO LEARN (in recommended order):")
        for i, s in enumerate(missing, 1):
            priority = "HIGH" if i <= 3 else "MEDIUM" if i <= 6 else "NICE TO HAVE"
            print(f"    {i:>2}. {s} [{priority}]")

    # 90-day learning plan
    print(f"\n  YOUR 90-DAY LEARNING PLAN:")
    print(f"  {'=' * 42}")

    if missing:
        month1 = missing[:2] if len(missing) >= 2 else missing
        month2 = missing[2:4] if len(missing) >= 4 else missing[2:] if len(missing) > 2 else []
        month3 = missing[4:6] if len(missing) >= 6 else missing[4:] if len(missing) > 4 else []

        print(f"\n  Month 1 (Foundation):")
        for s in month1:
            print(f"    - Learn {s}")
        print(f"    - Complete 1 online course")
        print(f"    - Build 1 small project")

        if month2:
            print(f"\n  Month 2 (Building):")
            for s in month2:
                print(f"    - Learn {s}")
            print(f"    - Build 1 portfolio project")
            print(f"    - Start posting on LinkedIn weekly")

        if month3:
            print(f"\n  Month 3 (Launching):")
            for s in month3:
                print(f"    - Learn {s}")
            print(f"    - Apply for a certification")
            print(f"    - Start applying to jobs")
            print(f"    - Network with 10 people in {target.lower()}")

    # Certifications
    print(f"\n  CERTIFICATIONS TO PURSUE:")
    print(f"  {'=' * 42}")
    for i, cert in enumerate(field["certifications"], 1):
        print(f"    {i}. {cert}")


# ============================================================
# STEP 9: SAVE ALL CONTENT
# ============================================================

def save_everything(profile):
    """Save all generated content to a text file."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = profile["name"].replace(" ", "_").lower()
    filename = f"career_plan_{safe_name}_{timestamp}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    target = profile["target_field"]
    field = FIELD_DATA[target]
    existing = [s.lower() for s in profile["existing_skills"]]

    with open(filepath, "w") as f:
        f.write(f"Career Coach Pro - Personal Career Plan\n")
        f.write(f"Generated for: {profile['name']}\n")
        f.write(f"Date: {datetime.now().strftime('%d/%m/%Y at %H:%M')}\n")
        f.write(f"Target field: {target}\n")
        f.write(f"Career stage: {profile['stage']}\n")
        f.write(f"{'=' * 55}\n\n")

        # Profile summary
        f.write(f"YOUR PROFILE SUMMARY\n")
        f.write(f"{'-' * 40}\n")
        f.write(f"Name: {profile['name']}\n")
        f.write(f"Location: {profile['city']}, {profile['country']}\n")
        f.write(f"Education: {profile['degree']} from {profile['university']}\n")
        f.write(f"Experience: {profile['experience_level']}\n")
        if profile['current_role']:
            f.write(f"Current role: {profile['current_role']} at {profile['current_company']}\n")
        f.write(f"Target field: {target}\n")
        f.write(f"Skills you have: {', '.join(profile['existing_skills']) if profile['existing_skills'] else 'Building from scratch'}\n\n")

        # Skills roadmap
        f.write(f"SKILLS ROADMAP\n")
        f.write(f"{'-' * 40}\n")
        all_skills = field["technical_skills"] + field["soft_skills"]
        for skill in all_skills:
            status = "[x]" if skill.lower() in existing else "[ ]"
            f.write(f"  {status} {skill}\n")

        # Salary info
        f.write(f"\nSALARY RANGES ({target})\n")
        f.write(f"{'-' * 40}\n")
        for level, label in [("entry", "Entry"), ("mid", "Mid"), ("senior", "Senior")]:
            f.write(f"  {label}: £{field['avg_salary_gbp'][level]:,}\n")

        # Certifications
        f.write(f"\nCERTIFICATIONS TO PURSUE\n")
        f.write(f"{'-' * 40}\n")
        for cert in field["certifications"]:
            f.write(f"  - {cert}\n")

        # Job titles to search for
        f.write(f"\nJOB TITLES TO SEARCH FOR\n")
        f.write(f"{'-' * 40}\n")
        for title in field["job_titles"]:
            f.write(f"  - {title}\n")

    print(f"\n  Career plan saved to: {filepath}")
    print(f"  Open this file anytime for your personalised career guide!")

    return filepath


# ============================================================
# STEP 10: MAIN MENU
# ============================================================

def show_menu(tone=None):
    """Display the main menu."""
    print("\n" + "=" * 55)
    print("  Career Coach Pro")
    print("  Your Personal Career Agency")
    print("  by Ayesha Shimu")
    print("=" * 55)
    if tone:
        print(f"  Current tone: {tone['name']}")
    print()
    print("   1.  Start here (tell me about yourself)")
    print("   2.  LinkedIn profile optimizer")
    print("   3.  CV / Resume guidance")
    print("   4.  Cover letter tips")
    print("   5.  Job market insights")
    print("   6.  Interview preparation")
    print("   7.  Skills roadmap")
    print("   8.  Save my career plan to file")
    print("   9.  Change writing tone")
    print("  10.  Start over (new profile)")
    print("  11.  Exit")
    print()


def main():
    """Main function."""
    profile = None
    tone = None

    print("\n  Welcome to Career Coach Pro!")
    print("  Your personal career agency, powered by Python.")
    print("  Whether you're starting out, switching fields, or levelling up,")
    print("  I've got you covered.\n")
    print("  Start with option 1 to tell me about yourself!\n")

    while True:
        show_menu(tone)
        choice = input("  Pick an option (1-11): ").strip()

        if choice == "1":
            profile = collect_user_profile()
            print(f"\n  Got it, {profile['name'].split()[0]}! Now let's pick your writing style.")
            tone = choose_tone()
            print(f"\n  Perfect! Try any option from the menu to get started!")

        elif choice in [str(i) for i in range(2, 9)]:
            if not profile:
                print("\n  I need to know about you first! Pick option 1 to get started.")
                continue
            if not tone:
                print("\n  Let's pick your writing tone first!")
                tone = choose_tone()

            if choice == "2":
                linkedin_optimizer(profile, tone)
            elif choice == "3":
                cv_guidance(profile, tone)
            elif choice == "4":
                cover_letter_guidance(profile, tone)
            elif choice == "5":
                job_market_insights(profile)
            elif choice == "6":
                interview_prep(profile)
            elif choice == "7":
                skills_roadmap(profile)
            elif choice == "8":
                save_everything(profile)

        elif choice == "9":
            tone = choose_tone()

        elif choice == "10":
            profile = None
            tone = None
            print("\n  Profile cleared! Pick option 1 to start fresh.")

        elif choice == "11":
            print("\n  Go out there and own your career!")
            print("  Remember: every expert was once a beginner.")
            print("  You've got this!\n")
            break

        else:
            print("\n  Invalid option! Pick a number between 1 and 11.")


if __name__ == "__main__":
    main()
