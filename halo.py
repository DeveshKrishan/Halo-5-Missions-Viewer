#Program created by Devesh Krishan
#Note that the HALO API has the limit of 10 requests per 10 seconds.

import http.client, urllib.request, urllib.parse, urllib.error, json

def main() -> None:
    '''Converts bytes file to json and return its.'''
    key = 'FILL OUT WITH YOUR KEY'
    data = json.loads(extract_data(key))
    return data

def extract_data(key: str) -> bytes:
    '''Grabs data from HALO API and decodes and returns it.
    The parameter "key" is the authentication key.'''
    #Need to have valid key and registered user for 343 Industries Developers.
    #Visit https://developer.haloapi.com/docs/services/
    headers = {
        'Accept-Language': 'en',
        'Ocp-Apim-Subscription-Key': key,
    }
    params = urllib.parse.urlencode({})
    try:
        conn = http.client.HTTPSConnection('www.haloapi.com')
        conn.request("GET", "/metadata/h5/metadata/campaign-missions?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return data.decode()
    except Exception as e: print("[Errno {0}] {1}".format(e.errno, e.strerror))
    finally: conn.close()

def get_data(data: dict) -> list[str]:
    '''Grabs the data and returns a list of strings that has mission's name, description, and number.'''
    mission_info = list()
    for mission_data in data:
        missNum = mission_data['missionNumber']
        missName = mission_data['name']
        missDesc = mission_data['description']
        mission_info.append(f'Mission {missNum} is {missName} where {missDesc}')
    return mission_info

if __name__ == "__main__":
    main()
