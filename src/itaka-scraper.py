import requests
from bs4 import BeautifulSoup as bs

OFFER_CSS = "offer_column offer_column-second col-sm-7 col-lg-8 clearfix"


def getURL(**kwargs):
    settings = {
        'departureDate': '2019-05-11',
        'peopleCount': 5
    }

    settings.update(kwargs)
    resultURL = ("https://www.itaka.pl/last-minute/?view=offerList&" +
                 "package-type=wczasy&adults=" + str(settings["peopleCount"]) +
                 "&date-from=" + settings["departureDate"] +
                 "&food=allInclusive&dep-region=warszawa-modlin%2Cwarszawa&" +
                 "promo=lastMinute&order=priceAsc&total-price=0&page=1&" +
                 "transport=flight&currency=PLN")
    return resultURL


def getGeoInfo(pageInfo):
    geoInfo = {}
    cutParts = pageInfo.split(" / ")
    geoInfo["country"] = cutParts[0]
    geoInfo["city"] = cutParts[-1]
    return geoInfo

def getHotelStars(offer):
    stars = -1
    if offer.find("span", class_="header_stars header_stars-30"):
        stars = 3
    if offer.find("span", class_="header_stars header_stars-35"):
        stars = 3.5
    if offer.find("span", class_="header_stars header_stars-40"):
        stars = 4
    if offer.find("span", class_="header_stars header_stars-45"):
        stars = 4.5
    if offer.find("span", class_="header_stars header_stars-50"):
        stars = 5
    return stars


if __name__ == '__main__':
    url = getURL()
    request = requests.get(url)
    soup = bs(request.content, "html.parser")

    for offer in soup.findAll("div", class_=OFFER_CSS):
        hotelInfo = {}
        hotelLocalization = offer.find("div", class_="header_geo-labels").text
        price = offer.find("span",
                           class_="current-price_value").text.replace(" ", "")
        hotelInfo.update(getGeoInfo(hotelLocalization))
        offerUrl = offer.find("header",
                              class_="offer_header").findAll("a")[0]["href"]
        hotelInfo["hotelName"] = offer.find("h2", class_="header_title").text
        hotelInfo["pricePerPerson"] = int(price)
        hotelInfo["offerUrl"] = ("https://www.itaka.pl" + offerUrl)
        hotelInfo["hotelStars"] = getHotelStars(offer)
        print(hotelInfo)

    if offer.find("span", class_="header_stars header_stars-40"):
        stars = 4
