import os
import re
import PyPDF2
import logging
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

logger = logging.getLogger(__name__)

class ResumeParser:
    def __init__(self):
        self.skills_keywords = [
            # Technical skills
            'python', 'javascript', 'java', 'c++', 'sql', 'html', 'css', 'react', 'angular', 'node.js',
            'django', 'flask', 'spring', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git',
            # Soft skills
            'leadership', 'communication', 'teamwork', 'problem solving', 'critical thinking',
            'time management', 'project management', 'creativity', 'adaptability', 'collaboration',
            # Common tools and frameworks
            'excel', 'powerpoint', 'word', 'tableau', 'power bi', 'photoshop', 'illustrator',
            'salesforce', 'jira', 'confluence', 'agile', 'scrum', 'kanban', 'lean', 'six sigma'
        ]
        
        self.degree_patterns = [
            r'(?:B\.?S\.?|Bachelor of Science)',
            r'(?:B\.?A\.?|Bachelor of Arts)',
            r'(?:M\.?S\.?|Master of Science)',
            r'(?:M\.?B\.?A\.?|Master of Business Administration)',
            r'(?:Ph\.?D\.?|Doctor of Philosophy)',
            r'(?:M\.?D\.?|Doctor of Medicine)',
            r'(?:J\.?D\.?|Juris Doctor)',
            r'Associate(?:\s+of\s+(?:Arts|Science|Applied Science))?'
        ]
        
        self.experience_patterns = [
            r'(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\s+(?:-|to|–)\s+(?:(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}|Present|Current)',
            r'\d{4}\s+(?:-|to|–)\s+(?:\d{4}|Present|Current)',
            r'(?:Senior|Junior|Lead)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*',
            r'(?:Manager|Director|Engineer|Developer|Designer|Analyst|Consultant|Specialist|Coordinator|Administrator)'
        ]
        
        self.stop_words = set(stopwords.words('english'))
        
    def parse_pdf(self, file_path):
        try:
            text = ""
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
            
            return self._analyze_resume_text(text)
        
        except Exception as e:
            logger.error(f"Error parsing PDF: {str(e)}")
            return {
                "error": str(e),
                "skills": [],
                "education": [],
                "experience": []
            }
    
    def _analyze_resume_text(self, text):
        if not text:
            return {
                "error": "No text could be extracted from the resume",
                "skills": [],
                "education": [],
                "experience": []
            }
        
        # Extract skills
        skills = self._extract_skills(text)
        
        # Extract education
        education = self._extract_education(text)
        
        # Extract experience
        experience = self._extract_experience(text)
        
        return {
            "skills": skills,
            "education": education,
            "experience": experience
        }
    
    def _extract_skills(self, text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in self.stop_words]
        
        skills = []
        for keyword in self.skills_keywords:
            if keyword in ' '.join(filtered_tokens):
                skills.append(keyword)
        
        return skills
    
    def _extract_education(self, text):
        education = []
        
        # Look for degree patterns
        for pattern in self.degree_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get the context around the match
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end]
                
                # Clean up the context
                context = re.sub(r'\s+', ' ', context)
                education.append(context.strip())
        
        return education
    
    def _extract_experience(self, text):
        experience = []
        
        # Look for experience patterns
        for pattern in self.experience_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get the context around the match
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end]
                
                # Clean up the context
                context = re.sub(r'\s+', ' ', context)
                experience.append(context.strip())
        
        return experience
