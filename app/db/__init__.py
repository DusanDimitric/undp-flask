import os

from flask_sqlalchemy import SQLAlchemy

from main import app

MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')

DB_CONN_STR = 'mysql+pymysql://test:test@%s:3306/UNDP' % MYSQL_HOST

app.config['SQLALCHEMY_DATABASE_URI']        = DB_CONN_STR
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']  = True

db = SQLAlchemy(app)

class ApplicationTypes(db.Model):
    __tablename__ = 'application_types'
    id = db.Column(
        'id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    name = db.Column(
        'name',
        db.String(100),
        nullable=False
    )

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(
        'id', 
        db.Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    uuid = db.Column(
        'uuid', 
        db.Unicode(36),
        unique=True,
        nullable=False
    )
    application_type_id = db.Column(
        'application_type_id',
        db.Integer,
        db.ForeignKey('application_types.id'),
        nullable=False
    )
    title = db.Column(
        'title',
        db.String(255),
        nullable=False
    )
    relevant_interests = db.Column(
        'relevant_interests',
        db.Text,
        nullable=False
    )
    self_government = db.Column(
        'self_government',
        db.String(500),
        nullable=False
    )
    contact_person = db.Column(
        'contact_person', 
        db.JSON,
        nullable=False
    )
    applicant_website = db.Column(
        'applicant_website',
        db.String(2083),
        nullable=False
    )
    project_duration_in_months = db.Column(
        'project_duration_in_months', 
        db.SmallInteger,
        nullable=False
    )
    other_applicants = db.Column(
        'other_applicants',
        db.JSON,
        nullable=True
    )
    project_summaries = db.Column(
        'project_summaries',
        db.JSON,
        nullable=False
    )
    detailed_description = db.Column(
        'detailed_description',
        db.Text,
        nullable=False
    )
    innovation = db.Column(
        'innovation',
        db.Text,
        nullable=False
    )
    project_activities = db.Column(
        'project_activities',
        db.Text,
        nullable=False
    )
    expected_outcomes = db.Column(
        'expected_outcomes',
        db.Text,
        nullable=False
    )
    gender_approach = db.Column(
        'gender_approach',
        db.Text,
        nullable=False
    )
    project_budget = db.Column(
        'project_budget',
        db.Text,
        nullable=False
    )


