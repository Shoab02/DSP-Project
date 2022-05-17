# importing the requests library
import requests
#import pandas as pd

# api-endpoint
URL = "https://epita-2022-dsp-api.herokuapp.com/predict"

def tempPostRequest(selected_file):
    endPoint = URL
    files = {'csv_file':selected_file.getvalue()}
    r =  requests.post(url=endPoint, files=files)
    if( r.status_code == 200):
        #array = r.json()
        #df = pd.DataFrame(array)
        print('request is successiful')
        return r.json()
    else:
        print('post request was not succesifull')
        print(r)
        return r.status_code


