import threading
import time 
def boil_milk():
    print("Start boiling milk")
    time.sleep(2)
    print("Finished boiling milk")
def burn_toast():
    print("Start toasting")
    time.sleep(3)
    print("Finished toasting")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=burn_toast)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Finished! Total time taken {end-start:.2f} seconds")