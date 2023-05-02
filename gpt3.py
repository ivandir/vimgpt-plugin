import openai
import sys
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

def query_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = sys.argv[1]
    result = query_gpt3(prompt)
    print(result)
