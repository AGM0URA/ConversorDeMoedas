import requests 
import os
from dotenv import load_dotenv

currency = input("Enter the currency you want to convert from: ")
amount = float(input("Enter the amount: "))
toCurrency = input("Enter the currency you want to convert to: ")

response = requests.get(f"")
