from openai import OpenAI
from dotenv import load_dotenv
import os


# Load the .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")


# Create the OpenAI client using the loaded API key
client = OpenAI(api_key=api_key)

# Your function for getting responses from GPT-4o-mini
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=1.5,
    )
    response = completion.choices[0].message.content
    #response = completion.choices[0].message['content']
    return response

def print_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=1.5,
    )
    # Print the response instead of returning it
    print(completion.choices[0].message.content)

# Test the function
#response = get_llm_response("Why is Python so popular?")
#print(response)
