import re

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    number_of_lines = len(lines)

    copies = {}

    for x in range(1, number_of_lines + 1):
        copies[x] = 1

    for line in lines:
        index = int((line.rstrip()).split(':')[0].split()[1])

        winning_numbers = set((line.rstrip()).split(': ')[1].split(" | ")[0].split())
        numbers_you_have = set((line.rstrip()).split(': ')[1].split(" | ")[1].split())

        common_numbers = winning_numbers.intersection(numbers_you_have)
        how_many = len(common_numbers)

        if how_many > 0:
            for x in range(1, how_many + 1):
                if index + x <= number_of_lines:
                    copies[index + x] += copies[index]

    total_cards = sum(copies.values())

    print(total_cards)
    

if __name__ == '__main__':
    main()