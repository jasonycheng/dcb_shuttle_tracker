import urllib3
from requests import requests
from bs4 import BeautifulSoup
import json


def main():
    link = 'https://api.syncromatics.com/portal/stops/6693507/arrivals?count=5&routeId=3354&api-key=302ab81bc3e3f2058b355c3ef29ec2402608e358f303e429c81e01d9ad65d6e0'
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html5lib')
    response = json.loads(soup.text)
    try:
        if (response[0]['secondsToArrival']) > 3600:
            print ("No bus arrivals in the next hour.")
            result = "No bus arrivals in the next hour."
        else:
            mybus = response[0]['pattern']['name'] + ' - Minutes to Arrival: ' + str(round(response[0]['secondsToArrival'] / 60,0))
            print (mybus)
            result = mybus
    except:
        print("There are no more bus arrivals today.")
        result = "There are no more bus arrivals today."

    return result



if __name__ == '__main__':
	main()
