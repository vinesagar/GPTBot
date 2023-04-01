import os
import openai
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv("OPENAI_API_KEY"))

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(model="text-davinci-003", prompt="", temperature=0.6, max_tokens=1)
messages = [
        {"role": "system", "content": "Your name is John."},
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": "Be precise in answers."},
        {"role": "system", "content": "analyse https://www.expertmarketresearch.com/reports/aluminium-cans-market."},
        {"role": "system", "content": "The global aluminium cans market attained a value of USD 48.16 billion in 2022 and expected to grow at a CAGR of 3.2% in the forecast period of 2023-2028.  "},
        {"role": "system", "content": "Competitors and key players are synonymous"},
        {"role": "system", "content": "current value is market value in recent year"},
        {"role": "system", "content": "often informing that this is only an overview."},
        {"role": "system", "content": "often informing that Complete and more Elaborate details are in full report."},
        {"role": "system", "content": "often remind full report contains more in-depth information."},
    ]

while True:
    user_inp = input("You: ")
    messages.append({'role': 'user', 'content': user_inp})

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    )
    # print(response) 
    # print(response['choices'][0]['message']) 
    messages.append(response['choices'][0]['message'])
    print(f"""Assistant: {response["choices"][0]["message"]['content']}""")