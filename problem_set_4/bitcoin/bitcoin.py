import sys
import requests


with open("API.txt" ,"r") as file:
    API_KEY = file.read()

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=' + API_KEY)
    except requests.RequestException:
        print(requests.RequestException)

    p = response.json()
    result = p["data"]
    price = float(result["priceUsd"]) * bitcoin

    print(f"${price:,.4f}")

