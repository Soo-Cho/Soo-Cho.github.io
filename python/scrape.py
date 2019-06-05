# get the libraries we need.
import nltk
from bs4 import BeautifulSoup
from urllib import request
# (line 4 comes with python, asking for info from web)

# store the url we're using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# using that url, get the HTML from it
# (look inside the request library, find the method that opens the url, and when you get that, read it)
html = request.urlopen(url).read()

# took the URL and turned into a soup object
# BeautifulSoup means (take the html, and make it into soup-like things into it)
# str(5) CF 5: two data types
# data type = object
# object oriented programming (OOP) = code in humane groupings
# when you turn things into an object, you basically, turn it into 3D CF. linear process of 2D of doing things step by step (which will cause problems when you have to reverse)

#so, this means we've turned things into a soup object, and by using lxml, parsed html
soup = BeautifulSoup(html, "lxml")
# soup.text: BeautifulSoup allows us to do
our_text = soup.text
#(if you only want some parts of it (all the things between 0 and 10 here)
links = soup.find_all("a")[0:10]

#look in our_text and give first 0 to 2000 characters
##--> print(our_text[0:2000])
#(we got gunk! a lot of white spaces. let's get rid of that)
#(\n means all the new line spaces)
# replace the line breaks with spaces
## --> print(soup.text.replace("\n", " "))

#(not all the links are what we care about, so we're going to restrict some)
#td.content is a html thing. should look into more
links_html = soup.select("td.content a")
this_link = links_html[0]
#(if you run it, you can see that it is a list, cause there is a bracket in the end)
# [0] means to just pull the first one


## print(this_link["href"]) ---> pull out the whole list
# take each link and make a new list w/ processed urls
# (this will make things into a list)
urls = []
## for link in links_html:
##    print(link["href"])
##    urls.append(link["href"])

# (we're trying to clean it up now, so modifying the one above)
## for link in links_html:
##     to_append = link["href"].replace("blob/", " ")
##     urls.append(to_append)

# for this, we needed the front part of the url
# careful!! no space in between ""
for link in links_html:
    to_append = link["href"].replace("blob/", "")
    urls.append("https://raw.githubusercontent.com" + to_append)

print(urls)

#pull out fourth item.
# this wil pull a whole (one) text from the website
## html = request.urlopen(test_url).read()
## soup = BeautifulSoup(html, "lxml")
## text = soup.text.replace("\n", "")
## print(text)

# now we are trying to get all the texts
# remember now that parameter test_url now should be url
# also, now we're making a new list of texts
# also, for every text in new corpus_text
test_url = urls[3]
corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace("\n", "")
    corpus_texts.append(text)
    print("Scraping " + url)

# to see the length of it
print(len(corpus_texts))
# it's going to tell us how long it is
print(len(corpus_texts[0]))

#now since we have all the materials, we are going to use text analysis library
#shift t a new library
# what we got is a huge string. by using nltk, cut it into words
# then most common words 
this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
print(process_this_text[0:20])
print(nltk.FreqDist(process_this_text).most_common(50))
