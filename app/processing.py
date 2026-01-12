import time
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# -------- Input Schema --------
class InputPayload(BaseModel):
    resume_text: str
    job_description_text: str


# -------- Core Business Logic --------
def operation_task(resume_text: str, job_description_text: str):
    # Simulate long computation
    time.sleep(3)

    return {
        "data_1": f"dummy summary",
        "data_2": f"dummy suggestions",
        "data_3": 0.7
    }


# -------- API Route --------
@router.post("/process")
def process_text(payload: InputPayload):
    result = operation_task(
        payload.resume_text,
        payload.job_description_text
    )
    return result
