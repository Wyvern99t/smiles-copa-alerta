import requests

url = "https://www.smiles.com.ar/emission?originAirportCode=BUE&destinationAirportCode=PUJ&departureDate=2027-04-10&adults=1&children=0&infants=0&isFlexibleDateChecked=false&tripType=1&cabinType=economic&currencyCode=ARS&returnDate=2027-04-18"

r = requests.get(url, timeout=30)

print("Status:", r.status_code)
print("Longitud HTML:", len(r.text))
print(r.text[:500])
