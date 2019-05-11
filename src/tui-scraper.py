import requests
import codecs
from bs4 import BeautifulSoup as bs

OFFER_CSS = "offer-item offer-item-with-slider"


def getURL(departureDate, peopleCount, pageIndex):
    """
    departureDate must be formatted like 11.05.2019
    """

    resultURL = ("https://www.travelplanet.pl/wczasy/super-last-minute/" +
                 str(pageIndex) + "/?wylot=" + departureDate +
                 "&przylot=02.06.2019&osoby=" + str(peopleCount) +
                 "&czas=6:8&lotnisko=Warszawa,Warszawa%20-%20Modlin&" +
                 "wyzywienie=1&ocena=3&dojazd=F&sortowanie=1&" +
                 "kolejnosc=up&limit=25")
    return resultURL

def getOffers(departureDate, peopleCount):
    url = getURL(departureDate, peopleCount, 1)
    request = requests.get(url)
    soup = bs(request.content, "html.parser")
    print(url)


    for offer in soup.findAll("section", class_ = OFFER_CSS):
        print(offer.find("span", {"itemprop" : "name"}).text)



getOffers("12.05.2019", 2)
