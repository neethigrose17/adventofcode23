def go_north(current_coordinates, distance):
        distance += 1
        previous_location = go_south
        new_coordinates = (current_coordinates[0], current_coordinates[1] - 1)
        return new_coordinates, previous_location, distance

def go_south(current_coordinates, distance):
        distance += 1
        previous_location = go_north
        new_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
        return new_coordinates, previous_location, distance

def go_east(current_coordinates, distance):
        distance += 1
        previous_location = go_west
        new_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
        return new_coordinates, previous_location, distance

def go_west(current_coordinates, distance):
        distance += 1
        previous_location = go_east
        new_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
        return new_coordinates, previous_location, distance

def decide_directions(current_coordinates, previous_location, value_dict, height, width):
        directions = {go_north: False, go_south: False, go_east: False, go_west: False}
        directions_to_check = list(directions.keys())

        x_value = current_coordinates[0]
        y_value = current_coordinates[1]

        if previous_location in directions.keys():
            directions_to_check.remove(previous_location)
        if x_value == 0:
            if go_west in directions_to_check: directions_to_check.remove(go_west)
        if y_value == 0:
            if go_north in directions_to_check: directions_to_check.remove(go_north)
        if x_value == width:
            if go_east in directions_to_check: directions_to_check.remove(go_east)
        if y_value == height:
            if go_south in directions_to_check: directions_to_check.remove(go_south)

        for x in directions_to_check:
            if x == go_north:
                if value_dict[(x_value, y_value - 1)] in ("|", "7", "F"):
                    directions[x] = True
            if x == go_south:
                if value_dict[(x_value, y_value + 1)] in ("|", "L", "J"):
                    directions[x] = True
            if x == go_east:
                if value_dict[(x_value + 1, y_value)] in ("-", "J", "7"):
                    directions[x] = True
            if x == go_west:
                if value_dict[(x_value - 1, y_value)] in ("-", "L", "F"):
                    directions[x] = True
        
        return directions

def main():

    with open("test.txt", "r") as file:
        lines = file.readlines()

    y_value = []
    x_value = []
    char_value = []

    starting_coordinates = ()

    row_index = 0

    for line in lines:
        column_index = 0
        for char in line:
            if char != "\n":
                y_value.append(row_index)
                x_value.append(column_index)
                char_value.append(char)
                if char == "S":
                    starting_coordinates = (column_index, row_index)
                column_index += 1
        row_index += 1

    value_dict = dict(zip(zip(x_value, y_value), char_value))

    previous_location = "home"
    height = len(lines) - 1
    width = len(lines[0]) - 2 # because of newlines

    starting_directions = decide_directions(starting_coordinates, previous_location, value_dict, height, width)
    print("starting coordinates are " + str(starting_coordinates))
    print("starting directions are " + str(starting_directions))

    distance = 0
    final_distance = 0

    stop = False

    going_from = starting_coordinates
    
    for key, value in starting_directions.items():
        print("key is " + str(key))
        if starting_directions[key] == True:
            directions = starting_directions
            while directions[key] == True and stop == False:
                new_coordinates, previous_location, distance = key(going_from, distance)
                print("new coordinates are " + str(new_coordinates))
                if new_coordinates != starting_coordinates:
                    directions = decide_directions(new_coordinates, previous_location, value_dict, height, width)
                    going_from = new_coordinates
                    print("new directions are " + str(directions))

                    if all(directions.values()) == False:
                        print("end is " + str(going_from))
                        final_distance = distance
                else:
                    print("end is " + str(new_coordinates))
                    stop = True
                    final_distance = distance
    
    print("distance is " + str(distance))

    print("final distance is " + str(final_distance))


    # if directions["south"]:
    #     new_coordinates, previous_location = go_south(starting_coordinates)

    # if directions["east"]:
    #     new_coordinates, previous_location = go_east(starting_coordinates)

    # if directions["west"]:
    #     new_coordinates, previous_location = go_west(starting_coordinates)


    # remember starting coordinate
    # +1 for each movement
    # if you complete movement and there's nowhere left to go, set "distance" variable to total
    # if you get back to starting coordinates, set "distance" variable to half?
    # create another dictionary for the distance variable and the coordinates?
    # find highest distance variable and find coordinates based on that?
    

if __name__ == '__main__':
    main()