from fastapi import FastAPI, UploadFile, File
from app.loader import load_document
from app.retriever import Retriever

app = FastAPI()
retriever = Retriever()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    retriever.add_document(file.filename, content, file.content_type)
    return {"status": "Document uploaded", "filename": file.filename}

@app.get("/query/")
def query(q: str):
    results = retriever.query(q)
    return {"results": results}
