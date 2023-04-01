from fastapi import FastAPI
import os
import openai
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


class Details(BaseModel):
    report_description_url: str
    messages: list[dict[str, str]]


@app.get("/")
def root():
    return {'hello': "world"}

@app.post("/v1/assistants/response")
def assistant_response(details: Details):
    # https://www.expertmarketresearch.com/reports/detergent-grade-enzymes-market-asia-pacific

    rd_url = details.report_description_url
    messages = details.messages

    system_messages = [
        {"role": "system", "content": "You are a John."},
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": "Be precise in answers."},
        {"role": "system", "content": f"Analyse {rd_url}"},
        {"role": "system", "content": "Competitors and key players are synonymous"},
        {"role": "system", "content": "often informing that this is only an overview."},
        {"role": "system", "content": "often informing that Complete and more Elaborate details are in full report."},
        {"role": "system", "content": "often remind full report contains more in-depth information."},
    ]
    messages = system_messages + messages
    response = openai.ChatCompletion.create( 
    model="gpt-3.5-turbo",
    messages=messages,
    )

    return {
        "status": "201",
        "response": {
            "role": "assistant",
            "content": response.choices[0].message.content, # type: ignore
        }
    }
