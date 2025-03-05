__author__ = "qiao"

"""
generate the search keywords for each patient
"""

import json
import os
from openai import AzureOpenAI
import openai
import sys

# client = AzureOpenAI(
# 	api_version="2023-09-01-preview",
# 	azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
# 	api_key=os.getenv("OPENAI_API_KEY"),
#comment this out and use OpenAI instead

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Use OpenAI API key directly
)
def get_keyword_generation_messages(note):
	system = 'You are a helpful assistant and your task is to help search relevant clinical trials for a given patient description. Please first summarize the main medical problems of the patient. Then generate up to 32 key conditions for searching relevant clinical trials for this patient. The key condition list should be ranked by priority. Please output only a JSON dict formatted as Dict{{"summary": Str(summary), "conditions": List[Str(condition)]}}.'

	prompt =  f"Here is the patient description: \n{note}\n\nJSON output:"

	messages = [
		{"role": "system", "content": system},
		{"role": "user", "content": prompt}
	]
	
	return messages


if __name__ == "__main__":
	# the corpus: trec_2021, trec_2022, or sigir
	corpus = sys.argv[1]

	# the model index to use
	model = sys.argv[2]

	outputs = {}
	

	#added absolute path instead
	dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset", corpus, "queries.jsonl"))

	with open(dataset_path, "r") as f:
	#with open(f"dataset/{corpus}/queries.jsonl", "r") as f:
		for line in f.readlines():
			entry = json.loads(line)
			messages = get_keyword_generation_messages(entry["text"])

			response = client.chat.completions.create(
				model=model,
				messages=messages,
				temperature=0,
				max_tokens = 500 #set this to avoid being charged too much
			)

			output = response.choices[0].message.content
			output = output.strip("`").strip("json")
			
			outputs[entry["_id"]] = json.loads(output)



			# with open(f"results/retrieval_keywords_{model}_{corpus}.json", "w") as f:
			# 	json.dump(outputs, f, indent=i

		# Ensure the "results" directory exists
		results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))
		os.makedirs(results_dir, exist_ok=True)

		# Generate the full path for the output file
		results_path = os.path.join(results_dir, f"retrieval_keywords_{model}_{corpus}.json")

		# Print the path to debug
		print(f"Python is trying to save the file to: {results_path}")

		# Try writing to the file
		with open(results_path, "w") as f:
			json.dump(outputs, f, indent=4)
