from multiprocessing import Process, Queue
import time
# we can pass Queue as an argument to process

def sava_data_with_process(queue, items):
    for item in items:
        queue.put(item)
def save_data_only_queue(queue, items):
    for item in items:
        queue.put(item)

if __name__ == "__main__":
    queue = Queue()
    my_item = ["masala tea", "ginger tea"]
    my_item_2 = ["mint tea", "cardamom tea"]
    start_1 = time.time()
    process_1 = Process(target=sava_data_with_process, args=(queue, my_item,))
    process_2 = Process(target=sava_data_with_process, args=(queue, my_item_2,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    end_1 = time.time()
    q1 = [queue.get() for _ in range(queue.qsize())]
    print(f"Items are {q1} and total time taken to finish the job is {end_1 - start_1:.2f} seconds")