import random

def NDICE():
    a=int(input("How many sides does your dice have? "))
    if a==4:
        print("Your roll is ",random.randint(1,4))        
    if a==6:
        print("Your roll is ",random.randint(1,6))
    if a==8:
        print("Your roll is ",random.randint(1,8))    
    if a==10:
        print("Your roll is ",random.randint(1,10))

NDICE()
