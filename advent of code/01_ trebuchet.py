
import helper
input = helper.getFile("./advent of code/inputs/01.txt")
input = [x[0] for x in input]

def part1_naive():
    sum = 0 
    for word in input:
        digits = []
        for x in word: 
            if x.isdigit():
                digits.append(x)
        
        number = int(digits[0] + digits[-1])
        sum += number
    return sum

def part2_anstrengend():

    mapping = helper.make_mapping('0123456789')
    mapping |= helper.make_mapping(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))


    def findCalibValue(line:str, reverse:bool):
        if reverse:
            line = line[::-1]
        bestIdx = len(line) 
        best = None
        for search, digit in mapping.items():
            if reverse:
                 search = search[::-1]
            if search in line:
                idx = line.index(search)
                if idx < bestIdx:
                    bestIdx = idx
                    best = digit 
        return best 

    sum = 0
    for line in input:
        val1 = findCalibValue(line, False) * 10
        val2 = findCalibValue(line, True)

        sum += val1 + val2

    return sum        
        

print(part2_anstrengend())
