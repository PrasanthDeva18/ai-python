import tiktoken
from transformers import GPT2Tokenizer


# Load the tokenizer
tokenizer = tiktoken.encoding_for_model("gpt-5")

tokenizer2 = GPT2Tokenizer.from_pretrained("gpt2")

text = "AI engineering is fun!"


token_ids2 = tokenizer.encode(text)
print("Token IDs:", token_ids2)

# Convert text into unique token IDs
token_ids = tokenizer.encode(text)
print("Token IDs:", token_ids)

# See the exact text each ID maps to
for token_id in token_ids:
    token_str = tokenizer.decode([token_id])
    print(f"ID: {token_id} -> Token: '{token_str}'")

for token_id in token_ids2:
    token_str = tokenizer.decode([token_id])
    print(f"ID: {token_id} -> Token: '{token_str}'")

