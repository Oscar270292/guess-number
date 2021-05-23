import random
r = random.randint(1, 100)

while True:
	num = int(input('請輸入數字： '))
	if r == num:
		print('Right!')
		break
	elif num > r:
		print('too big')
	else:
		print('too small')