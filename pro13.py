from random import randint

set=set([])
while True : 
    set.add(randint(1,46))
    if len(set)==6 :
        print(set)
        break

