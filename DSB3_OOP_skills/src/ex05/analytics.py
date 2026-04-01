import os
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise Exception("File does not exist")

        with open(self.path, "r") as file:
            lines = file.readlines()

        if len(lines) < 1:
            raise Exception("Incorrect file structure")

        data_lines = lines[1:] if has_header else lines

        result = []
        for line in data_lines:
            line = line.strip()

            if not line:
                raise Exception("Invalid data string")

            if line not in ("0,1", "1,0"):
                raise Exception("Invalid data string")

            parts = line.split(",")
            result.append([int(parts[0]), int(parts[1])])

        return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0

            for row in self.data:
                if row == [1, 0]:
                    heads += 1
                elif row == [0, 1]:
                    tails += 1

            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                raise Exception("No data")

            head_frac = int(heads / total * 10000) / 10000
            tail_frac = int(tails / total * 10000) / 10000
            return head_frac, tail_frac

    class Analytics(Calculations):
        def predict_random(self, number_predictions):
            if number_predictions < 1:
                raise Exception("Incorrect number of predictions")

            result = []
            for _ in range(number_predictions):
                coin = randint(0, 1)
                if coin == 1:
                    result.append([1, 0])
                else:
                    result.append([0, 1])

            return result

        def predict_last(self):
            if len(self.data) == 0:
                raise Exception("No data")
            return self.data[-1]

        def save_file(self, data, file_name, ext):
            if not file_name:
                raise Exception("Incorrect file name")
            if not ext:
                raise Exception("Incorrect file extension")

            safe_ext = ext.lstrip(".")
            full_name = f"{file_name}.{safe_ext}"

            with open(full_name, "w") as f:
                f.write(str(data))

            return full_name
