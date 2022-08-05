from twilio.rest import Client

account_sid = ''
auth_token = ''

SENDER_NR = ''
RECEIVER_NR = ''


class NotificationManager:

    def notify(self, message_body):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=message_body,
                from_=SENDER_NR,
                to=RECEIVER_NR,
        )
        if message.status == "queued":
            print("Notification queued")