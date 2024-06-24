#Python specific packages
import os

#pip imported packages
import panda as pd

class SketchData:
	def __init__(self, directory) -> None:
		self.dir = directory
		self.name = os.path.splitext(self.dir)
		self.type = "SKETCH"
		self.TID = 1
		self.df = self.CreateDataFrame()
		pass
	def CreateDataFrame(self):
		pass