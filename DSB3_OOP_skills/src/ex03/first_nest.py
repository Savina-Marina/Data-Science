import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise Exception("File does not exist")

        with open(self.path, 'r') as file:
            lines = file.readlines()

        if has_header:
            data_lines = lines[1:]
        else:
            data_lines = lines

        result = []

        for line in data_lines:
            line = line.strip()

            if line not in ("0,1", "1,0"):
                raise Exception("Invalid data string")

            parts = line.split(',')
            result.append([int(parts[0]), int(parts[1])])

        return result

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for row in data:
                if row == [1, 0]:
                    heads += 1
                elif row == [0, 1]:
                    tails += 1
            return heads, tails

        def fractions(self, heads, tails):
            sum = heads + tails
            if sum == 0:
                raise Exception("No data")
            head_frac = int(heads / sum * 10000) / 10000
            tail_frac = int(tails / sum * 10000) / 10000
            return head_frac, tail_frac


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Incorrect number of arguments")

    path = sys.argv[1]

    research = Research(path)
    data = research.file_reader()

    print(data)

    calc = research.Calculations()  

    heads, tails = calc.counts(data)  
    print(heads, tails)

    head_frac, tail_frac = calc.fractions(heads, tails) 
    print(head_frac, tail_frac)
