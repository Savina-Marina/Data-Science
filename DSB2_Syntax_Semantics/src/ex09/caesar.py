import sys

def caesar():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments")
    
    mode = sys.argv[1]
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be a number")
    
    if mode not in ("encode" , "decode"):
        raise Exception("Invalid mode")
    
    if mode == "decode":
        shift = -shift
    result = ""

    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char

        elif 'A' <= char <= 'Z':
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char

        else:
            result += char
    print(result)

if __name__ == "__main__":
    caesar()
            

        

    



