from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from . import database, models
from sqlalchemy.orm import Session  


router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str
    
class CreateUser(BaseModel):
    username: str
    email: str
    password: str
    
#hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) 

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {"message": "Login successful"}
    

@router.post("/register")
def register(createUser: CreateUser, db: Session = Depends(get_db)):
    hashed_pw = hash_password(createUser.password)
    db_user = models.User (
        username = createUser.username,
        email = createUser.email ,
        hashed_password = hashed_pw
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user