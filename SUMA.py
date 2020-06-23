suma = 0
while True:
	try:
		a = int(input())
		suma+=a
		print(suma)
	except EOFError:
		exit()
	
