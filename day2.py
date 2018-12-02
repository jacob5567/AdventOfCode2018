# Jacob Faulk


def main():
    with open("input/day2input.txt",'r') as f:
        input_list = f.readlines()
    print(get_checksum(input_list))
    


def get_checksum(input_list):
    num_twos = 0
    num_threes = 0
    for element in input_list:
        two = False
        three = False
        letters_list = list(set(element))
        for letter in letters_list:
            if element.count(letter) == 2:
                two = True
            if element.count(letter) == 3:
                three = True
        if two:
            num_twos += 1
        if three:
            num_threes += 1
    return num_twos * num_threes



if __name__ == "__main__":
    main()
