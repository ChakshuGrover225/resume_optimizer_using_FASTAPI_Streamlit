from fastapi import FastAPI
from processing import router

app = FastAPI(title="Resume Job Matcher API")
 
 
app.include_router(router)
