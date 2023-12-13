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

    seeds = []
    for x in seed_ranges:
        for x in range(x[0], x[0] + x[1]):
            seeds.append(x)

    dict_of_transitions = {"seed_to_soil": seed_to_soil, "soil_to_fertilizer": soil_to_fertilizer, "fertilizer_to_water": fertilizer_to_water, "water_to_light": water_to_light, "light_to_temperature": light_to_temperature, "temperature_to_humidity": temperature_to_humidity, "humidity_to_location": humidity_to_location}

    print(seeds)

    return seeds, dict_of_transitions

def make_transition(source_array, transition_type, dict_of_transitions):
    destination_array = []
    transition_dict = dict_of_transitions[transition_type]

    for item in source_array:
        destination = ""
        for key in transition_dict.keys():
            if item in range(key[1], key[1] + transition_dict[key]):
                destination = key[0] + (item - key[1])
                destination_array.append(destination)
        if destination == "":
            destination = item
            destination_array.append(destination)
    return destination_array


def main():

    seeds, dict_of_transitions = read_file()

    soils = make_transition(seeds, "seed_to_soil", dict_of_transitions)
    fertilizers = make_transition(soils, "soil_to_fertilizer", dict_of_transitions)
    waters = make_transition(fertilizers, "fertilizer_to_water", dict_of_transitions)
    lights = make_transition(waters, "water_to_light", dict_of_transitions)
    temperatures = make_transition(lights, "light_to_temperature", dict_of_transitions)
    humidities = make_transition(temperatures, "temperature_to_humidity", dict_of_transitions)
    locations = make_transition(humidities, "humidity_to_location", dict_of_transitions)

    solution = min(locations)
    print(solution)
    

if __name__ == '__main__':
    main()