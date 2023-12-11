def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    card_values = []

    for line in lines:
        winning_numbers = set((line.rstrip()).split(': ')[1].split(" | ")[0].split(" "))
        numbers_you_have = set((line.rstrip()).split(': ')[1].split(" | ")[1].split(" "))

        common_numbers = winning_numbers.intersection(numbers_you_have)
        how_many = len(common_numbers)

        if how_many > 0:
            if how_many == 1:
                value_of_card = 1
            if how_many > 1:
                value_of_card = 2 ** (how_many - 1)
            card_values.append(value_of_card)
    
    print(sum(card_values))
    

if __name__ == '__main__':
    main()