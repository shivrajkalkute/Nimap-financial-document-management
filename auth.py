from jose import jwt
from passlib.context import CryptContext

SECRET_KEY='student_project_secret'
pwd=CryptContext(schemes=['bcrypt'])

def hash_password(password):
    return pwd.hash(password)

def verify_password(password, hashed):
    return pwd.verify(password, hashed)

def create_token(username):
    return jwt.encode({'sub':username}, SECRET_KEY, algorithm='HS256')
