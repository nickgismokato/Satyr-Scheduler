#Python specific packages
import os

#pip imported packages
import panda as pd

class SongData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.splitext(self.dir)
		self.type = "SONG"
		self.TID = 0
		self.df = self.CreateDataFrame()
		pass
	def CreateDataFrame(self):
		pass