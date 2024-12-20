#--- Day 1: Trebuchet?! ---
import sys
import re

def valueCalc(arr):
    #something
    arr = cleanString(arr)
    line = re.findall("\d",arr)
    if len(line) == 0:
        print("Empty String")
    print(counter,arr.strip(),line[0] + line[len(line)-1])

    return line[0] + line[len(line)-1]
    
def cleanString(unclean):
    nums = {"one":"o1e","two":"t2o","three":"th3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}
    index = 0
    while index > -1:
        index = len(unclean)-1
        chKey = ""
        for key in nums.keys():
            checkV = unclean.find(key)
            if checkV < index and checkV > -1:
                index = unclean.find(key)
                chKey = key
                        
        if chKey != "":
            unclean = unclean.replace(chKey,nums[chKey])
        else:
            index = -1
        
    return unclean
    
def test_calibration_values():
    # define test cases with expected outcomes
    test_cases = [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ]

    # test get_combined_digits function
    for line, expected in test_cases:
        val = valueCalc(line)
        assert int(val) == expected, f"Failed on {line},{val},{expected}"

    # indicate all tests passed
    print("All tests passed")

if __name__ == "__main__":
    #Setup Arrays/Values
    
    sum = 0
    counter = 1

    #test_calibration_values()
        
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            val = int(valueCalc(line))
            sum += val
            counter += 1
            
    print(sum)