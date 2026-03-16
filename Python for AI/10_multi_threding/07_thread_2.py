import threading
import time

def serve(type_, wait):
    print(f"Preparing {type_} tea")
    time.sleep(wait)
    print(f"{type_} tea prepared")

start = time.time()
t1 = threading.Thread(target=serve, args=("masala", 2,))
t2 = threading.Thread(target=serve, args=("ginger", 3,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Total time taken to finish is- {end-start:.2f}")