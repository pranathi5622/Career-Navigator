"""
Resume Optimizer Module

This module provides functions to analyze a resume and generate
optimization suggestions based on target careers and best practices.
"""

import re
import logging
from collections import Counter
from resume_parser import extract_text_from_pdf
from career_data import get_career_details, get_all_careers

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Resume sections typically found
RESUME_SECTIONS = [
    "summary", "objective", "profile", 
    "experience", "work experience", "employment", "work history",
    "education", "academic", "qualifications", "training",
    "skills", "abilities", "competencies", "expertise",
    "projects", "achievements", "accomplishments",
    "certifications", "certificates", "licenses",
    "volunteer", "community service",
    "languages", "language skills",
    "interests", "hobbies", "activities"
]

# Common action verbs that strengthen resume content
STRONG_ACTION_VERBS = [
    "achieved", "improved", "increased", "decreased", "reduced", "saved",
    "developed", "created", "designed", "implemented", "launched", "established",
    "managed", "led", "directed", "supervised", "mentored", "trained",
    "analyzed", "evaluated", "researched", "identified", "solved", "resolved",
    "coordinated", "organized", "planned", "executed", "delivered", "produced",
    "negotiated", "secured", "obtained", "generated", "streamlined", "optimized"
]

# Common weak words and phrases to avoid in resumes
WEAK_WORDS = [
    "responsible for", "duties included", "worked on", "helped with",
    "assisted with", "was tasked with", "tried to", "attempted to",
    "was involved in", "participated in", "supported", "handled"
]

def analyze_resume(resume_text):
    """
    Analyze resume text and identify potential improvement areas
    
    Args:
        resume_text: String content of the resume
        
    Returns:
        Dictionary with analysis results
    """
    # Handle case where resume_text might be None
    if resume_text is None:
        resume_text = ""
    
    resume_text = resume_text.lower()
    
    # Identify which sections are present in the resume
    sections_present = []
    for section in RESUME_SECTIONS:
        if section in resume_text or section.title() in resume_text:
            sections_present.append(section)
    
    # Count action verbs used
    action_verb_count = 0
    for verb in STRONG_ACTION_VERBS:
        action_verb_count += len(re.findall(r'\b' + verb + r'\b', resume_text))
    
    # Count weak phrases used
    weak_phrase_count = 0
    for phrase in WEAK_WORDS:
        weak_phrase_count += len(re.findall(r'\b' + phrase + r'\b', resume_text))
    
    # Check for quantifiable achievements (numbers, percentages)
    quantifiable_achievements = len(re.findall(r'\d+%|\$\d+|\d+ percent|\d+ people|\d+ team', resume_text))
    
    # Check for contact information
    has_email = bool(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resume_text))
    has_phone = bool(re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', resume_text))
    has_linkedin = "linkedin.com" in resume_text
    
    # Bullet point usage
    bullet_points = len(re.findall(r'•|\*|\-|\–', resume_text))
    
    # Approximate resume length based on word count
    word_count = len(resume_text.split())
    
    # Find common keywords used
    words = re.findall(r'\b[a-zA-Z]{3,}\b', resume_text)
    common_words = Counter(words).most_common(10)
    
    return {
        "sections_present": sections_present,
        "missing_sections": [s for s in ["summary", "experience", "education", "skills"] if s not in sections_present],
        "action_verb_count": action_verb_count,
        "weak_phrase_count": weak_phrase_count,
        "quantifiable_achievements": quantifiable_achievements,
        "has_complete_contact_info": has_email and has_phone,
        "has_linkedin": has_linkedin,
        "bullet_point_count": bullet_points,
        "word_count": word_count,
        "common_words": common_words
    }

def get_career_keyword_matches(resume_text, career_name):
    """
    Find matches between resume content and career-specific keywords
    
    Args:
        resume_text: String content of the resume
        career_name: Target career name
        
    Returns:
        Dictionary with matching and missing keywords
    """
    # Handle case where resume_text might be None
    if resume_text is None:
        resume_text = ""
        
    resume_text = resume_text.lower()
    career_details = get_career_details(career_name)
    
    # Extract skills and keywords from career details
    career_skills = []
    
    # Handle case where career_details might be None
    if career_details is None:
        return {
            "matching_skills": [],
            "missing_skills": [],
            "match_percentage": 0
        }
        
    required_skills = career_details.get('required_skills')
    
    if required_skills is not None:
        if isinstance(required_skills, list):
            career_skills = [skill.lower() for skill in required_skills]
        elif isinstance(required_skills, str):
            career_skills = [skill.strip().lower() for skill in required_skills.split(',')]
    
    # Find matches
    matching_skills = []
    missing_skills = []
    
    for skill in career_skills:
        if skill in resume_text:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)
    
    match_percentage = 0
    if career_skills:
        match_percentage = round((len(matching_skills) / len(career_skills)) * 100)
    
    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }

def generate_optimization_suggestions(resume_file_path, target_career=None):
    """
    Generate resume optimization suggestions based on analysis
    
    Args:
        resume_file_path: Path to resume PDF file
        target_career: Optional target career to optimize for
        
    Returns:
        Dictionary with optimization suggestions
    """
    try:
        # Extract text from resume
        resume_text = extract_text_from_pdf(resume_file_path)
        
        # Basic resume analysis
        analysis = analyze_resume(resume_text)
        
        # Generate general suggestions
        suggestions = []
        
        # Check for essential sections
        if analysis["missing_sections"]:
            suggestions.append({
                "category": "Structure",
                "title": "Add Missing Sections",
                "description": f"Your resume is missing these key sections: {', '.join(analysis['missing_sections'])}",
                "impact": "High"
            })
        
        # Action verb usage
        if analysis["action_verb_count"] < 5:
            suggestions.append({
                "category": "Language",
                "title": "Use More Action Verbs",
                "description": "Strengthen your experience descriptions with powerful action verbs like 'achieved', 'developed', or 'implemented'",
                "impact": "High"
            })
        
        # Weak phrases
        if analysis["weak_phrase_count"] > 2:
            suggestions.append({
                "category": "Language",
                "title": "Remove Weak Phrases",
                "description": f"Replace weak phrases like 'responsible for' or 'helped with' with stronger action verbs",
                "impact": "Medium"
            })
        
        # Quantifiable achievements
        if analysis["quantifiable_achievements"] < 3:
            suggestions.append({
                "category": "Content",
                "title": "Add Quantifiable Achievements",
                "description": "Include specific numbers, percentages, or metrics to demonstrate your impact",
                "impact": "High"
            })
        
        # Contact information
        if not analysis["has_complete_contact_info"]:
            suggestions.append({
                "category": "Contact",
                "title": "Complete Contact Information",
                "description": "Ensure you have included your email and phone number",
                "impact": "Critical"
            })
        
        # LinkedIn profile
        if not analysis["has_linkedin"]:
            suggestions.append({
                "category": "Contact",
                "title": "Add LinkedIn Profile",
                "description": "Include your LinkedIn profile URL to enhance your professional presence",
                "impact": "Medium"
            })
        
        # Bullet points
        if analysis["bullet_point_count"] < 10:
            suggestions.append({
                "category": "Formatting",
                "title": "Use More Bullet Points",
                "description": "Break down experience into concise bullet points for better readability",
                "impact": "Medium"
            })
        
        # Resume length
        if analysis["word_count"] < 300:
            suggestions.append({
                "category": "Content",
                "title": "Expand Your Resume",
                "description": "Your resume seems brief. Consider adding more details about your experience and achievements",
                "impact": "Medium"
            })
        elif analysis["word_count"] > 1000:
            suggestions.append({
                "category": "Content",
                "title": "Make Your Resume More Concise",
                "description": "Your resume is quite lengthy. Focus on the most relevant information",
                "impact": "Medium"
            })
        
        # Career-specific suggestions
        career_suggestions = []
        career_keyword_match = None
        
        if target_career:
            career_keyword_match = get_career_keyword_matches(resume_text, target_career)
            
            if career_keyword_match["missing_skills"]:
                career_suggestions.append({
                    "category": "Career Alignment",
                    "title": f"Add {target_career} Keywords",
                    "description": f"Include these relevant skills for {target_career}: {', '.join(career_keyword_match['missing_skills'][:5])}",
                    "impact": "High"
                })
            
            career_details = get_career_details(target_career)
            if career_details is not None and career_details.get("required_education"):
                if career_details["required_education"].lower() not in resume_text:
                    career_suggestions.append({
                        "category": "Education",
                        "title": "Highlight Relevant Education",
                        "description": f"Emphasize education that aligns with the {career_details.get('required_education')} requirement for this career",
                        "impact": "High"
                    })
        
        # Summary of findings
        summary = {
            "overall_score": calculate_resume_score(analysis, career_keyword_match),
            "general_suggestions": suggestions,
            "career_specific_suggestions": career_suggestions,
            "keyword_match_percentage": career_keyword_match["match_percentage"] if career_keyword_match else None,
            "target_career": target_career
        }
        
        return summary
        
    except Exception as e:
        logger.error(f"Error generating resume suggestions: {e}")
        return {"error": str(e)}

def calculate_resume_score(analysis, career_match=None):
    """
    Calculate an overall score for the resume based on analysis
    
    Args:
        analysis: Result of resume analysis
        career_match: Result of career keyword matching
        
    Returns:
        Score from 0-100
    """
    score = 50  # Starting score
    
    # Structure (20 points)
    if not analysis["missing_sections"]:
        score += 20
    else:
        score += max(0, 20 - (len(analysis["missing_sections"]) * 5))
    
    # Language (15 points)
    action_verb_points = min(10, analysis["action_verb_count"])
    weak_phrase_penalty = min(5, analysis["weak_phrase_count"])
    score += action_verb_points - weak_phrase_penalty
    
    # Content quality (15 points)
    score += min(15, analysis["quantifiable_achievements"] * 5)
    
    # Contact information (10 points)
    if analysis["has_complete_contact_info"]:
        score += 7
    if analysis["has_linkedin"]:
        score += 3
    
    # Career alignment (40 points)
    if career_match:
        score += (career_match["match_percentage"] * 0.4)
    
    return min(100, max(0, round(score)))