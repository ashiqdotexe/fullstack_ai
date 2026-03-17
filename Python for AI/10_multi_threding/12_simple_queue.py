from multiprocessing import Queue
import time
def save_data_only_queue(queue, items):
    for item in items:
        queue.put(item)
my_item = ["masala tea", "ginger tea"]
my_item_2 = ["mint tea", "cardamom tea"]
start_2 = time.time()
queue_2 = Queue()
save_data_only_queue(queue_2, my_item)
save_data_only_queue(queue_2, my_item_2)
q2 = [queue_2.get() for _ in range(queue_2.qsize())]
end_2 = time.time()
print(f"Items are {q2} and total time taken to finish the job is {end_2 - start_2:.2f} seconds")