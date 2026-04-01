class Research:
    def file_reader(self):
        with open('data.csv', 'r', encoding='utf-8') as file:
            return file.read()

print(Research().file_reader())