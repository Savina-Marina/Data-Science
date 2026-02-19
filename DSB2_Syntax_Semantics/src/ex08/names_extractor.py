import sys

def names(word):
    return word[0].upper() + word[1:].lower()

if len(sys.argv) != 2:
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    emails = f.read().splitlines()

lines = []
for email in emails:
    name_part = email.split('@')[0]
    name, surname = name_part.split('.')
    name = names(name)
    surname = names(surname)
    lines.append(f"{name}\t{surname}\t{email}")

with open('.employees.tsv', 'w') as f:
    f.write("Name\tSurname\tE-mail\n")
    f.write("\n".join(lines))