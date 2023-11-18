from flask import Flask, request
from openai import OpenAI

# to get an API key, login to your open-ai account and go to https://platform.openai.com/account/api-keys
client = OpenAI(
    api_key="My API Key", # put your API key here
)

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    """
    Returns the prompt that was sent to the server

    args:
        prompt: the query to returned
    """
    prompt = request.args.get('prompt')

    return "Prompt: " + prompt


# you need an API key to use this endpoint
@app.route('/gpt', methods=['GET'])
def gpt():
    """
    Transfer the query to the model and return the response

    args:
        prompt: the query to be transfered to the model
    """
    # note : you can add a to the prompt to give the model some context
    prompt = request.args.get('prompt')
    
    completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )
    
    return completion.choices[0].message.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
