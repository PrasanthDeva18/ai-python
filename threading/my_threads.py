import threading
import time

def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2) # Simulating a 2-second network delay
    print(f"Finished download: {file_name}")

# Create two threads
thread1 = threading.Thread(target=download_file, args=("image1.jpg",))
thread2 = threading.Thread(target=download_file, args=("image2.jpg",))

# Start both threads (they run at the same time)
thread1.start()
thread2.start()

# Wait for both to finish before moving on
thread1.join()
thread2.join()

print("All downloads complete!")
