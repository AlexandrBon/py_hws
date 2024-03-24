from multiprocessing import Process
import time
from fib import fib


def main():
    FIB_NUM = 35

    for process_num in range(1, 11):
        tasks = [Process(target=fib, args=(FIB_NUM, )) for _ in range(process_num)]

        start_time = time.time()

        [task.start() for task in tasks]
        [task.join() for task in tasks]

        end_time = time.time()
        print(end_time - start_time)


if __name__ == "__main__":
    main()
