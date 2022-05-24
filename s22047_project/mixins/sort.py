from abc import ABC, abstractmethod
import time
from typing import Callable, List


class Sort(ABC):
    @staticmethod
    @abstractmethod
    def measure_func_speed(func: Callable, arr, *args) -> str:
        start = time.time()
        try:
            func(arr, *args)
            exe_time = time.time() - start
            return "Executing sorting: '{}' has took: {} seconds".format(func.__name__, exe_time)
        except Exception as e:
            print(e)
            return str(time.time() - start)

    # @staticmethod
    # def try_to_sort(func: Callable, arr: list, *args):  # TODO p: int, r: int):
    #     try:
    #         func(arr, *args)
    #     except Exception as e:
    #         print(e)
