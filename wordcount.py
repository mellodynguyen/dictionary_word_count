"""Count words in file."""
#create function
    #open file
    #loop over each line
def count_words_in_file (filename):
    # goal of func is to count how many times a word appears
    # the = x amount of times

    #create empty dictionary for words
    word_count = {}

    file = open(filename)

    # loop to go through each line in file
    for line in file:
        
        words = line.rstrip().split(" ")
        # print(words) -> saw it created a list of words from the line

        # loop over words to count each time word appears
        for word in words:
            # similar to lecture
            word_count[word] = word_count.get(word, 0) + 1
    for key in word_count:
        # printing key value pairs
        # value = word_count
        print(f"{key} {word_count[key]}")
        #example:
        #As 1
        #I 2
        # was 1


    # print(word_count)
    return word_count
    
    # need to pick when file closes (aka when to stop pulling data)
    # 
count_words_in_file("twain.txt")
