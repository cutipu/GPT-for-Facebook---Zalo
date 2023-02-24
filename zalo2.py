import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set up device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Define function to generate response
def generate_response(input_text, max_length=50):
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    outputs = model.generate(input_ids, max_length=max_length, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Get input message from Zalo user
input_message = "Xin chào"

# Generate response using GPT-2
response = generate_response(input_message)

# Send response back to Zalo user
send_message(response)
