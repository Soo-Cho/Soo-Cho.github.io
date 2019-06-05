
#store the data
words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonocial_spellings = ['color','amuck','adviser','pepper']

#--> how to you connect the words with correct words
# compare the words in some way - a la stemming: it's a compicated way but flexible way

# loop over the list of words
# need a new list in the end
# --> thus, creat a empty list
new_list = []

#you give a paring
mappings = {"colour":"color", "amok": "amuck", "advisor":"adviser"}
#{key:value}

for word in words:
    #if a word is mispelled do something
    if word in mappings:
#shorhand: 파이톤에선 mappings라고만 쳐도 알아서 key만 찾아볼 거야.
# correct the spelling using the mappings dictionary
        corrected_word = mappings[word]
#CF: list에선 mapping[0]등...이라고 했겠지. 여기는 dictionary니까
#it's telling python to look at first part of the dictionary
# add that corrected words
        new_list.append(corrected_word)
    else:
    #if a word is correct do something else
        new_list.append(word)
#because we know that it is correct word, just add
print(new_list)
