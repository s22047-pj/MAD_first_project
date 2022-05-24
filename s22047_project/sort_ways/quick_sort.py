from typing import List
from generate_data import File
from mixins.sort import Sort
import sys
sys.setrecursionlimit(5000)


class QuickSort(Sort):

    @staticmethod
    def quick_sort(arr: List[float], p: int, r: int):
        if p < r:
            q = QuickSort.quick_sort_partition(arr, p, r)
            QuickSort.quick_sort(arr, p, q-1)
            QuickSort.quick_sort(arr, q+1, r)

    @staticmethod
    def quick_sort_partition(arr: List[float], p: int, r: int):
        x = arr[r]
        i = p-1
        for j in range(p, r):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1


if __name__ == "__main__":
    new_file = File()
    new_file.generate_data_and_save_to_file()
    data_to_process = new_file.load_data_from_file()

    # print(QuickSort.measure_func_speed(QuickSort.quick_sort, data_to_process, 0, len(data_to_process)-1))
    # print(data_to_process)

    # data_to_process.sort()
    # print(QuickSort.measure_func_speed(QuickSort.quick_sort, data_to_process, 0, len(data_to_process)-1))
    # print(data_to_process)

    # ata_to_process = data_to_process[::-1]
    # print(QuickSort.measure_func_speed(QuickSort.quick_sort, data_to_process, 0, len(data_to_process)-1))
    # print(data_to_process)
