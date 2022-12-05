import requests
import json 



def get_quote():
    url = "https://api.chucknorris.io/jokes/random"
    res = requests.request("GET", url)
    data = json.loads(res.text)
    jso = (json.dumps(data, indent=4))
    jso = json.loads(jso)
    quote = (jso['value'])
    return quote

