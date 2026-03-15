from multiprocessing import Process
import time

def serve():
    print(f"Preaparing your tea")
    count = 0
    for i in range(100_000_000):
        count+=1
    print(f"Finished preparing your tea")
if __name__ == "__main__":
    start = time.time()
    process = Process(target=serve)
    process2 = Process(target=serve)
    process.start()
    process2.start()
    process.join()
    process2.join()
    end = time.time()
    print(f"Total time taken to finished the job is {end - start:.2f} seconds")