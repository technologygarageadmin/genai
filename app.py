import openai
from openai import OpenAI

# Set your OpenAI API key here
openai.api_key = ''

def get_gpt_response(prompt):
    print(f"`get_gpt_response` function is invoked...")
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
    ]
    )
    result = completion.choices[0].message.content
    print(result)
    return {
        'StatusCode': 200,
        'body': result
    }
    # response = openai.Completion.create(
    #     engine="text-davinci-003",  # Or use "gpt-4" if you have access
    #     prompt=prompt,
    #     max_tokens=150,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    # )
    # return response.choices[0].text.strip()

import json
def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")
    prompt = event.get('prompt')
    return get_gpt_response(prompt)
    # print("Welcome to the OpenAI GPT prompt-response program!")
    # while True:
    #     prompt = input("Enter your prompt (or type 'exit' to quit): ")
    #     if prompt.lower() == 'exit':
    #         print("Goodbye!")
    #         break
    #     response = get_gpt_response(prompt)
    #     print("Response:", response)

if __name__ == "__main__":
    lambda_handler()