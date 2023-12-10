import re

def main():

    solution = 0

    pattern = re.compile("([0-9]|one|two|three|four|five|six|seven|eight|nine)+?")

    beginning_of_line_pattern = re.compile("^([1-9]|one|two|three|four|five|six|seven|eight|nine)+?")

    number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        numbers = []
        length = len(line)
        
        for x in range(0, length - 1):
            new_number = re.search(beginning_of_line_pattern, line)
            if new_number != None:
                numbers.append(new_number.group())
                if new_number.group().isdigit():
                    line = line[1:]
                else:
                    pos = new_number.span()[1]
                    line = line[(pos - 1):]
            if new_number == None and x < length - 1:
                line = line[1:]
            
        if numbers[0] in number_dict.keys():
            first_digit = number_dict[numbers[0]]
        else:
            first_digit = numbers[0]

        if numbers[len(numbers) - 1] in number_dict.keys():
            second_digit = number_dict[numbers[len(numbers) - 1]]
        else:
            second_digit = numbers[len(numbers) - 1]

        number_from_line = first_digit + second_digit
        
        solution += int(number_from_line)

    print(solution)

        # numbers = pattern.findall(line)

        # skip = False
        # done = False

        # for index, number in enumerate(numbers):
        #     if(number.isdigit()):
        #         skip = True

        #     if done == False:
        #         if skip == True:
        #             skip = False
        #             continue

        #         first_occurrence = re.search(number, line)
        #         pos = first_occurrence.span()[1]

        #         new_string = line[(pos - 1):]
        #         new_number = re.search(beginning_of_line_pattern, new_string)

        #         if new_number == None:
        #             last_number = numbers[len(numbers) - 1]
        #             check = new_string.find(last_number)
        #             if check == -1:
        #                 done = True
        #         else:
        #             numbers.insert(index + 1, new_number.group())
        #             skip = True




if __name__ == '__main__':
    main()