from multiprocessing import Process
import time

def save_file(name):
    with open(f"{name}.txt", "w") as file:
        file.write("amar shonar bangla")

if __name__ == "__main__":
    start = time.time()
    process_1 = Process(target=save_file, args=("file1",))
    process_2 = Process(target=save_file, args=("file2",))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    end = time.time()
    print(f"Time taken to finish the job {end-start}")