from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SelectMultipleField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from career_data import get_all_careers

class CareerForm(FlaskForm):
    career = SelectField('Career', validators=[DataRequired()], 
                         choices=[(career, career) for career in get_all_careers()])
    experience_level = SelectField('Experience Level', validators=[DataRequired()],
                                  choices=[
                                      ('entry', 'Entry Level (0-2 years)'),
                                      ('mid', 'Mid-Level (3-5 years)'),
                                      ('senior', 'Senior Level (6-10 years)'),
                                      ('expert', 'Expert Level (10+ years)')
                                  ])
    skills = SelectMultipleField('What skills do you currently have?', validators=[DataRequired()],
                              choices=[
                                  ('analytical', 'Analytical & Problem-Solving'),
                                  ('communication', 'Communication & Presentation'),
                                  ('technical', 'Technical & Programming'),
                                  ('creativity', 'Creativity & Design'),
                                  ('management', 'Leadership & Management'),
                                  ('math', 'Mathematics & Quantitative'),
                                  ('research', 'Research & Data Analysis'),
                                  ('interpersonal', 'Interpersonal & Teamwork'),
                                  ('writing', 'Writing & Editing'),
                                  ('languages', 'Languages & Linguistics')
                              ])
    education = SelectField('What is your highest level of education?', validators=[DataRequired()],
                         choices=[
                             ('highschool', 'High School Diploma'),
                             ('associate', 'Associate Degree'),
                             ('bachelor', 'Bachelor\'s Degree'),
                             ('master', 'Master\'s Degree'),
                             ('phd', 'Doctorate or PhD'),
                             ('trade', 'Trade School/Certificate'),
                             ('selftaught', 'Self-taught/No Formal Degree')
                         ])
    years_experience = IntegerField('Years of Experience in Related Field', 
                                validators=[DataRequired(), NumberRange(min=0, max=50)],
                                description="Enter the number of years of experience you have in fields related to your target career")

class ComparisonForm(FlaskForm):
    career1 = SelectField('First Career', validators=[DataRequired()], 
                          choices=[(career, career) for career in get_all_careers()])
    career2 = SelectField('Second Career', validators=[DataRequired()], 
                          choices=[(career, career) for career in get_all_careers()])

class QuestionnaireForm(FlaskForm):
    interests = SelectMultipleField('What are your main interests?', validators=[DataRequired()],
                                  choices=[
                                      ('technology', 'Technology & Computing'),
                                      ('science', 'Science & Research'),
                                      ('creative', 'Creative Arts & Design'),
                                      ('business', 'Business & Entrepreneurship'),
                                      ('healthcare', 'Healthcare & Medicine'),
                                      ('education', 'Education & Teaching'),
                                      ('social', 'Social Services & Community'),
                                      ('engineering', 'Engineering & Architecture'),
                                      ('writing', 'Writing & Communication'),
                                      ('legal', 'Legal & Politics')
                                  ])
    
    skills = SelectMultipleField('What skills do you have or enjoy using?', validators=[DataRequired()],
                               choices=[
                                   ('analytical', 'Analytical & Problem-Solving'),
                                   ('communication', 'Communication & Presentation'),
                                   ('technical', 'Technical & Programming'),
                                   ('creativity', 'Creativity & Design'),
                                   ('management', 'Leadership & Management'),
                                   ('math', 'Mathematics & Quantitative'),
                                   ('research', 'Research & Data Analysis'),
                                   ('interpersonal', 'Interpersonal & Teamwork'),
                                   ('writing', 'Writing & Editing'),
                                   ('languages', 'Languages & Linguistics')
                               ])
    
    values = SelectMultipleField('What values are most important to you in a career?', validators=[DataRequired()],
                               choices=[
                                   ('worklife', 'Work-Life Balance'),
                                   ('compensation', 'High Compensation'),
                                   ('stability', 'Job Stability'),
                                   ('growth', 'Growth Opportunities'),
                                   ('autonomy', 'Autonomy & Independence'),
                                   ('impact', 'Social Impact'),
                                   ('challenge', 'Intellectual Challenge'),
                                   ('recognition', 'Recognition & Status'),
                                   ('creativity', 'Creativity & Expression'),
                                   ('travel', 'Travel Opportunities')
                               ])
    
    personality = SelectField('How would you describe your work personality?', validators=[DataRequired()],
                            choices=[
                                ('analytical', 'Analytical & Detail-Oriented'),
                                ('creative', 'Creative & Innovative'),
                                ('practical', 'Practical & Hands-On'),
                                ('leader', 'Leader & Organizer'),
                                ('social', 'Social & Collaborative'),
                                ('independent', 'Independent & Self-Motivated')
                            ])
    
    education = SelectField('What is your current or planned education level?', validators=[DataRequired()],
                          choices=[
                              ('highschool', 'High School Diploma'),
                              ('associate', 'Associate Degree'),
                              ('bachelor', 'Bachelor\'s Degree'),
                              ('master', 'Master\'s Degree'),
                              ('phd', 'Doctorate or PhD'),
                              ('trade', 'Trade School/Certificate'),
                              ('selftaught', 'Self-taught/No Formal Degree')
                          ])
    
    work_environment = SelectMultipleField('What type of work environment do you prefer?', validators=[DataRequired()],
                                         choices=[
                                             ('office', 'Traditional Office'),
                                             ('remote', 'Remote/Work from Home'),
                                             ('outdoors', 'Outdoors/Field Work'),
                                             ('travel', 'Frequent Travel'),
                                             ('startup', 'Fast-paced Startup'),
                                             ('corporate', 'Corporate Structure'),
                                             ('flexible', 'Flexible Schedule'),
                                             ('creative', 'Creative Environment')
                                         ])

class ResumeUploadForm(FlaskForm):
    resume = FileField('Upload Your Resume (PDF format)', validators=[DataRequired()])


