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

#Python own packages
import datetime

#RAbsolute import from SatyrScheduler
from SatyrScheduler.GetData import GetData

class Schedule:
	def __init__(self, date, breaktime, deltatime, starttime, endtime, lst_GetData):
		self.date = date
		self.breaktime	= breaktime
		self.deltatime	= deltatime
		self.startime	= datetime.datetime.strptime(starttime, '%H:%M')
		self.endtime	= datetime.datetime.strptime(endtime, '%H:%M')
		self.sketches	= lst_GetData[1]
		self.songs		= lst_GetData[0]
		self.rooms		= lst_GetData[2]
		pass


def InitSchedule(**kwargs):
	defaultKwargs = {'breaktime' : 0, 'deltatime' : 25, 'starttime' : "17:00", 'endtime' : "21:25"}
	kwargs = {**defaultKwargs, **kwargs}
	#print(kwargs)
	list_GetData = GetData.GetData()
	list_GetData.sort(key=lambda x: x.TID, reverse = False)
	created_schedule = Schedule(datetime.datetime(2024, 7, 26), kwargs.get('breaktime'), kwargs.get('deltatime'), kwargs.get('starttime'), kwargs.get('endtime'), list_GetData)
	attrs = vars(created_schedule)
	#print(', '.join("%s: %s" % item for item in attrs.items()))
	return created_schedule
