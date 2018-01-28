import json, requests
from jsonFSmng import json_search
from charts import ColumnChart, PieChart

client_id = 'SMM'
client_secret = 'SMM'
versioning = '20180122'

category = '4bf58dd8d48988d164941735' #categoria piazza
url = 'https://api.foursquare.com/v2/venues/search'
file_name = 'piazze.json'

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
column_chart = ColumnChart('Piazze', 'Checkins', 'Checkins nei primi '+str(n)+' luoghi', 900, 450, '70%', 'column_script.html')
pie_chart = PieChart('Piazze', 'Checkins', '% di checkins nei primi '+str(n)+' luoghi', True, 500, 500, 'pie_script.html')
data = srch.sortByCheckins()

for i in range(n):
	venue = data[i]
	column_chart.addElement(venue['name'], venue['stats']['checkinsCount'], 'darkred')
	pie_chart.addElement(venue['name'], venue['stats']['checkinsCount'])
	
column_chart.makeChart('piazze_column.html')
pie_chart.makeChart('piazze_pie.html')








