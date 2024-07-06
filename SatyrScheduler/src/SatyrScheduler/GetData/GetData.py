#Python specific packages
import os

#pip imported packages
import pandas as pd

####################################################################################################
#	CLASS: 			SketchData
#	INPUT INIT: 	<String> - directory path
####################################################################################################
class SketchData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.basename(self.dir)
		self.type = "SKETCH"
		self.TID = 1
		self.lstSketchObj = self.CreateListOfSketchObjects(self.dir)
	def CreateListOfSketchObjects(self, dir):
		df = pd.read_csv(dir)
		returnlst = [Sketch(col1, col2, col3, col4) for col1, col2, col3, col4 in zip(df['Title'].str.lstrip(), df['Weight'], df['People'], df['Instructor'].str.lstrip())]
		return returnlst
####################################################################################################
#	CLASS: 			Sketch
#	INPUT INIT: 	{
#						<String> - Title of sketch
#						<Int> - Weight of progress
#						<String>[] - People involved
#						<String> - Instructor of sketch
#					}
####################################################################################################
class Sketch:
	def __init__(self, title, weight, people, instructor) -> None:
		self.title = ""
		self.people = []
		self.ranking = -1
		self.instructor = ""
		self.UpdateData(title, weight, people, instructor)
	def UpdateData(self, title, weight, peoples, instructor):
		self.title = title
		self.ranking = int(weight)
		self.instructor = instructor
		tmpPeopleList = peoples.split(';')
		tmplist = []
		for people in tmpPeopleList:
			tmplist.append(people.strip())
		self.people = tmplist
		return None

####################################################################################################
#	CLASS: 			SongData
#	INPUT INIT: 	<String> - directory path
####################################################################################################
class SongData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.basename(self.dir)
		self.type = "SONG"
		self.TID = 0
		self.lstSongObj = self.CreateListOfSongObjects(self.dir)
	def CreateListOfSongObjects(self, dir):
		df = pd.read_csv(dir)
		returnlst = [Song(col1, col2, col3, col4) for col1, col2, col3, col4 in zip(df['Title'].str.lstrip(), df['Weight'], df['People'], df['Instructor'].str.lstrip())]
		return returnlst
####################################################################################################
#	CLASS: 			Song
#	INPUT INIT: 	{
#						<String> - Title of sketch
#						<Int> - Weight of progress
#						<String>[] - People involved
#						<String> - Instructor of sketch
#					}
####################################################################################################
class Song:
	def __init__(self, title, weight, people, instructor) -> None:
		self.title = ""
		self.people = []
		self.ranking = -1
		self.instructor = ""
		self.UpdateData(title, weight, people, instructor)
	def UpdateData(self, title, weight, peoples, instructor):
		self.title = title
		self.ranking = weight
		self.instructor = instructor
		tmpPeopleList = peoples.split(';')
		tmplist = []
		for people in tmpPeopleList:
			tmplist.append(people.strip())
		self.people = tmplist
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
