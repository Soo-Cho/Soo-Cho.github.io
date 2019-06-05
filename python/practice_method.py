# def wish(food):
#     print("I am craving " + food)
#
foods = ["bubble tea","smoothie","frappuchino","shake","icecream"]
#
# for food in foods:
#     wish(food)

#--> NOTE: print wish(food) - does not work
#--> because print is also a method

# def want(a,b):
#     print(a + " wants " + "a " + b)

names = ["Soo", "Mina","June", "Sandra", "Toni"]

# for name in names:
#     want(name,"tea")

# for name in names:
#     for food in foods:
#         want(name,food)

#--> NOTE: both works


# if names[2] == "June":
#     print("dude")
# elif names[2] == "Soo" or "Mina":
#     print("hmm")
# else:
#     print("huh")


for name in names:
    if name == "June":
        print("dude")
    elif name == "Soo" or name == "Mina":
        print("hmm")
    else:
        print("huh")

#--> Note that elif need second NAME == MINA!! otherwise, you are just asking, if it exists, and it does cause I've just created one!
# ex) if "name":
#         print("strings are true because they exit")
#     it'll show up to be strings are true because they exit

# def method_one()
#     print("look I'm a mothod")
#
# def method_two(name):
#     print("about to call our first method for" + name)
#     method_one()
# #--> this will not run without the following sentence. Because it was excuted in method_two("Brandon"), name = "Brandon"
#
# method_two("Brandon")
