from pydantic import BaseModel


class resume_request_model(BaseModel):        # request's payload
    resume_text: str
    job_desc_text: str