import requests

#some comment

class CurrencyConverter:
    
    #Initializes the currency converter class with an API key and the base Currency 
    def __init__(self, api_key = "5993833351b547ccab9f25e1492ec155"):
        self.api_key = api_key
        self.api_url = f"https://openexchangerates.org/api/latest.json?app_id={self.api_key}"
        self.rates = None

    def get_exchange_rates(self):
        
        #Get the latest exchange rates
        #Returns an exception if API request fails or returns an error

        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                self.rates = data.get('rates')
                print("Exchange rates successfully updated.")
            else:
                raise Exception("Error:" + response.status_code)
            
        except requests.RequestException as e:
            raise Exception("Error: "+ e)

    def convert(self, amount, from_currency, to_currency):
        
        #Converts an amount from one currency to another.
        
        if self.rates is None:
            self.get_exchange_rates()
        
        from_rate = self.rates.get(from_currency)
        to_rate = self.rates.get(to_currency)
        
        if from_rate is None or to_rate is None:
            raise ValueError("Error: One or more of the currencies are unsupported")

        amount_in_base_currency = amount / from_rate
        converted_amount = amount_in_base_currency * to_rate

        return round(converted_amount, 2)



converter = CurrencyConverter()
amount = 100
from_currency = "CAD"
to_currency = "EUR"
converted_amount = converter.convert(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

converted_amount = converter.convert(amount, from_currency, to_currency)

