import time, os, platform
from datetime import datetime

# check system
system = platform.system()
supported = 'Windows', 'Linux', 'Darwin'
if system not in supported:
	print('--------------')
	print('|   ERROR!   |')
	print('--------------')
	print('UNSUPPORTED OS')
	exit()

# welcome screen
print('--------------')
print('|  WELCOME!  |')
print('--------------')
print('--------------')
print('|  LOADING.  |')
print('--------------')
time.sleep(0.5)

# initializing
now = datetime.now() # gets current time
sol = datetime.now().timetuple().tm_yday # gets day of year
timeSecs = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # converts time into seconds

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

print('--------------')
print('|  FINISHED  |')
print('--------------')
time.sleep(1)

# clock loop, starts at current time then uses loop clock
while True:
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
		decisol = 0 # resets deciSols to 0 every Sol

	try:
		os.system('clear') # Linux-based
	except:
		try:
			os.system('cls') # DOS-based
		except:
			print()
			print('--------------')
			print('|   ERROR!   |')
			print('--------------')
			os.system('exit'); # exit Python (even if this command doesn't work, it'll cause an uncaught error)

	# display section
	print('--------------')
	print('| ' + str(sol).zfill(3) + ' ' + str(decisol) + str(millisol).zfill(2) + '.' + str(nanosol).zfill(2) + ' |')
	print('--------------')