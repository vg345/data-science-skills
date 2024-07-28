# Program to take user input (sentence) and return every alternate word in uppercase

# user input
string = input("Enter a sentence here:\n")

# split the string into characters. 
character_list = list(string)
print(character_list)   # works as expected.


index1 = 0              # start index counter for the first loop 
build_characters = []   # declare list to store characters in the required case.

# iterate over every character in list
for character in character_list:
    # uppercase if index is even, lowercase otherwise. 
    if index1 % 2 == 0:
        character = character.upper()
    else:
        character = character.lower()
    # increase index counter every time you loop
    index1 += 1 
    # add the modified character to list
    build_characters.append(character)

# create new string with characters alterrnating in upper and lower case. 
alternate_characters = "".join(build_characters)
print(alternate_characters) # works as expected

# split string into words
word_list = string.split()
print(word_list) # works as expected


index2 = 0              # start index counter for second loop
build_words = []        # declare list variable to store modified words.

# iterate over every word in list
for word in word_list: 
    # as per the task description, every odd indexed word needs to be in upper case, and even indexes in lower case
    if index2 % 2 == 1:
        word = word.upper()
    else:
        word = word.lower()
    # increase index counter in every loop
    index2 += 1
    # add modified words to list
    build_words.append(word)

# create new string with words alternating in upper and lower case
alternate_words = " ".join(build_words)
print(alternate_words) # works fine. 