import os
import requests as rq

SH_KEY = os.environ['SH_KEY']
SH_ID = os.environ['SH_ID']

SH_ENDPOINT = f"https://api.sheety.co/{SH_ID}/flightDeals/users"

sh_header = {
    "Authorization": SH_KEY
}

welcome_message = f"Welcome to Tomek's Exclusive Flight Club\nWe find the best flight deals and email you!\n"
print(welcome_message)
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")

is_confirmed = False

while is_confirmed == False:
    email = input("What's your emai? ")
    email_confirm = input("Confirm your email: ")
    if email == email_confirm:
        is_confirmed = True
    else:
        print(f"Entered emails don't match. Please reenter.")

data_sent_ok = f"Email confirmed. We saved your data as follows:\nFirst name: {first_name}\n" \
               f"Last name: {last_name}\nEmail: {email}\nThank's for flying with us ✈️"

sending_error = "There's been an error and your data has NOT been saved. Try again later"

def save_data():
    print("Gathering data...")
    json_body = {
        "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
        }
    }
    print("Connecting...")
    response = rq.post(url=f"{SH_ENDPOINT}", json=json_body, headers=sh_header)
    # print(response.status_code)
    if response.status_code == 200:
        print(data_sent_ok)
    else:
        print(f"{sending_error}. Code {response.status_code}")

if is_confirmed == True:
    save_data()
