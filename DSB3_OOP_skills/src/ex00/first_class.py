class Must_Read:
    with open('data.csv', 'r', encoding='utf-8') as file:
        text = file.read()
    print(text)