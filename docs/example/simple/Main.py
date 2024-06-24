#remember to do: "pip install SatyrScheduler"
import SatyrScheduler as ss

import os

def Main():
	a = ss.GetData()
	for obj in a:
		print(obj.df)
	return None

if __name__ == "__main__":
	Main()