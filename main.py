def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("After swapping a=" ,a, "b=" ,b)

def swap2(a,b):
    a=(a&b) + (a|b)
    b=a+(-b)+1
    a=a+(-b)+1
    print("After swapping a =" ,a,"b= " ,b)
a=int(input("enter a: "))
b=a=int(input("enter b: "))
print("Before swapping: a=" ,a, "b=" ,b)
swap(a,b)
swap2(a,b)
