import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

from openai import OpenAI
# openai.api_key = OPENAI_KEY

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

def send_to_GPT(messages, model='gpt-3.5-turbo'):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].message.content
    print (f"AI says: {message}")
    messages.append(response.choices[0].message)
    return message