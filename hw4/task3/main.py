import multiprocessing as mp
from threading import Thread
import codecs
import time
import queue


SEND_THRESHOLD_SECONDS = 5.0

def process_a_func(rqueue: mp.Queue, squeue: mp.Queue):
    last_send = time.time() - SEND_THRESHOLD_SECONDS
    messages = []

    while True:
        try:
            message = rqueue.get(block=False)
            messages.append(str(message).lower())
        except queue.Empty:
            pass

        now = time.time()
        if len(messages) != 0 and now - last_send > SEND_THRESHOLD_SECONDS:
            squeue.put(messages.pop(0))
            last_send = now


def process_b_func(rqueue: mp.Queue, squeue: mp.Queue):
    while True:
        encoded_message = codecs.encode(str(rqueue.get()), "rot_13")
        print(time.strftime('%X'), ": ", encoded_message)
        squeue.put(encoded_message)


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


if __name__ == "__main__":
    main()
