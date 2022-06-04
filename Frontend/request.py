# importing the requests library
import requests
#import pandas as pd

# api-endpoint
URL = "https://epita-2022-dsp-api.herokuapp.com"

def tempPostRequest(selected_file):
    endPoint = URL + '/predict'
    files = {'csv_file':selected_file.getvalue()}
    r =  requests.post(url=endPoint, files=files)
    if( r.status_code == 200):
        return r.json()
    else:
        print('Error During Query: tempPostRequest()')
        print(r)
        return r.status_code

# send json object
def postJsonRequest(json):
    #TODO: update when endpoint is available
    endPoint = URL + '/'
    data = {
        'powerPS': json['powerPS']['0'], 
        'vehicleType': json['vehicleType']['0'], 
        'brand': json['brand']['0'], 
        'fuelType': json['fuelType']['0'], 
        'kilometer': json['kilometer']['0']
        }
    r =  requests.post(url=endPoint, data=data)
    if( r.status_code == 200):
        return r.json()['result']
    else:
        print('Error During Query: postJsonRequest()')
        print(r)
        return '0'

#display history array
def getDisplayHistory():
    endPoint = URL + '/car_predictions'
    r =  requests.get(url=endPoint)
    if( r.status_code == 200):
        return r.json()
    else:
        print('Error During query: getDisplayHistory()')
        return r.status_code






