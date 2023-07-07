def a():
	while True:
		print("aaaaaa")
		yield

def b():
	for _ in a():
		print("bbbbbb")

b()
