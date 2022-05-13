import random
def BruteForce():
    PassWord = str(random.randint(0,9999))
    for i in range(10000):
        Trial = str(i)  
        if Trial == PassWord:
            return(f"The Password is {PassWord}")
        else:
            continue
BruteForce()
