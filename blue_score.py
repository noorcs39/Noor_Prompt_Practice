import subprocess
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Example ground truth and model outputs
ground_truths = [
    "The capital of France is Paris.",
    "Paris is the capital city of France."
]

model_outputs = [
    "The capital of France is Paris.",
    "Paris is the capital of France."
]

# Function to calculate BLEU score for each pair of model output and ground truth
def calculate_bleu(reference, hypothesis):
    # Tokenize the sentences
    reference_tokens = [ref.split() for ref in reference]
    hypothesis_tokens = hypothesis.split()

    # Calculate BLEU score
    smoothing_function = SmoothingFunction().method1  # Applying smoothing function to handle zero counts
    score = sentence_bleu(reference_tokens, hypothesis_tokens, smoothing_function=smoothing_function)
    return score

# Iterate through outputs and calculate BLEU scores
for i, output in enumerate(model_outputs):
    bleu_score = calculate_bleu(ground_truths, output)
    print(f"Model Output: {output}")
    print(f"BLEU Score: {bleu_score:.4f}\n")

# Run the LLaMA model via Ollama
result = subprocess.run(
    ['ollama', 'run', 'llama3.1'],
    input="What is the capital of France?",
    capture_output=True,
    text=True,
    encoding='utf-8'
)

# Get the response from the model
response = result.stdout.strip()
print(f"LLM Response: {response}")

# Calculate BLEU score for the response
response_bleu_score = calculate_bleu(ground_truths, response)
print(f"BLEU Score for LLM Response: {response_bleu_score:.4f}")
