def read_file():
    with open("test2.txt", "r") as file:
        lines = file.readlines()

    seed_ranges = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    current_category = ""
    for line in lines:
        if line.startswith("seeds"):
            current_category = "seeds"
        if line.startswith("seed-to-soil"):
            current_category = "seed-to-soil"
        if line.startswith("soil-to-fertilizer"):
            current_category = "soil-to-fertilizer"
        if line.startswith("fertilizer-to-water"):
            current_category = "fertilizer-to-water"
        if line.startswith("water-to-light"):
            current_category = "water-to-light"
        if line.startswith("light-to-temperature"):
            current_category = "light-to-temperature"
        if line.startswith("temperature-to-humidity"):
            current_category = "temperature-to-humidity"
        if line.startswith("humidity-to-location"):
            current_category = "humidity-to-location"
        if line.startswith("\n"):
            current_category = ""

        if line[:1].isdigit():
            if current_category == "seeds":
                for x in range(0, len(line.split()), 2):
                    seed_ranges.append((int(line.split()[x]), int(line.split()[x+1])))
            if current_category == "seed-to-soil":
                seed_to_soil[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "soil-to-fertilizer":
                soil_to_fertilizer[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "fertilizer-to-water":
                fertilizer_to_water[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "water-to-light":
                water_to_light[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "light-to-temperature":
                light_to_temperature[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "temperature-to-humidity":
                temperature_to_humidity[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])
            if current_category == "humidity-to-location":
                humidity_to_location[(int(line.split()[0]), int(line.split()[1]))] = int(line.split()[2])


    dict_of_transitions = {"seed_to_soil": seed_to_soil, "soil_to_fertilizer": soil_to_fertilizer, "fertilizer_to_water": fertilizer_to_water, "water_to_light": water_to_light, "light_to_temperature": light_to_temperature, "temperature_to_humidity": temperature_to_humidity, "humidity_to_location": humidity_to_location}
    return seed_ranges, dict_of_transitions


def find_intersection(range_one, range_two):
    intersection_start = max(range_one.start, range_two.start)
    intersection_stop = min(range_one.stop, range_two.stop)

    if intersection_start < intersection_stop:
        return range(intersection_start, intersection_stop)
    else:
        return None
    

def sort_dict(dictionary):
    return dict(sorted(dictionary.items()))

def get_next_range(old_range, dictionary):
    dictionary = sort_dict(dictionary)

    next_range = None

    for key, value in dictionary.items():
        corresponding_range = range(key[0], key[0] + value)
        overlap = find_intersection(old_range, corresponding_range)
        if overlap != None:
            next_range = range(key[1], key[1] + len(overlap))
            print(f"next range {next_range}")
            break
        
    return next_range


def main():
    # get seed ranges and dictionaries
    seed_ranges, dict_of_transitions = read_file()

    # destination, source, range-length
    
    # sort last dictionary small to large
    # get smallest location range
    
    humidity_to_location_sorted = sort_dict(dict_of_transitions["humidity_to_location"])
    # print(f"humidity to location {humidity_to_location_sorted}")

    humidity_ranges = []

    for key, value in humidity_to_location_sorted.items():
        humidity_range = range(key[1], key[1] + value)
        humidity_ranges.append(humidity_range)

    print(f"humidity range {humidity_ranges[0]}")

    temperature_range = get_next_range(humidity_ranges[0], dict_of_transitions["temperature_to_humidity"])
    light_range = get_next_range(temperature_range, dict_of_transitions["light_to_temperature"])
    water_range = get_next_range(light_range, dict_of_transitions["water_to_light"])
    fertilizer_range = get_next_range(water_range, dict_of_transitions["fertilizer_to_water"])
    soil_range = get_next_range(fertilizer_range, dict_of_transitions["soil_to_fertilizer"])
    seed_range = get_next_range(soil_range, dict_of_transitions["seed_to_soil"])

    print(f"seed range {seed_range}")

    # seeds_found = False

    # while seeds_found == False:
    #     for next_range in humidity_ranges:
    #         for dictionary in dict_of_transitions.values():
    #             next_range = get_next_range(next_range, dictionary)
    #         if next_range != None:
    #             print("found a seed range")
    #             seeds_found = True

    # find corresponding humidity ranges, in order - DONE
    # find corresponding temperature range
    # find corresponding light range
    # find corresponding water range
    # find fertilizer range
    # find soil range
    # find target seed range
    
    # sort seed ranges small to large
    # find if target seed range overlaps with any existing seed ranges
    # find lowest seed number in overlap???

    # temperature_to_humidity_sorted = sort_dict(dict_of_transitions["temperature_to_humidity"])
    # print(f"temperature to humidity {temperature_to_humidity_sorted}")

    # overlap = None

    # for key, value in temperature_to_humidity_sorted.items():
    #     humidity_range = range(key[0], key[0] + value)
    #     print(f"new humidity range {humidity_range}")
    #     overlap = find_intersection(humidity_ranges[0], humidity_range)
    #     if overlap != None:
    #         next_range = range(key[1], key[1] + len(overlap))
    #         print(f"next range {next_range}")
    #         break
        
    # print(f"overlap {overlap}")
    # print(len(overlap))

    # get next range
    
    # next_range = 



if __name__ == '__main__':
    main()