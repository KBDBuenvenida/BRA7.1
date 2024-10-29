import requests

def get_public_ip_info():
    try:
        response = requests.get("https://ipapi.co/json")
        response.raise_for_status()

        data = response.json()
        
        ip = data.get("ip", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        org = data.get("org", "N/A")
        loc = data.get("loc", "N/A")

        print(f"Public IP Address         : {ip}")
        print(f"Location                  : {city}, {region}, {country}")
        print(f"Location                  : {loc}")
        print(f"Internet Service Provider : {org}")

    except requests.RequestException as e:
        print(f"Error: Failed to fetch IP information: {e}")

if __name__ == "__main__":
    get_public_ip_info()