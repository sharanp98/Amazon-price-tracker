import requests
from bs4 import BeautifulSoup
import smtplib
import time
import argparse

def check_price(email,password,email_to,URL,reqd_price):
    original_URL = URL
    URL = requests.get(URL)
    soup = BeautifulSoup(URL.content,'html.parser')
    actual_price = soup.find(id='priceblock_ourprice').get_text()
    actual_price,_ = actual_price[2:].split('.')
    actual_price = int(actual_price.replace(',',''))

    if reqd_price <= actual_price :
        send_mail(email,password,email_to,original_URL)

def send_mail(email,password,email_to,URL):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email,password)

    subject = 'Price Fell Down!'
    body = 'Check the link:' + str(URL)
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        email, #FROM
        email_to, #TO
        msg
    )
    print('SUCCESS')


parser = argparse.ArgumentParser(description='Check Amazon prices!')
parser.add_argument("--email",required=True,type=str, help="Your gmail id")
parser.add_argument("--password", required=True, type=str, help="Your Password")
parser.add_argument("--email_to", required=True, type=str, help="Email of receiver")
parser.add_argument("--url", required=True, type=str, help="URL of amazon website")
parser.add_argument("--price", required=True, type=int, help="Price drop")


args = parser.parse_args()

while True:
    check_price(args.email,args.password,args.email_to,args.url,args.price)
    time.sleep(60*60)
