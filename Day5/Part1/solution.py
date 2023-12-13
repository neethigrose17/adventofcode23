def read_file():
    with open("test.txt", "r") as file:
        lines = file.readlines()

    seeds = []
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
                for x in line.split():
                    seeds.append(int(x))
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

    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location

def main():

    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = read_file()

    print(seeds)
    print(seed_to_soil)
    print(soil_to_fertilizer)
    print(fertilizer_to_water)
    print(water_to_light)
    print(light_to_temperature)
    print(temperature_to_humidity)
    print(humidity_to_location)

    



    

if __name__ == '__main__':
    main()