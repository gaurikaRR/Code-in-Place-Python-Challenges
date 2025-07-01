import random

print("Khansole Academy")
a=random.randint(10,99)
b=random.randint(10,99)
c=a+b
print("What is", a,"+",b,end="")
print("?")
d=int(input("Your answer: "))
if d==c:
    print("Correct!")
else:
    print("Incorrect.")
    print("The expected answer is",c)
