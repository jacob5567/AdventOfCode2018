# Jacob Faulk

def main():
    input_file = open("input/day1input.txt", "r")
    input_list = input_file.readlines()
    input_file.close()
    print(find_duplicate_frequency(input_list))

def find_duplicate_frequency(input_list):
    frequency = 0
    frequency_set = set()
    while True:
        for element in input_list:
            if element[0] == '+':
                frequency += int(element[1:])
            else:
                frequency -= int(element[1:])
            if frequency in frequency_set:
                return frequency
            else:
                frequency_set.add(frequency)


if __name__ == "__main__":
    main()
