"""
Functions with return values

@author: amos
@date 10 June 2019
"""

def fun1():
    return 2 + 2

def fun2():
    import random
    num = random.randint(1, 10)
    
    import time
    
    # write to a file
    timenow = str(time.gmtime())
    timenow = timenow.lower()
    timenow = timenow.replace(" ", "_")
    timenow = timenow.replace("(", "")
    timenow = timenow.replace(")", "")
    timenow = timenow.replace("=", "")
    timenow = timenow.replace(",", "")
    
    f = open("data_{}.txt".format(timenow), "w")
    f.write(str(num) + "\n")
    f.close()
    
    
    if num == 5:
        return
    
    print("This is great... you didn't get a 5")
    
    
def fun3():
    f = open("data.txt", "r")
    line = f.readline()
    f.close()
    return line

print(fun1() + 2 ) #6


print(fun2())

print(fun3())