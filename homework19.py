import os
os.chdir('D:/DEV/Python/lesson19')
import time
from threading import Thread

def create_file(file_name):
    time.sleep(1)
    with open(file_name, 'w') as file:
        file.write("funny monkey")

start_time = time.time()

threads = []

for i in range(100):
    thread = Thread(target=create_file, args=(f"file_{i}.txt",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
time_passed = end_time - start_time
print(f"прошло времени: {time_passed} секунд.")
