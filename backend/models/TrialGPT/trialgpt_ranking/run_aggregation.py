__author__ = "qiao"

"""
Using GPT to aggregate the scores by itself.
"""

from beir.datasets.data_loader import GenericDataLoader
import json
from nltk.tokenize import sent_tokenize
import os
import sys
import time

from TrialGPT import trialgpt_aggregation

if __name__ == "__main__":
	corpus = sys.argv[1] 
	model = sys.argv[2]

	# the path of the matching results
	matching_results_path = sys.argv[3]
	results = json.load(open(matching_results_path))

	# loading the trial2info dict
	trial2info = json.load(open("models/TrialGPT/dataset/trial_info.json"))	
	# trial2info = json.load(open("dataset/trial_info.json"))
	
	# loading the patient info
	# _, queries, _ = GenericDataLoader(data_folder=f"dataset/{corpus}/").load(split="test")
	data_path = "models/TrialGPT/dataset/synthetic/"
	corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="test")
	print(f"Loaded query IDs: {list(queries.keys())}")

	# output file path
	# output_path = f"results/aggregation_results_{corpus}_{model}.json"
	output_path = f"results/aggregation_results_synthetic_{model}.json"

	if os.path.exists(output_path):
		output = json.load(open(output_path))
	else:
		output = {}

	# patient-level
	for patient_id, info in results.items():
		# get the patient note
		patient = queries[patient_id]
		sents = sent_tokenize(patient)
		sents.append("The patient will provide informed consent, and will comply with the trial protocol without any practical issues.")
		sents = [f"{idx}. {sent}" for idx, sent in enumerate(sents)]
		patient = "\n".join(sents)

		if patient_id not in output:
			output[patient_id] = {}
		
		# label-level, 3 label / patient
		# print("Contents of results:", json.dumps(results, indent=4))
        #print("Total patients in results:", len(results))

		for label, trials in info.items():
				
			# trial-level
			for trial_id, trial_results in trials.items():
				# already cached results
				if trial_id in output[patient_id]:
					continue

				if type(trial_results) is not dict:
					output[patient_id][trial_id] = "matching result error"

					with open(output_path, "w") as f:
						json.dump(output, f, indent=4)

					continue

				# specific trial information
				trial_info = trial2info[trial_id]	

				try:
					print(f"Processing trial {trial_id} for patient {patient_id}")
					result = trialgpt_aggregation(patient, trial_results, trial_info, model)
					output[patient_id][trial_id] = result 
					
					print(f"Saving results to: {output_path}")
					with open(output_path, "w") as f:
						json.dump(output, f, indent=4)
					print("Results successfully saved.")

				except Exception as e:
					print(f"⚠️ Error processing trial {trial_id} for patient {patient_id}: {e}")
					continue
