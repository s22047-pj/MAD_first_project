import random
from typing import Iterable
from os.path import exists


class File:

    def __init__(self, file_name="random_data.txt"):
        self._file_name = file_name

    def generate_data(self, data_n: int) -> Iterable:
        # Generate random float data between 0 and data_n 100 by default
        for i in range(data_n):
            yield round(random.uniform(0, 100), 5)

    def save_data_to_file(self, generator_data: Iterable) -> None:
        # Save data to a file random_data.txt by default
        try:
            with open(self._file_name, 'w') as save_to_file:
                for random_num in generator_data:
                    save_to_file.write(str(random_num) + '\n')
        finally:
            save_to_file.close()

    def load_data_from_file(self) -> list:
        # Load data from file and return as list of floats
        with open(self._file_name, "r") as file_data:
            f_list = [float(i) for i in file_data.readlines() if i.strip()]
        return f_list

    def generate_data_and_save_to_file(self, data_n: int = 300001) -> None:
        if not exists(self._file_name):
            random_data = self.generate_data(data_n)
            self.save_data_to_file(random_data)


if __name__ == '__main__':
    new_file = File
    new_file.generate_data_and_save_to_file()
