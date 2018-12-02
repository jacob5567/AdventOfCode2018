# Jacob Faulk

def main():
    input_file = open("input/day1input.txt", "r")
    input_list = input_file.readlines()
    input_file.close()
    frequency = 0
    for element in input_list:
        if element[0] == '+':
            frequency += int(element[1:])
        else:
            frequency -= int(element[1:])
    print(frequency)


if __name__ == "__main__":
    main()
