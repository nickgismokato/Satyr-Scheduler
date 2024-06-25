#remember to do: "pip install SatyrScheduler"
import SatyrScheduler as ss

import os

def Main():
	data = ss.GetData()
	for obj in data:
		print(f"Object name: [{obj.name}]\nObject Directory: [{obj.dir}]\nObject TID: [{obj.TID}]")
		if(obj.TID == 1):
			for sketch in obj.lstSketchObj:
				print(f"\tSketch: {sketch.title}\tRanking: {sketch.ranking}\tInstructor: {sketch.instructor}\t People: {sketch.people}")
		if(obj.TID == 0):
			for song in obj.lstSongObj:
				print(f"\tSong: {song.title}\tRanking: {song.ranking}\tInstructor: {song.instructor}\t People: {song.people}")
		print("---------------------------------")
	return None

if __name__ == "__main__":
	Main()