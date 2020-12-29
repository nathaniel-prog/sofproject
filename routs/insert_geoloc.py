#import googlemaps
import requests
from urllib.parse import urlencode
import json
from datetime import datetime




api_key='AIzaSyBhvlgznzR_nqaRxryX_HhdyF4UcMErarI'
#url= 'https://maps.googleapis.com/maps/api/geocode/json


#test= f'https://maps.googleapis.com/maps/api/geocode/json?address={user_input}&key={api_key}

#data_type='json'
#endpoint=f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
#params={'address': "Paris , CDG", 'key': api_key}
#url_param= urlencode(params)

#urll=f'{endpoint}?{url_param}'
#print(urll)


def extract_lat_lng(address , data_type='json'):
	data_type='json'
	endpoint=f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
	params={'address': address, 'key': api_key}
	url_param= urlencode(params)
	urll=f'{endpoint}?{url_param}'
	r= requests.get(urll)
	if r.status_code not in range(200,299):
		return {}
	else:
		return r.json()['results'][0]['geometry']['location_type']


#print(extract_lat_lng('London'))


