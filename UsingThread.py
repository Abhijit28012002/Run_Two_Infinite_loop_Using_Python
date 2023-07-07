from time import sleep
from threading import Thread




def a():
	while True:
		print("aaaaaa")
		sleep(1)

def b():
	while True:
		print("bbbbbb")
		sleep(1)

thread1=Thread(target=a)
thread1.start()

thread2=Thread(target=b)
thread2.start()
