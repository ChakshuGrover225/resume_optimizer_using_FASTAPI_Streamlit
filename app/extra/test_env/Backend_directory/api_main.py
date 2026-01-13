from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class ProcessRequest(BaseModel):
    resume_text: str
    job_desc_text: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
@app.post("/processing")
def process_resume(payload: ProcessRequest):
    
    # langchain
    # groq
    # prom
    # invoke
    # json 
    
    
    
    
    
    return {
        "resume_length": 1200,
        "job_desc_length": 800,
        "score_value": 0.75
    }