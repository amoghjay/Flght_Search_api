import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "PacxmK06XhSn-EKJsiqWxpv2vU6WMUvp"


class FlightSearch:

    def get_destination_code(self, city_name):
        loc = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {"term": city_name,
                 "location_types": "city"}
        res = requests.get(url=loc, headers=headers, params=query)
        print(res)
        answers = res.json()["locations"]
        code = answers[0]["code"]
        return code
