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

import datetime

from collections import namedtuple

CustomClock = namedtuple("CustomClock",["hour", "minute"])

class CustomTime:
    def __init__(self, startTime, endTime, deltaTime, breakTime):
        self.startTime_InMinute = 0
        self. endTime_InMinute = 0
        self.deltaTime = deltaTime
        self.breakTime = breakTime
        self.clockStart = None
        self.clockEnd = None

        
        self.UpdateFields(startTime, endTime)
        return None

    def UpdateFields(self, startTime, endTime):
        startTime_Hour          = int(startTime.strftime("%H"))
        startTime_Minute        = int(startTime.strftime("%M"))
        self.startTime_InMinute = startTime_Hour*60 + startTime_Minute
        endTime_Hour            = int(endTime.strftime("%H"))
        endTime_Minute          = int(endTime.strftime("%M"))
        self.endTime_InMinute   = endTime_Hour*60 + endTime_Minute

        self.clockStart              = CustomClock(startTime_Hour,startTime_Minute)
        self.clockEnd                = CustomClock(endTime_Hour, endTime_Minute)




def CreateTimeClass(startime, endtime, deltatime, breaktime):
    timeClass = CustomTime(startime, endtime, deltatime, breaktime)
    return timeClass