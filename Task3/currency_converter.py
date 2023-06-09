import requests
from pprint import pprint


# Open Exchange Rate API used to get the latest currency exchange rates 

API_ID="b0f1664ef91a4dc2a658e133ac0f876d" 
BASE_URL="https://openexchangerates.org/api"


parameters={

    "app_id":API_ID
}


response=requests.get(url=f"{BASE_URL}/latest.json",params=parameters)
data=response.json()

currency_exchange_rates=(data["rates"])


currencies = []
for currency in currency_exchange_rates.keys():
    currencies.append(currency)

print("\n Available currencies : \n"  )
pprint(currencies, depth=1, width=60, compact=True)

print("\n----------------------------------------------------------------------------\n")

CONVERT=True

while CONVERT:

    from_currency=input("Enter the base currency: ").upper()
    to_currency=input("Enter the target currency: ").upper()

    print("\n")

    amount=float(input("Enter the amount to be converted : " ))

    converted_amount= (amount/currency_exchange_rates[from_currency]) * currency_exchange_rates[to_currency]

    print(f"{amount} {from_currency} = {converted_amount} {to_currency}\n")

    choice=input("Convert another amount(Yes/No): ").lower()

    if(choice =="no"):
        
        print("\n**************  Thank You for using my Currency Converter!  **************")
        CONVERT=False

    print("\n----------------------------------------------------------------------------\n")


