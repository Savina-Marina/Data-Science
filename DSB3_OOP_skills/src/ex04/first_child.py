import sys
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise Exception("File does not exist")

        if len(lines) < 1:
            raise Exception("Incorrect file structure")

        if has_header:
            data_lines = lines[1:]
        else:
            data_lines = lines

        result = []

        for line in data_lines:
            line = line.strip()

            if not line:
                raise Exception("Invalid data string")

            if line not in ("0,1", "1,0"):
                raise Exception("Invalid data string")

            parts = line.split(',')
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
            for n in range(number_predictions):
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Incorrect number of arguments")

    path = sys.argv[1]

    research = Research(path)
    data = research.file_reader()

    print(data)

    analytics = research.Analytics(data)

    heads, tails = analytics.counts()
    print(heads, tails)

    head_frac, tail_frac = analytics.fractions(heads, tails)
    print(head_frac, tail_frac)

    print(analytics.predict_random(3))

    print(analytics.predict_last())
