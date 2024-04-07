import time
from fib import fib


def main():
    FIB_NUM = 35

    start_time = time.time()
    
    for _ in range(10):
        fib(FIB_NUM)

    end_time = time.time()
    print(end_time - start_time)


if __name__ == "__main__":
    main()
