# Jacob Faulk

WILDCARD_CHAR = '*'


def main():
    with open("input/day2input.txt", 'r') as f:
        input_list = [line[:-1] for line in f]
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
    for word1 in range(len(input_list)):
        substitutions = []
        for char in range(len(input_list[word1])):
            substitutions.append(
                input_list[word1][:char] + WILDCARD_CHAR + input_list[word1][char+1:])
        for word2 in range(word1+1, len(input_list)):
            for current_sub in substitutions:
                match = True
                for char in range(len(input_list[word2])):
                    if not (input_list[word2][char] == current_sub[char] or current_sub[char] == WILDCARD_CHAR):
                        match = False
                if match:
                    return input_list[word1], input_list[word2]
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
