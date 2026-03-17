from multiprocessing import Process, Queue

# we can pass Queue as an argument to process

def sava_data_with_process(queue, items):
    for item in items:
        queue.put(item)

if __name__ == "__main__":
    queue = Queue()
    my_item = ["masala tea", "ginger tea"]
    processes = Process(target=sava_data_with_process, args=(queue, my_item,))
    processes.start()
    processes.join()
    q = [queue.get() for _ in range(queue.qsize())]
    print(f"Items are {q}")