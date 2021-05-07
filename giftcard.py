import requests
import time
from msgbot import email_alert

def main():
    # message to check for when determining if gift cards are in stock
    status = 'gift cards are out of stock'
    # webpage url to check for gift cards
    webpage = 'https://www.walmart.com/ip/Subway-Multi-Pack-30-Gift-Card/180076122'

    # while loop that checks every gift card availability every minute
    while True:
        page = requests.get(webpage)
        if status not in page.text:
            break
        time.sleep(60)

    # alert message to send user once gift cards are in stock
    # subject header for the email
    subject = 'Cards are in stock'
    # email body to send user
    body = '**********************************\n' +
        '*********ITEM IS IN STOCK*********\n'
        + '**********************************'
    # user's email address; sample email address to be replaced with user's real email address
    recipient = 'somebody@gmail.com'
    # send email
    email_alert(subject, body, recipient)

if __name__ == "__main__":
    main()