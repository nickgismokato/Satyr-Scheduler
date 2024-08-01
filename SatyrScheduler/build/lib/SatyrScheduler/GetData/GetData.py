'''
MIT License

Copyright (c) 2024 Nickgismokato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
		self.dir			= directory
		self.name			= os.path.basename(self.dir)
		self.type			= "SKETCH"
		self.TID			= 1
		self.lstSketchObj	= self.CreateListOfSketchObjects(self.dir)
	def CreateListOfSketchObjects(self, dir):
		df = pd.read_csv(dir)
		returnlst = [Sketch(col1, col2, col3, col4, col5) for col1, col2, col3, col4, col5 in zip(df['Title'].str.lstrip(), df['Weight'], df['People'], df['Instructor'].str.lstrip(), df['Need Instructor'])]
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
	def __init__(self, title, weight, people, instructor, need_ins) -> None:
		self.title 				= ""
		self.people 			= []
		self.ranking 			= -1
		self.instructor 		= ""
		self.need_Instructor	= 0
		self.UpdateData(title, weight, people, instructor, need_ins)
	def UpdateData(self, title, weight, peoples, instructor, need_ins):
		self.title		= title
		self.ranking	= int(weight)
		self.instructor	= instructor
		tmpPeopleList	= peoples.split(';')
		
		tmplist = []
		for people in tmpPeopleList:
			tmplist.append(people.strip())
		self.people = tmplist
		if(need_ins == 1):
			self.need_Instructor = 1		
		return None

####################################################################################################
#	CLASS: 			SongData
#	INPUT INIT: 	<String> - directory path
####################################################################################################
class SongData:
	def __init__(self, directory) -> None:
		self.dir		= directory
		self.name		= os.path.basename(self.dir)
		self.type		= "SONG"
		self.TID		= 0
		self.lstSongObj	= self.CreateListOfSongObjects(self.dir)
	def CreateListOfSongObjects(self, dir):
		df = pd.read_csv(dir)
		returnlst = [Song(col1, col2, col3, col4, col5) for col1, col2, col3, col4, col5 in zip(df['Title'].str.lstrip(), df['Weight'], df['People'], df['Instructor'].str.lstrip(), df['Need Instructor'])]
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
	def __init__(self, title, weight, people, instructor, need_ins) -> None:
		self.title				= ""
		self.people				= []
		self.ranking			= -1
		self.instructor			= ""
		self.need_Instructor	= 0
		self.UpdateData(title, weight, people, instructor, need_ins)
	def UpdateData(self, title, weight, peoples, instructor, need_ins):
		self.title		= title
		self.ranking	= weight
		self.instructor	= instructor
		tmpPeopleList 	= peoples.split(';')
		
		tmplist = []
		for people in tmpPeopleList:
			tmplist.append(people.strip())
		self.people = tmplist
		if(need_ins == 1):
			self.need_Instructor = 1
		return None

####################################################################################################
#	CLASS: 			RoomData
#	INPUT INIT: 	<String> - directory path
####################################################################################################
class RoomData:
	def __init__(self, directory):
		self.dir		= directory
		self.name		= os.path.basename(self.dir)
		self.type		= "ROOM"
		self.TID		= 2
		self.lstRoom	= self.CreateListOfRoomObjects()
	def CreateListOfRoomObjects(self):
		df = pd.read_csv(self.dir)
		retLst = [Room(col1, col2) for col1, col2 in zip(df['Name'].str.strip(),df['Usage'])]
		return retLst
####################################################################################################
#	CLASS: 			Room
#	INPUT INIT: 	{
#						<String> - Title of room
#						<Int> - Song or Sketch usage
#					}
####################################################################################################
class Room:
	def __init__(self, name, usage):
		self.name		= name
		self.usage		= usage
		self.usageName	= 'Sketch' if self.usage == 1 else 'Song'

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
			if(os.path.basename(csvFile) == "room.csv"):
				myClass = RoomData(csvFile)
			list_Objects.append(myClass)
	if not list_Objects:
		print("ERROR:\n\tNo .csv files was detected was empty!\n\tMake sure to have a song.csv or/and song.csv file withing your main program.")
		raise RuntimeError("list of valid .csv file is empty")
	list_Objects.sort(key=lambda x: x.TID, reverse = False)
	return list_Objects
