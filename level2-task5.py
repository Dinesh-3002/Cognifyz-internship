# Program to count the number of occurrence of a word in a text file
# And display the result ina alphabetical order with their respective counts

# Opening a text file
file = open("file.txt", "r")


# creating empty dictionary to store word frequency
d = dict()

# Iterating through each line of the text file
for i in file:
    # Using strip() we are removing all the leading whitespaces and newline characters fom each line
    i = i.strip()
    # Using lower() we are converting all the characters in the text file to lower case characters
    i = i.lower()
    # Using split() we split each line into individual words
    word = i.split(" ")

# Iterate through each word in the text file and update its frequency in the dictionary(d)
    for w in word:
        # Checks if the is already present in the dictionary(d)
        if w in d:
            # If it is present then increment it by 1
            d[w] = d[w]+1
        else:
            # If it is not in the dictionary then add it to dictionary(d) with count of 1
            d[w] = 1
# Closing the file
file.close()

# Printing the contents in the dictionary by displaying each word with its occurrence in alphabetical order
for key in sorted(d.keys()):
    print(key, ':', d[key])
