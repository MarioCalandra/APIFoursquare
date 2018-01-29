import json, requests
from jsonFSmng import json_search
from charts import ColumnChart, PieChart

client_id = 'HY5VTLYMVXHH0SOTC2MR2PGZTIGZJ2ZQN4T4RHDADQNWQWLL'
client_secret = 'RLZUPWGYNKKLJN13WUNGFTI4SQJKWQFHRPCZ1RVYID0I2BBO'
versioning = '20180122'

category = '4d4b7105d754a06374d81259' #categoria cibi
url = 'https://api.foursquare.com/v2/venues/search'
file_name = 'cibi.json'

params = dict(
	client_id=client_id,
	client_secret=client_secret,
	v=versioning,
	near='Catania',
	radius=10000,
	limit=50,
	categoryId=category
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
srch = json_search(data)

with open(file_name, 'w') as out:
	json.dump(srch.sortByCheckins(), out, indent=3)
	out.close()

#creazione grafici a colonna e a torta
n = 7
column_chart = ColumnChart('Cibi', 'Checkins', 'Checkins nei primi '+str(n)+' luoghi principali in cui mangiare', 900, 450, '70%', 'column_script.html')
pie_chart = PieChart('Cibi', 'Checkins', '% di checkins nei luoghi principali in cui mangiare', True, 500, 500, 'pie_script.html')
data = srch.sortByCheckins()

other_checkins = 0
i = 0
for venue in data:
	if i<n:
		column_chart.addElement(venue['name'], venue['stats']['checkinsCount'], 'darkblue')
		pie_chart.addElement(venue['name'], venue['stats']['checkinsCount'])
	else:
		other_checkins += venue['stats']['checkinsCount']
	i+=1

pie_chart.addElement('Altro', other_checkins)
	
column_chart.makeChart('cibi_column.html')
pie_chart.makeChart('cibi_pie.html')








