
# Best Flight Deals

This program searches for cheap flights usign the Kiwi service. Compares your data from a spreadsheet like destination city name and max price. If there's a match, script sends you a text message with infos. Deals finder should be run from main.py

user_register.py is a separate program that is made to be hosted outside your enviroment. Registering by this file will add a new username and email to our spreadsheet. Next time you'll run main.py all registered users will be notified by email with best flight deals.


## Features

- Searches  Kiwi dataase for flights below defined price
- Saves the lowest prices to spreadseet prices on sheety.co
- Users registered by user_register.py are saved to users on sheety.co
- Sends emails with best deals to registered users
- Sends text messages with best deals using Twilio


## Run Locally

Clone the project

```bash
  git clone https://github.com/tomekkurzydlak/best-flight-deals.git
```

Go to the project directory

```bash
  cd best-flight-deals
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Set-up the apikeys.py

```bash
  Have account created on sheety, create google spreadsheet 
  named Flight Deals with two sheets: prices and users. Conect with sheety.co
  Create Twillio account and set-up your api keys in apikeys.py

```

Register

```bash
  run user_register.py and provide your details
```

Run main program

```bash
  run main.py
```

## Environment Variables

To run this project, you will need to create apikeys.py file and add the following variables to apikeys.py file
or use import os and add these variables to your enviroment

`my_email` - email used to send notifications

`password` - password to your email account

`SMTP_SERV` - your SMTP server

`account_sid` - Twilio SID

`auth_token` - Twilio Token

`SENDER_NR` - create your number on Twilio

`RECEIVER_NR` - your mobile phone number to receive SMS notifications

`TQ_ENDPOINT` - Kiwi endpoint

`TQ_API_KEY` - Kiwi Key

`SH_ID` - Sheety account ID

`SH_KEY` - Sheety account Key

`SH_ENDPOINT` - Sheety endpoint for reading destinations and prices

`CLUB_ENDPOINT` - Sheety endpoint for saving and reading users