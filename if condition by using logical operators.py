#ifcondition by using logical operations
'''a=4
b=5
if a<b and b>a:
    print("true")'''

'''a=3
b=6
if a!=b and b==a:
    print("true")'''

'''a=4
b=5
if a<=b and b>=a:
    print("true")'''

'''a=5
b=6
if a!=b or b==a:
    print("true")'''

'''a=5
b=6
if a<=b or b>=a:
    print("true")'''

'''a=5
b=6
if a<b or b>a:
    print("true")'''

'''a=7
b=2
if not a>b:
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("true")'''

'''a=input("data1")
b=input("data2")
if a=="python" and b=="java":
    print("true")'''

'''a=input("data1")
b=input("data2")
if a==a and b==b:
    print("true")'''

#if condition on by using identify operations
#is  is not
'''a=5
if type(a) is int:
    print("true")'''

'''a=9
if type(a) is not int:
    print("false")'''

'''a=9.5
if type(a) is float:
    print("true")'''

'''a=input("layer")
if type(a) is complex:
    print("false")'''

'''a=input("layer")
if type(a) is bool:
    print("true")'''

#if condition by using memebership operations
'''a=(1,3,5,7,9,11,14,16)
if 5 in a:
    print("true")'''

'''a=(1,4,5,2,7,8,11,14)
if 3 not in a:
    print("true")'''

'''a=(1,2,5,8,9)
b=int(input("a value"))
if b in a:
    print("false")'''

#if else condition by using logical operations
'''a=7
b=3
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=9
b=6
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=8
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=5
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=(1,2,3,4,5,6)
if 3 in a:
    print("true")
else:
    print("false")'''

'''a=(1,2,3,4,5,6)
if 2 not in a:
    print("true")
else:
    print("false")'''

#if - elif conditions
'''a=5
b=3
if a<b:
    print("greater")
elif a>b:
    print("less")'''

'''a=5
b=3
if a<=b:
    print("true")
elif a==b:
    print("false")
elif a!=b:
    print("true")'''

'''a=5
b=3
if a<b or a>b:
    print("true")
elif a!=b or a==b:
    print("false")'''

'''a=5
b=3
if a>b and a<b:
    print("true")
elif a<b and a>b:
    print("false")'''

#if-elif-else conditions
'''a=5
b=3
if a<b:
    print("true")
elif b>a:
        print("false")
else:
    print("less")'''


'''a=5
b=3
if a<b or a>b:
    print("true")
elif b>a or b<a:
        print("false")
else:
    print("less")'''

'''a=5
b=3
if not a<b and a>b:
    print("true")
elif not b>a and b<a:
        print("false")
else:
    print("less")'''

#multiple-if-conditions
'''a=5
b=7
if not a<b and a>b:
    print("true")
elif not b>a and b<a:
        print("false")
else:
            print("less")'''

a=5
b=7
if a>b:
    print("true")
elif  b<a:
        print("false")
if a!=b:
    print("less")

