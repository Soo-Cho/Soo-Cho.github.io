domain = "http://walshbr.com/"
pages = ["about","blog","pedagody","projects","cv"]

URLs = []

for page in pages:
    URLs.append(domain + page)

print(URLs)
