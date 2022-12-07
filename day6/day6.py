datastream = open("input.txt", "r").read()


def all_characters_different(s):
    seen_characters = set()  # initialize empty set

    for c in s:
        if c in seen_characters:  # character already seen
            return False  # not all characters are different

        seen_characters.add(c)  # add character to set

    return True  # all characters are different


def find_marker(datastream):
    buffer = datastream[:14]  # initialize buffer with first four characters

    for i, c in enumerate(datastream[14:]):  # iterate over remaining characters in datastream

        if all_characters_different(buffer):  # check if characters are different
            return i + 14  # return index of last character in buffer plus 4

        buffer = buffer[1:] + c  # add new character at the beginning and remove last character from the end

    return -1

# example:
marker_index = find_marker(datastream)
print(marker_index)  # should output 7