import json

# Load the original JSON file
with open("C:/Users/joyce/Documents/biostat-285-finalproject/backend/results/matching_results_synthetic_gpt-4o.json", "r") as file:
    data = json.load(file)

# Create a simplified JSON format for Label Studio
simplified_data = []

# Iterate through the nested structure to extract text and labels
for group_key, group_value in data.items():
    for entry_key, entry_value in group_value.items():
        for trial_id, trial_data in entry_value.items():
            # Process inclusion criteria
            if 'inclusion' in trial_data:
                for inc_key, inc_value in trial_data['inclusion'].items():
                    simplified_data.append({
                        "text": inc_value[0],
                        "label": "included" if inc_value[2] == "included" else "not included"
                    })
            # Process exclusion criteria
            if 'exclusion' in trial_data:
                for exc_key, exc_value in trial_data['exclusion'].items():
                    simplified_data.append({
                        "text": exc_value[0],
                        "label": "not excluded" if exc_value[2] == "not excluded" else "excluded"
                    })

# Save the simplified JSON file
output_path = "C:/Users/joyce/Documents/biostat-285-finalproject/backend/results/simplified_label_data.json"
with open(output_path, "w") as outfile:
    json.dump(simplified_data, outfile, indent=4)

print(f"File saved at: {output_path}")
