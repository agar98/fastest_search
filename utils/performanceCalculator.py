import time
import utils.globalVariables as globalVariables


def performance(func):
    def wrap(*args, **kwargs):

        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        globalVariables.performance_list.append((func.__name__, end-start))

        return result

    return wrap
