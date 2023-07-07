import openai
import os
from flask import Flask, request

# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the Flask app
app = Flask(__name__)

# Define the initial prompt for the chatbot
prompt = "Hello, how can I help you today?"

# Define a route to serve the chatbot webpage
@app.route('/')
def chatbot_page():
    return '''
        <html>
            <body>
                <h1>Welcome to the chatbot!</h1>
                <form method="POST" action="/chatbot">
                    <label for="message">Enter your message:</label><br>
                    <input type="text" id="message" name="message"><br>
                    <input type="submit" value="Send">
                </form>
            </body>
        </html>
    '''

# Define a route to receive user input and generate a response
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from the request body
    user_input = request.form['message']

    # Add the user input to the prompt
    global prompt
    prompt += f"\nUser: {user_input}\nChatbot:"

    # Generate a response based on the prompt using the OpenAI API
    response = generate_response(prompt)

    # Add the response to the prompt
    prompt += f" {response}\n"

    # Return the response to the client
    return '''
        <html>
            <body>
                <h1>Chatbot response:</h1>
                <p>{}</p>
                <a href="/">Return to chat</a>
            </body>
        </html>
    '''.format(response)

def generate_response(prompt):
    # Generate a response using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extract the generated response from the OpenAI API response
    response_text = response.choices[0].text.strip()

    return response_text

if __name__ == '__main__':
    # Run the Flask app
    app.run()
