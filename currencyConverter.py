import requests 
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")



currency = input("Enter the currency you want to convert from [ex: BRL]: ").upper()
amount = float(input("Enter the amount: "))
toCurrency = input("Enter the currency you want to convert to [ex: USD]: ").upper()

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency}"


response = requests.get(url)
data = response.json()

if response.status_code != 200 or data['result'] != 'success': 
    print("Error fetching api request")
else:
    try:
        rate = data['conversion_rates'][toCurrency]
        convertedAmount = amount * rate
        print(f"{amount:.2f} {currency} = {convertedAmount:.2f} {toCurrency}")
    except KeyError:
        print(f"Currency '{toCurrency}' not found.")
        

