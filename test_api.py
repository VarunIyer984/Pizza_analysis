import requests

test_data = {
    "pizza_category": "Classic",
    "pizza_size": "L",
    "unit_price": 20.0
}

url = 'http://localhost:5000/predict'

try:
    response = requests.post(url, json=test_data)

    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(response.json())

except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
    print("Is the 'python app.py' server running in the other terminal?")