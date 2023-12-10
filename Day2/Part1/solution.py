import re

def main():

    red_limit = 12
    green_limit = 13
    blue_limit = 14

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

    allowed_games = game_numbers

    for key, value in game_dict.items():
        for pair in value:
            if "red" in str(pair) and pair[0] > red_limit:
                if key in allowed_games: allowed_games.remove(key)
            if "green" in str(pair) and pair[0] > green_limit:
                if key in allowed_games: allowed_games.remove(key)
            if "blue" in str(pair) and pair[0] > blue_limit:
                if key in allowed_games: allowed_games.remove(key)

    solution = sum(allowed_games)
    print(solution)
    

if __name__ == '__main__':
    main()