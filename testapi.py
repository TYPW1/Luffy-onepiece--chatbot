import os
import openai

if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    print(os.getenv("OPENAI_API_KEY"))
    print("OPENAI_API_KEY environment variable is not set.")
    #print(os.environ)