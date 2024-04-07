from concurrent.futures import ThreadPoolExecutor
from math import ceil


def integrate(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step

    return acc


def integrate_parallel(f, a, b, n_jobs=1, n_iter=10_000_000, executor=ThreadPoolExecutor):
    n_iter_per_partition = ceil(n_iter / n_jobs)
    partition_len = (b - a) / n_jobs
    tasks = []

    with executor(max_workers=n_jobs) as executor0:
        for i in range(n_jobs):
            new_a = a + i * partition_len
            new_b = new_a + partition_len
            tasks.append(executor0.submit(integrate, f, new_a, new_b, n_iter_per_partition))

        return sum([task.result() for task in tasks])
