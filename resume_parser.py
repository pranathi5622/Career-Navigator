import os
import re
import logging
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Set up logging
logger = logging.getLogger(__name__)

# Download NLTK data if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Define skill keywords for different domains
SKILL_KEYWORDS = {
    "technical": [
        "python", "java", "javascript", "html", "css", "sql", "nosql", "react", "angular", "vue", 
        "node.js", "django", "flask", "spring", "asp.net", "php", "ruby", "c#", "c++", "swift",
        "kotlin", "typescript", "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "jenkins",
        "git", "cicd", "linux", "windows", "macos", "bash", "powershell", "rest", "graphql", "api"
    ],
    "data_science": [
        "machine learning", "ml", "artificial intelligence", "ai", "deep learning", "nlp",
        "natural language processing", "computer vision", "data analysis", "data mining",
        "pandas", "numpy", "scipy", "scikit-learn", "tensorflow", "pytorch", "keras",
        "r", "tableau", "power bi", "statistics", "regression", "classification",
        "clustering", "big data", "hadoop", "spark", "data visualization", "data modeling"
    ],
    "design": [
        "ui", "ux", "user interface", "user experience", "figma", "sketch", "adobe xd",
        "photoshop", "illustrator", "indesign", "wireframing", "prototyping", "typography",
        "color theory", "responsive design", "web design", "graphic design", "visual design",
        "interaction design", "user research", "usability testing", "information architecture"
    ],
    "business": [
        "project management", "agile", "scrum", "kanban", "product management", "marketing",
        "sales", "customer relationship management", "crm", "seo", "sem", "content marketing",
        "social media marketing", "email marketing", "market research", "analytics", "strategy",
        "business development", "leadership", "team management", "budgeting", "financial analysis"
    ],
    "communication": [
        "writing", "editing", "public speaking", "presentation", "communication", "negotiation",
        "conflict resolution", "teamwork", "collaboration", "interpersonal", "customer service",
        "client relationship", "consulting", "facilitation", "interviewing", "storytelling",
        "technical writing", "content creation", "copywriting", "documentation"
    ]
}

# Define education-related keywords
EDUCATION_KEYWORDS = [
    "bachelor", "master", "phd", "doctorate", "mba", "bs", "ba", "ms", "ma", "btech", "mtech",
    "associate", "diploma", "certificate", "certification", "degree", "university", "college",
    "institute", "school", "academy", "major", "minor", "concentration", "specialization"
]

# Define experience-related keywords and patterns
EXPERIENCE_PATTERNS = [
    r'(\d+)\+?\s*years?\s*of\s*experience',
    r'experience\s*of\s*(\d+)\+?\s*years?',
    r'(\d+)\+?\s*years?\s*experience',
]

def process_resume_file(file_path):
    """
    Extract relevant information from a resume file.
    Returns tuple of (skills, education, experience_years)
    """
    try:
        # Check file extension
        _, ext = os.path.splitext(file_path)
        
        if ext.lower() == '.pdf':
            text = extract_text_from_pdf(file_path)
        else:
            # For simplicity, we'll only support PDF files in this implementation
            logger.warning(f"Unsupported file format: {ext}")
            return [], [], 0
        
        # Process the extracted text
        skills = extract_skills(text)
        education = extract_education(text)
        experience_years = extract_experience(text)
        
        return skills, education, experience_years
        
    except Exception as e:
        logger.error(f"Error processing resume: {str(e)}")
        return [], [], 0

def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + " "
        
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        return ""

def extract_skills(text):
    """Extract skills from resume text"""
    skills = []
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Tokenize the text
    words = word_tokenize(text_lower)
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if w.isalnum() and w not in stop_words]
    
    # Check for skills in each category
    for category, keywords in SKILL_KEYWORDS.items():
        for skill in keywords:
            # Check for exact matches (for multi-word skills)
            if " " in skill and skill in text_lower:
                skills.append(skill)
            # Check for single word skills
            elif skill in filtered_words:
                skills.append(skill)
    
    # Remove duplicates and return
    return list(set(skills))

def extract_education(text):
    """Extract education information from resume text"""
    education = []
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Check for education keywords
    for keyword in EDUCATION_KEYWORDS:
        if keyword in text_lower:
            # Find the sentence containing the keyword
            sentences = re.split(r'[.!?]+', text_lower)
            for sentence in sentences:
                if keyword in sentence:
                    # Clean and add the education info
                    clean_sentence = sentence.strip()
                    if clean_sentence and len(clean_sentence) > 5:  # Avoid very short fragments
                        education.append(clean_sentence)
    
    # Return unique education entries
    return list(set(education))

def extract_experience(text):
    """Extract years of experience from resume text"""
    text_lower = text.lower()
    
    for pattern in EXPERIENCE_PATTERNS:
        matches = re.search(pattern, text_lower)
        if matches:
            try:
                years = int(matches.group(1))
                return years
            except (ValueError, IndexError):
                continue
    
    # If no clear years of experience found, estimate based on job history
    # This is a simplified approach - in a production system, you'd do more sophisticated parsing
    job_count = len(re.findall(r'\b(job title|position|role)\b', text_lower, re.IGNORECASE))
    if job_count > 0:
        # Rough estimate: 2 years per job mentioned
        return min(job_count * 2, 20)  # Cap at 20 years to avoid overestimation
    
    return 0
