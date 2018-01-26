# Esempio di applicazione dell'API details
# Restituisce in output informazioni in formato JSON relative a Piazza Duomo

import json, requests

client_id = 'SMM'
client_secret = 'SMM'
versioning = '20180122'

venueid = '4cf16112f98ba090661cc873'	# venueid di Piazza Duomo
file_name = 'details_piazza_duomo.json'

url = 'https://api.foursquare.com/v2/venues/'+venueid

params = dict(
	client_id=client_id, 
	client_secret=client_secret, 
	v=versioning
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

with open(file_name, 'w') as out:
	json.dump(data, out, indent=3)
	out.close()
