import sys

def letter_starter():
    if len(sys.argv) != 2:
        return

    email_v = sys.argv[1]

    with open('employees.tsv', 'r', encoding='utf-8') as f:
        for string in f:
            string = string.strip()
            if not string:
                continue

            clean = string.split('\t')
            if len(clean) < 3:
                continue

            name, surname, email = clean

            if email == email_v:
                print(f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                break


if __name__ == '__main__':
    letter_starter()
