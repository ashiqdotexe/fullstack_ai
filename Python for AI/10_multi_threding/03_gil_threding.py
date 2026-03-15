import threading
import time
def serve():
    print(f"Preparing {threading.current_thread().name} tea")
    count = 0 
    for i in range(100_000_000):
        count+=1
    print(f"FInished {threading.current_thread().name} tea")

start = time.time()
order_thread = threading.Thread(target=serve, name="masala-1")
brew_thread = threading.Thread(target=serve, name= "masala-2")
order_thread.start()
brew_thread.start()
order_thread.join()
brew_thread.join()
end = time.time()
print(f"Total time taken to finished {end-start}")

