from transformers import AutoTokenizer, AutoModelForCausalLM, TFAutoModelForCausalLM

prompt = "Write a short email asking my manager for leave tomorrow."


# Here using base model and instruct model 
#  Base Model  - 
# Instruct Model - Train with system, user, assistant - 

messages = [
    {"role": "user", "content": "Write a short email asking my manager for leave tomorrow."}
]

for name in ["Qwen/Qwen2-0.5B", "Qwen/Qwen2-0.5B-Instruct"]:
    print("Loading", name)
 
    tokenizer = AutoTokenizer.from_pretrained(name) # used for load tokenizer and converts text to number and back, download the tokenized from the huggingface - first time only
    model = AutoModelForCausalLM.from_pretrained(name) #loads the model itself , model predicts the next word which is what chat models do., it download the model weights and load them into memory

    if name == "Qwen/Qwen2-0.5B-Instruct":
        prompt = tokenizer.apply_chat_template(messages,tokenize=True, add_generation_prompt=True) #add_generation_prompt - tells the model it is now its turn to answer

   # tokenize=False, add_generation_prompt=True
    inputs = tokenizer(prompt, return_tensors="pt") 

    print(inputs)
    # output = model.generate(**inputs, max_new_tokens=200)

    # print("MODEL:", name)
    # print(tokenizer.decode(output[0], skip_special_tokens=True))
    # print("-" * 40)


#     Symbol	Unpacks	Example
# *	A list or tuple into positional arguments	func(*[1, 2]) is func(1, 2)
# **	A dictionary into named arguments	func(**{"a": 1}) is func(a=1)

model = TFAutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")

inputs = tokenizer(prompt, return_tensors="tf")
print(inputs["input_ids"])