import requests
from requests import JSONDecodeError
from pprint import pprint
def download_json() -> dict[any]:
    aqi_url = "https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON"
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("Invalid Connection")
    else:
        if response.status_code == 200:
            try:
                all_data:dict[any] = response.json()
                return all_data
            except JSONDecodeError:
                raise Exception("This api_key is for testing and you have exceeded max retries. Try again later.")
        else:
            raise Exception("Download Failed")
def main():
    try:
        all_data:dict[any] = download_json()
        pprint(all_data['records'])
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
