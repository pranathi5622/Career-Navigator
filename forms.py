from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ResumeUploadForm(FlaskForm):
    resume = FileField('Upload Resume (PDF)', validators=[
        FileRequired(),
        FileAllowed(['pdf'], 'PDF files only!')
    ])
    submit = SubmitField('Upload')

class RoadmapForm(FlaskForm):
    career_title = StringField('What career are you interested in?', validators=[DataRequired()])
    experience_level = SelectField('Experience Level', 
                                  choices=[('beginner', 'Beginner (0-2 years)'), 
                                          ('intermediate', 'Intermediate (3-5 years)'), 
                                          ('advanced', 'Advanced (6+ years)')],
                                  validators=[DataRequired()])
    current_role = StringField('Current Role (if any)')
    desired_skills = TextAreaField('Skills you want to develop')
    submit = SubmitField('Generate Roadmap')

class ComparisonForm(FlaskForm):
    career_one = StringField('First Career Option', validators=[DataRequired()])
    career_two = StringField('Second Career Option', validators=[DataRequired()])
    important_factors = SelectField('Most Important Factor', 
                                   choices=[('salary', 'Salary Potential'), 
                                           ('stability', 'Job Stability'), 
                                           ('growth', 'Growth Opportunity'),
                                           ('work_life', 'Work-Life Balance'),
                                           ('satisfaction', 'Job Satisfaction')],
                                   validators=[DataRequired()])
    submit = SubmitField('Compare Careers')

class QuestionnaireForm(FlaskForm):
    # These fields will be dynamically added based on the questionnaire
    submit = SubmitField('Submit Answers')

class InterestForm(FlaskForm):
    interests = SelectField('Select your primary interest area', 
                           choices=[('technology', 'Technology & Computing'), 
                                   ('healthcare', 'Healthcare & Medicine'), 
                                   ('business', 'Business & Finance'),
                                   ('arts', 'Arts & Creative Fields'),
                                   ('science', 'Science & Research'),
                                   ('education', 'Education & Training'),
                                   ('trades', 'Skilled Trades'),
                                   ('service', 'Service Industry')],
                           validators=[DataRequired()])
    submit = SubmitField('Continue')
