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
TimingClock = namedtuple("TimingClock",["start_Hour", "start_Minute", "end_Hour", "end_Minute"])

class CustomTime:
    def __init__(self, startTime, endTime, deltaTime, breakTime):
        self.startTime_InMinute = 0
        self.endTime_InMinute   = 0
        self.deltaTime          = deltaTime
        self.breakTime          = breakTime
        self.clockStart         = None
        self.clockEnd           = None  
        self.UpdateFields(startTime, endTime)
        return None

    def UpdateFields(self, startTime, endTime):
        startTime_Hour          = int(startTime.strftime("%H"))
        startTime_Minute        = int(startTime.strftime("%M"))
        self.startTime_InMinute = startTime_Hour*60 + startTime_Minute
        endTime_Hour            = int(endTime.strftime("%H"))
        endTime_Minute          = int(endTime.strftime("%M"))
        self.endTime_InMinute   = endTime_Hour*60 + endTime_Minute

        self.clockStart         = CustomClock(startTime_Hour,startTime_Minute)
        self.clockEnd           = CustomClock(endTime_Hour, endTime_Minute)

    def GetTimeList(self):
        retList = []
        count = 1
        calc_Minute = self.clockStart.minute
        calc_Hour = self.clockStart.hour
        temp_Minute = self.clockStart.minute
        temp_Hour = self.clockStart.hour
        while(True):
            caryy_Hour = 0
            if(count == 1):
                temp_Minute = (self.clockStart.minute + self.deltaTime) % 60
                if(self.clockStart.minute + self.deltaTime > 59):                  
                    temp_Hour = (self.clockStart.hour + 1) % 24
            else:
                temp_Minute = (calc_Minute + self.deltaTime) % 60
                if(calc_Minute + self.deltaTime > 59):
                    temp_Hour = (calc_Hour + 1) % 24
            if((temp_Hour >= self.clockEnd.hour) and (temp_Minute >= self.clockEnd.minute)):
                
            retList.append(calc_Hour, calc_Minute, temp_Hour, temp_Minute)
            if(temp_Minute + self.breakTime > 59):
                calc_Hour = (temp_Hour + 1) % 24
            calc_Minute = (temp_Minute + self.breakTime) % 60
            count += 1
        return retList



def CreateTimeClass(startime, endtime, deltatime, breaktime):
    timeClass = CustomTime(startime, endtime, deltatime, breaktime)
    return timeClass