import random
min=1
max=6
roll="yes"

while roll=="yes" :
    print("dice is rolling...")
    print("value is...")
    print(random.randint(min,max))

    
    roll=input("do u want to roll again")
