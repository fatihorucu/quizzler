import requests as rq

parameters = {
    "type": "boolean",
    "amount": 10,
    "difficulty": "medium"
}
response = rq.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]