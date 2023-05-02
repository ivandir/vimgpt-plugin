import openai
import sys
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

def query_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Code only: " + prompt}
        ],
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = sys.argv[1]
    result = query_gpt4(prompt)
    print(result)
