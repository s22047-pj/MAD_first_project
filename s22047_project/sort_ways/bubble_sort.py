from typing import List
from generate_data import File
from mixins.sort import Sort


class BubbleSort(Sort):

    @staticmethod
    def bubble_sort(arr: List[float]):
        for i in range(len(arr)):
            start = 0
            stop = len(arr) - i - 1
            for j in range(start, stop):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


new_file = File()
new_file.generate_data_and_save_to_file()
data_to_process = new_file.load_data_from_file()
print(BubbleSort.measure_func_speed(BubbleSort.bubble_sort, data_to_process))
print(data_to_process)


if __name__ == "__main__":
    new_file = File()
    new_file.generate_data_and_save_to_file()
    data_to_process = new_file.load_data_from_file()
    print(BubbleSort.measure_func_speed(BubbleSort.bubble_sort, data_to_process))
    # print(data_to_process)

    # data_to_process.sort()
    # print(BubbleSort.measure_func_speed(BubbleSort.bubble_sort, data_to_process))
    # print(data_to_process)
    #
    # data_to_process = data_to_process[::-1]
    # print(BubbleSort.measure_func_speed(BubbleSort.bubble_sort, data_to_process))
    # print(data_to_process)
