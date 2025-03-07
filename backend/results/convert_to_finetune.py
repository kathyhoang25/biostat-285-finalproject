import json

# Load labeled data
with open("C:/Users/joyce/Documents/biostat-285-finalproject/backend/results/labeled_data.json", "r") as file:
    data = json.load(file)

# Create a new dataset in the format required for fine-tuning
finetune_data = []
for entry in data:
    prompt_text = entry['data']['text']
    label = entry['annotations'][0]['result'][0]['value']['choices'][0]
    finetune_data.append({"prompt": prompt_text, "completion": label})

# Save the new dataset
with open("C:/Users/joyce/Documents/biostat-285-finalproject/backend/results/fine_tune_data.json", "w") as outfile:
    for entry in finetune_data:
        json.dump(entry, outfile)
        outfile.write("\n")

print("Fine-tuning dataset created successfully!")
