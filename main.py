from fastapi import FastAPI, UploadFile, File
from database import Base, engine, SessionLocal
from models import Document
import os

print("MAIN.PY LOADED")
app = FastAPI(title="Financial Documents Management API")

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Financial Documents Management API"}

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    db = SessionLocal()
    doc = Document(
        title=file.filename,
        file_path=file_path,
        uploaded_by="student"
    )
    db.add(doc)
    db.commit()

    return {"message": "Document uploaded successfully"}

@app.get("/documents")
def get_documents():
    db = SessionLocal()
    docs = db.query(Document).all()

    return [
        {
            "id": d.id,
            "title": d.title
        }
        for d in docs
    ]