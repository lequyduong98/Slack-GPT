from flask import Blueprint, session, Flask, request
import json
import requests
import threading
import openai
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
from slack_bolt import App

OPENAI_API_KEY  = "sk-***********************"
webhook_url = "YOUR SLACK WEB HOOK"

main = Blueprint('main', __name__)

# handle message from slack and get response (text competition) from openai 
def handle_message_events(body):

    # Create prompt for ChatGPT
    prompt = str(body["event"]["text"]).split(">")[1]
    
    # Check ChatGPT
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    # print(response)
    answer = response.choices[0].text.strip()

    payload = {
        "text": str(answer)
    }
    headers = {
        "Content-type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        raise ValueError(
            f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}"
        )
    pass

# listen to slack post request (Event Subcription)
@main.route('/slack-subcriptions',methods=['POST'])
def slack_subcriptions():

    token = request.json.get('token')
    challenge = request.json.get('challenge')
    type = request.json.get('type')
    data= request.json
    print(data)

    thread = threading.Thread(target=handle_message_events, args=(data,))
    thread.start()
    if not challenge:
        return "OK"
    else: 
        return challenge