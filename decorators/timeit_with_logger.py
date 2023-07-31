import timeit
import logging

# Set Up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timeit_with_logger(self, func):
    """
    A decorator to measure the execution time of a function and log the results.

    Parameters:
        func (function): The function to be timed.

    Returns:
        function: The wrapped function.
    """
    
    def wrapper(*args, **kwargs):
        start_time  = timeit.default_timer()
        result      = func(*args, **kwargs)
        end_time    = timeit.default_timer()
        exec_time   = end_time - start_time

        logger.info(f"Function '{func.__name__}' executed in {exec_time:.6f} seconds")
        return result

    return wrapper