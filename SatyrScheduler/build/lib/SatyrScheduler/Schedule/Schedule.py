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
	def __init__(self, date, breaktime, deltatime, starttime, endtime):
		self.date = date
		self.breaktime = breaktime
		self.deltatime = deltatime
		self.startime = datetime.strptime(starttime, '%H:%M')
		self.endtime = datetime.strptime(endtime, '%H:%M')
		pass


def InitSchedule(**kwargs):
	defaultKwargs = {'breaktime' : 0, 'deltatime' : 25, 'starttime' : "17:00", 'endtime' : "21:25"}
	kwargs = {**defaultKwargs, **kwargs}
	print(kwargs)
	print(GetData.GetData())
	return None