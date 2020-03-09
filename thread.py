import threading
from queue import Queue
import time

print_lock =threading.Lock()
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()
        
q=Queue()
# 10 thread
for x in range(10):
    t=threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()
#20 cong viec , one work =0.5s .Neu dung da luong se mat 1.1s
#Nguoc lai neu dung don luong se mat 10 s

for worker in range(20):
    q.put(worker)

q.join()
print('Entire job took:',time.time()-start)
