import requests
import json

import gradio as gr

#Ollama url for API request
url = "http://localhost:11434/api/generate" 

# Header for the http REST request
headers ={
    'Content-Type': 'application/json' 
}

def query(prompt):
    data={
        "model" : "mechbot",
        "prompt" : prompt,
        "stream" : False
    }

    # json.dumps()converts a subset of Python objects(dict) into a json string.
    res = requests.post(url,headers = headers,data=json.dumps(data) ) #HTTP Post for request
    
    # Deserialization : conversion of JSON objects into their respective Python objects. 
    # The load() method is used for it

    if res.status_code == 200:
        res= res.text # Converts response object to unicode text
        data=json.loads(res) # convert JSON object to Python dict
        finalRes = data['response']
        return finalRes
    else:
        print("error",res.text) # print the unicode text error as it is

interface =  gr.Interface(
    fn = query,
    inputs = gr.Textbox(lines=4,placeholder = "What can I help You with?"),
    outputs = "text",
    title = " MechBot : an Awesome mechanic bot",
    desc = " A mechanic in Indian town, an expert of local vehicle repair along with know how of mechanical job. Created by Sachin Sekiro."
    )

interface.launch(share=True)