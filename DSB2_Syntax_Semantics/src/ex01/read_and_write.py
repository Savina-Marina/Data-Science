import csv 

def read_and_write():

    with open('ds.csv', 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.reader(csv_file)
        with open('ds.tsv', 'w', encoding='utf-8', newline='') as tsv_file:
            writer = csv.writer(tsv_file, delimiter='\t')

            for line in reader:
                writer.writerow(line)

if __name__ == '__main__':
    read_and_write()
    