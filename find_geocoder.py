import requests
from distance import *


def find_organisation(long, lat, delta1, delta2, n):
    search_api_server = "https://search-maps.yandex.ru/v1/"

    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": "аптека",
        "lang": "ru_RU",
        "ll": f"{long},{lat}",
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        pass

    json_response = response.json()

    points = many_organisations(json_response["features"][:n])

    org = json_response["features"][0]

    point = org["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    delta = "0.005"

    distance = lonlat_distance([float(long), float(lat)], [float(point[0]), float(point[1])])

    if len(points) == 1:
        org_name = org["properties"]["CompanyMetaData"]["name"]
        org_address = org["properties"]["CompanyMetaData"]["address"]
        org_hours = org["properties"]["CompanyMetaData"]["Hours"]["text"]
        print(org_name, org_address, org_hours, round(distance), sep='\n')

    map_params = {
        "l": "map",
        "pt": f"{long},{lat},pm2rdl~" + points,
        "z": "13"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=map_params)


def many_organisations(organisations):
    points = []
    for org in organisations:
        if "Hours" in org["properties"]["CompanyMetaData"].keys():
            if len(org["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]) == 2:
                point = org["geometry"]["coordinates"]
                org_point = "{0},{1},pm2gnm".format(point[0], point[1])
            else:
                point = org["geometry"]["coordinates"]
                org_point = "{0},{1},pm2blm".format(point[0], point[1])
        else:
            point = org["geometry"]["coordinates"]
            org_point = "{0},{1},pm2grm".format(point[0], point[1])
        points.append(org_point)
    return "~".join(points)