from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
import uuid
import json
import logging

from app import app, db
from forms import (
    RegistrationForm, LoginForm, ResumeUploadForm, 
    RoadmapForm, ComparisonForm, QuestionnaireForm, 
    InterestForm
)
from resume_parser import ResumeParser
from career_data import get_career_info, compare_careers, get_recommendations
from config import QUESTIONNAIRE, SKILLS_QUESTIONS, INTERESTS_QUESTIONS, VALUES_QUESTIONS

# Configure logging
logger = logging.getLogger(__name__)

# Initialize resume parser
resume_parser = ResumeParser()

# Utility functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}

@app.route('/')
def index():
    """Home page with three different career guidance paths."""
    return render_template('index.html')

@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    """Career roadmap generator for users who know their career."""
    form = RoadmapForm()
    
    if form.validate_on_submit():
        career_title = form.career_title.data
        experience_level = form.experience_level.data
        current_role = form.current_role.data
        desired_skills = form.desired_skills.data
        
        # Store form data in session
        session['roadmap_data'] = {
            'career_title': career_title,
            'experience_level': experience_level,
            'current_role': current_role,
            'desired_skills': desired_skills
        }
        
        # Get career information
        career_info = get_career_info(career_title)
        
        # Filter milestones based on experience level
        if experience_level == 'beginner':
            relevant_milestones = [m for m in career_info['milestones'] if m['level'] in ['Beginner', 'Intermediate']]
        elif experience_level == 'intermediate':
            relevant_milestones = [m for m in career_info['milestones'] if m['level'] in ['Intermediate', 'Advanced']]
        else:  # advanced
            relevant_milestones = [m for m in career_info['milestones'] if m['level'] == 'Advanced']
        
        # Store results in session
        session['roadmap_results'] = {
            'career_title': career_title,
            'career_info': career_info,
            'relevant_milestones': relevant_milestones
        }
        
        return redirect(url_for('results', result_type='roadmap'))
    
    return render_template('roadmap.html', form=form)

@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    """Career comparison tool for users confused between options."""
    form = ComparisonForm()
    
    if form.validate_on_submit():
        career_one = form.career_one.data
        career_two = form.career_two.data
        important_factors = form.important_factors.data
        
        # Store form data in session
        session['comparison_data'] = {
            'career_one': career_one,
            'career_two': career_two,
            'important_factors': important_factors
        }
        
        # Get comparison results
        comparison_results = compare_careers(career_one, career_two)
        
        # Store results in session
        session['comparison_results'] = comparison_results
        
        return redirect(url_for('results', result_type='comparison'))
    
    return render_template('comparison.html', form=form)

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    """Initial page for the recommendation path."""
    form = InterestForm()
    
    if form.validate_on_submit():
        interest = form.interests.data
        
        # Store interest in session
        session['recommendation_data'] = {
            'interests': [interest]  # Store as list for later use
        }
        
        # Redirect to questionnaire for more detailed preferences
        return redirect(url_for('questionnaire'))
    
    return render_template('recommendation.html', form=form)

@app.route('/resume-analysis', methods=['GET', 'POST'])
def resume_analysis():
    """Resume upload and analysis functionality."""
    form = ResumeUploadForm()
    
    if form.validate_on_submit():
        # Check if the post request has the file part
        if 'resume' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
            
        file = request.files['resume']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            # Generate unique filename
            original_filename = secure_filename(file.filename)
            filename = f"{uuid.uuid4()}_{original_filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Save the file
            file.save(filepath)
            
            try:
                # Parse the resume
                resume_data = resume_parser.parse_pdf(filepath)
                
                # Store resume data in session
                session['resume_data'] = resume_data
                
                # If we have recommendation data, update it with resume skills
                if 'recommendation_data' in session:
                    recommendation_data = session['recommendation_data']
                    recommendation_data['resume_skills'] = resume_data['skills']
                    session['recommendation_data'] = recommendation_data
                else:
                    # Initialize recommendation data with resume skills
                    session['recommendation_data'] = {
                        'resume_skills': resume_data['skills'],
                        'interests': []
                    }
                
                flash('Resume successfully uploaded and analyzed!', 'success')
                return redirect(url_for('questionnaire'))
                
            except Exception as e:
                logger.error(f"Error analyzing resume: {str(e)}")
                flash(f'Error analyzing resume: {str(e)}', 'danger')
                return redirect(request.url)
        else:
            flash('Allowed file type is PDF', 'danger')
            return redirect(request.url)
    
    return render_template('resume_analysis.html', form=form)

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    """Interactive questionnaire for user preferences and skills."""
    form = QuestionnaireForm()
    
    # Get questionnaire data
    skills_questions = SKILLS_QUESTIONS
    interests_questions = INTERESTS_QUESTIONS
    values_questions = VALUES_QUESTIONS
    
    if request.method == 'POST':
        # Process questionnaire responses
        responses = {}
        for key, value in request.form.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                responses[question_id] = value
        
        # Extract skill and interest values from responses
        skills = []
        interests = []
        values = []
        
        for q_id, option_value in responses.items():
            # Find which question group this belongs to
            if q_id <= 5:  # Skills questions
                skills.append(option_value)
            elif q_id <= 8:  # Interest questions
                interests.append(option_value)
            else:  # Values questions
                values.append(option_value)
        
        # Update recommendation data in session
        recommendation_data = session.get('recommendation_data', {})
        if 'interests' not in recommendation_data:
            recommendation_data['interests'] = []
        
        # Add new interests from questionnaire
        recommendation_data['interests'].extend(interests)
        recommendation_data['skills'] = skills
        recommendation_data['values'] = values
        
        session['recommendation_data'] = recommendation_data
        
        # Get recommendations based on interests, skills, and resume skills (if available)
        resume_skills = recommendation_data.get('resume_skills', [])
        recommendations = get_recommendations(
            interests=recommendation_data['interests'],
            skills=recommendation_data['skills'],
            resume_skills=resume_skills
        )
        
        # Store recommendations in session
        session['recommendation_results'] = {
            'recommendations': recommendations
        }
        
        return redirect(url_for('results', result_type='recommendation'))
    
    return render_template('questionnaire.html', 
                          form=form, 
                          skills_questions=skills_questions,
                          interests_questions=interests_questions,
                          values_questions=values_questions)

@app.route('/results/<result_type>')
def results(result_type):
    """Display results based on the chosen path."""
    if result_type == 'roadmap' and 'roadmap_results' in session:
        results = session['roadmap_results']
        return render_template('results.html', 
                              result_type=result_type,
                              results=results)
    
    elif result_type == 'comparison' and 'comparison_results' in session:
        results = session['comparison_results']
        return render_template('results.html', 
                              result_type=result_type,
                              results=results)
    
    elif result_type == 'recommendation' and 'recommendation_results' in session:
        results = session['recommendation_results']
        return render_template('results.html', 
                              result_type=result_type,
                              results=results)
    
    else:
        flash('No results available. Please complete a career guidance path first.', 'warning')
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logger.error(f"Server error: {str(e)}")
    return render_template('error.html', error_code=500, error_message="Internal server error"), 500

# Static files route
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
