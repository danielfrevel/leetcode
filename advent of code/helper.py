import os
#z.B. "./inputs/01.txt

def getFile(filename:str):
    print(os.getcwd())

    if not os.path.isfile(filename):
        print(f"File does not exist: {filename}")
        return None

    with open(filename, 'r') as file:
        rawinput = file.read()

    input = [line.split(" ") for line in rawinput.split("\n")]
    return input


def make_mapping(digit_sequence):
    mapping = {}
    for d, c in enumerate(digit_sequence):
        mapping[c] = d
    return mapping
