import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
alt = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "PacxmK06XhSn-EKJsiqWxpv2vU6WMUvp"
#"PacxmK06XhSn-EKJsiqWxpv2vU6WMUvp"



def get_destination_code():
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        loc = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": "Melbourne",
                 "location_types": "city"}
        res = requests.get(url=loc, headers=headers, params=query)
        print(res.json())
        # answers = res.json()["locations"]
        # code = answers[0]["code"]
        #return code
get_destination_code()