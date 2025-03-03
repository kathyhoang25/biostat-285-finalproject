import React, { useState } from "react";
import axios from "axios";

function App() {
  const [patientPrompt, setPatientPrompt] = useState("");
  const [trials, setTrials] = useState([]);

  const matchTrials = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/match_trials/", {
        patient_prompt: patientPrompt,
      });
      setTrials(response.data.matched_trials);
    } catch (error) {
      console.error("Error fetching trials:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Georgia" }}>
      <h1>Clinical Trial Matcher</h1>
      <input
        type="text"
        placeholder="Enter patient details..."
        value={patientPrompt}
        onChange={(e) => setPatientPrompt(e.target.value)}
        style={{ width: "100%", 
          marginBottom: "10px"
        }}
      />
      <button onClick={matchTrials} style={{ 
          padding: "10px", 
          background:"#007bff",
          color: "white",
          border: "1px solid rgba(0, 0, 0, 0.1)", //light grey border
          boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",  // Soft shadow
          borderRadius: "8px",
          fontSize: "16px", 
          fontWeight: "bold",
          cursor: "pointer" }}>
        Find Trials
      </button>

      <h2>Matched Clinical Trials</h2>
      <ul>
        {trials.length > 0 ? (
          trials.map((trial, index) => (
            <li key={index}>
              <strong>{trial.title}</strong> (ID: {trial.trial_id}) - Match Score: {trial.match_score}
            </li>
          ))
        ) : (
          <p>No trials matched yet.</p>
        )}
      </ul>
    </div>
  );
}

export default App;
