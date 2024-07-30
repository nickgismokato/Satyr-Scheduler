#remember to do: "pip install SatyrScheduler"
import SatyrScheduler as ss

import os

def Main():
	data = ss.GetData()
	for obj in data:

		print(f"Object name: [{obj.name}]\nObject Directory: [{obj.dir}]\nObject TID: [{obj.TID}]")
		if(obj.TID == 1):
			count = 0
			for sketch in obj.lstSketchObj:
				if not(count == 0):
					print(f"\tSketch: {sketch.title}\tRanking: {sketch.ranking}\tInstructor: {sketch.instructor}\t People: {sketch.people}\t\t Need Instructor: {sketch.need_Instructor}")
				else:
					print(f"\tSketch: {sketch.title}\tRanking: {sketch.ranking}\tInstructor: {sketch.instructor}\t People: {sketch.people}\t Need Instructor: {sketch.need_Instructor}")
				count += 1
		if(obj.TID == 0):
			count = 0
			for song in obj.lstSongObj:
				if not(count == 0):
					print(f"\tSong: {song.title}\tRanking: {song.ranking}\tInstructor: {song.instructor}\t People: {song.people}\t\t\t Need Instructor: {song.need_Instructor}")
				else:
					print(f"\tSong: {song.title}\tRanking: {song.ranking}\tInstructor: {song.instructor}\t People: {song.people}\t Need Instructor: {song.need_Instructor}")
				count += 1
		if(obj.TID == 2):
			for room in obj.lstRoom:
				if(len(room.name)>8):
					print(f"\tRoom: {room.name},\tUsage: {room.usageName}")
				else:
					print(f"\tRoom: {room.name},\t\tUsage: {room.usageName}")
		print("---------------------------------")
	ss.InitSchedule(breaktime = 10, hello = "World!")
	return None

if __name__ == "__main__":
	Main()