import json, requests

client_id = 'SMM'
client_secret = 'SMM'
versioning = '20180122'

url = 'https://api.foursquare.com/v2/venues/search'

params = dict(
	client_id=client_id,
	client_secret=client_secret,
	v=versioning,
	query='Villa Bellini',	# ricerca Villa Bellini
	intent='global'		# estendi il contenuto della query di ricerca a tutto il mondo
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

with open('search.json', 'w') as out:
	json.dump(data, out, indent=2)
	
