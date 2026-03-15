# All the task done at a single time
from multiprocessing import Process
import time
def serve_tea(name):
    print(f"Serving {name} tea")
    time.sleep(3)
    print(f"End of serving {name} tea")

if __name__ == "__main__":
    tea_makers = [
        Process(target=serve_tea, args=(tea,)) 
        for tea in ["masala", "ginger", "min"]
    ]
    for process in tea_makers:
        process.start()
    for process in tea_makers:
        process.join()
    print("All tea has been served")