from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Enable CORS (Allow frontend to talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (frontend & backend)
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods
    allow_headers=["*"],   # Allow all headers
)

# Define request format
class PatientRequest(BaseModel):
    patient_prompt: str

# Fake response for now (replace with AI later)
@app.post("/match_trials/")
async def match_trials(request: PatientRequest):
    return {
        "matched_trials": [
            {"trial_id": "NCT12345", "title": "Diabetes Treatment Study", "match_score": 0.92},
            {"trial_id": "NCT67890", "title": "Hypertension Drug Trial", "match_score": 0.85}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

