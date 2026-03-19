# When we use daemon=True in our program- it basically means that the thread will stop whenever we are finished with our task
import time, threading
def tea_order():
    while True:
        print("monitoring tea temparature")
        time.sleep(1)
t = threading.Thread(target=tea_order, daemon=True)
t.start()
print("Tea monitoring finished")
