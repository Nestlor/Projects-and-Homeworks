from time import sleep  
from datetime import datetime
import random
import os
os.chdir('d:/DEV/PYTHON/lesson22/')

from threading import Thread

def write_random_number(index):
    sleep(1)
    with open(f'output_{index}.txt', 'w') as file:
        file.write(str(random.randint(1, 1000)))

start_time = datetime.now()
for i in range(1000):
    write_random_number(i)

threads = []

for i in range(1000):
    thread = Thread(target=write_random_number, args=(i, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = datetime.now()
time_passed = end_time - start_time
print(f"прошло времени: {time_passed} секунд.")