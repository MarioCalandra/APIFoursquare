class json_explore:
	def __init__(self, data):
		self.data = data

	def getItems(self):
		response = self.data['response']
		items = response['groups'][0]['items']
		return items
		
	def getVenueInfo(self, item):
		return item['venue']
		
	def getItemByName(self, name):
		for i in getItems():
			venue = getVenueInfo(i)
			if venue['name'] == name:
				return i
		
	def getItemByVenueID(self, id):
		for i in getItems():
			venue = getVenueInfo(i)
			if venue['id'] == id:
				return i
				
	def sortByCheckins(self): #restituisce una lista di items ordinati per checkins
		item_list = self.getItems()
		sorted_list = list()
		while len(item_list) > 0:	
			max_value = 0
			for item in item_list:
				venue = self.getVenueInfo(item)
				checkins = venue['stats']['checkinsCount']
				if checkins > max_value:
					max_value = checkins
					max_place = item
			sorted_list.append(max_place)
			item_list.remove(max_place)
		return sorted_list
		
class json_similar:
	def __init__(self, data):
		self.data = data
		
	def getItems(self):
		response = self.data['response']
		items = response['similarVenues']['items']
		return items
		
	def sortByCheckins(self): #restituisce una lista di items ordinati per checkins
		item_list = self.getItems()
		sorted_list = list()
		while len(item_list) > 0:	
			max_value = 0
			for item in item_list:
				checkins = item['stats']['checkinsCount']
				if checkins > max_value:
					max_value = checkins
					max_place = item
			sorted_list.append(max_place)
			item_list.remove(max_place)
		return sorted_list
		
class json_search:
	def __init__(self, data):
		self.data = data
	
	def getVenues(self):
		response = self.data['response']
		return response['venues']
	
	def sortByCheckins(self): #restituisce una lista di venues ordinati per checkins
		venue_list = list()
		sorted_list = list()
		for venue in self.getVenues():
			venue_list.append(venue)
		while len(venue_list) > 0:	
			max_value = 0
			for venue in venue_list:
				checkins = venue['stats']['checkinsCount']
				if checkins > max_value:
					max_value = checkins
					max_place = venue
			sorted_list.append(max_place)
			venue_list.remove(max_place)
		return sorted_list
		
class json_nextvenues:
	def __init__(self, data):
		self.data = data
		
	def getVenues(self):
		response = self.data['response']
		items = response['nextVenues']['items']
		return items
		
	def sortByCheckins(self): #restituisce una lista di venues ordinati per checkins
		venue_list = list()
		sorted_list = list()
		for venue in self.getVenues():
			venue_list.append(venue)
		while len(venue_list) > 0:	
			max_value = 0
			for venue in venue_list:
				checkins = venue['stats']['checkinsCount']
				if checkins > max_value:
					max_value = checkins
					max_place = venue
			sorted_list.append(max_place)
			venue_list.remove(max_place)
		return sorted_list