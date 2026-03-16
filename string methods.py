Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#negative striding
a="python course"
a[-2:-12:-4]
'sch'
a[-3:-13:-5]
'rn'
a[-5:-11:-2]
'o o'
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
a=input()
b=len(a)
print(b)
python course
#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("l")
4
a.count(" ")
3
a.count("a")
1
#find a string
a="python"
a[1]
'y'
a.find("n")
5
b="codegnan"
b.find("n")
5
b[5]+b[7]
'nn'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
a="name:nandu\nmobileno:9110702678\tmailid:nandu@gmail.com.\ncity:pmr"
print(a)
name:nandu
mobileno:9110702678	mailid:nandu@gmail.com.
city:pmr
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper()
'PYTHON'
d="capitalize"
d.capitalize()
'Capitalize'
a[0].upper()
'H'
>>> a="code"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.startswith("c")
True
>>> a.endswith("e")
True
>>> b="python course"
>>> b.isalpha()
False
>>> b.isdigit()
False
>>> c='123456"
SyntaxError: unterminated string literal (detected at line 1)
>>> c="123456"
>>> c.isdigit()
True
>>> c.isalnum()
True
>>> d="nandu@2828"
>>> d.isalnum()
False
>>> #strip()
>>> #strip(),rstrip()
>>> a="    nandu      "
>>> a.strip()
'nandu'
>>> a.istrip()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.istrip()
AttributeError: 'str' object has no attribute 'istrip'. Did you mean: 'lstrip'?
>>> a.lstrip()
'nandu      '
>>> a.rstrip()
'    nandu'
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
b="i am learning python course"
b.split()
['i', 'am', 'learning', 'python', 'course']
#join()
a="python","java","c","c++"
"".join(a)
'pythonjavacc++'
" ".join(a)
'python java c c++'
"n".join(a)
'pythonnjavancnc++'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="nandu"
lname="a"
print(fname+lname)
nandua
print(fname+" "+lname)
nandu a
print(fname.title()+" "+lname.title())
Nandu A
print(fname+" "+lname.title())
nandu A
#formatting
a=3
b=6
print(a+b)
9
print("the sum is",a+b)
the sum is 9
print("the sum is a+b")
the sum is a+b
city="vja"
print("the city is",city)
the city is vja
name="nandu
SyntaxError: unterminated string literal (detected at line 1)
name="nandu"
print("name is",name)
name is nandu
#format method
a="nandu"
b="nandini"
print("hello {}{}".format(a,b))
hello nandunandini
print("hello {} {}".format(a,b))
hello nandu nandini
print("hello {} hello {}".format(a,b))
hello nandu hello nandini
#fstring
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
print(f"hello {a} hello {b}")
hello sita hello ram
#list[]
a[3,5.6,"python",6+9j,true,false]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a[3,5.6,"python",6+9j,true,false]
NameError: name 'true' is not defined. Did you mean: 'True'?
a[3,5.6,"python",6+9j,True,False]
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a[3,5.6,"python",6+9j,True,False]
TypeError: string indices must be integers, not 'tuple'
a=[3,5.6,"python",6+9j,True,False]
a=["python","ds","ml","java"]
a.append(c)
a
['python', 'ds', 'ml', 'java', '123456']
a.append("c++","java")
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    a.append("c++","java")
TypeError: list.append() takes exactly one argument (2 given)
a=["html","css"]
a.extend(["python","java"])
a
['html', 'css', 'python', 'java']
#inset()
a
['html', 'css', 'python', 'java']
a.insert(1,"ds")
a
['html', 'ds', 'css', 'python', 'java']
a.insert(4,"c")
a
['html', 'ds', 'css', 'python', 'c', 'java']
a=["apple","banana","grapes","mango"]
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes', 'mango']
b=a.copy()
b
['apple', 'banana', 'grapes', 'mango']
a.clear()
a
[]
b=[]
b.append("c")
b
['c']
b.extend(["apple", "banana"])
b
['c', 'apple', 'banana']
#pop()
a="hi","hello","how","are","you"]
SyntaxError: unmatched ']'
a=["hi","hello","how","are","you"]
a.pop()
'you'
a
['hi', 'hello', 'how', 'are']
a.pop(3)
'are'
a
['hi', 'hello', 'how']
#sort()
a=["java","c","ml","ai","ds"]
a.sort()
a
['ai', 'c', 'ds', 'java', 'ml']
b=["4","7","3","1"]
b.sort()
b
['1', '3', '4', '7']
#reverse
a=["white","black","red"]
a.reverse()
a
['red', 'black', 'white']
a=["3","6","9","5"]
a.reverse()
a
['5', '9', '6', '3']
#remove
a=["html","css","js"]
a.remove("js")
a
['html', 'css']
b=["1","6","9"]
b.remove("9")
b
['1', '6']
a=["mango","kiwi","dragon"]
len(a)
3
b="mango"
len(b)
5
c=["mango"]
len(c)
1
c.count("mango")
1
