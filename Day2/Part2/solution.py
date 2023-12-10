import re

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    game_numbers = []
    array_of_games = []

    for line in lines:
        game_number = (line.split(":"))[0].split("Game ")[1]
        game_numbers.append(int(game_number))

        game = ((line.rstrip()).split(": "))[1]
        pairs = re.split(', |; ', game)
        array_of_hands = []

        for pair in pairs:
            hand = (int(pair.split(" ")[0]), pair.split(" ")[1])
            array_of_hands.append(hand)
        
        array_of_games.append(array_of_hands)

    game_dict = {}

    for index, number in enumerate(game_numbers):
        game_dict[number] = array_of_games[index]

    powers = []

    for key, value in game_dict.items():
        min_red = 0
        min_green = 0
        min_blue = 0

        for pair in value:
            if "red" in str(pair) and pair[0] > min_red:
                min_red = pair[0]
            if "green" in str(pair) and pair[0] > min_green:
                min_green = pair[0]
            if "blue" in str(pair) and pair[0] > min_blue:
                min_blue = pair[0]
        
        power = min_red * min_green * min_blue
        powers.append(power)

    solution = sum(powers)
    print(solution)
    

if __name__ == '__main__':
    main()