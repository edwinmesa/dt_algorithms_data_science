import timeit
import functools

def timeit_big_o(func):
    @functools.wraps(func) # to preserve the original function's name and
    def wrapper(*args, **kwargs):
        num_runs   = 5
        exec_times = timeit.repeat(lambda: func(*args, **kwargs), number = 1, repeat=num_runs)

        avg_time = sum(exec_times) / num_runs
        min_time = min(exec_times)
        max_time = max(exec_times)

        print(f"Function '{func.__name__}':")
        print(f"Avg execution time: {avg_time:.6f} seconds")
        print(f"Min execution time: {min_time:.6f} seconds")
        print(f"Max execution time: {max_time:.6f} seconds")

        return func(*args, **kwargs)

    return wrapper