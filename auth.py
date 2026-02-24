from jose import jwt
from passlib.context import CryptContext


SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

hash_pass = CryptContext(schemes=["bcrypt"])


def hash_password(password: str):
    return hash_pass.hash(password)

def verify_password(password, hashed_password):
    return hash_pass.verify(password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)