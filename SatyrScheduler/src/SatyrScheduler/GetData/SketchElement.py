



class Sketch:
	def __init__(self, data) -> None:
		self.title = ""
		self.people = []
		self.ranking = -1
		self.instructor = ""
		self.UpdateData(data)

	def UpdateData(self, data):
		self.title = data[0]
		self.ranking = data[1]
		for people in data[2]:
			self.people.append(people)
		self.instructor = data[3]
		return None
	