import re

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    indexes = {}

    for line in lines:
        index = int((line.rstrip()).split(':')[0].split()[1])

        winning_numbers = set((line.rstrip()).split(': ')[1].split(" | ")[0].split())
        numbers_you_have = set((line.rstrip()).split(': ')[1].split(" | ")[1].split())

        common_numbers = winning_numbers.intersection(numbers_you_have)
        how_many = len(common_numbers)

        if how_many > 0:
            current_index = index
            for x in range(how_many):
                if current_index + 1 <= 207:
                    if current_index + 1 not in indexes.keys():
                        indexes[current_index + 1] = 1
                    else:
                        indexes[current_index + 1] += 1
                    current_index += 1

    total_cards = len(lines) + sum(indexes.values())

    print(total_cards)
    

if __name__ == '__main__':
    main()