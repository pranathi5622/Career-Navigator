"""
Configuration settings for the Career Guidance application.
"""

import os

# Flask configuration
DEBUG = True
SECRET_KEY = os.environ.get("SESSION_SECRET", "development-secret-key")
PORT = 5000
HOST = "0.0.0.0"

# File upload configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///career_guidance.db")

# Questionnaire configuration
SKILLS_QUESTIONS = [
    {
        "id": 1,
        "text": "Which of these activities do you enjoy the most?",
        "options": [
            {"id": 1, "text": "Solving complex problems", "value": "problem-solving"},
            {"id": 2, "text": "Creating visual designs", "value": "design"},
            {"id": 3, "text": "Analyzing data and finding patterns", "value": "analytics"},
            {"id": 4, "text": "Writing code and building applications", "value": "programming"},
            {"id": 5, "text": "Explaining complex ideas to others", "value": "communication"}
        ]
    },
    {
        "id": 2,
        "text": "What type of projects would you prefer to work on?",
        "options": [
            {"id": 6, "text": "Building a new application or website", "value": "programming"},
            {"id": 7, "text": "Creating a user interface for a product", "value": "design"},
            {"id": 8, "text": "Analyzing data to find business insights", "value": "analytics"},
            {"id": 9, "text": "Solving technical challenges and bugs", "value": "problem-solving"},
            {"id": 10, "text": "Creating documentation or presentations", "value": "communication"}
        ]
    },
    {
        "id": 3,
        "text": "Which tools or technologies are you most interested in learning?",
        "options": [
            {"id": 11, "text": "Programming languages (Python, JavaScript, etc.)", "value": "programming"},
            {"id": 12, "text": "Design software (Figma, Adobe XD, etc.)", "value": "design"},
            {"id": 13, "text": "Data analysis tools (Excel, Tableau, R, etc.)", "value": "analytics"},
            {"id": 14, "text": "Problem-solving methodologies", "value": "problem-solving"},
            {"id": 15, "text": "Communication and presentation tools", "value": "communication"}
        ]
    },
    {
        "id": 4,
        "text": "In a team project, which role would you naturally take?",
        "options": [
            {"id": 16, "text": "The implementer who builds the solution", "value": "programming"},
            {"id": 17, "text": "The designer who creates the look and feel", "value": "design"},
            {"id": 18, "text": "The analyst who evaluates data and options", "value": "analytics"},
            {"id": 19, "text": "The troubleshooter who solves problems", "value": "problem-solving"},
            {"id": 20, "text": "The communicator who explains ideas", "value": "communication"}
        ]
    },
    {
        "id": 5,
        "text": "Which achievement would make you most proud?",
        "options": [
            {"id": 21, "text": "Building a successful application", "value": "programming"},
            {"id": 22, "text": "Creating a beautiful and intuitive design", "value": "design"},
            {"id": 23, "text": "Discovering insights that drive business decisions", "value": "analytics"},
            {"id": 24, "text": "Solving a difficult technical challenge", "value": "problem-solving"},
            {"id": 25, "text": "Effectively explaining complex concepts", "value": "communication"}
        ]
    }
]

INTERESTS_QUESTIONS = [
    {
        "id": 6,
        "text": "Which industry interests you the most?",
        "options": [
            {"id": 26, "text": "Technology and computing", "value": "technology"},
            {"id": 27, "text": "Healthcare and medicine", "value": "healthcare"},
            {"id": 28, "text": "Business and finance", "value": "business"},
            {"id": 29, "text": "Arts and creative fields", "value": "arts"},
            {"id": 30, "text": "Science and research", "value": "science"}
        ]
    },
    {
        "id": 7,
        "text": "What type of workplace environment do you prefer?",
        "options": [
            {"id": 31, "text": "Tech startup or innovative company", "value": "technology"},
            {"id": 32, "text": "Healthcare facility or research lab", "value": "healthcare"},
            {"id": 33, "text": "Corporate office or financial institution", "value": "business"},
            {"id": 34, "text": "Creative studio or design agency", "value": "arts"},
            {"id": 35, "text": "Research institution or laboratory", "value": "science"}
        ]
    },
    {
        "id": 8,
        "text": "Which of these activities would you find most fulfilling?",
        "options": [
            {"id": 36, "text": "Developing new technologies", "value": "technology"},
            {"id": 37, "text": "Improving healthcare or patient outcomes", "value": "healthcare"},
            {"id": 38, "text": "Growing businesses or managing finances", "value": "business"},
            {"id": 39, "text": "Creating art or designing experiences", "value": "arts"},
            {"id": 40, "text": "Conducting research or experiments", "value": "science"}
        ]
    }
]

VALUES_QUESTIONS = [
    {
        "id": 9,
        "text": "Which of these work values is most important to you?",
        "options": [
            {"id": 41, "text": "Innovation and staying at the cutting edge", "value": "innovation"},
            {"id": 42, "text": "Work-life balance and stability", "value": "balance"},
            {"id": 43, "text": "Financial rewards and compensation", "value": "compensation"},
            {"id": 44, "text": "Making a positive impact on society", "value": "impact"},
            {"id": 45, "text": "Continuous learning and growth", "value": "growth"}
        ]
    },
    {
        "id": 10,
        "text": "When choosing a career, what matters most to you?",
        "options": [
            {"id": 46, "text": "Opportunity to be creative and innovative", "value": "innovation"},
            {"id": 47, "text": "Predictable hours and job security", "value": "balance"},
            {"id": 48, "text": "High earning potential and benefits", "value": "compensation"},
            {"id": 49, "text": "Making a difference in people's lives", "value": "impact"},
            {"id": 50, "text": "Constant challenges and learning opportunities", "value": "growth"}
        ]
    }
]

# Combine all questions for the questionnaire
QUESTIONNAIRE = SKILLS_QUESTIONS + INTERESTS_QUESTIONS + VALUES_QUESTIONS
