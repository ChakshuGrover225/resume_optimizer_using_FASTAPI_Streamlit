'''  

->  Starts our FastAPI server, mentions routes
->  Start FastAPI and Streamlit server from app Directory (test_env for developement Phase)
->  All the configurations are done as per:

    app/ CURRENT_WORKING_DIRECTORY

        backend/    FASTAPI FILES
            --- backend files ---
        
        Frontend/   
            --- Streamlit files ---
        
        main.py     STARTER CODE

''' 

from fastapi import FastAPI         
from pydantic import BaseModel
from Backend import processing  # logical layer; "/processing" endpoint
from Backend.schemas import resume_request_model    # pydantic object for Request Payload




app = FastAPI()
app.include_router(processing.router)   # adds "/processing/" route 




@app.get("/")
def read_root():
    return {"message": "Welcome to the NEWEST API"}