import multiprocessing as mp
import codecs
import time


def process_a_func(rqueue: mp.Queue, squeue: mp.Queue):
    while True:
        squeue.put(str(rqueue.get()).lower())
        time.sleep(5)


def process_b_func(rqueue: mp.Queue, squeue: mp.Queue):
    while True:
        squeue.put(codecs.encode(str(rqueue.get()), "rot_13"))


def main():
    ma_queue = mp.Queue()
    ab_queue = mp.Queue()
    bm_queue = mp.Queue()

    process_A = mp.Process(target=process_a_func, args=(ma_queue, ab_queue, ))
    process_B = mp.Process(target=process_b_func, args=(ab_queue, bm_queue, ))

    process_A.start()
    process_B.start()

    while True:
        message = input()
        ma_queue.put(message)

        recieved = bm_queue.get()
        print(time.strftime('%X'), ": ", recieved)


if __name__ == "__main__":
    main()
