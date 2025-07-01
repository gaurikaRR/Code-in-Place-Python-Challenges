JOKE = ("""Here is a joke for you! Karel is heading out to the grocery store. 
        A programmer tells her: get a liter of milk, and if they have eggs, get 12.
         Karel returns with 13 liters of milk. 
        The programmer asks why and Karel replies: 'because they had eggs.""")
def JOKEBOT():
    a=input("What do you want? ")
    b=a.title()
    if b=="Joke":
        print(JOKE)
    else:
        print("Sorry I only tell jokes")

JOKEBOT()
