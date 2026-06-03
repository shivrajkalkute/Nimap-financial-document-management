from fastapi import FastAPI,UploadFile,File,HTTPException
from database import Base,engine,SessionLocal
from models import User,Document
from auth import *
from rag import index_document,search
import os

app=FastAPI(title='Financial Document Management API')
Base.metadata.create_all(bind=engine)

PERMISSIONS={
'Admin':['all'],
'Analyst':['upload','edit'],
'Auditor':['review'],
'Client':['view']
}

@app.post('/auth/register')
def register(username:str,password:str):
    db=SessionLocal()
    user=User(username=username,password=hash_password(password))
    db.add(user)
    db.commit()
    return {'message':'registered'}

@app.post('/auth/login')
def login(username:str,password:str):
    db=SessionLocal()
    user=db.query(User).filter(User.username==username).first()
    if not user or not verify_password(password,user.password):
        raise HTTPException(401,'invalid credentials')
    return {'token':create_token(username)}

@app.post('/users/assign-role')
def assign_role(user_id:int,role:str):
    db=SessionLocal()
    user=db.query(User).get(user_id)
    user.role=role
    db.commit()
    return {'message':'role assigned'}

@app.get('/users/{user_id}/permissions')
def permissions(user_id:int):
    db=SessionLocal()
    user=db.query(User).get(user_id)
    return {'permissions':PERMISSIONS.get(user.role,[])}

@app.post('/documents/upload')
async def upload_document(
    title:str,
    company_name:str,
    document_type:str,
    uploaded_by:str,
    file:UploadFile=File(...)
):
    os.makedirs('uploads',exist_ok=True)
    path=f'uploads/{file.filename}'
    content=await file.read()
    with open(path,'wb') as f:
        f.write(content)

    db=SessionLocal()
    doc=Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        uploaded_by=uploaded_by,
        file_path=path
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    try:
        index_document(doc.id,content.decode(errors='ignore'))
    except:
        pass

    return {'document_id':doc.id}

@app.get('/documents')
def get_documents():
    db=SessionLocal()
    return db.query(Document).all()

@app.get('/documents/{document_id}')
def get_document(document_id:int):
    db=SessionLocal()
    return db.query(Document).get(document_id)

@app.delete('/documents/{document_id}')
def delete_document(document_id:int):
    db=SessionLocal()
    doc=db.query(Document).get(document_id)
    db.delete(doc)
    db.commit()
    return {'message':'deleted'}

@app.post('/rag/search')
def rag_search(query:str):
    return search(query)
