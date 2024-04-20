import phonenumbers
import requests

def parse_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            return None
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

def gather_social_media_info(phone_number):
    # You would need to replace these URLs with the actual social media APIs
    facebook_url = f"https://graph.facebook.com/v12.0/{phone_number}"
    instagram_url = f"https://www.instagram.com/{phone_number}/?__a=1"

    response = {}
    try:
        facebook_response = requests.get(facebook_url)
        if facebook_response.status_code == 200:
            response['facebook'] = facebook_response.json()

        instagram_response = requests.get(instagram_url)
        if instagram_response.status_code == 200:
            response['instagram'] = instagram_response.json()
    except requests.exceptions.RequestException:
        pass

    return response

if __name__ == "__main__":
    phone_number = "+15555555555"  # Replace with the phone number you want to lookup
    parsed_number = parse_phone_number(phone_number)
    if parsed_number:
        social_media_info = gather_social_media_info(parsed_number)
        print(social_media_info)
    else:
        print("Invalid phone number.")
