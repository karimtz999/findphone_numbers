import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim
import requests

print("x" * 50)

input_number = input("Enter phone number: ")

try:
    phone_number = phonenumbers.parse(input_number, "MA")
    if phonenumbers.is_valid_number(phone_number):
        print(f"\033[1m{input_number}\033[0m")

        # Get location description or fallback to a default message
        description = geocoder.description_for_number(phone_number, 'en') or "No description available"
        print(f"\033[1m{description}\033[0m")

        # Get carrier information or fallback
        carrier_name = carrier.name_for_number(phone_number, 'en') or "Unknown carrier"
        print(f"Carrier: \033[1m{carrier_name}\033[0m")

        # Get timezones or fallback
        timezones = timezone.time_zones_for_number(phone_number)
        if timezones:
            print(f"Timezones: \033[1m{', '.join(timezones)}\033[0m")
        else:
            print("No timezone information available.")

        # Get latitude and longitude using geopy
        geolocator = Nominatim(user_agent="phone_number_locator")
        location = geolocator.geocode(description)
        if location:
            print(f"Latitude: \033[1m{location.latitude}\033[0m, Longitude: \033[1m{location.longitude}\033[0m")
            google_maps_url = f"https://www.google.com/maps?q={location.latitude},{location.longitude}"
            print(f"Google Maps URL: \033[1m{google_maps_url}\033[0m")
        else:
            print("No location information available.")

        # Use Pipl API to find social media accounts
        api_key = "YOUR_PIPL_API_KEY"
        url = f"https://api.pipl.com/search/?phone={input_number}&key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'person' in data:
                person = data['person']
                if 'social_profiles' in person:
                    print("Social Media Accounts:")
                    for profile in person['social_profiles']:
                        print(f" - {profile['url']}")
                else:
                    print("No social media accounts found.")
            else:
                print("No person found with this phone number.")
        else:
            print(f"Error fetching social media accounts: {response.status_code}")
    else:
        print("The phone number entered is not valid.")
except phonenumbers.NumberParseException as e:
    print(f"Error parsing phone number: {e}")
