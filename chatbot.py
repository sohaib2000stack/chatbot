from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

def chatbot(user_input):
    # Load the model and tokenizer
    model_name = "facebook/blenderbot-400M-distill"
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

    # Generate response
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids
    response_ids = model.generate(input_ids)[0]
    response = tokenizer.decode(response_ids, skip_special_tokens=True)

    return response
