import time
from fastapi import APIRouter
from Backend.schemas import resume_request_model
import Backend.resume_scoring_parser as RSP

router = APIRouter(
    prefix= "/processing"
)


@router.get("/")
def get_processing_health_check():
    return {"message":"Enter processing.py; running get[/processing] endpoint "}

@router.post("/calculate_resume_results")
def calculate_resume_results(payload: resume_request_model):
    return RSP.resume_parsing(payload)

