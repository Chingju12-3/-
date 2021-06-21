import random
r = random.randint(1,10)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('bingo')
		break
	elif num > r:
		print('您猜的數字比答案大喔!')	
	elif num < r:
		print('您猜的數字比答案小喔!')	