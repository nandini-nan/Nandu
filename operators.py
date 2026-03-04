Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arthematic operator
>>> a=1
>>> b=9
>>> print(a+b)
10
>>> print(a-b)
-8
>>> print(a*b)
9
>>> print(a//b)
0
>>> print(a**b)
1
>>> print(a%b)
1
>>> #assignment operators
>>> a=13
>>> b=5
>>> print(a+=13)
SyntaxError: invalid syntax
>>> 
>>> a+=b
>>> a
18
>>> a-=b
>>> b
5
>>> a*=5
>>> a
65
>>> a//=65
>>> a
1
>>> a**=65
>>> a
1
>>> b-=a
>>> b
4
>>> b-=4
b
0
b*=0
b
0
b//=5
b
0
#comparsion operator
a=15
b=10
a<b
False
b>a
False
a<=b
False
b>=
SyntaxError: invalid syntax
b>=a
False
a/=b
a==b
False
b==a
False
#logical operator
a=9
b=15
a<b and b>a
True
a<=b and b>a
True
a!=b and a==b
False
a<b or b>a
True
a<b or b>a
True
a!=b and a==b
False
a!=b or a==b
True
a<b not b>a
SyntaxError: invalid syntax
#identity operator
a=5
if type(a) is int;
SyntaxError: invalid syntax
if type (a) is int:
    print("it is nandu")

    
it is nandu
if type(a) is not float:
    print("it is nandini")

    
it is nandini
if type (a) is not int:
    print("it is tuff")

    
#membership operator
    
a=10,9,3,4,5
if 5 in a:
    print(true)

    
Traceback (most recent call last):
  File "<pyshell#70>", line 2, in <module>
    print(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
if 5 in a:
    print(5)

    
5
if 6 in a:
    print(a)

    
if 5 not in a:
    print(a)

    
if 5 not in a:
    print(5)

    
#bitwise operator
    
a=5
b=3
a&b
1
bin(5)
'0b101'
bin(3)
'0b11'
a=10
b-12
-9
a&b
2
bin(10)
'0b1010'
bin(12)
'0b1100'
a=2
b=1
a/b
2.0
bin(2)
'0b10'
bin(8)
'0b1000'
a=4
b=6
a^b
2
bin(4)
'0b100'
bin(6)
'0b110'
a=7
b=5
a^b
2
bin(7)
'0b111'
bin(5)
'0b101'
