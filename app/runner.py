import threading
import time
import requests
import uvicorn
from main import app


def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")


if __name__ == "__main__":
    # Start FastAPI in background thread
    server_thread = threading.Thread(target=run_server, daemon=True) # creates an individual OS thread, 
    server_thread.start()

    # Give server time to boot
    time.sleep(1)

    # -------- Input Data --------
    resume_text = "Experienced data scientist with ML background"
    job_description_text = "Looking for a data scientist with ML and Python skills"

    payload = {
        "resume_text": resume_text,
        "job_description_text": job_description_text
    }

    # -------- API Call --------
    response = requests.post(
        "http://127.0.0.1:8000/process",
        json=payload,
        timeout=30
    )

    print("API Response:")
    print(response.json())
