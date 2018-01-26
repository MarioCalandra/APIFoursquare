import json, requests
from jsonFSmng import json_explore

client_id = 'HY5VTLYMVXHH0SOTC2MR2PGZTIGZJ2ZQN4T4RHDADQNWQWLL'
client_secret = 'RLZUPWGYNKKLJN13WUNGFTI4SQJKWQFHRPCZ1RVYID0I2BBO'
versioning = '20180122'

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
	client_id=client_id, 
	client_secret=client_secret, 
	v=versioning,
	limit=50,
	near='Catania',
	radius=30000,
	section='plazas'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

exp = json_explore(data)
	
with open('explore_out/sort_checkins.json', 'w') as out:
	for l in exp.sortByCheckins():
		json.dump(l, out, indent=3)
	out.close()
		