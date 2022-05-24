from typing import List
from generate_data import File
from mixins.sort import Sort


class InsertionSort(Sort):

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__ == "__main__":
    new_file = File()
    new_file.generate_data_and_save_to_file()
    data_to_process = new_file.load_data_from_file()
    print(InsertionSort.measure_func_speed(InsertionSort.insertion_sort, data_to_process))
    #print(data_to_process)

    data_to_process.sort()
    print(InsertionSort.measure_func_speed(InsertionSort.insertion_sort, data_to_process))
    #print(data_to_process)

    data_to_process = data_to_process[::-1]
    print(InsertionSort.measure_func_speed(InsertionSort.insertion_sort, data_to_process))
    #print(data_to_process)