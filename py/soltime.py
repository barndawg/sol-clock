import time, os
from datetime import datetime

print('[WELCOME] Welcome to sol.py!')
print('[WELCOME] sol.py is copyright (c) &py, barndawg 2016')
time.sleep(1)
print('[INIT] Initialising clock...')

now = datetime.now() # gets current time
print('[INIT-TIME] Current time: ' + str(now))
timeSecs = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # converts time into seconds
print('[INIT-TIME] Current time in seconds' + str(timeSecs))
yearDay = datetime.now().timetuple().tm_yday # gets day of year
print('[INIT-TIME] Current day of year: ' + str(yearDay))

if timeSecs >= 8640: # 8640 seconds in a decisol
	print('[INIT-CALC] Calculated current deciSol')
	decisol = divmod(timeSecs, 8640)
	timeSecs = decisol[1]
	decisol = int(decisol[0])
else:
	decisol = 0

if timeSecs >= 86.4: # 86.4 seconds in a millisol
	print('[INIT-CALC] Calculated current milliSol')
	millisol = divmod(timeSecs, 86.4)
	timeSecs = millisol[1]
	millisol = int(millisol[0])
else:
	millisol = 0

if timeSecs >= 0.864: # 0.864 seconds in a nanosol
	print('[INIT-CALC] Calculated current nanoSol')
	nanosol = divmod(timeSecs, 0.864)
	nanosol = int(nanosol[0])
else:
	nanosol = 0

print('[INIT] Initialized! Starting clock...')
time.sleep(1)

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
			print('[ERROR] YOUR OS IS NOT SUPPORTED. ATTEMPTING TO EXIT...') # Error message
			os.system('exit'); # Exit Python (even if this command doesn't work, it'll cause an uncaught error)

	print('----&PY SOLTIME 1.2----') # title
	print('|   TIME   |  FORMAT  |') # header text
	print('-----------------------') # divider
	print('| ' + str(decisol).zfill(2) + ':' +str(millisol).zfill(2) + ':' + str(nanosol).zfill(2) + ' | dS:mS:nS |') # div display
	print('-----------------------') # divider
	print('|  ' + str(decisol) + str(millisol).zfill(2) + '.' + str(nanosol).zfill(2) + '  |  dmS.nS  |') # time display
	print('-----------------------') # divider
	print('| SOL: ' + str(yearDay).zfill(3) + ' | SOL: day |') # sol display
	print('-----------------------') # divider

