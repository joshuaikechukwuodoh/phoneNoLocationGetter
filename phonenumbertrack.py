import phonenumbers
from phonenumbers import geocoder

phonenumber1 = input("Enter phone number with country code: ")

try:
    # 1. Parse the phone number string into a PhoneNumber object
    phonenumber_obj = phonenumbers.parse(phonenumber1)

    # 2. Now use the PhoneNumber object with description_for_number
    description = geocoder.description_for_number(phonenumber_obj, "en")  # "en" for English

    # 3. Print the results
    print(f"Location: {description}")  # Use f-strings for cleaner output

except phonenumbers.NumberParseException as e:
    print(f"Invalid phone number: {e}")  # Handle parsing errors
except Exception as e: # Catch any other potential errors
    print(f"An error occurred: {e}")


# Example of getting carrier information (if available and you have the carrier library installed)
try:
    from phonenumbers import carrier
    carrier_name = carrier.name_for_number(phonenumber_obj, "en")
    print(f"Carrier: {carrier_name}")
except phonenumbers.NumberParseException:
    print("Carrier information not available for this number.")
except ImportError:
    print("Carrier information requires the phonenumbers carrier library. Install it using: pip install phonenumbers[carrier]")
except Exception as e:
    print(f"An error occurred while getting carrier info: {e}")