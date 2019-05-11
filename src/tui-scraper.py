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

def getHotelStars(offer):
    stars = -1
    if offer.find("i", class_="stars-small stars-3"):
        stars = 3
    if offer.find("i", class_="stars-small stars-4"):
        stars = 4
    if offer.find("i", class_="stars-small stars-5"):
        stars = 5
    return stars

def getOffers(departureDate, peopleCount):
    url = getURL(departureDate, peopleCount, 1)
    request = requests.get(url)
    soup = bs(request.content, "html.parser")
    offers = []


    for offer in soup.findAll("section", class_=OFFER_CSS):
        hotelInfo = {}
        price = offer.find("span", class_="pb-hp-onepreson").contents[0]
        hotelInfo["hotelName"] = offer.find("span", {"itemprop" : "name"}).text
        hotelInfo["pricePerPerson"] = int(price[:-3].replace(" ", ""))
        hotelInfo["offerUrl"] = offer.find("a", class_="oi-h-link")["href"]
        hotelInfo["hotelStars"] = getHotelStars(offer)
        offers.append(hotelInfo)

    return offers



offers = getOffers("12.05.2019", 2)
print(offers)
