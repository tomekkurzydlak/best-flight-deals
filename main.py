from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIG_CITY_IATA = "WAW"

data_manager = DataManager()
sheet_iata = data_manager.get_city()

flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_iata[0]["iataCode"] == "":
    for entry in sheet_iata:
        iata_code = flight_search.get_iata_code(entry["city"])
        entry["iataCode"] = iata_code
    data_manager.destination_data = sheet_iata
    data_manager.save_iata()

for entry in sheet_iata:
    flight = flight_search.get_flight_data(ORIG_CITY_IATA, entry["iataCode"])
    try:
        if flight is not None and flight.price < entry["lowestPrice"]:
            message_ready_to_send = f"Lowest price alert! Only €{flight.price} to fly from {flight.orig_city}-{flight.orig_airport}" \
                                    f" to {flight.dest_city}-{flight.dest_airport}, from {flight.out_date} to {flight.return_date}"
            notification_manager.notify(
                message_body=message_ready_to_send
            )
            data_manager.fetch_club_members()
            for row in data_manager.club_members["users"]:
                club_member = row["firstName"]
                email_member = row["email"]
                message_body = f"{message_ready_to_send}\n\nBook this flight in one click going to link:\n {flight.link}"
                notification_manager.send_email(message_body, club_member, email_member)

    except AttributeError:
        pass







