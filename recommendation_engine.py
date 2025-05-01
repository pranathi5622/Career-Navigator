import logging
from career_data import get_all_careers, get_career_details

# Set up logging
logger = logging.getLogger(__name__)

def get_career_recommendations(interests, skills, values, personality, education, work_environment, limit=5):
    """
    Generate career recommendations based on user preferences and skills.
    
    Args:
        interests: List of user's interest areas
        skills: List of user's skills
        values: List of user's career values
        personality: User's work personality type
        education: User's education level
        work_environment: User's preferred work environments
        limit: Maximum number of recommendations to return
    
    Returns:
        List of recommended careers with scores and reasoning
    """
    all_careers = get_all_careers()
    recommendations = []
    
    for career in all_careers:
        career_details = get_career_details(career)
        score = 0
        match_reasons = []
        
        # Score based on skills match
        career_skills = [s.lower() for s in career_details.get("required_skills", [])]
        skill_matches = [s for s in skills if any(s in cs.lower() for cs in career_skills)]
        skill_score = len(skill_matches) * 10  # 10 points per matching skill
        if skill_score > 0:
            score += skill_score
            match_reasons.append(f"Matched {len(skill_matches)} skills: {', '.join(skill_matches[:3])}")
        
        # Score based on interests
        if interests:
            for interest in interests:
                if interest.lower() in career_details.get("description", "").lower():
                    score += 5
                    match_reasons.append(f"Interest match: {interest}")
                    break
        
        # Score based on education
        edu_level_scores = {
            "highschool": 1,
            "associate": 2,
            "bachelor": 3, 
            "master": 4,
            "phd": 5,
            "trade": 2,
            "selftaught": 1
        }
        
        user_edu_level = edu_level_scores.get(education, 0) if isinstance(education, str) else 0
        
        required_edu = career_details.get("required_education", "").lower()
        if "bachelor" in required_edu and user_edu_level >= 3:
            score += 15
            match_reasons.append("Education match: Bachelor's degree or higher")
        elif "associate" in required_edu and user_edu_level >= 2:
            score += 15
            match_reasons.append("Education match: Associate degree or higher")
        elif "master" in required_edu and user_edu_level >= 4:
            score += 15
            match_reasons.append("Education match: Master's degree or higher")
        elif "phd" in required_edu and user_edu_level >= 5:
            score += 15
            match_reasons.append("Education match: PhD")
        
        # Score based on work environment
        career_environment = career_details.get("work_environment", "").lower()
        env_matches = [env for env in work_environment if env.lower() in career_environment]
        if env_matches:
            score += len(env_matches) * 5
            match_reasons.append(f"Work environment match: {', '.join(env_matches[:2])}")
        
        # Score based on values
        for value in values:
            # Check for work-life balance
            if value == "worklife" and "flexible" in career_environment:
                score += 5
                match_reasons.append("Value match: Work-life balance")
            
            # Check for compensation
            if value == "compensation" and any(high_pay in career_details.get("salary_range", "") 
                                             for high_pay in ["$100,000", "$150,000", "$200,000"]):
                score += 5
                match_reasons.append("Value match: High compensation potential")
            
            # Check for growth
            if value == "growth" and "growth" in career_details.get("job_outlook", "").lower():
                score += 5
                match_reasons.append("Value match: Career growth opportunities")
        
        # Score based on personality
        if personality == "analytical" and any(analytical in career_details.get("description", "").lower() 
                                            for analytical in ["analytical", "analysis", "data", "research"]):
            score += 10
            match_reasons.append("Personality match: Analytical role")
        
        elif personality == "creative" and any(creative in career_details.get("description", "").lower() 
                                            for creative in ["creative", "design", "innovative"]):
            score += 10
            match_reasons.append("Personality match: Creative role")
        
        elif personality == "leader" and any(leader in career_details.get("description", "").lower() 
                                          for leader in ["lead", "manage", "direct", "supervise"]):
            score += 10
            match_reasons.append("Personality match: Leadership role")
        
        elif personality == "social" and any(social in career_details.get("description", "").lower() 
                                          for social in ["social", "people", "team", "collaborate"]):
            score += 10
            match_reasons.append("Personality match: Social/collaborative role")
        
        recommendations.append({
            "career": career,
            "score": score,
            "match_reasons": match_reasons[:3],  # Top 3 reasons only
            "details": career_details
        })
    
    # Sort by score and limit results
    sorted_recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)
    return sorted_recommendations[:limit]

def get_career_roadmap(career, experience_level, skills, education, experience_years):
    """
    Generate a career roadmap based on a selected career path.
    
    Args:
        career: Selected career path
        experience_level: User's current experience level
        skills: User's current skills
        education: User's education background
        experience_years: User's years of experience
    
    Returns:
        Dictionary with roadmap information
    """
    career_details = get_career_details(career)
    
    # Define the roadmap stages
    stages = [
        {
            "title": "Entry Level",
            "description": f"Beginning roles in {career}",
            "typical_roles": get_typical_roles(career, "entry"),
            "skills_to_develop": get_skills_to_develop(career, "entry", skills),
            "education_requirements": get_education_requirements(career, "entry"),
            "time_estimate": "0-2 years"
        },
        {
            "title": "Mid-Level",
            "description": f"Intermediate roles in {career} with some experience",
            "typical_roles": get_typical_roles(career, "mid"),
            "skills_to_develop": get_skills_to_develop(career, "mid", skills),
            "education_requirements": get_education_requirements(career, "mid"),
            "time_estimate": "3-5 years"
        },
        {
            "title": "Senior Level",
            "description": f"Advanced roles in {career} with substantial experience",
            "typical_roles": get_typical_roles(career, "senior"),
            "skills_to_develop": get_skills_to_develop(career, "senior", skills),
            "education_requirements": get_education_requirements(career, "senior"),
            "time_estimate": "6-10 years"
        },
        {
            "title": "Expert / Leadership",
            "description": f"Top-level positions in {career} field",
            "typical_roles": get_typical_roles(career, "expert"),
            "skills_to_develop": get_skills_to_develop(career, "expert", skills),
            "education_requirements": get_education_requirements(career, "expert"),
            "time_estimate": "10+ years"
        }
    ]
    
    # Determine user's current stage based on experience level
    current_stage_index = {
        "entry": 0,
        "mid": 1,
        "senior": 2,
        "expert": 3
    }.get(experience_level, 0)
    
    # Identify skill gaps at current and next levels
    current_required_skills = set(get_skills_to_develop(career, experience_level, []))
    user_skills = set(skills)
    skill_gaps = list(current_required_skills - user_skills)
    
    # Prepare resources
    resources = career_details.get("resources", [])
    
    return {
        "career": career,
        "overview": career_details.get("description", ""),
        "current_stage": current_stage_index,
        "stages": stages,
        "skill_gaps": skill_gaps,
        "recommended_resources": resources,
        "salary_progression": {
            "entry": "Entry Level: " + (career_details.get("salary_range", "").split("-")[0] 
                                      if "-" in career_details.get("salary_range", "") else "Varies"),
            "mid": "Mid-Level: Middle of range",
            "senior": "Senior Level: " + (career_details.get("salary_range", "").split("-")[1] 
                                        if "-" in career_details.get("salary_range", "") else "Varies"),
            "expert": "Expert Level: Top of range and beyond"
        }
    }

def get_typical_roles(career, level):
    """Get typical roles for a career at a specific level"""
    # Mapping of careers to roles at different levels
    role_mappings = {
        "Software Developer": {
            "entry": ["Junior Developer", "Software Engineer I", "Associate Developer"],
            "mid": ["Software Engineer II", "Full Stack Developer", "Application Developer"],
            "senior": ["Senior Software Engineer", "Software Architect", "Technical Lead"],
            "expert": ["Principal Engineer", "Software Engineering Manager", "CTO", "VP of Engineering"]
        },
        "Data Scientist": {
            "entry": ["Junior Data Scientist", "Data Analyst", "Research Assistant"],
            "mid": ["Data Scientist", "Machine Learning Engineer", "Analytics Specialist"],
            "senior": ["Senior Data Scientist", "Lead Data Scientist", "Data Science Manager"],
            "expert": ["Principal Data Scientist", "Director of Data Science", "Chief Data Officer"]
        },
        "UX/UI Designer": {
            "entry": ["Junior Designer", "UI Designer", "Visual Designer"],
            "mid": ["UX/UI Designer", "Interaction Designer", "Experience Designer"],
            "senior": ["Senior UX Designer", "Lead Designer", "UX Manager"],
            "expert": ["Design Director", "VP of Design", "Chief Design Officer"]
        },
        "Product Manager": {
            "entry": ["Associate Product Manager", "Product Analyst", "Product Owner"],
            "mid": ["Product Manager", "Senior Product Owner", "Technical Product Manager"],
            "senior": ["Senior Product Manager", "Group Product Manager", "Product Lead"],
            "expert": ["Director of Product", "VP of Product", "Chief Product Officer"]
        }
    }
    
    # Return specific roles if available, otherwise return generic roles
    if career in role_mappings and level in role_mappings[career]:
        return role_mappings[career][level]
    else:
        # Generic roles based on level
        generic_roles = {
            "entry": ["Entry Level " + career, "Junior " + career, "Associate " + career],
            "mid": [career, "Experienced " + career, career + " Specialist"],
            "senior": ["Senior " + career, "Lead " + career, career + " Manager"],
            "expert": ["Principal " + career, "Director of " + career, "Chief " + career + " Officer"]
        }
        return generic_roles.get(level, ["Role information not available"])

def get_skills_to_develop(career, level, current_skills):
    """Get skills to develop for a career at a specific level"""
    # Convert current skills to lowercase for case-insensitive comparison
    current_skills_lower = [s.lower() for s in current_skills]
    
    # Get career details
    career_details = get_career_details(career)
    base_skills = career_details.get("required_skills", [])
    
    # Define additional skills by level
    additional_skills = {
        "Software Developer": {
            "entry": ["Programming Fundamentals", "Data Structures", "Version Control"],
            "mid": ["Design Patterns", "System Architecture", "CI/CD", "Code Optimization"],
            "senior": ["Scalability", "Microservices", "Technical Leadership", "Mentoring"],
            "expert": ["Enterprise Architecture", "Technology Strategy", "Team Leadership"]
        },
        "Data Scientist": {
            "entry": ["Python Programming", "Statistics", "Data Visualization"],
            "mid": ["Machine Learning", "Data Pipelines", "Feature Engineering"],
            "senior": ["Advanced ML Algorithms", "MLOps", "Research Methods"],
            "expert": ["AI Strategy", "Research Leadership", "Cross-functional Leadership"]
        },
        "UX/UI Designer": {
            "entry": ["Design Software", "Visual Design", "Wireframing"],
            "mid": ["User Research", "Prototyping", "Information Architecture"],
            "senior": ["Design Systems", "Team Collaboration", "Project Management"],
            "expert": ["Design Strategy", "Design Leadership", "Business Acumen"]
        }
    }
    
    # Get level-specific skills if available
    level_skills = []
    if career in additional_skills and level in additional_skills[career]:
        level_skills = additional_skills[career][level]
    
    # Combine base skills and level-specific skills
    all_skills = base_skills + level_skills
    
    # Return skills that the user doesn't already have
    return [skill for skill in all_skills if not any(skill.lower() in cs for cs in current_skills_lower)]

def get_education_requirements(career, level):
    """Get education requirements for a career at a specific level"""
    # Get career details
    career_details = get_career_details(career)
    base_education = career_details.get("required_education", "Bachelor's degree or equivalent experience")
    
    # Define additional education by level
    additional_education = {
        "Software Developer": {
            "entry": "Bachelor's in Computer Science or equivalent bootcamp/self-learning",
            "mid": "Bachelor's in Computer Science plus specialized certifications",
            "senior": "Bachelor's/Master's plus extensive experience",
            "expert": "Master's/PhD may be preferred, extensive experience required"
        },
        "Data Scientist": {
            "entry": "Bachelor's in Statistics, Computer Science, or related field",
            "mid": "Master's degree often preferred plus specialized knowledge",
            "senior": "Master's/PhD plus domain expertise",
            "expert": "PhD common at this level plus research contributions"
        },
        "UX/UI Designer": {
            "entry": "Degree in Design, HCI, or strong portfolio",
            "mid": "Degree plus proven work experience and diverse portfolio",
            "senior": "Portfolio more important than formal education at this stage",
            "expert": "Track record of successful projects, formal education secondary"
        }
    }
    
    # Return level-specific education if available, otherwise return base education
    if career in additional_education and level in additional_education[career]:
        return additional_education[career][level]
    
    # Generic education requirements by level
    generic_education = {
        "entry": base_education,
        "mid": base_education + " with 3-5 years of experience",
        "senior": base_education + " with 6-10 years of experience, advanced certifications may be beneficial",
        "expert": "Advanced degrees often preferred, 10+ years of experience, specialized expertise and leadership experience"
    }
    
    return generic_education.get(level, base_education)

def compare_careers(career1, career2, skills, education, experience_years):
    """
    Compare two careers based on user's background.
    
    Args:
        career1, career2: The careers to compare
        skills: User's current skills
        education: User's education background
        experience_years: User's years of experience
    
    Returns:
        Dictionary with comparison information
    """
    career1_details = get_career_details(career1)
    career2_details = get_career_details(career2)
    
    # Calculate skill match percentages
    career1_skills = career1_details.get("required_skills", [])
    career2_skills = career2_details.get("required_skills", [])
    
    skills_lower = [s.lower() for s in skills]
    
    career1_matches = sum(1 for skill in career1_skills if any(s in skill.lower() for s in skills_lower))
    career2_matches = sum(1 for skill in career2_skills if any(s in skill.lower() for s in skills_lower))
    
    career1_match_pct = (career1_matches / len(career1_skills)) * 100 if career1_skills else 0
    career2_match_pct = (career2_matches / len(career2_skills)) * 100 if career2_skills else 0
    
    # Determine education compatibility
    education_levels = ["highschool", "associate", "bachelor", "master", "phd"]
    
    def get_required_edu_level(career_details):
        required_edu = career_details.get("required_education", "").lower()
        if "bachelor" in required_edu:
            return 2  # Index of bachelor in education_levels
        elif "associate" in required_edu:
            return 1
        elif "master" in required_edu:
            return 3
        elif "phd" in required_edu or "doctorate" in required_edu:
            return 4
        return 0  # Default to high school
    
    career1_edu_level = get_required_edu_level(career1_details)
    career2_edu_level = get_required_edu_level(career2_details)
    
    # Create more detailed comparison
    comparison = {
        "overview": {
            "career1": {
                "name": career1,
                "description": career1_details.get("description", ""),
                "skill_match": round(career1_match_pct, 1),
                "matching_skills": [skill for skill in career1_skills if any(s in skill.lower() for s in skills_lower)],
                "missing_skills": [skill for skill in career1_skills if not any(s in skill.lower() for s in skills_lower)]
            },
            "career2": {
                "name": career2,
                "description": career2_details.get("description", ""),
                "skill_match": round(career2_match_pct, 1),
                "matching_skills": [skill for skill in career2_skills if any(s in skill.lower() for s in skills_lower)],
                "missing_skills": [skill for skill in career2_skills if not any(s in skill.lower() for s in skills_lower)]
            }
        },
        "education": {
            "career1": {
                "required": career1_details.get("required_education", ""),
                "level_index": career1_edu_level
            },
            "career2": {
                "required": career2_details.get("required_education", ""),
                "level_index": career2_edu_level
            }
        },
        "compensation": {
            "career1": career1_details.get("salary_range", ""),
            "career2": career2_details.get("salary_range", "")
        },
        "outlook": {
            "career1": career1_details.get("job_outlook", ""),
            "career2": career2_details.get("job_outlook", "")
        },
        "work_environment": {
            "career1": career1_details.get("work_environment", ""),
            "career2": career2_details.get("work_environment", "")
        },
        "transition_difficulty": calculate_transition_difficulty(career1, career2, skills, experience_years),
        "related_careers": {
            "career1": career1_details.get("related_careers", []),
            "career2": career2_details.get("related_careers", [])
        }
    }
    
    return comparison

def calculate_transition_difficulty(career1, career2, skills, experience_years):
    """Calculate the difficulty of transitioning between two careers"""
    career1_details = get_career_details(career1)
    career2_details = get_career_details(career2)
    
    # Compare required skills
    career1_skills = set([s.lower() for s in career1_details.get("required_skills", [])])
    career2_skills = set([s.lower() for s in career2_details.get("required_skills", [])])
    
    # Calculate overlap
    skill_overlap = len(career1_skills.intersection(career2_skills))
    skill_total = len(career2_skills)
    
    # Calculate skill match percentage
    skill_match_pct = (skill_overlap / skill_total) * 100 if skill_total > 0 else 0
    
    # Determine transition difficulty based on skill match and experience
    if skill_match_pct >= 70:
        difficulty = "Easy"
        description = "The careers have significant skill overlap, making this a natural transition."
    elif skill_match_pct >= 40:
        difficulty = "Moderate"
        description = "You'll need to develop some new skills, but there's meaningful overlap."
    else:
        difficulty = "Challenging"
        description = "These careers require substantially different skillsets, requiring significant retraining."
    
    # Adjust for experience
    if experience_years >= 10 and difficulty != "Easy":
        difficulty_modifier = "Your extensive experience may help offset some challenges."
    elif experience_years <= 2 and difficulty != "Easy":
        difficulty_modifier = "Your limited experience may make this transition more challenging."
    else:
        difficulty_modifier = ""
    
    # Suggest education or certification needs
    education_needs = []
    if career2_details.get("required_education", "").lower() not in career1_details.get("required_education", "").lower():
        education_needs.append(career2_details.get("required_education", ""))
    
    return {
        "level": difficulty,
        "description": description,
        "experience_factor": difficulty_modifier,
        "skill_gap": list(career2_skills - career1_skills),
        "additional_education": education_needs,
        "skill_overlap_percentage": round(skill_match_pct, 1)
    }
