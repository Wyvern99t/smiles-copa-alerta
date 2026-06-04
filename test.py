import requests

url = "https://api-air-flightsearch-green.smiles.com.ar/v1/airlines/search?adults=1&cabinType=all&children=0&currencyCode=ARS&departureDate=2027-04-10&destinationAirportCode=PUJ&infants=0&isFlexibleDateChecked=false&originAirportCode=BUE&returnDate=2027-04-18&tripType=1&forceCongener=false&r=ar"

headers = {
    "authorization": "PEGA_AQUI_TU_BEARER",
    "x-api-key": "PEGA_AQUI_TU_API_KEY",
    "channel": "Web",
    "language": "es-ES",
    "region": "ARGENTINA",
    "origin": "https://www.smiles.com.ar",
    "referer": "https://www.smiles.com.ar/",
    "user-agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=30)

print("STATUS:", r.status_code)
print("TIPO:", r.headers.get("content-type"))
print(r.text[:2000])
