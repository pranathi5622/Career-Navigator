from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    resumes = db.relationship('Resume', backref='user', lazy=True)
    career_paths = db.relationship('CareerPath', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Analysis results
    skills = db.Column(db.Text)  # Stored as JSON string
    experience = db.Column(db.Text)  # Stored as JSON string
    education = db.Column(db.Text)  # Stored as JSON string
    
    def __repr__(self):
        return f'<Resume {self.filename}>'

class CareerPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    career_title = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    path_type = db.Column(db.String(50))  # 'roadmap', 'comparison', or 'recommendation'
    comparison_with = db.Column(db.String(128))  # For comparison path_type
    
    # Results stored as JSON strings
    milestones = db.Column(db.Text)
    resources = db.Column(db.Text)
    skills_required = db.Column(db.Text)
    
    def __repr__(self):
        return f'<CareerPath {self.career_title}>'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'skills', 'interests', 'values', etc.
    
    # Relationship to options
    options = db.relationship('QuestionOption', backref='question', lazy=True)
    
    def __repr__(self):
        return f'<Question {self.text[:20]}...>'

class QuestionOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<QuestionOption {self.text[:20]}...>'

class UserResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('question_option.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('responses', lazy=True))
    question = db.relationship('Question')
    option = db.relationship('QuestionOption')
    
    def __repr__(self):
        return f'<UserResponse user:{self.user_id} question:{self.question_id}>'
