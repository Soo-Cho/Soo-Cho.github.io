
#store the information
#how to cut it down
#make it into a dictionary
#aim: Jane Eyre was published in 1847
#hint: for title, date in texts.items():
    #do something to title and date

collection = {
"Jane Eyre":"1847",
"Cane":"1923",
"Wide Sargasso Sea":"1966",
"Citizen:An American Lyric":"2014"
}

for title, date in collection.items():
    print(title + " was published in " + date)

#.items!! Gives us order and pair, so that orderless dictionary would have an end to a loop
