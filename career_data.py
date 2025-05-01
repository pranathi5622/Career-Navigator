"""
Career data module that provides information about various career paths,
including milestones, resources, skills, and comparison metrics.
"""

# Dictionary of career paths with their details
CAREER_PATHS = {
    "software developer": {
        "milestones": [
            {"title": "Learn programming fundamentals", "level": "Beginner", "description": "Master a programming language like Python or JavaScript and understand basic algorithms and data structures."},
            {"title": "Build personal projects", "level": "Beginner", "description": "Create small applications to apply your knowledge and start building a portfolio."},
            {"title": "Learn version control", "level": "Beginner", "description": "Become proficient with Git and GitHub for collaboration and code management."},
            {"title": "Gain frontend/backend expertise", "level": "Intermediate", "description": "Specialize in either frontend (React, Angular) or backend (Node.js, Django) technologies."},
            {"title": "Learn testing methodologies", "level": "Intermediate", "description": "Master unit testing, integration testing, and test-driven development approaches."},
            {"title": "Understand DevOps basics", "level": "Intermediate", "description": "Learn CI/CD pipelines, containerization with Docker, and deployment strategies."},
            {"title": "Master system design", "level": "Advanced", "description": "Learn how to design scalable, resilient systems and microservice architectures."},
            {"title": "Lead development teams", "level": "Advanced", "description": "Take on leadership roles and guide junior developers in project implementation."},
            {"title": "Contribute to open source", "level": "Advanced", "description": "Collaborate on open-source projects to gain visibility and broaden your experience."}
        ],
        "resources": [
            {"title": "freeCodeCamp", "url": "https://www.freecodecamp.org", "type": "Learning Platform"},
            {"title": "The Odin Project", "url": "https://www.theodinproject.com", "type": "Learning Platform"},
            {"title": "LeetCode", "url": "https://leetcode.com", "type": "Practice Platform"},
            {"title": "GitHub", "url": "https://github.com", "type": "Version Control"},
            {"title": "Stack Overflow", "url": "https://stackoverflow.com", "type": "Community"},
            {"title": "Dev.to", "url": "https://dev.to", "type": "Community"}
        ],
        "skills_required": [
            "Problem-solving",
            "Programming fundamentals",
            "Data structures & algorithms",
            "Version control",
            "Frontend/backend technologies",
            "Database management",
            "Software architecture",
            "Testing methodologies",
            "Communication",
            "Teamwork"
        ],
        "salary_range": "$70,000 - $150,000+",
        "job_growth": "22% (Much faster than average)",
        "work_life_balance": 4,
        "job_satisfaction": 4.5,
        "job_stability": 4
    },
    "data scientist": {
        "milestones": [
            {"title": "Learn programming basics", "level": "Beginner", "description": "Master Python and R for data analysis and manipulation."},
            {"title": "Master data wrangling", "level": "Beginner", "description": "Learn to clean, transform, and prepare data for analysis."},
            {"title": "Learn statistics fundamentals", "level": "Beginner", "description": "Understand descriptive and inferential statistics for data interpretation."},
            {"title": "Master data visualization", "level": "Intermediate", "description": "Use tools like Matplotlib, Seaborn, and Tableau to create compelling visualizations."},
            {"title": "Learn machine learning", "level": "Intermediate", "description": "Understand supervised and unsupervised learning algorithms and their applications."},
            {"title": "Master feature engineering", "level": "Intermediate", "description": "Learn techniques to extract and select relevant features from raw data."},
            {"title": "Learn deep learning", "level": "Advanced", "description": "Understand neural networks, CNNs, RNNs, and their implementations."},
            {"title": "Master big data technologies", "level": "Advanced", "description": "Learn Hadoop, Spark, and other big data processing frameworks."},
            {"title": "Develop expertise in MLOps", "level": "Advanced", "description": "Learn to deploy, monitor, and maintain machine learning models in production."}
        ],
        "resources": [
            {"title": "Kaggle", "url": "https://www.kaggle.com", "type": "Learning & Competition"},
            {"title": "DataCamp", "url": "https://www.datacamp.com", "type": "Learning Platform"},
            {"title": "Coursera", "url": "https://www.coursera.org", "type": "Learning Platform"},
            {"title": "Towards Data Science", "url": "https://towardsdatascience.com", "type": "Publication"},
            {"title": "Stack Exchange Data Science", "url": "https://datascience.stackexchange.com", "type": "Community"},
            {"title": "GitHub", "url": "https://github.com", "type": "Version Control"}
        ],
        "skills_required": [
            "Programming (Python, R)",
            "Statistics",
            "Machine learning",
            "Deep learning",
            "Data wrangling",
            "Data visualization",
            "SQL and database knowledge",
            "Big data processing",
            "Communication",
            "Critical thinking"
        ],
        "salary_range": "$85,000 - $170,000+",
        "job_growth": "31% (Much faster than average)",
        "work_life_balance": 3.5,
        "job_satisfaction": 4.2,
        "job_stability": 4.5
    },
    "ux designer": {
        "milestones": [
            {"title": "Learn design fundamentals", "level": "Beginner", "description": "Understand color theory, typography, and layout principles."},
            {"title": "Master UX research methods", "level": "Beginner", "description": "Learn user interviews, surveys, and usability testing techniques."},
            {"title": "Learn wireframing", "level": "Beginner", "description": "Create low-fidelity designs and user flows using tools like Figma or Adobe XD."},
            {"title": "Master prototyping", "level": "Intermediate", "description": "Create interactive prototypes to test user interactions and flows."},
            {"title": "Learn information architecture", "level": "Intermediate", "description": "Organize and structure content for optimal user experience."},
            {"title": "Master UI design", "level": "Intermediate", "description": "Create visually appealing interfaces that balance aesthetics and usability."},
            {"title": "Learn accessibility standards", "level": "Advanced", "description": "Ensure designs are inclusive and usable by people with diverse abilities."},
            {"title": "Master design systems", "level": "Advanced", "description": "Create and maintain scalable design systems for consistent user experiences."},
            {"title": "Lead UX teams", "level": "Advanced", "description": "Guide design processes and mentor junior designers on projects."}
        ],
        "resources": [
            {"title": "Figma", "url": "https://www.figma.com", "type": "Design Tool"},
            {"title": "Adobe XD", "url": "https://www.adobe.com/products/xd.html", "type": "Design Tool"},
            {"title": "Dribbble", "url": "https://dribbble.com", "type": "Inspiration"},
            {"title": "Behance", "url": "https://www.behance.net", "type": "Inspiration"},
            {"title": "Nielsen Norman Group", "url": "https://www.nngroup.com", "type": "Research & Articles"},
            {"title": "Interaction Design Foundation", "url": "https://www.interaction-design.org", "type": "Learning Platform"}
        ],
        "skills_required": [
            "Visual design",
            "User research",
            "Wireframing",
            "Prototyping",
            "Information architecture",
            "Usability testing",
            "Design thinking",
            "UI design",
            "Communication",
            "Empathy"
        ],
        "salary_range": "$65,000 - $125,000+",
        "job_growth": "13% (Faster than average)",
        "work_life_balance": 4,
        "job_satisfaction": 4.3,
        "job_stability": 3.8
    },
    "digital marketer": {
        "milestones": [
            {"title": "Learn marketing fundamentals", "level": "Beginner", "description": "Understand basic marketing principles, customer journey, and buyer personas."},
            {"title": "Master content creation", "level": "Beginner", "description": "Learn to create engaging blog posts, social media content, and email campaigns."},
            {"title": "Learn SEO basics", "level": "Beginner", "description": "Understand search engine optimization to improve content visibility."},
            {"title": "Master social media marketing", "level": "Intermediate", "description": "Develop strategies for effective social media campaigns across platforms."},
            {"title": "Learn paid advertising", "level": "Intermediate", "description": "Understand PPC, display ads, and social media advertising strategies."},
            {"title": "Master analytics", "level": "Intermediate", "description": "Learn to analyze campaign performance using tools like Google Analytics."},
            {"title": "Learn marketing automation", "level": "Advanced", "description": "Implement automated marketing workflows and lead nurturing campaigns."},
            {"title": "Master conversion optimization", "level": "Advanced", "description": "Optimize landing pages and user journeys to improve conversion rates."},
            {"title": "Develop integrated marketing strategies", "level": "Advanced", "description": "Create comprehensive multi-channel marketing plans aligned with business goals."}
        ],
        "resources": [
            {"title": "HubSpot Academy", "url": "https://academy.hubspot.com", "type": "Learning Platform"},
            {"title": "Google Digital Garage", "url": "https://learndigital.withgoogle.com", "type": "Learning Platform"},
            {"title": "Moz", "url": "https://moz.com", "type": "SEO Resource"},
            {"title": "Content Marketing Institute", "url": "https://contentmarketinginstitute.com", "type": "Publication"},
            {"title": "Search Engine Journal", "url": "https://www.searchenginejournal.com", "type": "Publication"},
            {"title": "MarketingProfs", "url": "https://www.marketingprofs.com", "type": "Community & Resources"}
        ],
        "skills_required": [
            "Content creation",
            "SEO",
            "Social media marketing",
            "Email marketing",
            "Paid advertising",
            "Analytics",
            "Marketing automation",
            "Conversion optimization",
            "Communication",
            "Creativity"
        ],
        "salary_range": "$50,000 - $110,000+",
        "job_growth": "10% (Faster than average)",
        "work_life_balance": 3.5,
        "job_satisfaction": 4.0,
        "job_stability": 3.5
    },
    "product manager": {
        "milestones": [
            {"title": "Learn product fundamentals", "level": "Beginner", "description": "Understand the product development lifecycle and management methodologies."},
            {"title": "Master market research", "level": "Beginner", "description": "Learn to analyze market trends, user needs, and competitive landscape."},
            {"title": "Learn user story creation", "level": "Beginner", "description": "Create clear, concise user stories to guide product development."},
            {"title": "Master roadmap planning", "level": "Intermediate", "description": "Develop strategic product roadmaps aligned with business goals."},
            {"title": "Learn agile methodologies", "level": "Intermediate", "description": "Understand Scrum, Kanban, and other agile frameworks for product development."},
            {"title": "Master stakeholder management", "level": "Intermediate", "description": "Develop skills to manage expectations and communication across teams."},
            {"title": "Learn product analytics", "level": "Advanced", "description": "Use data and metrics to drive product decisions and improvements."},
            {"title": "Master feature prioritization", "level": "Advanced", "description": "Develop frameworks for prioritizing features based on impact and effort."},
            {"title": "Lead product strategy", "level": "Advanced", "description": "Shape long-term product vision and strategy aligned with business objectives."}
        ],
        "resources": [
            {"title": "Product School", "url": "https://www.productschool.com", "type": "Learning Platform"},
            {"title": "Mind the Product", "url": "https://www.mindtheproduct.com", "type": "Community & Resources"},
            {"title": "ProductPlan", "url": "https://www.productplan.com", "type": "Tool & Resources"},
            {"title": "Product Hunt", "url": "https://www.producthunt.com", "type": "Product Discovery"},
            {"title": "Atlassian", "url": "https://www.atlassian.com/agile", "type": "Agile Resources"},
            {"title": "UserVoice", "url": "https://www.uservoice.com", "type": "Feedback Tool"}
        ],
        "skills_required": [
            "Market research",
            "User story writing",
            "Roadmap planning",
            "Agile methodologies",
            "Stakeholder management",
            "Product analytics",
            "Feature prioritization",
            "Strategic thinking",
            "Communication",
            "Leadership"
        ],
        "salary_range": "$80,000 - $160,000+",
        "job_growth": "8% (As fast as average)",
        "work_life_balance": 3.5,
        "job_satisfaction": 4.2,
        "job_stability": 4.0
    }
}

# List of additional careers for recommendations
ADDITIONAL_CAREERS = [
    "web developer",
    "mobile app developer",
    "cloud solutions architect",
    "business analyst",
    "cybersecurity analyst",
    "network administrator",
    "database administrator",
    "IT project manager",
    "technical writer",
    "quality assurance engineer",
    "devops engineer",
    "machine learning engineer",
    "business intelligence analyst",
    "frontend developer",
    "backend developer",
    "full stack developer",
    "UI designer",
    "game developer",
    "artificial intelligence specialist",
    "blockchain developer"
]

# Interest to career mapping for recommendations
INTEREST_TO_CAREERS = {
    "technology": [
        "software developer", 
        "data scientist", 
        "web developer", 
        "cybersecurity analyst", 
        "cloud solutions architect",
        "mobile app developer",
        "devops engineer"
    ],
    "healthcare": [
        "health informatics specialist",
        "medical researcher",
        "healthcare administrator",
        "biomedical engineer",
        "clinical data analyst"
    ],
    "business": [
        "product manager",
        "business analyst",
        "digital marketer",
        "financial analyst",
        "business intelligence analyst"
    ],
    "arts": [
        "ux designer",
        "UI designer",
        "graphic designer",
        "content creator",
        "game developer"
    ],
    "science": [
        "data scientist",
        "research scientist",
        "machine learning engineer",
        "artificial intelligence specialist",
        "bioinformatics scientist"
    ],
    "education": [
        "instructional designer",
        "technical trainer",
        "educational technology specialist",
        "curriculum developer",
        "e-learning developer"
    ],
    "trades": [
        "IT support specialist",
        "network technician",
        "computer technician",
        "telecommunications specialist",
        "audio/visual technician"
    ],
    "service": [
        "IT project manager",
        "customer success manager",
        "technical account manager",
        "technical support specialist",
        "technical consultant"
    ]
}

# Skills to career mapping for recommendations
SKILLS_TO_CAREERS = {
    "programming": [
        "software developer",
        "web developer",
        "mobile app developer",
        "data scientist",
        "game developer"
    ],
    "analytics": [
        "data scientist",
        "business intelligence analyst",
        "data analyst",
        "business analyst",
        "financial analyst"
    ],
    "design": [
        "ux designer",
        "UI designer",
        "graphic designer",
        "web developer",
        "product manager"
    ],
    "communication": [
        "product manager",
        "digital marketer",
        "technical writer",
        "customer success manager",
        "IT project manager"
    ],
    "problem-solving": [
        "software developer",
        "data scientist",
        "cybersecurity analyst",
        "business analyst",
        "devops engineer"
    ]
}

def get_career_info(career_title):
    """Get information about a specific career path."""
    career_title = career_title.lower()
    
    if career_title in CAREER_PATHS:
        return CAREER_PATHS[career_title]
    else:
        # Return default structure for unknown careers
        return {
            "milestones": [
                {"title": "Research this career path", "level": "Beginner", "description": "This career isn't in our database yet. Start by researching online about this field."},
            ],
            "resources": [
                {"title": "Indeed Career Guide", "url": "https://www.indeed.com/career-advice", "type": "Career Information"},
                {"title": "Bureau of Labor Statistics", "url": "https://www.bls.gov/ooh/", "type": "Government Resource"},
            ],
            "skills_required": ["Research skills to learn more about this career path"],
            "salary_range": "Unknown - please research",
            "job_growth": "Unknown - please research",
            "work_life_balance": 3,
            "job_satisfaction": 3,
            "job_stability": 3
        }

def compare_careers(career_one, career_two):
    """Compare two career paths and provide detailed comparison."""
    career_one = career_one.lower()
    career_two = career_two.lower()
    
    career_one_info = get_career_info(career_one)
    career_two_info = get_career_info(career_two)
    
    # Common skills between the two careers
    common_skills = list(set(career_one_info["skills_required"]) & 
                         set(career_two_info["skills_required"]))
    
    # Unique skills for each career
    career_one_unique = list(set(career_one_info["skills_required"]) - 
                             set(career_two_info["skills_required"]))
    career_two_unique = list(set(career_two_info["skills_required"]) - 
                             set(career_one_info["skills_required"]))
    
    comparison = {
        "career_one": {
            "title": career_one,
            "info": career_one_info,
            "unique_skills": career_one_unique
        },
        "career_two": {
            "title": career_two,
            "info": career_two_info,
            "unique_skills": career_two_unique
        },
        "common_skills": common_skills,
        "comparison_metrics": {
            "salary": {
                "career_one": career_one_info["salary_range"],
                "career_two": career_two_info["salary_range"]
            },
            "job_growth": {
                "career_one": career_one_info["job_growth"],
                "career_two": career_two_info["job_growth"]
            },
            "work_life_balance": {
                "career_one": career_one_info["work_life_balance"],
                "career_two": career_two_info["work_life_balance"]
            },
            "job_satisfaction": {
                "career_one": career_one_info["job_satisfaction"],
                "career_two": career_two_info["job_satisfaction"]
            },
            "job_stability": {
                "career_one": career_one_info["job_stability"],
                "career_two": career_two_info["job_stability"]
            }
        }
    }
    
    return comparison

def get_recommendations(interests=None, skills=None, resume_skills=None):
    """Get career recommendations based on interests and skills."""
    recommended_careers = set()
    
    # Add recommendations based on interests
    if interests:
        for interest in interests:
            if interest in INTEREST_TO_CAREERS:
                recommended_careers.update(INTEREST_TO_CAREERS[interest])
    
    # Add recommendations based on skills
    if skills:
        for skill in skills:
            if skill in SKILLS_TO_CAREERS:
                recommended_careers.update(SKILLS_TO_CAREERS[skill])
    
    # Add recommendations based on resume skills
    if resume_skills:
        for skill in resume_skills:
            skill_lower = skill.lower()
            # Look for partial matches in skill keys
            for key in SKILLS_TO_CAREERS:
                if skill_lower in key or key in skill_lower:
                    recommended_careers.update(SKILLS_TO_CAREERS[key])
    
    # Convert to list and get career info for each
    recommendations = []
    for career in list(recommended_careers)[:5]:  # Limit to top 5
        if career in CAREER_PATHS:
            recommendations.append({
                "title": career,
                "info": CAREER_PATHS[career]
            })
    
    return recommendations
