import threading
import time
counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter+=1
thread = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in thread]
[t.join() for t in thread]
print(f"Total count is {counter}")