This repository contains a Python script that parses and validates phone numbers, retrieves location descriptions, carrier information, timezones, and displays the exact location on a map. Additionally, it uses the Pipl API to find social media accounts associated with the phone number.

## Requirements

- Python 3.x
- `phonenumbers` library
- `geopy` library
- `requests` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/karimtz999/findphone_numbers.git
cd findphone_numbers
```

2. Install the required libraries:

```sh
pip install phonenumbers geopy requests
```

## Usage

1. Open the `main.py` file and replace `"YOUR_PIPL_API_KEY"` with your actual Pipl API key.

2. Run the script:

```sh
python main.py
```

3. Enter a phone number when prompted. The script will display the following information:
   - Phone number
   - Location description
   - Carrier information
   - Timezones
   - Latitude and longitude
   - Google Maps URL
   - Social media accounts associated with the phone number (if available)

## Example

```sh
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Enter phone number: +212694774260
+212694774260
Morocco
Carrier: Maroc Telecom
Timezones: Africa/Casablanca
Latitude: 31.791702, Longitude: -7.09262
Google Maps URL: https://www.google.com/maps?q=31.791702,-7.09262
Social Media Accounts:
 - https://www.facebook.com/example
 - https://www.twitter.com/example
```
