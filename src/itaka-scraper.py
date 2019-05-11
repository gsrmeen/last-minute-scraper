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
    "&date-from=" + settings["departureDate"] + "&food=allInclusive&" +
    "dep-region=warszawa-modlin%2Cwarszawa&promo=lastMinute&order=priceAsc&" +
    "total-price=0&page=1&currency=PLN")
    return resultURL


if __name__ == '__main__':
    url = getURL()
    request = requests.get(url)
    soup = bs(request.content, "html.parser")

    for offer in soup.findAll("div", class_=OFFER_CSS):
        hotelInfo = {}
        hotelInfo["hotelName"] = offer.find("h2", class_="header_title").text
        hotelInfo["local"] = offer.find("div", class_="header_geo-labels").text
        print(hotelInfo)
