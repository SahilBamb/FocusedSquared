import time


def countDownTime(t):
	while timeLeft:
		minutes, seconds = divmod(t, 60)
		timeText = '{:02d}:{:02d}'.format(minutes, seconds)
		print(timeText)
		time.sleep(1)
		t -= 1

for x in range(4):
	print(x)