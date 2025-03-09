import React, { useState } from "react";
import axios from "axios";
import { FaGithub, FaInfoCircle, FaEnvelope } from "react-icons/fa"; // Import icons

function App() {
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");
  const [race, setRace] = useState("");
  const [condition, setCondition] = useState("");
  const [trials, setTrials] = useState([]);
  const [loading, setLoading] = useState(false);

  // const matchTrials = async () => {
  //   setLoading(true);
  //   try {
  //     const response = await axios.post("http://127.0.0.1:8000/match_trials/", {
  //       age: age,
  //       gender: gender,
  //       race: race,
  //       condition: condition,
  //     });
  //     setTrials(response.data.matched_trials);
  //   } catch (error) {
  //     console.error("Error fetching trials:", error);
  //   } finally {
  //     setLoading(false);
  //   }
  // };

  // const matchTrials = async () => {
  //   setLoading(true);
  //   try {
  //     // Step 1: Get Matched Trials
  //     const response = await axios.post("http://127.0.0.1:8000/match_trials/", {
  //       age: age,
  //       gender: gender,
  //       race: race,
  //       condition: condition,
  //     });
  
  //     setTrials(response.data.matched_trials);
  
  //     // Step 2: Get Ranked Trials After Matching
  //     const patientId = response.data.patient_id || "synthetic-001";  // Replace with actual patient ID
  //     const rankedResponse = await axios.get(`http://127.0.0.1:8000/ranked_trials/${patientId}`);
  
  //     if (rankedResponse.data.ranked_trials) {
  //       setTrials(rankedResponse.data.ranked_trials);  // Update trials with ranked ones
  //     }
  //   } catch (error) {
  //     console.error("Error fetching trials:", error);
  //   } finally {
  //     setLoading(false);
  //   }
  // };  

  // attempt 3
  const [patientPrompt, setPatientPrompt] = useState("");
  // const [trials, setTrials] = useState([]);

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
    <div style={styles.container}>
      {/* Top Header */}
      <div style={styles.header}>
        <div style={styles.logoContainer}>
          <img src="/ucla-logo.png" alt="UCLA Logo" style={styles.logo} />
          <div style={styles.departmentText}>Department of Biostatistics</div>
        </div>
        <div style={styles.navbar}>
          <a href="https://github.com/kathyhoang25/biostat-285-finalproject" target="_blank" rel="noopener noreferrer" style={styles.navLink}>
            <FaGithub size={20} /> GitHub
          </a>
          <a href="/about" style={styles.navLink}>
            <FaInfoCircle size={20} /> About
          </a>
          <a href="/contact" style={styles.navLink}>
            <FaEnvelope size={20} /> Contact Us
          </a>
        </div>
      </div>

      <h1 style={styles.title}>Clinical Trial Matcher</h1>
      <p style={styles.subtitle}>
        Our system helps match patients with clinical trials based on medical conditions, demographics, and eligibility criteria.
        Enter your details below to find the best trials for you.
      </p>

      <div style={styles.formContainer}>
        {/* Age Input */}
        <div style={styles.inputGroup}>
          <label style={styles.label}>Your Age:</label>
          <input
            type="number"
            placeholder="Enter your age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            style={styles.input}
          />
        </div>

        {/* Gender Selection */}
        <div style={styles.inputGroup}>
          <label style={styles.label}>Your Gender:</label>
          <select value={gender} onChange={(e) => setGender(e.target.value)} style={styles.input}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </div>

        {/* Race Selection */}
        <div style={styles.inputGroup}>
          <label style={styles.label}>Your Race:</label>
          <select value={race} onChange={(e) => setRace(e.target.value)} style={styles.input}>
            <option value="">Select Race</option>
            <option value="Asian">Asian</option>
            <option value="Black or African American">Black or African American</option>
            <option value="Hispanic or Latino">Hispanic or Latino</option>
            <option value="White">White</option>
            <option value="Other">Other</option>
          </select>
        </div>

        {/* Condition Input */}
        <div style={styles.inputGroup}>
          <label style={styles.label}>Your Condition:</label>
          <input
            type="text"
            placeholder="Enter your condition (e.g., Type 2 Diabetes)"
            value={condition}
            onChange={(e) => setCondition(e.target.value)}
            style={styles.input}
          />
        </div>

        {/* Search Button */}

        <button onClick={matchTrials} className="searchButton" disabled={loading}>
          🔍 {loading ? "Searching..." : "Click Here to Begin Your Trial Search"}
        </button>


        {/* Disclaimer (Restored Style) */}
        <p style={styles.disclaimer}>
          * Information entered on this site is being stored anonymously for research purposes.
        </p>
      </div>

      {/* Results Section
      <h2 style={styles.resultsTitle}>Matched Clinical Trials</h2>

      <div style={styles.resultsContainer}>
        {trials.length > 0 ? (
          trials.map((trial, index) => (
            <div key={index} style={styles.trialCard}>
              <h3 style={styles.trialTitle}>{trial.title}</h3>
              <p><strong>ID:</strong> {trial.trial_id}</p>
              <p><strong>Location:</strong> {trial.location}</p>
              <p><strong>Status:</strong> {trial.status}</p>
              <p><strong>Match Score:</strong> {trial.match_score}</p>
            </div>
          ))
        ) : (
          <p style={styles.noResults}>No trials matched yet.</p>
        )}
      </div> */}
      {/* Results Section */}
      <h2 style={styles.resultsTitle}>Ranked Clinical Trials</h2>

      <div style={styles.resultsContainer}>
        {trials.length > 0 ? (
          trials.map((trial, index) => (
            <div key={index} style={styles.trialCard}>
              <h3 style={styles.trialTitle}>{trial.title || `Trial ${index + 1}`}</h3>
              <p><strong>ID:</strong> {trial.trial_id || "N/A"}</p>
              <p><strong>Relevance Score:</strong> {trial.relevance_score_R ? trial.relevance_score_R.toFixed(2) : "N/A"}</p>
              <p><strong>Eligibility Score:</strong> {trial.eligibility_score_E ? trial.eligibility_score_E.toFixed(2) : "N/A"}</p>
              <p><strong>Matching Score:</strong> {trial.matching_score_M ? trial.matching_score_M.toFixed(2) : "N/A"}</p>
              <p><strong>Total Score:</strong> {((trial.relevance_score_R + trial.eligibility_score_E)/100 + trial.matching_score_M).toFixed(2)}</p>
            </div>
          ))
        ) : (
          <p style={styles.noResults}>No trials matched yet.</p>
        )}
      </div>
    </div>
  );
}

// CSS Styling
const styles = {
  container: {
    maxWidth: "700px",
    margin: "40px auto",
    textAlign: "center",
    fontFamily: "Georgia, serif",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "10px",
    backgroundColor: "#f8f9fa",
    borderBottom: "1px solid #ddd",
  },
  logoContainer: {
    display: "flex",
    flexDirection: "column",
    alignItems: "flex-start",
  },
  logo: {
    height: "50px",
  },
  departmentText: {
    fontSize: "14px",
    fontWeight: "bold",
    color: "#555",
  },
  navbar: {
    display: "flex",
    gap: "20px",
  },
  navLink: {
    display: "flex",
    alignItems: "center",
    gap: "5px",
    textDecoration: "none",
    color: "#007bff",
    fontSize: "16px",
    fontWeight: "bold",
  },
  formContainer: {
    backgroundColor: "#f8f9fa",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
  },
  inputGroup: {
    textAlign: "left",
    marginBottom: "15px",
  },
  label: {
    fontSize: "16px",
    fontWeight: "bold",
    display: "block",
    marginBottom: "5px",
  },
  input: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    border: "1px solid #ccc",
    borderRadius: "8px",
  },
  button: {
    width: "100%",
    padding: "12px",
    fontSize: "16px",
    fontWeight: "bold",
    color: "white",
    background: "linear-gradient(90deg, #007bff, #0056b3)",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
  },
  disclaimer: {
    fontSize: "12px",
    fontStyle: "italic",
    color: "#666", 
    marginTop: "10px",
  },
};

export default App;
