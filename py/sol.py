from datetime import datetime
import math

def sol( solcmd ):
	now = datetime.now() # gets current time
	timeSecs = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # converts time into seconds
	sol = datetime.now().timetuple().tm_yday # gets day of year
	fifth = int(math.ceil(sol / 73)) # calculate fifth

	if timeSecs >= 8640: # 8640 seconds in a decisol
		decisol = divmod(timeSecs, 8640)
		timeSecs = decisol[1]
		decisol = int(decisol[0])
	else:
		decisol = 0

	if timeSecs >= 86.4: # 86.4 seconds in a millisol
		millisol = divmod(timeSecs, 86.4)
		timeSecs = millisol[1]
		millisol = int(millisol[0])
	else:
		millisol = 0

	if timeSecs >= 0.864: # 0.864 seconds in a nanosol
		nanosol = divmod(timeSecs, 0.864)
		nanosol = int(nanosol[0])
	else:
		nanosol = 0

	if solcmd == 'decisol':
		return decisol
	elif solcmd == 'millisol':
		return millisol
	elif solcmd == 'nanosol':
		return nanosol
	elif solcmd == 'sol':
		return sol
	elif solcmd == 'fifth':
		return fifth
	elif solcmd == 'all':
		current = [fifth, sol, decisol, millisol, nanosol]
		return current
	# elif solcmd == 'clock':
	# 	global clock
	# 	clock = 1
	# 	clock()
	# elif solcmd == 'stopclock':
	# 	clock = 0
	elif solcmd == 'help':
		print('sol.py help')
		print('available commands:')
		print('fifth - returns current fifth of year')
		print('sol - returns current sol (day of year)')
		print('decisol - returns current decisol')
		print('millisol - returns current millisol')
		print('nanosol - returns current nanosol')
		print('all - returns all of the above in an array in that order')
		# print('clock - starts a clock, returns every nanosol')
		# print('stopclock - stops running clock')
		print('help - shows this screens')

def clock():
	while clock == 1:
		time.sleep(0.864) # 864 milliseconds = 1 nanosol

		nanosol = nanosol + 1 # nanoSol (second) counter

		if nanosol == 100:
			millisol = millisol + 1 # milliSol (minute) counter
			nanosol = 0 # resets nanoSols to 0 every milliSol

		if millisol == 100:
			decisol = decisol + 1 # deciSol (hour) counter
			millisol = 0 # resets milliSols to 0 every deciSol

		if decisol == 10:
			sol = sol + 1 # Sol (day) counter
			fifth = int(math.ceil(sol / 73)) # recalculate fifth
			decisol = 0 # resets deciSols to 0 every Sol

		current = [fifth, sol, decisol, millisol, nanosol]
		return current

