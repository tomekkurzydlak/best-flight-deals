import twilio.base.exceptions
from twilio.rest import Client
import smtplib as smtp
import apikeys

my_email = apikeys.my_email
password = apikeys.password
SMTP_SERV = apikeys.SMTP_SERV

account_sid = apikeys.account_sid
auth_token = apikeys.auth_token

SENDER_NR = apikeys.SENDER_NR
RECEIVER_NR = apikeys.RECEIVER_NR


class NotificationManager:

    def notify(self, message_body):
        client = Client(account_sid, auth_token)
        try:
            message = client.messages \
                .create(
                    body=message_body,
                    from_=SENDER_NR,
                    to=RECEIVER_NR,
            )
        except twilio.base.exceptions.TwilioRestException as e:
            print(f"Could not send: {e}")
        else:
            if message.status == "queued":
                print("Notification queued")

    def send_email(self, message_body, club_member, email_member):
        mail_subject = f"Hi {club_member}. We've found a deal for you!"
        msg_body = f"Subject: {mail_subject}" \
                   f"\n\n{message_body}".encode('utf-8')
        with smtp.SMTP(SMTP_SERV, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email_member, msg=msg_body)
        print(f"Email to {club_member}: {email_member} has been sent")