import os
import phonenumbers
from phonenumbers import geocoder as region_lookup, carrier
import folium
from opencage.geocoder import OpenCageGeocode


def get_number_info(raw_number: str):
    """Parse and validate the phone number. Returns a PhoneNumber object or None."""
    try:
        parsed = phonenumbers.parse(raw_number, None)
    except phonenumbers.NumberParseException as e:
        print(f"Could not parse number: {e}")
        return None

    if not phonenumbers.is_valid_number(parsed):
        print("That doesn't look like a valid phone number.")
        return None

    return parsed


def main():
    raw_number = input("Enter the phone number with country code (e.g. +14155552671): ").strip()

    phone_obj = get_number_info(raw_number)
    if phone_obj is None:
        return

    # Region-level description (NOT precise location, NOT real-time)
    region = region_lookup.description_for_number(phone_obj, "en")
    if not region:
        print("No region information available for this number.")
        return
    print("Region (approximate, based on area code): " + region)

    # Original carrier the number block was assigned to (may be outdated if ported)
    service_provider = carrier.name_for_number(phone_obj, "en")
    print("Carrier on record: " + (service_provider or "Unknown"))

    api_key = os.getenv("OPENCAGE_API_KEY", "Your-Api-Key-Here")
    if api_key == "Your-Api-Key-Here":
        print("\nSet OPENCAGE_API_KEY as an environment variable to also plot this region on a map.")
        return

    og_geocoder = OpenCageGeocode(api_key)
    results = og_geocoder.geocode(str(region))

    if not results:
        print("Region could not be geocoded to map coordinates.")
        return

    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    my_map = folium.Map(location=[lat, lng], zoom_start=7)
    folium.Marker(
        [lat, lng],
        popup=region,
        tooltip="Approximate region only — not the phone's actual location",
    ).add_to(my_map)
    my_map.save("Location.html")
    print("\nMap of the approximate region saved as 'Location.html'.")
    print("Reminder: this pin marks the region tied to the number's area code, not the phone itself.")


if __name__ == "__main__":
    main()
