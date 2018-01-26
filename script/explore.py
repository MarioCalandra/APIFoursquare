# Esempio di applicazione dell'API explore
# Restituisce in output i primi 50 luoghi più raccomandati entro 30km dal centro di Catania

import json, requests

client_id = 'SMM'
client_secret = 'SMM'
versioning = '20180122'

url = 'https://api.foursquare.com/v2/venues/explore'	#url a cui fare richiesta per l'explore

params = dict(		#definisce i parametri in input all'explore
	client_id=client_id, 
	client_secret=client_secret, 
	v=versioning,
	limit=50,
	near='Catania',
	radius=30000
)

resp = requests.get(url=url, params=params)		#esegue la get all'url indicato passando i parametri contenuti nel dizionario params
data = json.loads(resp.text)		#carica in data il risultato ottenuto tramite la get in formato json 
	
with open('explore.json', 'w') as out:
	json.dump(data, out, indent=2)		#stampa in "explore.json" il contenuto di data con indentazione pari a 2
		
