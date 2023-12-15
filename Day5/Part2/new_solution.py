def read_file():
    with open("input.txt", "r") as file:
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

    reverse_dict = {"temperature_to_humidity": temperature_to_humidity, "light_to_temperature": light_to_temperature, "water_to_light": water_to_light, "fertilizer_to_water": fertilizer_to_water, "soil_to_fertilizer": soil_to_fertilizer, "seed_to_soil": seed_to_soil}

    return seed_ranges, dict_of_transitions, reverse_dict


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


def find_seeds(seed_ranges, target_range):
    seed_ranges.sort()
    full_seed_ranges = []
    for item in seed_ranges:
        full_seed_ranges.append(range(item[0], item[0] + item[1]))

    for item in full_seed_ranges:
        result = find_intersection(target_range, item)
        if result != None:
            break
    return result


def get_destination_value(source_value, dictionary):
    destination_value = ""

    for key, value in dictionary.items():
        if source_value in range(key[1], key[1] + value):
            destination_value = key[0] + (source_value - key[1])
    print(f"source {source_value} destination {destination_value}")
    return destination_value


def main():
    # get seed ranges and dictionaries
    seed_ranges, dict_of_transitions, reverse_dict = read_file()

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

    seeds_found = False

    final_seeds = None

    while seeds_found == False:
        for item in humidity_ranges:
            next_range = item
            for dictionary in reverse_dict.values():
                if next_range != None:
                    new_range = get_next_range(next_range, dictionary)
                    next_range = new_range
            if next_range != None:
                print(f"last range {next_range}")
                final_seeds = find_seeds(seed_ranges, next_range)
            if final_seeds != None:
                seeds_found = True

    print(final_seeds)

    start_value = final_seeds.start
    print(f"start value {start_value}")
    next_value = ""

    for dictionary in dict_of_transitions.values():
        next_value = get_destination_value(start_value, dictionary)
        start_value = next_value

    location = next_value

    print(location)

    # OR
    
    seed_ranges.sort()
    full_seed_ranges = []
    for item in seed_ranges:
        full_seed_ranges.append(range(item[0], item[0] + item[1]))

    # find range of numbers less than 3113752778 

    # exclusion_start = ""
    # exclusion_end = ""

    # for item in full_seed_ranges:
    #     for key, value in sort_dict(dict_of_transitions["seed_to_soil"]).items():
    #         if item.start < key[1]:
    #             exclusion_start = item.start
    #             if item.stop >= key[1]:
    #                 exclusion_end = key[1]
    #             else:
    #                 exclusion_end = item.stop
    #         exclusion = range(exclusion_start, exclusion_end)

    
    





if __name__ == '__main__':
    main()