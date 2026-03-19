#It will run finitely even after we finish our main task
import time, threading
def tea_order():
    while True:
        print("monitoring tea temparature")
        time.sleep(1)
t = threading.Thread(target=tea_order)
t.start()
print("Tea monitoring finished")
