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
            # 2.899999999666666
            {"trial_id": "NCT12345678", "title": "Diabetes Treatment Study", "relevance_score_R": 95 , "eligibility_score_E": 95 , "matching_score_M": .8999999996666661},
            {"trial_id": "NCT34567890", "title": "Hypertension Drug Trial", "relevance_score_R": 85 , "eligibility_score_E": 75 , "matching_score_M": 0.7},
            {"trial_id": "NCT45678901", "title": "Cardiovascular Risk Reduction Trial", "relevance_score_R":  80 , "eligibility_score_E": 60 , "matching_score_M": 1.2},
            {"trial_id": "NCT23456789", "title": "Diabetic Neuropathy Research", "relevance_score_R": 70 , "eligibility_score_E": -70 , "matching_score_M": -1.0}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# from fastapi import FastAPI
# import json

# app = FastAPI()

# @app.get("/ranked_trials/{patient_id}")
# def get_ranked_trials(patient_id: str):
#     # Load ranked results
#     with open("results/ranked_results_synthetic_gpt-4o.json") as f:
#         ranked_trials = json.load(f)

#     # Check if patient_id exists in results
#     if patient_id in ranked_trials:
#         return {"patient_id": patient_id, "ranked_trials": ranked_trials[patient_id]}
#     else:
#         return {"error": "No ranked trials found for this patient."}
