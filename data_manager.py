import requests as rq
import apikeys

SH_ID = apikeys.SH_ID
SH_KEY = apikeys.SH_KEY
SH_ENDPOINT = f"https://api.sheety.co/{SH_ID}/flightDeals/prices"
CLUB_ENDPOINT = f"https://api.sheety.co/{SH_ID}/flightDeals/users"

sh_header = {
    "Authorization": SH_KEY
}


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.club_members = {}

    def get_city(self):
        city_response = rq.get(url=SH_ENDPOINT, headers=sh_header)
        city_to_decode = city_response.json()  # ["prices"][0]["city"]
        self.destination_data = city_to_decode["prices"]
        return self.destination_data

    def save_iata(self):
        for city in self.destination_data:
            iata_body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = rq.put(url=f"{SH_ENDPOINT}/{city['id']}", json=iata_body, headers=sh_header)
            print(response.text)

    def fetch_club_members(self):
        club_response = rq.get(url=CLUB_ENDPOINT, headers=sh_header)
        self.club_members = club_response.json()
        return self.club_members
