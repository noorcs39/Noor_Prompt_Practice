from transformers import pipeline, AutoTokenizer
import torch
torch.manual_seed(0)
model = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

torch.manual_seed(0)
prompt = """Classify the text into neutral, negative or positive. 
Text: This movie is definitely one of my favorite movies of its kind. The interaction between respectable and morally strong characters is an ode to chivalry and the honor code amongst thieves and policemen.
Sentiment:
"""

sequences = pipe(
    prompt,
    max_new_tokens=10,
)


for seq in sequences:
    print(f"Result: {seq['generated_text']}")