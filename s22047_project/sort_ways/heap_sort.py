from typing import List
from generate_data import File
from mixins.sort import Sort


class HeapSort(Sort):

    @staticmethod
    def heapify(arr: List[float], n, i):
        largest_element = i
        left_half = 2 * i + 1
        right_half = 2 * i + 2
        if left_half < n and arr[i] < arr[left_half]:
            largest_element = left_half
        if right_half < n and arr[largest_element] < arr[right_half]:
            largest_element = right_half
        if largest_element != i:
            arr[i], arr[largest_element] = arr[largest_element], arr[i]
            HeapSort.heapify(arr, n, largest_element)

    @staticmethod
    def heap_sort(arr):
        arr_length = len(arr)

        start = int(arr_length/(2-1))
        stop = -1
        step = -1
        for i in range(start, stop, step):
            HeapSort.heapify(arr, arr_length, i)

        start = arr_length - 1
        stop = 0
        step = -1
        for i in range(start, stop, step):
            arr[i], arr[0] = arr[0], arr[i]
            HeapSort.heapify(arr, i, 0)


if __name__ == "__main__":
    new_file = File()
    new_file.generate_data_and_save_to_file()
    data_to_process = new_file.load_data_from_file()
    print(HeapSort.measure_func_speed(HeapSort.heap_sort, data_to_process))
    #print(data_to_process)

    data_to_process.sort()
    print(HeapSort.measure_func_speed(HeapSort.heap_sort, data_to_process))
    #print(data_to_process)

    data_to_process = data_to_process[::-1]
    print(HeapSort.measure_func_speed(HeapSort.heap_sort, data_to_process))
    #print(data_to_process)


"""
Executing sorting: 'heap_sort' has took: 4.299959659576416 seconds
Executing sorting: 'heap_sort' has took: 4.2588794231414795 seconds
Executing sorting: 'heap_sort' has took: 3.9440386295318604 seconds
"""
