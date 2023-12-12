
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


    mapping = helper.make_mapping('123456789')
    mapping |= helper.make_mapping(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))
    for line in input:
        bestIdx = 0
        best = None
        for 
        if search in line:
            for search, digit in mapping:
                idx = line.index(search)
                if idx < bestIdx:
                    bestIdx = idx
            


            
    




