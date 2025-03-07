import openai

#run this file to see which models openai gives access to
openai.api_key = "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"  # Replace with your actual key

models = openai.models.list()

for model in models:
    print(model.id)