# multi threading is the process of concurrence working.. one task is done and it waits for another task to finish it jobs and then the first task resume its own task again
import time
import threading

def serve_tea(name):
    for _ in range(3):
        print(f"Serving {name}  tea")
        time.sleep(2)
def brew_tea(name):
    for _ in range(3):
        print(f"Brewing {name} tea")
        time.sleep(3)

#initializing the thread
order_thread = threading.Thread(target=serve_tea, args=("masala",)) 
brew_thread = threading.Thread(target=brew_tea, args=("masala",))

# starting the thread
order_thread.start() 
brew_thread.start()

# waiting for the thread to finish its task
order_thread.join()
brew_thread.join()
print("All thread finished")