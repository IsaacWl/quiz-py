import requests

PARAMS = {
    "amount": 10,
    "type": "boolean"
}

URL = "https://opentdb.com/api.php"

response = requests.get(URL, params=PARAMS)
response.raise_for_status()

question_data = response.json()["results"]
