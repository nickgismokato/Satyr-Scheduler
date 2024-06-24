#Python specific packages
import os

#pip imported packages


#Self created dependencies
import SongData.py
import SketchData.py


def GetData(lstCSV):
	list_Objects = []
	for csvFile in lstCSV:
		if(os.path.splitext(csvFile) == "song.csv"):
			myClass = SongData(csvFile)
		if(os.path.splitext(csvFile) == "sketch.csv"):
			myClass = SketchData(csvFile)
		list_Objects.append(myClass)
	if not list_Objects:
		print("ERROR:\n\tNo .csv files was detected was empty!\n\tMake sure to have a song.csv or/and song.csv file withing your main program.")
		raise RuntimeError("list of valid .csv file is empty")
	return list_Objects
