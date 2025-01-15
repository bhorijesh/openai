from openai import OpenAI
import os
from decouple import config 

api_key = config("OPENAI_API_KEY") 

client = OpenAI(api_key=api_key)
messages = [
    {'role':'system',"content": "you are kind helpful assistant"},
]

while True:
    message = input('User:')
    if message:
        messages.append(
            {"role":"user","content":message},
        )
        chat = client.chat.completions.create(
            model = 'gpt-4o-mini' , messages = messages
        )
    reply = chat.choices[0].message.content
    print(f'ChatGpt: {reply}')
    messages.append({"role":"assistant","content": reply})