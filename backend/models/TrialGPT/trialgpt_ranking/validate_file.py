import json

def validate_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                data = json.loads(line)
                print(f"Line {line_number}: Valid JSON with _id = {data.get('_id', 'N/A')}")
            except json.JSONDecodeError as e:
                print(f"Line {line_number}: Invalid JSON - {e}")

if __name__ == "__main__":
    file_path = 'models/TrialGPT/dataset/synthetic/queries.jsonl'
    validate_jsonl(file_path)