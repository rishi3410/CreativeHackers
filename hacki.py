import requests
from bs4 import BeautifulSoup as BS
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


URL = "https://www.amazon.in/HP-15-6-inches-Micro-Edge-Anti-Glare-15s-eq2182AU/dp/B0B4N77Y34/ref=sr_1_5?crid=1LAZAJQGDWIT5&dib=eyJ2IjoiMSJ9.yBLtX5CW_7yJp0ypl9Iztx-5MHiq8_ssLZeAwFgl4HoTEUa7x8Votqx3CQR2OZEmCCQ2Y6nvA0nqQ64mKduK5fovM-IuoOhHLD0f2CNRtSsVVOGOVPJ-qz1WGlG_ORqnYuLViI-TTA3RB3kHOgE4xHWTmlDdPv2KDjB4yJ7Z-6RrJRzVR5tMGgYUFVW2SJJhHrpO0rUXiGEJKmgsywEWPBffTVNHgcGapWddPfSouPs.QJ7T8M-JwK-wFhwxdEhHibCHk-QaR8Gu3ghnXcEsJmI&dib_tag=se&keywords=laptop&qid=1725046138&sprefix=laptop%2Caps%2C364&sr=8-5&th=1"
def extract():
    
   page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"})
   soup = BS(page.content, "html.parser")
   price = float(soup.find(class_="a-price-whole").text.replace(",",""))
   return price
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL = "rishivarun2004@gmail.com"
PASSWORD = "trhk wxdm hrbo jlzp"

def notify():
    server = SMTP(SMTP_SERVER, PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    subject = "BUY NOW"
    body = "Price has fallen. Buy it now." + URL
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(EMAIL, EMAIL, msg)  
    server.quit()

AFFORDABLE_PRICE = 42000
if extract() <= AFFORDABLE_PRICE:
    notify()