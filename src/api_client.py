import requests, ipaddress

def get_location(ip):
    ipaddress.ip_address(ip)  
    url = f"https://freeipapi.com/api/json/{ip}" # si es inválida, lanza AddressValueError
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
        "country_code": data["countryCode"]
    }

if __name__ == "__main__":
    print(get_location("8.8.8.8")) 