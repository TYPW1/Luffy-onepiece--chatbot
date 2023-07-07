import openai
import os

# Set up the OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt for the chatbot
prompt = "Hello, how can I help you today?"

# Loop to receive and respond to user input
while True:
    # Get user input
    user_input = input("User: ")
    
    # Add the user input to the prompt
    prompt += f"\nUser: {user_input}\nChatGPT:"

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=50
    )

    # Extract the response text from the OpenAI API response
    bot_message = response.choices[0].text.strip()

    # Print the response to the terminal
    print(f"ChatGPT: {bot_message}")

    # Add the bot message to the prompt
    prompt += f" {bot_message}\n"
