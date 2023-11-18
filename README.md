
# Chat-GPT Bridge

**Server Side**

In the folder.
Build the docker container : 
```
sudo docker build -t chat_gpt_bridge .
```

Run the docker container :
```
sudo docker run -p 5000:5000 chat_gpt_bridge
```

Then use port-forwarding to expose the app.


**Client Side (python)**

Test the app :
```py
import requests

# Replace this URL with the public IP or domain of your Flask app
url = "http://YOUR IP:YOUR PORT/test"

# Specify the query parameter 'prompt'
params = {'prompt': 'Your query goes here'}

# Make a GET request to the /test endpoint with the specified parameters
response = requests.get(url, params=params)

# Print the response from the server
print(response.text)
```

Use Chat-GPT :
```py
import requests

# Replace this URL with the public IP or domain of your Flask app
url = "http://YOUR IP:YOUR PORT/gpt"

# Specify the query parameter 'prompt'
params = {'prompt': 'Your query goes here'}

# Make a GET request to the /test endpoint with the specified parameters
response = requests.get(url, params=params)

# Print the response from the server
print(response.text)
```

**Client Side (Linux)**

*These commands can be used in python too thanks to the os module*

Test the app :
```
prompt="Your query goes here"
```

```
curl -X GET "http://YOUR_IP:YOUR_PORT/test" -G --data-urlencode "prompt=$prompt"
```

Use Chat-GPT :
```
prompt="Your query goes here"
```

```
curl -X GET "http://YOUR_IP:YOUR_PORT/gpt" -G --data-urlencode "prompt=$prompt"
```
