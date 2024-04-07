import math
import os
import time

from concurrent.futures import ProcessPoolExecutor

from integrate import integrate_parallel


def main():
    print("ThreadPoolExecutor:\n\n")
    for i in range(1, os.cpu_count() * 2 + 1):
        print(f"{i} threads")
        start_time = time.time()

        print("result: ", integrate_parallel(math.cos, 0, math.pi / 2, n_jobs=i))

        end_time = time.time()
        print("time: ", end_time - start_time)

    print("\n\nProcessPoolExecutor:\n\n")
    for i in range(1, os.cpu_count() * 2 + 1):
        print(f"{i} processes")
        start_time = time.time()

        print("result: ", integrate_parallel(math.cos, 0, math.pi / 2, n_jobs=i, executor=ProcessPoolExecutor))

        end_time = time.time()
        print("time: ", end_time - start_time)


if __name__ == "__main__":
    main()
