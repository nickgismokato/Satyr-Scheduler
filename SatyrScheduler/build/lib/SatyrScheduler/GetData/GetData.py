#Python specific packages
import os

#pip imported packages
import pandas as pd

class SketchData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.basename(self.dir)
		self.type = "SKETCH"
		self.TID = 1
		self.df = pd.read_csv(self.dir)
		pass

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

class SongData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.basename(self.dir)
		self.type = "SONG"
		self.TID = 0
		self.df = self.CreateDataFrame()
		pass
	def CreateDataFrame(self):
		pass

class Song:
	def __init__(self, data) -> None:
		self.title = ""
		self.people = []
		self.ranking = -1
		self.instructor = ""
		self.UpdateData(data)
	
	def UpdataData(self, data):
		self.title = data[0]
		self.ranking = data[1]
		for people in data[2]:
			self.people.append(people)
		self.instructor = data[3]
		return None

def GetData():
	directory = os.getcwd()
	file_list = []
	for filename in os.listdir(directory):
		file_list.append(os.path.join(directory, filename))
	list_Objects = []
	for csvFile in file_list:
		if(csvFile.endswith('.csv')):
			myClass = None
			if(os.path.basename(csvFile) == "song.csv"):
				myClass = SongData(csvFile)
			if(os.path.basename(csvFile) == "sketch.csv"):
				myClass = SketchData(csvFile)
			list_Objects.append(myClass)
	if not list_Objects:
		print("ERROR:\n\tNo .csv files was detected was empty!\n\tMake sure to have a song.csv or/and song.csv file withing your main program.")
		raise RuntimeError("list of valid .csv file is empty")
	return list_Objects
