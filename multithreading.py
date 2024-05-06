import threading


def print_numbers():
    for i in range(1, 6):
        print("Thread 1:", i)


def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print("Thread 2:", letter)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Threads finished its work!")
