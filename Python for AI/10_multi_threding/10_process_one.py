# comparison between process and threading
import threading
import time
from multiprocessing import Process

class Threading:
    def incremental(self):
        total = 0
        print("Crunching some number")
        for i in range(10**7):
            total +=i 
        print("Crunch finished")
    def threading_main(self):
        start = time.time()
        thredings = [threading.Thread(target=self.incremental) for _ in range(2)]
        [t.start() for t in thredings]
        [t.join() for t in thredings]
        end = time.time()
        return f"{end-start}"
    
class Process:
    def incremental(self):
        total = 0
        print("Crunching some number")
        for i in range(10**7):
            total +=i 
        print("Crunch finished")
    def process_main(self):
        start = time.time()
        processes = [Process(target=self.incremental) for _ in range(2)]
        [t.start() for t in processes]
        [t.join() for t in processes]
        end = time.time()
        return f"{end-start}"



