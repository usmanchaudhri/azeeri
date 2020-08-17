"""
Write a function that takes-in a string and return its longest substring without duplicate characters.
You can safely assume that their will only be one longest substring without duplication


"clementisacap"

- we will traverse the string and will keep track of the repeating characters in a hashmap.
- we will have a start index pointer which will keep track of the start index of the largest string so far.
- when a duplicate character is encountered we will check in the hashmap at what
    index the last position of that character was and move the start_index to the location 1 next to it
"""
def longestSubstringWithoutDuplication(string):
    last_seen = {}
    longest_string = [0, 1] # the current longest string
    start_idx = 0

    for i in range(len(string)):
        character = string[i]
        if character in last_seen:
            start_idx = max(start_idx, last_seen[character]+1)

        if longest_string[1] - longest_string[0] < i + 1 - start_idx:
            # the start_idx is equivalent to longest_string[0]
            # the i+1 is because we have setup longest_string to reflect
            # i+1 as the ending index.

            # if the current difference of the curr_index (where we are at) and start_index
            # is greater than 'i' the current index + current start index than we have found a
            # longer string and we will update the longest_string to longest_string[start_index, i+1]

            longest_string[start_idx, i + 1]

        # this will take case of both cases if we have seen the character or we haven't seen the character
        last_seen[character] = i

    # slicing the array the second element will be -1 so they way we have setup above will take case of
    # this -1 case since we add the i+1 in longest_string[start_idx, i + 1]
    return string[longest_string[0]: longest_string[1]]








