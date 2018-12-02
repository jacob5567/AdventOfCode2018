# Jacob Faulk

WILDCARD_CHAR = '*'


def main():
    with open("input/day2input.txt", 'r') as f:
        input_list = f.readlines()
    print(get_checksum(input_list))
    word1, word2 = get_matching_ids(input_list)
    print(get_common_letters(word1, word2))


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


def get_matching_ids(input_list):
    for i in range(len(input_list)):
        substitutions = []
        for k in range(len(input_list[i])):
            substitutions.append(
                input_list[k][:k] + WILDCARD_CHAR + input_list[k][k+1:])
        for j in range(i+1, len(input_list)):
            match = True
            for l in range(len(input_list[j])):
                if not (input_list[j][l] == input_list[i][l] or input_list[j][l] == WILDCARD_CHAR):
                    match = False
            if match:
                return input_list[i], input_list[j]
    print("No match found!")
    exit('1')


def get_common_letters(word1, word2):
    common_letters = []
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common_letters.append(word1[i])
    return "".join(common_letters)


if __name__ == "__main__":
    main()
