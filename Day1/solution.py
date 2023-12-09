def main():

    solution = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        indices = []
        number = ""
        for index, char in enumerate(line):
            if char.isdigit():
                indices.append(index)
        number += line[indices[0]]
        number += line[indices[len(indices) - 1]]
        number = int(number)
        solution += number
        
    print(solution)

if __name__ == '__main__':
    main()