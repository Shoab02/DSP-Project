# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:8000/predict"

def tempPostRequest(selected_file):
    endPoint = URL
    r =  requests.post(url=endPoint, files={'file': selected_file})
    if( r.status_code == 200):
        return r.json()
    else:
        print('post request was not succesifull')
        return r.status_code


