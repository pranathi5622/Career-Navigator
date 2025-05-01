# Career data module - provides career information and details

def get_all_careers():
    """Return a list of all available careers"""
    careers = [
        "Software Developer",
        "Data Scientist",
        "UX/UI Designer",
        "Product Manager",
        "Digital Marketer",
        "Financial Analyst",
        "Nurse",
        "Physician",
        "Teacher",
        "Civil Engineer",
        "Mechanical Engineer",
        "Human Resources Manager",
        "Graphic Designer",
        "Content Writer",
        "Business Analyst",
        "Project Manager",
        "Cybersecurity Specialist",
        "Accountant",
        "Sales Manager",
        "Research Scientist"
    ]
    return sorted(careers)

def get_career_details(career_name):
    """
    Get detailed information about a specific career.
    Returns a dictionary with career details.
    """
    career_data = {
        "Software Developer": {
            "description": "Design, build, and maintain software applications and systems.",
            "required_education": "Bachelor's degree in Computer Science or related field; certifications or bootcamp training can be alternatives.",
            "required_skills": ["Programming Languages (Python, Java, JavaScript, etc.)", "Data Structures & Algorithms", "Version Control", "Testing & Debugging", "Problem Solving"],
            "salary_range": "$70,000 - $150,000+",
            "job_outlook": "Much faster than average (22% growth by 2030)",
            "work_environment": "Office, Remote, Tech companies, Startups, Enterprises",
            "related_careers": ["Web Developer", "Mobile App Developer", "DevOps Engineer", "Software Architect"],
            "resources": ["GitHub", "Stack Overflow", "LeetCode", "Coursera", "edX"]
        },
        "Data Scientist": {
            "description": "Analyze and interpret complex data to help organizations make better decisions.",
            "required_education": "Master's degree or PhD in Statistics, Computer Science, or related field.",
            "required_skills": ["Programming (Python, R)", "Statistics", "Machine Learning", "Data Visualization", "SQL/Database Knowledge"],
            "salary_range": "$85,000 - $170,000+",
            "job_outlook": "Much faster than average (31% growth by 2030)",
            "work_environment": "Tech companies, Research institutions, Finance, Healthcare, Consulting",
            "related_careers": ["Machine Learning Engineer", "Business Intelligence Analyst", "Research Scientist", "Data Engineer"],
            "resources": ["Kaggle", "DataCamp", "Towards Data Science", "AI Research Papers", "Industry Conferences"]
        },
        "UX/UI Designer": {
            "description": "Create user-friendly and visually appealing digital interfaces for websites and applications.",
            "required_education": "Bachelor's degree in Design, HCI, or related field; portfolio is crucial.",
            "required_skills": ["User Research", "Wireframing", "Prototyping", "Visual Design", "Design Software (Figma, Adobe XD)"],
            "salary_range": "$65,000 - $130,000+",
            "job_outlook": "Faster than average (13% growth by 2030)",
            "work_environment": "Design agencies, Tech companies, Product companies, Startups, Freelance",
            "related_careers": ["Product Designer", "Interaction Designer", "UX Researcher", "Visual Designer"],
            "resources": ["Behance", "Dribbble", "Nielsen Norman Group", "UX Collective", "Design Systems"]
        },
        "Product Manager": {
            "description": "Lead the development and launch of products, balancing business needs with user requirements.",
            "required_education": "Bachelor's degree in Business, Engineering, or related field; MBA beneficial.",
            "required_skills": ["Strategic Thinking", "User Research", "Data Analysis", "Communication", "Agile Methodologies"],
            "salary_range": "$80,000 - $160,000+",
            "job_outlook": "Faster than average (10% growth by 2030)",
            "work_environment": "Tech companies, Consumer products, Startups, Enterprises",
            "related_careers": ["Product Owner", "Program Manager", "Business Analyst", "Strategic Consultant"],
            "resources": ["Product School", "Mind the Product", "ProductPlan", "Product Management Books", "Industry Conferences"]
        },
        "Digital Marketer": {
            "description": "Plan and execute marketing campaigns across digital channels to promote products or services.",
            "required_education": "Bachelor's degree in Marketing, Communications, or related field.",
            "required_skills": ["SEO/SEM", "Social Media Marketing", "Content Creation", "Analytics", "Email Marketing"],
            "salary_range": "$50,000 - $120,000+",
            "job_outlook": "Faster than average (10% growth by 2030)",
            "work_environment": "Marketing agencies, In-house marketing teams, Startups, Freelance",
            "related_careers": ["Social Media Manager", "SEO Specialist", "Content Marketer", "Marketing Analyst"],
            "resources": ["HubSpot Academy", "Google Digital Garage", "Moz", "Content Marketing Institute", "Industry Blogs"]
        },
        "Financial Analyst": {
            "description": "Analyze financial data to help businesses make investment decisions and financial planning.",
            "required_education": "Bachelor's degree in Finance, Economics, or related field; CFA beneficial.",
            "required_skills": ["Financial Modeling", "Excel/Spreadsheets", "Data Analysis", "Financial Statement Analysis", "Communication"],
            "salary_range": "$60,000 - $130,000+",
            "job_outlook": "Faster than average (6% growth by 2030)",
            "work_environment": "Banks, Investment firms, Insurance companies, Corporations",
            "related_careers": ["Investment Analyst", "Portfolio Manager", "Risk Analyst", "Financial Advisor"],
            "resources": ["CFA Institute", "Wall Street Prep", "Financial Times", "Bloomberg", "Industry Reports"]
        },
        "Nurse": {
            "description": "Provide and coordinate patient care in various healthcare settings.",
            "required_education": "Associate or Bachelor's degree in Nursing; RN licensure required.",
            "required_skills": ["Patient Care", "Medical Knowledge", "Critical Thinking", "Communication", "Empathy"],
            "salary_range": "$60,000 - $120,000+",
            "job_outlook": "Much faster than average (9% growth by 2030)",
            "work_environment": "Hospitals, Clinics, Long-term care facilities, Schools, Home healthcare",
            "related_careers": ["Nurse Practitioner", "Clinical Nurse Specialist", "Nursing Educator", "Healthcare Administrator"],
            "resources": ["American Nurses Association", "Nursing Journals", "Continuing Education Programs", "Healthcare Conferences"]
        },
        "Physician": {
            "description": "Diagnose and treat illnesses, injuries, and medical conditions.",
            "required_education": "Medical Doctor (MD) degree; residency and board certification.",
            "required_skills": ["Medical Knowledge", "Diagnosis", "Patient Care", "Communication", "Problem Solving"],
            "salary_range": "$150,000 - $300,000+",
            "job_outlook": "Faster than average (3% growth by 2030)",
            "work_environment": "Hospitals, Private practices, Clinics, Academic medical centers",
            "related_careers": ["Medical Specialist", "Surgeon", "Medical Researcher", "Healthcare Administrator"],
            "resources": ["American Medical Association", "Medical Journals", "Continuing Medical Education", "Specialty Organizations"]
        },
        "Teacher": {
            "description": "Educate students in various subjects and grade levels.",
            "required_education": "Bachelor's degree in Education or subject area; teaching certification.",
            "required_skills": ["Instruction", "Curriculum Development", "Classroom Management", "Communication", "Adaptability"],
            "salary_range": "$40,000 - $100,000+",
            "job_outlook": "Average (7% growth by 2030)",
            "work_environment": "Public schools, Private schools, Online education, International schools",
            "related_careers": ["Education Administrator", "Curriculum Developer", "Educational Consultant", "School Counselor"],
            "resources": ["Education Associations", "Teaching Journals", "Professional Development", "Education Conferences"]
        },
        "Civil Engineer": {
            "description": "Design, build, and maintain infrastructure projects like roads, buildings, and water systems.",
            "required_education": "Bachelor's degree in Civil Engineering; PE licensure for advanced roles.",
            "required_skills": ["Design Software (AutoCAD, etc.)", "Structural Analysis", "Project Management", "Technical Drawing", "Problem Solving"],
            "salary_range": "$65,000 - $140,000+",
            "job_outlook": "Average (8% growth by 2030)",
            "work_environment": "Engineering firms, Construction companies, Government agencies, Consulting",
            "related_careers": ["Structural Engineer", "Transportation Engineer", "Environmental Engineer", "Construction Manager"],
            "resources": ["American Society of Civil Engineers", "Engineering Journals", "CAD Tutorials", "Industry Conferences"]
        },
        "Mechanical Engineer": {
            "description": "Design, develop, and test mechanical and thermal devices and systems.",
            "required_education": "Bachelor's degree in Mechanical Engineering; PE licensure for advanced roles.",
            "required_skills": ["CAD Software", "Mechanical Design", "Thermal Analysis", "Problem Solving", "Technical Communication"],
            "salary_range": "$70,000 - $150,000+",
            "job_outlook": "Average (7% growth by 2030)",
            "work_environment": "Manufacturing, Automotive, Aerospace, Energy, Consulting",
            "related_careers": ["Design Engineer", "Manufacturing Engineer", "Automotive Engineer", "Robotics Engineer"],
            "resources": ["American Society of Mechanical Engineers", "Engineering Journals", "CAD/CAM Resources", "Industry Conferences"]
        },
        "Human Resources Manager": {
            "description": "Oversee the recruiting, interviewing, and hiring of new staff, and manage employee relations.",
            "required_education": "Bachelor's degree in HR, Business, or related field; HR certifications beneficial.",
            "required_skills": ["Recruiting", "Employment Law", "Benefits Administration", "Communication", "Conflict Resolution"],
            "salary_range": "$70,000 - $150,000+",
            "job_outlook": "Faster than average (9% growth by 2030)",
            "work_environment": "Corporations, Government, Nonprofits, HR consulting firms",
            "related_careers": ["Talent Acquisition Manager", "Compensation & Benefits Manager", "Training & Development Manager", "Employee Relations Specialist"],
            "resources": ["Society for Human Resource Management", "HR Magazines", "Employment Law Updates", "HR Certifications"]
        },
        "Graphic Designer": {
            "description": "Create visual concepts to communicate ideas that inspire, inform, or captivate consumers.",
            "required_education": "Bachelor's degree in Graphic Design or related field; portfolio is crucial.",
            "required_skills": ["Adobe Creative Suite", "Typography", "Layout Design", "Visual Communication", "Brand Identity"],
            "salary_range": "$45,000 - $110,000+",
            "job_outlook": "Average (3% growth by 2030)",
            "work_environment": "Design agencies, In-house creative teams, Marketing departments, Freelance",
            "related_careers": ["Art Director", "Brand Designer", "Web Designer", "Illustrator"],
            "resources": ["Behance", "Dribbble", "Adobe Tutorials", "Design Conferences", "Typography Resources"]
        },
        "Content Writer": {
            "description": "Create written content for websites, blogs, social media, and other platforms.",
            "required_education": "Bachelor's degree in English, Journalism, Communications, or related field.",
            "required_skills": ["Writing", "Editing", "SEO Knowledge", "Research", "Content Strategy"],
            "salary_range": "$45,000 - $100,000+",
            "job_outlook": "Average (4% growth by 2030)",
            "work_environment": "Marketing agencies, Media companies, In-house content teams, Freelance",
            "related_careers": ["Copywriter", "Technical Writer", "Content Strategist", "Editor"],
            "resources": ["Content Marketing Institute", "Grammarly", "Writing Courses", "Style Guides", "SEO Resources"]
        },
        "Business Analyst": {
            "description": "Analyze business processes and systems to recommend improvements and solutions.",
            "required_education": "Bachelor's degree in Business, IT, or related field; certifications beneficial.",
            "required_skills": ["Requirements Gathering", "Process Modeling", "Data Analysis", "Communication", "Problem Solving"],
            "salary_range": "$65,000 - $130,000+",
            "job_outlook": "Faster than average (14% growth by 2030)",
            "work_environment": "Corporations, Consulting firms, Financial institutions, Tech companies",
            "related_careers": ["Systems Analyst", "Product Owner", "Management Consultant", "Process Improvement Specialist"],
            "resources": ["International Institute of Business Analysis", "BA Times", "Process Modeling Tools", "Industry Certifications"]
        },
        "Project Manager": {
            "description": "Plan, execute, and close projects while ensuring they're completed on time and within budget.",
            "required_education": "Bachelor's degree in Business, Management, or related field; PMP certification beneficial.",
            "required_skills": ["Planning", "Team Leadership", "Risk Management", "Communication", "Budgeting"],
            "salary_range": "$70,000 - $150,000+",
            "job_outlook": "Faster than average (8% growth by 2030)",
            "work_environment": "Construction, IT, Healthcare, Manufacturing, Consulting",
            "related_careers": ["Program Manager", "Scrum Master", "Construction Manager", "Operations Manager"],
            "resources": ["Project Management Institute", "Agile Resources", "Project Management Software Tutorials", "PMP Certification"]
        },
        "Cybersecurity Specialist": {
            "description": "Protect computer systems and networks from threats, attacks, and unauthorized access.",
            "required_education": "Bachelor's degree in IT, Cybersecurity, or related field; certifications important.",
            "required_skills": ["Network Security", "Threat Analysis", "Security Tools", "Programming", "Risk Assessment"],
            "salary_range": "$75,000 - $160,000+",
            "job_outlook": "Much faster than average (33% growth by 2030)",
            "work_environment": "IT departments, Security firms, Government agencies, Financial institutions",
            "related_careers": ["Security Analyst", "Penetration Tester", "Security Engineer", "Information Security Manager"],
            "resources": ["SANS Institute", "Cybersecurity Conferences", "Security Certifications", "CTF Competitions"]
        },
        "Accountant": {
            "description": "Prepare and examine financial records to ensure accuracy and compliance with regulations.",
            "required_education": "Bachelor's degree in Accounting or related field; CPA for advanced roles.",
            "required_skills": ["Financial Reporting", "Tax Preparation", "Auditing", "Attention to Detail", "Analytical Skills"],
            "salary_range": "$55,000 - $130,000+",
            "job_outlook": "Average (7% growth by 2030)",
            "work_environment": "Accounting firms, Corporations, Government, Nonprofits",
            "related_careers": ["Financial Auditor", "Tax Accountant", "Forensic Accountant", "Controller"],
            "resources": ["American Institute of CPAs", "Accounting Software Tutorials", "CPA Exam Resources", "Accounting Standards Updates"]
        },
        "Sales Manager": {
            "description": "Lead sales teams to achieve revenue goals and implement sales strategies.",
            "required_education": "Bachelor's degree in Business, Marketing, or related field; experience crucial.",
            "required_skills": ["Sales Techniques", "Leadership", "Customer Relationship Management", "Negotiation", "Market Analysis"],
            "salary_range": "$65,000 - $170,000+",
            "job_outlook": "Average (5% growth by 2030)",
            "work_environment": "Retail, Manufacturing, Wholesale, Technology, Pharmaceuticals",
            "related_careers": ["Business Development Manager", "Account Executive", "Sales Director", "Regional Sales Manager"],
            "resources": ["Sales Training Programs", "CRM Software Tutorials", "Sales Books and Podcasts", "Industry Conferences"]
        },
        "Research Scientist": {
            "description": "Conduct research to advance knowledge in a particular field of science.",
            "required_education": "PhD in a scientific field like Biology, Chemistry, Physics, or related area.",
            "required_skills": ["Research Methodology", "Data Analysis", "Lab Techniques", "Technical Writing", "Critical Thinking"],
            "salary_range": "$70,000 - $150,000+",
            "job_outlook": "Faster than average (8% growth by 2030)",
            "work_environment": "Universities, Research institutions, Government labs, Pharmaceutical companies",
            "related_careers": ["Academic Researcher", "Clinical Researcher", "R&D Scientist", "Laboratory Manager"],
            "resources": ["Academic Journals", "Scientific Conferences", "Research Grants Information", "Lab Technique Resources"]
        }
    }
    
    # Return the career details if found, otherwise return a default structure
    if career_name in career_data:
        return career_data[career_name]
    else:
        return {
            "description": "Information not available",
            "required_education": "Information not available",
            "required_skills": [],
            "salary_range": "Information not available",
            "job_outlook": "Information not available",
            "work_environment": "Information not available",
            "related_careers": [],
            "resources": []
        }
