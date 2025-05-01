import os
import logging
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.utils import secure_filename
import tempfile
import os.path
from recommendation_engine import get_typical_roles, get_skills_to_develop, get_education_requirements

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
app.config["UPLOAD_FOLDER"] = tempfile.gettempdir()
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max upload

# Initialize the app with the extension
db.init_app(app)

with app.app_context():
    # Import models
    import models  # noqa: F401
    
    # Create tables
    db.create_all()

# Import routes and forms
from forms import CareerForm, ComparisonForm, QuestionnaireForm, ResumeUploadForm, MoodEntryForm
from resume_parser import process_resume_file
from recommendation_engine import get_career_recommendations, get_career_roadmap, compare_careers
from career_data import get_career_details, get_all_careers
from resume_optimizer import generate_optimization_suggestions
from models import MoodEntry

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Routes for career roadmap generator
@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    form = CareerForm()
    
    if form.validate_on_submit():
        career = form.career.data
        experience_level = form.experience_level.data
        session['selected_career'] = career
        session['experience_level'] = experience_level
        
        return redirect(url_for('upload_resume', path_type='roadmap'))
    
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
        
        return redirect(url_for('upload_resume', path_type='comparison'))
    
    return render_template('comparison.html', form=form, careers=get_all_careers())

# Routes for career recommendation system
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    return render_template('recommendation.html')

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

# Route for resume upload
@app.route('/upload_resume/<path_type>', methods=['GET', 'POST'])
def upload_resume(path_type):
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'resume' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        file = request.files['resume']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process resume
            skills, education, experience = process_resume_file(filepath)
            
            # Store resume data in session
            session['resume_skills'] = skills
            session['resume_education'] = education
            session['resume_experience'] = experience
            session['resume_filepath'] = filepath  # Store filepath for optimization feature
            
            # Redirect based on path type
            if path_type == 'roadmap':
                return redirect(url_for('roadmap_result'))
            elif path_type == 'comparison':
                return redirect(url_for('comparison_result'))
            elif path_type == 'recommendation':
                return redirect(url_for('questionnaire'))
            elif path_type == 'optimize':
                return redirect(url_for('optimize_resume'))
    
    return render_template('upload_resume.html', path_type=path_type)

@app.route('/optimize_resume', methods=['GET', 'POST'])
def optimize_resume():
    """
    Route for resume optimization feature
    """
    all_careers = get_all_careers()
    form = CareerForm()
    
    if form.validate_on_submit():
        target_career = form.career.data
        
        # Get resume filepath from session
        resume_filepath = session.get('resume_filepath')
        
        if not resume_filepath or not os.path.exists(resume_filepath):
            flash('Resume file not found. Please upload your resume again.', 'danger')
            return redirect(url_for('upload_resume', path_type='optimize'))
        
        # Generate optimization suggestions
        optimization_results = generate_optimization_suggestions(resume_filepath, target_career)
        
        # Store results in session
        session['optimization_results'] = optimization_results
        
        # Clean up file after generating suggestions
        if os.path.exists(resume_filepath):
            os.remove(resume_filepath)
            session.pop('resume_filepath', None)
            
        return redirect(url_for('optimization_results'))
    
    return render_template('optimize_resume.html', form=form, careers=all_careers)

@app.route('/optimization_results')
def optimization_results():
    """
    Route to display resume optimization results
    """
    # Get optimization results from session
    results = session.get('optimization_results')
    
    if not results:
        flash('No optimization results found. Please upload your resume and select a target career.', 'warning')
        return redirect(url_for('upload_resume', path_type='optimize'))
    
    return render_template('optimization_results.html', results=results)

# Routes for results
@app.route('/roadmap_result')
def roadmap_result():
    # Get data from session
    career = session.get('selected_career')
    experience_level = session.get('experience_level')
    skills = session.get('resume_skills', [])
    education = session.get('resume_education', [])
    experience = session.get('resume_experience', 0)
    
    # Get career roadmap
    career_details = get_career_details(career)
    roadmap = get_career_roadmap(career, experience_level, skills, education, experience)
    
    return render_template('result.html', 
                          result_type='roadmap',
                          career=career,
                          career_details=career_details,
                          roadmap=roadmap)

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

# Mood tracker routes
@app.route('/mood_tracker', methods=['GET'])
def mood_tracker():
    """
    Display mood tracking dashboard
    """
    # Placeholder for current user - in a real app, you'd use the logged-in user
    # For now, we'll just use a placeholder user_id
    user_id = 1
    
    form = MoodEntryForm()
    
    # Get the user's mood entries, ordered by date descending
    mood_entries = MoodEntry.query.filter_by(user_id=user_id).order_by(MoodEntry.entry_date.desc()).limit(30).all()
    
    # Prepare data for charts
    dates = []
    moods = []
    career_satisfaction = []
    work_life_balance = []
    stress_levels = []
    
    for entry in mood_entries:
        dates.append(entry.entry_date.strftime("%Y-%m-%d"))
        moods.append(entry.mood)
        career_satisfaction.append(entry.career_satisfaction)
        work_life_balance.append(entry.work_life_balance)
        stress_levels.append(entry.stress_level)
    
    # Reverse lists to display oldest to newest
    dates.reverse()
    moods.reverse()
    career_satisfaction.reverse()
    work_life_balance.reverse()
    stress_levels.reverse()
    
    # Convert Python lists to JSON for JavaScript
    chart_data = {
        'dates': dates,
        'moods': moods,
        'career_satisfaction': career_satisfaction,
        'work_life_balance': work_life_balance,
        'stress_levels': stress_levels
    }
    
    return render_template('mood_tracker.html', form=form, mood_entries=mood_entries, chart_data=chart_data)

@app.route('/mood_entry', methods=['POST'])
def mood_entry():
    """
    Add a new mood entry
    """
    form = MoodEntryForm()
    
    if form.validate_on_submit():
        # Placeholder for current user - in a real app, you'd use the logged-in user
        user_id = 1
        
        # Create new mood entry
        new_entry = MoodEntry(
            user_id=user_id,
            mood=form.mood.data,
            career_satisfaction=form.career_satisfaction.data,
            work_life_balance=form.work_life_balance.data,
            stress_level=form.stress_level.data,
            notes=form.notes.data
        )
        
        db.session.add(new_entry)
        db.session.commit()
        
        flash('Your mood has been recorded!', 'success')
        return redirect(url_for('mood_tracker'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{getattr(form, field).label.text}: {error}', 'danger')
    
    return redirect(url_for('mood_tracker'))

@app.route('/delete_mood_entry/<int:entry_id>', methods=['POST'])
def delete_mood_entry(entry_id):
    """
    Delete a mood entry
    """
    # Placeholder for current user - in a real app, you'd use the logged-in user
    user_id = 1
    
    entry = MoodEntry.query.filter_by(id=entry_id, user_id=user_id).first()
    
    if entry:
        db.session.delete(entry)
        db.session.commit()
        flash('Mood entry deleted successfully!', 'success')
    else:
        flash('Mood entry not found.', 'danger')
    
    return redirect(url_for('mood_tracker'))

# Career Path Explorer Routes
@app.route('/career_path_explorer', methods=['GET', 'POST'])
def career_path_explorer():
    """
    Interactive career path explorer with animated milestones
    """
    # Get all available careers for the dropdown
    careers = get_all_careers()
    selected_career = None
    career_path = None
    
    if request.method == 'POST':
        selected_career = request.form.get('career')
        if selected_career:
            # Get career details
            career_details = get_career_details(selected_career)
            
            # Generate career path with milestones
            career_path = {
                'career': selected_career,
                'description': career_details.get('description', ''),
                'milestones': generate_career_milestones(selected_career)
            }
            
    return render_template('career_path_explorer.html', 
                          careers=careers,
                          selected_career=selected_career,
                          career_path=career_path)

def generate_career_milestones(career):
    """
    Generate interactive milestones for a career path
    """
    career_details = get_career_details(career)
    
    # Create milestone stages (entry, mid, senior, expert)
    milestones = [
        {
            'level': 'entry',
            'title': 'Entry Level',
            'description': f'Beginning your journey as a {career}',
            'years': '0-2 years',
            'roles': get_typical_roles(career, 'entry'),
            'skills': career_details.get('required_skills', [])[:3],  # Top 3 skills for entry level
            'education': get_education_requirements(career, 'entry'),
            'salary': career_details.get('salary_range', '').split('-')[0].strip() if '-' in career_details.get('salary_range', '') else 'Varies',
            'key_challenges': [
                f'Learning the fundamentals of {career}',
                'Building a professional network',
                'Gaining practical experience'
            ],
            'success_metrics': [
                'Completing basic certifications',
                'Building a portfolio of work',
                'Receiving positive performance reviews'
            ]
        },
        {
            'level': 'mid',
            'title': 'Mid-Level Professional',
            'description': f'Developing expertise as a {career}',
            'years': '3-5 years',
            'roles': get_typical_roles(career, 'mid'),
            'skills': get_skills_to_develop(career, 'mid', []),
            'education': get_education_requirements(career, 'mid'),
            'salary': 'Middle of range',
            'key_challenges': [
                'Taking on more complex projects',
                'Developing specialized expertise',
                'Beginning to mentor others'
            ],
            'success_metrics': [
                'Leading small to medium projects',
                'Becoming a subject matter expert in specific areas',
                'Contributing to team growth'
            ]
        },
        {
            'level': 'senior',
            'title': 'Senior Professional',
            'description': f'Leading and innovating as a {career}',
            'years': '6-10 years',
            'roles': get_typical_roles(career, 'senior'),
            'skills': get_skills_to_develop(career, 'senior', []),
            'education': get_education_requirements(career, 'senior'),
            'salary': career_details.get('salary_range', '').split('-')[1].strip() if '-' in career_details.get('salary_range', '') else 'Varies',
            'key_challenges': [
                'Leading major initiatives',
                'Developing strategic vision',
                'Managing team dynamics'
            ],
            'success_metrics': [
                'Driving innovation in your field',
                'Mentoring junior team members',
                'Recognized industry expertise'
            ]
        },
        {
            'level': 'expert',
            'title': 'Expert / Leadership',
            'description': f'Shaping the future of {career}',
            'years': '10+ years',
            'roles': get_typical_roles(career, 'expert'),
            'skills': get_skills_to_develop(career, 'expert', []),
            'education': get_education_requirements(career, 'expert'),
            'salary': 'Top of range and beyond',
            'key_challenges': [
                'Setting vision and direction',
                'Driving organizational change',
                'Industry thought leadership'
            ],
            'success_metrics': [
                'Leading organizational strategy',
                'Contributing to industry standards',
                'Building and developing high-performing teams'
            ]
        }
    ]
    
    return milestones

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
