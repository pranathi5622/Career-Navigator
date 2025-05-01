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
    user_profiles = db.relationship('UserProfile', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resume_skills = db.Column(db.Text)
    resume_education = db.Column(db.Text)
    resume_experience = db.Column(db.Integer)
    interests = db.Column(db.Text)
    skills = db.Column(db.Text)
    values = db.Column(db.Text)
    personality = db.Column(db.String(64))
    education_level = db.Column(db.String(64))
    preferred_work_environment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserProfile {self.id}>'

class Career(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text)
    required_education = db.Column(db.String(128))
    required_skills = db.Column(db.Text)
    salary_range = db.Column(db.String(64))
    job_outlook = db.Column(db.String(64))
    
    def __repr__(self):
        return f'<Career {self.name}>'

class CareerPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    career_id = db.Column(db.Integer, db.ForeignKey('career.id'), nullable=False)
    level = db.Column(db.String(64))
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    required_skills = db.Column(db.Text)
    required_experience = db.Column(db.Integer)
    
    # Relationship
    career = db.relationship('Career', backref='career_paths')
    
    def __repr__(self):
        return f'<CareerPath {self.title}>'
