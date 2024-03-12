from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)  # Change to String for phone number
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) == 10:  # Check length of phone number string
            return phone_number
        else:
            raise ValueError('Invalid phone number')

    @validates('name')
    def validate_name(self, key, name):
        if name.strip():  # Check if name is not empty or only whitespace
            return name
        else:
            raise ValueError('Failed to validate name')

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content):
        if len(content) >= 250:
            return content
        else:
            raise ValueError('Failed to validate content length')

    @validates('category')
    def validate_category(self, key, category):
        if category in ['Fiction', 'Non-Fiction']:
            return category
        else:
            raise ValueError('Failed to validate category type')

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) <= 250:
            return summary
        else:
            raise ValueError('Failed to validate summary length')

    @validates('title')
    def validate_title(self, key, title):
        if any(word in title for word in ["Won't Believe", "Secret", "Top", "Guess"]):
            return title
        else:
            raise ValueError('Failed to validate title')

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'
