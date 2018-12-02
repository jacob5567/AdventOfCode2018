# Jacob Faulk


def main():
    input_string = input("Enter frequency changes: ")
    frequency = 0
    input_list = input_string.split(", ")
    for element in input_list:
        if element[0] == '+':
            frequency += int(element[1:])
        else:
            frequency -= int(element[1:])
    print(frequency)


if __name__ == "__main__":
    main()
