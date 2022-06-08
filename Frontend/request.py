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
def postJsonRequest(user_input):
    #TODO: update when endpoint is available
    endPoint = URL + '/predictSingle'
    data = {
        'powerPS': user_input[0],
        'vehicleType': user_input[1],
        'brand': user_input[2],
        'fuelType': user_input[3],
        'kilometer': user_input[4]
        }
    r = requests.post(url=endPoint, json=data)
    if( r.status_code == 200):
        return r.json()['results']
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






