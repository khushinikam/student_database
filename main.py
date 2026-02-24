from fastapi import FastAPI,Depends, HTTPException
import models, schemas, auth

from sqlalchemy.orm import Session
from database import get_db, BaseClass,engine


app = FastAPI()
BaseClass.metadata.create_all(bind=engine)


@app.get("/", response_model=list[schemas.studentResponse])
def get_users(db: Session = Depends(get_db)):
    student = db.query(models.Student).all()
    return student

@app.post("/signup")
def signup(student: schemas.createStudent, db: Session = Depends(get_db)):
    
    new_user = models.Student(
        student_name=student.student_name,
        student_email=student.student_email,
        student_password=auth.hash_password(student.student_password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


@app.post("/login", response_model=schemas.token)

def login(student: schemas.studentLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.Student).filter(models.Student.student_email == student.student_email).first()

    if not db_user or not auth.verify_password(student.student_password, db_user.student_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    

    token = auth.create_access_token({"subject": db_user.student_email})
    return {"access_token": token, "token_type": "bearer"}
