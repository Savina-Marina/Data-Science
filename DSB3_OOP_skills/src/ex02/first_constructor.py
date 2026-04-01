import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.path.exists(self.path):
            raise Exception("File does not exist")

        with open(self.path, 'r') as file:
            file_new = file.readlines()

        if len(file_new) < 2:
            raise Exception("Incorrect file structure")

        heading = file_new[0].strip()
        value = heading.split(',')
        if len(value) != 2:
            raise Exception("Incorrect heading structure")

        for line in file_new[1:]:
            line = line.strip()
            if line not in ("0,1", "1,0"):
                raise Exception("Invalid data string")

        return "".join(file_new)


def first_constructor():
    if len(sys.argv) != 2:
        raise Exception("python3 first_constructor.py data.csv")

    filepath = sys.argv[1]
    research = Research(filepath)
    result = research.file_reader()
    print(result)


if __name__ == "__main__":
    first_constructor()
