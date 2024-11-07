# An example introducint split() and join()


# Virgil, circa 29–19 BCE: Aeneid
 
original = "Sunt hic etiam sua praemia laudi; \
sunt lacrimae rerum et mentem mortalia tangunt. \
Solve metus; feret haec aliquam tibi fama salutem."

translation = "Here, too, the praiseworthy has its rewards; \
there are tears for things and mortal things touch the mind. \
Release your fear; this fame will bring you some safety."

# split it into separate words. 
# Here '.' and ' ' are the delimiters 
# TO DO: add ';'

mylistofwords = original.split('. ')

# prepare the result list
myresultlist = []

# now, sent each sentence to be transformed
for word in mylistofwords:

    # test: does the sentence start with uppercase?
    if word[0] == word[0].upper():
        print('This is a capitalised sentence: ', word)

        # fix the uppercase into lowercase!
        occurence =  word[0].lower() + word[1:]
    else:
        # do nothing, the word is fine as it is
        occurence = word

    myresultlist.append(occurence)

print(' '.join(myresultlist))


