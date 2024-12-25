import nbtlib
import os

def main():
	for file in os.listdir('./'):
		if '_old' in file:
			continue

		if '.cosarmor' in file:
			continue
		
		if 'find_empty_uuid.py' in file:
			continue
		
		nbtfile = nbtlib.load(file)
		try:
			nbtfile['UUID']
		except KeyError:
			try:
				print(file + ' is missing a UUID')
			except KeyError:
				print('major issue, unable to read a file. Ensure only playerdata is in the directory')
  
if __name__ == '__main__':
	main()