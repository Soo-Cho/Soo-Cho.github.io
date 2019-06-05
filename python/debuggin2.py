# #1
#
# greeting = input("Hello, possible pirate! What's the password? ")
# if greeting in ["Arrr!"]:
# 	print("Go away, pirate.")
# else:
#     print("Greetings, hater of pirates!")


# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
    }

for author,date in authors.items():
    print "%s" % authors + " died in " + "%d." % Date
}

still working on this
