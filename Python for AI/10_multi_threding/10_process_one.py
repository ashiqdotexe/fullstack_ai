# comparison between process and threading
import threading
import time
from multiprocessing import Process

class Threading:
    def incremental(self):
        total = 0
        print("Crunching some number with threading")
        for i in range(10**9):
            total +=i 
        print("Crunch finished")
    def threading_main(self):
        start = time.time()
        thredings = [threading.Thread(target=self.incremental) for _ in range(2)]
        [t.start() for t in thredings]
        [t.join() for t in thredings]
        end = time.time()
        return f"{end-start:.2f} seconds"
    
class Process_:
    def incremental(self):
        total = 0
        print("Crunching some number with multi-processor")
        for i in range(10**9):
            total +=i 
        print("Crunch finished")
    def process_main(self):
        start = time.time()
        processes = [Process(target=self.incremental) for _ in range(2)]
        [t.start() for t in processes]
        [t.join() for t in processes]
        end = time.time()
        return f"{end-start:.2f} seconds"
    
if __name__ == "__main__":
    thread = Threading()
    process = Process_()
    print(f"Total time taken by thread- {thread.threading_main()}")
    print(f"Total time taken by multi-process- {process.process_main()}")
