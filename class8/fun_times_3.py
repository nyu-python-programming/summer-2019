"""
Example of starting/completing functions

@author: amos
@date 10 June 2019
"""

def fun1():
    x = "starting fun1"
    print(x)
    fun2()
    print("ending fun1")
    
    
def fun2():
    x = "starting fun2"
    print(x)
    fun3()
    print("ending fun2")
    
    
def fun3():
    x = "starting fun3"
    print(x)
    print("ending fun3")
    
    
    
x = "done"

fun1()

print(x)
