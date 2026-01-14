from Backend.schemas import resume_request_model
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

def resume_parsing(Payload: resume_request_model):
    
    load_dotenv() # loads .env into environment
    #groq_api_key = os.getenv("GROQ_API_KEY")
    groq_api_key = "unknown"

    llm = ChatGroq(model= "llama-3.3-70b-versatile",
               temperature= 0.5,
               api_key= groq_api_key
               )

    template = """ 


impersonate as a HR manager hiring for the role as per given job description.
you are provided with the Resueme's data and Job description. This is the only pieces of relevant data. 
Strictly do not assume anything about candidate outside the resume data and about job role outside the job description data.

here is the resume data:
"
{resume_data}
"

here is the job description:
"
{job_description}
"



based on the compatibility score of the Candidate's Resume over the job description. give the Output as:

1. type - JSON
2. components:
    a. resume-to-job role Match score
    b. top 5 job roles based on resume
    c. hireability - (y/n)
    d. summary of Resume
    e. suggestions to improve resume as per job descriptio

3. structure of json output:
    "resume_score": float,
    "resume_summary" : string,
    "resume_suggestion" : string ,
    "recommended_job_titles" : list



"""

    prompt = PromptTemplate.from_template(template= template)

    parser = StrOutputParser()

    chain = prompt | llm | parser

    resume_data =  Payload.resume_text
    job_description = Payload.job_desc_text
    response_data = chain.invoke(
        {
            "resume_data": resume_data,
            "job_description": job_description
        }
    )


    print(response_data)

    import re
    import json

    def extract_json_from_text(text: str) -> dict:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group(0)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                print("Error: Found JSON block but could not parse it.")
                return {}
        else:
            print("No JSON found in text.")
            return {}
        
    parsed_json = extract_json_from_text(response_data)
    print(parsed_json)

    result = parsed_json
    result['inside'] = 'resume_scoring_parser.py file'
    result['Resume'] = Payload.resume_text
    result['Job Description'] = Payload.job_desc_text

    return result
'''
    return {
        "resume_score": 0.75,
        "inside":"resume_scoring_parser.py file",
        "Resume": Payload.resume_text,
        "Job Description": Payload.job_desc_text,
        "resume_summary" : "This is resume Summary",
        "resume_suggestion" : "This is suggestions" ,
        "recommended_job_titles" : ['Data Scein', 'ML engineer' , 'UI UX designer']
    }

'''