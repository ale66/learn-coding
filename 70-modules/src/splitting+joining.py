'''
Learn how to use split() and join() with examples
'''

# Virgil's Aeneid, circa 29–19 BCE -punctuation not original: 
 
original = "Sunt hic etiam sua praemia laudi; \
sunt lacrimae rerum et mentem mortalia tangunt. \
Solve metus; feret haec aliquam tibi fama salutem."

translation = "Here, too, the praiseworthy has its rewards; \
there are tears for things and mortal things touch the mind. \
Release your fear; this fame will bring you some safety."

# split it into separate words. 
# Here '.' is the delimiter 
# TO DO: manage ';'

sentences = original.split('. ')

# prepare the result list
result_list = []

# now, send each sentence to be transformed
for sent in sentences:

    # test: does the sentence start with uppercase?
    if sent[0] == sent[0].upper():
        print('This is a capitalised sentence: ', sent)

        # fix the uppercase into lowercase!
        restyled =  sent[0].lower() + sent[1:]
    else:
        # do nothing, the word is fine as it is
        restyled = sent

    result_list.append(restyled)

print('This is the reconstructed, all-lowercase version:')

print(' '.join(result_list))


