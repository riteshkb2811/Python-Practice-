from threading import Thread
from time import sleep
class mutli(Thread):
    def run(self):
        for i in range(5):
            print("Hello",i+1)
            sleep(0.2)
class multi1(Thread):
    def run(self):
        for j in range(5):
            print("Hi",j+1)
            sleep(0.2)

if __name__=="__main__":
    t1=mutli()
    t2=multi1() 
    t1.start()
    t2.start()       