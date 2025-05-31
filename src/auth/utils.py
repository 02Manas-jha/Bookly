from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from fastapi import HTTPException, status
import uuid
import jwt
import logging
from passlib.context import CryptContext
from src.config import Config

passwd_context = CryptContext(
    schemes=['bcrypt']
)

def generate_passwd_hash(password: str)->str:
    hash = passwd_context.hash(password)

    return hash

def verify_password(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)

def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False) -> str:
    payload = {
        'user':user_data,
        'exp': datetime.now() + (expiry if expiry is not None else timedelta(minutes=60)),
        'jti': str(uuid.uuid4()),
        'refresh': refresh
    }

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )
    return token

def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError as jwte:
        logging.exception(jwte)
        return None
    
    except Exception as e:
        logging.exception(e)
        return None

serializer = URLSafeTimedSerializer(
    secret_key=Config.JWT_SECRET, salt="email-configuration"
)

def create_url_safe_token(data: dict) -> str:
    """Serialize a dict into a URLSafe token"""

    token = serializer.dumps(data)

    return token

def decode_url_safe_token(token: str, max_age: int = 120) -> dict:
    """Deserialize a URLSafe token to get data"""
    try:
        token_data = serializer.loads(token, max_age=max_age)

        return token_data
    
    except SignatureExpired:
        logging.error("Token expired")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token has expired",
        )
    
    except BadSignature:
        logging.error("Invalid token signature")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token",
        )
    
    except Exception as e:
        logging.error(str(e))