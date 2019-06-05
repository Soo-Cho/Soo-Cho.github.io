#bebuggin 1

# pages = 457
# word_per_page = 250
# number_of_pieces = 100
#
# each_chunk = (pages * word_per_page)/number_of_pieces
# print(each_chunk)


#2
# text = {
# 	"Jane Eyre":"1847",
# 	"Cane":"1923",
# 	"Wide Sargasso Sea":"1966",
# 	"Citizen: An American Lyrics":"2014"
# }
#
# for title,date in text.items():
# 	print(title + " was published in " + date)

#3
# words =  ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
# canonical_spellings = ['color','amuck','adviser','pepper']
#
# mappings = {'colour':'color','amok':'amuck','advisor':'adviser'}
#
# new_list = []
# for word in words:
#     if word in mappings:
#         new_list.append(mappings[word])
#     else:
#         new_list.append(word)
#
# print(new_list)


# 4
domain = 'https://walshbr.com/'
pages = ['about','blog','pedagogy','projects','cv']

urls = []

for page in pages:
	url = domain + page
	urls.append(url)

print(urls)
