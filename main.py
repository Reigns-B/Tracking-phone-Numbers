import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import os

# Taking input of the phone number along with the country code
number = input("Enter the PhoneNumber with the country code: ")

# Parsing the phone number string to convert it into phone number format
phoneNumber = phonenumbers.parse(number)

# Storing the API Key securely using environment variables
# You can set your API key in your environment or replace 'OPENCAGE_API_KEY' with your API key directly
Key = os.getenv('OPENCAGE_API_KEY', 'Your-Api-Key-Here')

if Key == 'Your-Api-Key-Here':
    print("Please set your API key in the code or environment variable.")
else:
    # Using the geocoder module of phonenumbers to print the location in console
    yourLocation = geocoder.description_for_number(phoneNumber, "en")
    print("Location: " + yourLocation)

    # Using the carrier module of phonenumbers to print the service provider name in console
    yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
    print("Service Provider: " + yourServiceProvider)

    # Using OpenCage to get the latitude and longitude of the location
    geocoder = OpenCageGeocode(Key)
    query = str(yourLocation)
    results = geocoder.geocode(query)

    if results:
        # Assigning the latitude and longitude values to the lat and lng variables
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        # Getting the map for the given latitude and longitude
        myMap = folium.Map(location=[lat, lng], zoom_start=9)

        # Adding a marker on the map to show the location name
        folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

        # Save map to HTML file to open it and see the actual location in map format
        myMap.save("Location.html")
        print("Map has been saved as 'Location.html'")
    else:
        print("Location could not be geocoded.")
