import requests as rq
import datetime as dt
from flight_data import FlightData
import apikeys

today_day = dt.datetime.now().strftime("%d/%m/%Y")
end_day = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")


TQ_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TQ_API_KEY = apikeys.TQ_API_KEY

tq_header = {
    "apikey": TQ_API_KEY
}


class FlightSearch:

    def get_iata_code(self, city):
        query_response = rq.get(url=f"https://tequila-api.kiwi.com/locations/query?term={city}", headers=tq_header)
        iata_code = query_response.json()["locations"][0]["code"]
        return iata_code

    def get_flight_data(self, city_from, city_to):
        tq_params = {
            'fly_from': city_from,
            'fly_to': city_to,
            "date_from": today_day,
            "date_to": end_day,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 10,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        flight_response = rq.get(url=TQ_ENDPOINT, params=tq_params, headers=tq_header)

        try:
            response_data = flight_response.json()["data"][0]
        except IndexError:
            print(f"There's no flights for {city_to}")
            return flight_response.text

        flight_data = FlightData(
            price=response_data["price"],
            orig_city=response_data["route"][0]["cityFrom"],
            orig_airport=response_data["route"][0]["flyFrom"],
            dest_city=response_data["route"][0]["cityTo"],
            dest_airport=response_data["route"][0]["flyTo"],
            out_date=response_data["route"][0]["local_departure"].split("T")[0],
            return_date=response_data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.dest_city}: €{flight_data.price}")
        return flight_data
