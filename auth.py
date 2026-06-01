from jose import jwt

SECRET_KEY = "student_project_secret"

def create_token(username):
    return jwt.encode({"sub": username}, SECRET_KEY, algorithm="HS256")