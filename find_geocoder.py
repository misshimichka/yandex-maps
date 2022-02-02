import requests


def find_geocoder(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coords = toponym["Point"]["pos"]
    long, lat = coords.split(" ")
    bbox1 = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    bbox2 = toponym["boundedBy"]["Envelope"]["upperCorner"].split()

    delta1 = "{:.3f}".format(abs(float(bbox1[0]) - float(bbox2[0])))
    delta2 = "{:.3f}".format(abs(float(bbox1[1]) - float(bbox2[1])))
    return long, lat, delta1, delta2
