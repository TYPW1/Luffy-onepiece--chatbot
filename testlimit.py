import requests
import time

# Replace with your Flask app's URL
url = "http://127.0.0.1:5000/ask"

data = {
    'user_input': 'Hello',
    'conversation_history': 'User: Hello\nAI: Hi there!'
}

# Adjust the number of requests as needed
num_requests = 10

for i in range(num_requests):
    response = requests.post(url, data=data)
    print(f"Request {i + 1}: {response.status_code} - {response.text}")
    time.sleep(0.5)  # Adjust the delay between requests if necessary
