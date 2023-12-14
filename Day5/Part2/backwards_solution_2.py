def read_file():
    with open("test.txt", "r") as file:
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

    # seeds = []
    # for x in seed_ranges:
    #     for x in range(x[0], x[0] + x[1]):
    #         seeds.append(x)

    dict_of_transitions = {"seed_to_soil": seed_to_soil, "soil_to_fertilizer": soil_to_fertilizer, "fertilizer_to_water": fertilizer_to_water, "water_to_light": water_to_light, "light_to_temperature": light_to_temperature, "temperature_to_humidity": temperature_to_humidity, "humidity_to_location": humidity_to_location}

    # print(seeds)

    return seed_ranges, dict_of_transitions

def get_temperature_range_from_humidity_range(humidity_range, dict_of_transitions):
    humidity_dict = dict_of_transitions["temperature_to_humidity"]

    possible_temperature_ranges = []

    beginning_of_humidity_range = humidity_range[0]
    ending_of_humidity_range = humidity_range[1]

    for key, value in humidity_dict.items():
        beginning_of_match_range = key[0]
        ending_of_match_range = key[0] + value - 1

        beginning_of_temperature_range = key[1]
        ending_of_temperature_range = key[1] + value - 1

        if beginning_of_match_range <= beginning_of_humidity_range <= ending_of_match_range:
            if ending_of_humidity_range >= ending_of_match_range:
                new_ending = ending_of_match_range
            else:
                new_ending = 
            if beginning_of_humidity_range >= beginning_of_match_range:
                new_beginning = beginning_of_humidity_range
            else:
                new_beginning = beginning_of_match_range


def get_humidity_range_from_min_location(dict_of_transitions):

    # destination, source, range-length
    
    reverse_dict = dict_of_transitions["humidity_to_location"]

    locations = []

    keys = reverse_dict.keys()
    for key in keys:
        locations.append(key[0])

    closest_location = min(locations)
    print(f"closest location {closest_location}")

    for key, value in reverse_dict.items():
        if key[0] == closest_location:
            humidity_range = (key[1], key[1] + value - 1)
    print(f"humidity range {humidity_range}")
    return humidity_range


def make_transition(location_range, transition_type, dict_of_transitions):
    # destination_array = []
    
    transition_dict = dict_of_transitions[transition_type]
    
    for item in location_range:
        destination = ""
        for key in transition_dict.keys():
            if item in range(key[1], key[1] + transition_dict[key]):
                destination = key[0] + (item - key[1])
                location_range.append(destination)
        if destination == "":
            destination = item
            location_range.append(destination)
    # return destination_array


def main():

    seed_ranges, dict_of_transitions = read_file()

    humidity = get_humidity_range_from_min_location(dict_of_transitions)



    # START OVER:
    # find lowest location range
    # find humidity ranges that corresponds to
    # find temperature ranges that correspond to
    # find light ranges that correspond to
    # find water ranges that correspond to
    # find fertilizer ranges that correspond to
    # find soil ranges that correspond to
    # find seed ranges that correspond to
    # 
    # IF THERE ARE ANY SEED RANGES for the lowest location range then
    # find lowest number in the range that matches?
    # 
    # If not, repeat



    # soils = make_transition(seeds, "seed_to_soil", dict_of_transitions)
    # fertilizers = make_transition(soils, "soil_to_fertilizer", dict_of_transitions)
    # waters = make_transition(fertilizers, "fertilizer_to_water", dict_of_transitions)
    # lights = make_transition(waters, "water_to_light", dict_of_transitions)
    # temperatures = make_transition(lights, "light_to_temperature", dict_of_transitions)
    # humidities = make_transition(temperatures, "temperature_to_humidity", dict_of_transitions)
    # locations = make_transition(humidities, "humidity_to_location", dict_of_transitions)

    # solution = min(locations)
    # print(solution)
    

if __name__ == '__main__':
    main()