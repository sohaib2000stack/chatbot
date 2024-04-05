from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

def chatbot():
    # Load the model and tokenizer
    model_name = "facebook/blenderbot-400M-distill"
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

    while True:
        # Get user input
        user_input = input("You: ")

        # Generate response
        input_ids = tokenizer(user_input, return_tensors="pt").input_ids
        response_ids = model.generate(input_ids)[0]
        response = tokenizer.decode(response_ids, skip_special_tokens=True)

        # Print response
        print(f"Bot: {response}")

        # Check for exit command
        if user_input.lower() == "exit":
            break
chatbot()

