import random

class ColumnChart:
	def __init__(self, nameX, nameY, title, width, height, groupWidth, in_path):
		self.nameX = nameX
		self.nameY = nameY
		self.title = title
		self.width = width
		self.height = height
		self.groupWidth = groupWidth
		self.in_path = in_path
		self.attr = list()
		self.attr.append([nameX, nameY, {'role': 'style' }])
		self.elements = list()
		
	def addElement(self, name, value, colour):
		self.elements.append([name, value, colour])
		
	def makeGraph(self, out_path, shuffle=False, debug=True):
		with open(self.in_path, 'r') as input:
			code = input.read()
			if shuffle == True:
				random.shuffle(self.elements)
			data = self.attr + self.elements
			code = code.replace("_elements_", str(data))
			code = code.replace("_title_", '"'+self.title+'"')
			code = code.replace("_width_", str(self.width))
			code = code.replace("_height_", str(self.height))
			code = code.replace("_groupWidth_", '"'+self.groupWidth+'"')
			with open(out_path, 'w') as output:
				output.write(code)
				output.close()			
			if debug == True:
				print "Column Chart creato al path:", out_path

class PieChart:
	def __init__(self, nameX, nameY, title, is3D, width, height, in_path):
		self.nameX = nameX
		self.nameY = nameY
		self.title = title
		self.is3D = is3D
		self.width = width
		self.height = height
		self.in_path = in_path
		self.attr = list()
		self.attr.append([nameX, nameY])
		self.elements = list()
		
	def addElement(self, name, value):
		self.elements.append([name, value])
		
	def makeGraph(self, out_path, shuffle=False, debug=True):		
		with open(self.in_path, 'r') as input:
			code = input.read()
			if shuffle == True:
				random.shuffle(self.elements)
			data = self.attr + self.elements
			code = code.replace("_elements_", str(data))
			code = code.replace("_title_", '"'+self.title+'"')
			code = code.replace("_width_", str(self.width))
			code = code.replace("_height_", str(self.height))
			if self.is3D == True:
				code = code.replace("_is3D_", "true")
			else:
				code = code.replace("_is3D_", "false")
			with open(out_path, 'w') as output:
				output.write(code)
				output.close()			
			if debug == True:
				print "Pie Chart creato al path:", out_path
