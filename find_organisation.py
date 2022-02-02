import requests


def find_organisation(long, lat, delta1, delta2):
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

    org = json_response["features"][0]
    org_name = org["properties"]["CompanyMetaData"]["name"]
    org_address = org["properties"]["CompanyMetaData"]["address"]

    point = org["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    delta = "0.005"

    map_params = {
        "l": "map",
        "pt": "{0},pm2dgl~{1},pm2dgl".format(org_point, f"{long},{lat}")
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=map_params)