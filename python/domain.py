domain = "http://walshbr.com/"
pages = ["about","blog","pedagody","projects","cv"]

URLs = []

for page in pages:
    URLs.append(domain + page)

#for page in pages:
    # url = domain + page
    # urls.append(url)
# ---> same result. but this is is easier to follow. This takes memory: cause it'll remember what url is.
# ---> might help more later when your code gets longer

print(URLs)



# --> to make a comprehension: it's the same thig
# urls = [domain + page for page in pages]
