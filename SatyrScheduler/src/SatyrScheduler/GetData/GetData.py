#Python specific packages
import os

#pip imported packages
import panda as pd

class SongObject:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.splitext(self.dir)
		self.type = "SONG"
		self.TID = 0
		self.df = self.CreateDataFrame()
		pass
	def CreateDataFrame(self):
		pass
class SketchObject:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.type = "SKETCH"
		self.TID = 1
		self.df = self.CreateDataFrame()
		pass
	def CreateDataFrame(self):
		pass

def GetData(lstCSV):
	list_Objects = []
	for csvFile in lstCSV:
		if(os.path.splitext(csvFile) == "song.csv"):
			myClass = SongObject(csvFile)
		if(os.path.splitext(csvFile) == "sketch.csv"):
			myClass = SketchObject(csvFile)
		list_Objects.append(myClass)
	if not df_list:
		print("ERROR:\n\tNo .csv files was detected was empty!\n\tMake sure to have a song.csv or/and song.csv file withing your main program.")
		raise RuntimeError("list of valid .csv file is empty")
	
