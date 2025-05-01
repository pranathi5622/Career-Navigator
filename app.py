import os
import logging
logging.basicConfig(level=logging.DEBUG)
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create SQLAlchemy Base
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy
db = SQLAlchemy(model_class=Base)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///career_guidance.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the app with the extension
db.init_app(app)

with app.app_context():
    # Import models
    import models  # noqa: F401
    
    # Create tables
    db.create_all()

# Import routes and forms
from forms import CareerForm, ComparisonForm, QuestionnaireForm
from recommendation_engine import get_career_recommendations, get_career_roadmap, compare_careers
from career_data import get_career_details, get_all_careers

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Routes for career roadmap generator
@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    form = CareerForm()
    
    if request.method == 'POST':
        # Get form data directly from request
        career = request.form.get('career')
        experience_level = request.form.get('experience_level')
        education = request.form.get('education')
        skills = request.form.getlist('skills')  # Get list of all checked skills
        
        # Set default years of experience based on experience level
        experience_map = {
            'entry': 1,
            'mid': 4,
            'senior': 8,
            'expert': 12
        }
        years_experience = experience_map.get(experience_level, 0)
        
        # Basic validation
        if career and experience_level and education and skills:
            # Store in session for use in results page
            session['selected_career'] = career
            session['experience_level'] = experience_level
            session['resume_education'] = education  # Using the same session key as before
            session['resume_skills'] = skills  # Using the same session key as before
            session['resume_experience'] = years_experience  # Using the same session key as before
            
            # Go directly to results page
            return redirect(url_for('roadmap_result'))
        else:
            flash('Please fill out all required fields', 'danger')
    
    return render_template('roadmap.html', form=form, careers=get_all_careers())

# Routes for career comparison tool
@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    form = ComparisonForm()
    
    if form.validate_on_submit():
        career1 = form.career1.data
        career2 = form.career2.data
        session['career1'] = career1
        session['career2'] = career2
        
        # Set default empty values for skills and education
        session['resume_skills'] = []
        session['resume_education'] = ''
        session['resume_experience'] = 0
        
        return redirect(url_for('comparison_result'))
    
    return render_template('comparison.html', form=form, careers=get_all_careers())

# Routes for career recommendation system
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    # Go directly to questionnaire
    return redirect(url_for('questionnaire'))

# Route for questionnaire
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    form = QuestionnaireForm()
    
    if form.validate_on_submit():
        session['interests'] = form.interests.data
        session['skills'] = form.skills.data
        session['values'] = form.values.data
        session['personality'] = form.personality.data
        session['education'] = form.education.data
        session['work_environment'] = form.work_environment.data
        
        return redirect(url_for('recommendation_result'))
    
    return render_template('questionnaire.html', form=form)





# Routes for results
@app.route('/roadmap_result')
def roadmap_result():
    # Get data from session
    career = session.get('selected_career')
    experience_level = session.get('experience_level')
    skills = session.get('resume_skills', [])
    education = session.get('resume_education', '')
    experience = session.get('resume_experience', 0)
    
    # Check if we have the necessary data
    if not career or not experience_level:
        flash('Missing required career information. Please fill out the form again.', 'danger')
        return redirect(url_for('roadmap'))
    
    try:
        # Get career roadmap
        career_details = get_career_details(career)
        roadmap = get_career_roadmap(career, experience_level, skills, education, experience)
        
        # For debugging
        app.logger.debug(f"Career: {career}")
        app.logger.debug(f"Experience Level: {experience_level}")
        app.logger.debug(f"Skills: {skills}")
        app.logger.debug(f"Education: {education}")
        app.logger.debug(f"Experience: {experience}")
        
        return render_template('result.html', 
                              result_type='roadmap',
                              career=career,
                              career_details=career_details,
                              roadmap=roadmap)
    except Exception as e:
        app.logger.error(f"Error generating roadmap: {str(e)}")
        flash(f'Error generating roadmap: {str(e)}', 'danger')
        return redirect(url_for('roadmap'))

@app.route('/comparison_result')
def comparison_result():
    # Get data from session
    career1 = session.get('career1')
    career2 = session.get('career2')
    skills = session.get('resume_skills', [])
    education = session.get('resume_education', [])
    experience = session.get('resume_experience', 0)
    
    # Get career comparisons
    career1_details = get_career_details(career1)
    career2_details = get_career_details(career2)
    comparison = compare_careers(career1, career2, skills, education, experience)
    
    return render_template('result.html',
                          result_type='comparison',
                          career1=career1,
                          career2=career2,
                          career1_details=career1_details,
                          career2_details=career2_details,
                          comparison=comparison)

@app.route('/recommendation_result')
def recommendation_result():
    # Get questionnaire data from session
    interests = session.get('interests', [])
    skills = session.get('skills', [])
    values = session.get('values', [])
    personality = session.get('personality', '')
    education = session.get('education', '')
    work_environment = session.get('work_environment', [])
    
    # Get resume data from session if it exists
    resume_skills = session.get('resume_skills', [])
    resume_education = session.get('resume_education', [])
    
    # Combine resume and questionnaire data
    if resume_skills:
        skills = list(set(skills + resume_skills))
    
    # Get recommendations
    recommendations = get_career_recommendations(
        interests, skills, values, personality, 
        education or resume_education, work_environment
    )
    
    return render_template('result.html',
                          result_type='recommendation',
                          recommendations=recommendations)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
