import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "any url"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
ACCEPT_LANG = "en"
MY_EMAIl = "testermandem@gmail.com"
PASSWORD = "xvfr luek hgmz esdj"

response = requests.get(URL, headers={"User-Agent":USER_AGENT,
                                      "Accept-Language":ACCEPT_LANG})
soup = BeautifulSoup(response.text, 'lxml')

price = float(soup.select_one(".a-price span").getText().replace("$", ""))
product_name = soup.select_one("#title span").getText()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIl, password=PASSWORD)
    if price < 200:
        connection.sendmail(from_addr=MY_EMAIl,
                            to_addrs=MY_EMAIl,
                            msg=f"Subject: Amazon Price Alert!\n\n{product_name} is now {price}!".encode("utf8"))