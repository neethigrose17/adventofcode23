import math

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    y_value = []
    x_value = []
    char_value = []

    row_index = 0

    for line in lines:
        column_index = 0
        for char in line:
            if char != "\n":
                y_value.append(row_index)
                x_value.append(column_index)
                char_value.append(char)
                column_index += 1
        row_index += 1

    value_dict = dict(zip(zip(x_value, y_value), char_value))

    gears = {}

    line_length = len(lines[0]) - 2 # because of newline
    number_of_lines = len(lines) - 1

    for key, value in value_dict.items():
        if key[0] != 0:
            previous_key = (key[0] - 1, key[1])
            if value_dict[key].isdigit() and value_dict[previous_key].isdigit():
                continue
        number = ""

        coords_of_digits = []

        while value_dict[key].isdigit():
            number += value_dict[key]
            coords_of_digits.append(key)
            if key[0] != line_length:
                key = (key[0] + 1, key[1])
            else:
                break

        if number != "":
            adjacent_coords = []

            for coord in coords_of_digits:
                if coord[0] != 0:
                    left_side = (coord[0] - 1, coord[1])
                    adjacent_coords.append(left_side)

                if coord[0] != line_length:
                    right_side = (coord[0] + 1, coord[1])
                    adjacent_coords.append(right_side)
                
                if coord[1] != 0:
                    top = (coord[0], coord[1] - 1)
                    adjacent_coords.append(top)
                    if coord[0] != 0:
                        upper_left = (coord[0] - 1, coord[1] - 1)
                        adjacent_coords.append(upper_left)
                    if coord[0] != line_length:
                        upper_right = (coord[0] + 1, coord[1] - 1)
                        adjacent_coords.append(upper_right)

                if coord[1] != number_of_lines:
                    bottom = (coord[0], coord[1] + 1)
                    adjacent_coords.append(bottom)
                    if coord[0] != 0:
                        lower_left = (coord[0] - 1, coord[1] + 1)
                        adjacent_coords.append(lower_left)
                    if coord[0] != line_length:
                        lower_right = (coord[0] + 1, coord[1] + 1)
                        adjacent_coords.append(lower_right)


            for coord in adjacent_coords:
                if value_dict[coord] == "*":
                    if coord not in gears.keys():
                        gears[coord] = [int(number)]
                    if coord in gears.keys() and int(number) not in gears[coord]:
                        gears[coord].append(int(number))

    gear_ratios = []
    for key, value in gears.items():
        if len(value) == 2:
            gear_ratios.append(math.prod(value))
    
    print(sum(gear_ratios))


if __name__ == '__main__':
    main()