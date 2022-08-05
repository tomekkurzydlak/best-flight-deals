import requests as rq

SH_ID = ""
SH_KEY = ""
SH_ENDPOINT = f"https://api.sheety.co/{SH_ID}/flightDeals/prices"

sh_header = {
    "Authorization": SH_KEY
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

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
