from flask import Flask, request
import openai

# to get an API key, login to your open-ai account and go to https://platform.openai.com/account/api-keys
openai.api_key = "" # put your API key here
openai.Model.list()


app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_data():
    """
    Returns the prompt that was sent to the server

    args:
        prompt: the query to returned
    """
    prompt = request.args.get('prompt')

    return "Prompt: " + prompt


# you need an API key to use this endpoint
@app.route('/gpt', methods=['GET'])
def get_data():
    """
    Transfer the query to the model and return the response

    args:
        prompt: the query to be transfered to the model
    """
    # note : you can add a to the prompt to give the model some context
    prompt = request.args.get('prompt')

    completions = openai.Completion.create(
        model="gpt-3.5-turbo", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    
    return completions.choices[0].text.strip()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
