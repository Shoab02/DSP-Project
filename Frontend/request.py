# importing the requests library
import requests
#import pandas as pd

# api-endpoint
URL = "https://epita-2022-dsp-api.herokuapp.com"
def tempPostRequest(selected_file):
    endPoint = URL + '/predict'
    #     key = rows[0]
    #     data[key] = rows
    # print(data)
    files = {'csv_file':selected_file.getvalue()}
    r =  requests.post(url=endPoint, data=data)
    if( r.status_code == 200):
        print('request is successiful')
        return r.json()
    else:
        print('Error During Query: tempPostRequest()')
        print(r)
        return r.status_code


#json object
# def PostRequest():



#display history array
def GetRequest():
    endPoint = URL + '/car_predictions'
    r =  requests.get(url=endPoint)
    if( r.status_code == 200):
        return r.json()
    else:
        print('Error During query: GetRequest()')
        print(r)
        return r.status_code






