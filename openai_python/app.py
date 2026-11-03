from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

while True:
    question = input("User: ")

    if (question != "bye"):
        response = client.chat.completions.create(
            model="gpt-5.6-terra",
            messages=[{"role": "user", "content": question}],
            max_completion_tokens=50,
            n=1
        )

        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    else:
        print("AI: Bye...")
        break