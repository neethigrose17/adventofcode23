import re

def main():

    solution = 0

    pattern = re.compile("([0-9]|one|two|three|four|five|six|seven|eight|nine)+?")

    beginning_of_line_pattern = re.compile("^([1-9]|one|two|three|four|five|six|seven|eight|nine)+?")

    number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    with open("test.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        numbers = pattern.findall(line)
        done = False

        while done == False:
            skip = False

            for index, number in enumerate(numbers):
                if skip == True:
                    skip = False
                    continue

                first_occurrence = re.search(number, line)
                pos = first_occurrence.span()[1]
                new_string = line[(pos - 1):]
                new_number = re.search(beginning_of_line_pattern, new_string)

                if new_number == None:
                    done = True
                else:
                    numbers.insert(index + 1, new_number.group())
                    skip = True

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

if __name__ == '__main__':
    main()