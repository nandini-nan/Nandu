Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=4
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="nandu"
type(d)
<class 'str'>
e='''nandu'''
type(e)
<class 'str'>
f=5+4j
type(f)
<class 'complex'>
5j+5
(5+5j)
type(5j)
<class 'complex'>
x=True
type(x)
<class 'bool'>
z=False
type(z)
<class 'bool'>
#data type conservations
int(3)
3
int(3.4)
3
int('nandu')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int('nandu')
ValueError: invalid literal for int() with base 10: 'nandu'
int(3+4j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(False)
0
int(True)
1
float(3)
3.0
float(7.8)
7.8
float('nandu')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float('nandu')
ValueError: could not convert string to float: 'nandu'
float(7j+1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(7j+1)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(2)
'2'
str(6.8)
'6.8'
str("nandu")
'nandu'
>>> str(6j+3)
'(3+6j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> comple(1)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    comple(1)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(1)
(1+0j)
>>> complex(4.7)
(4.7+0j)
>>> complex("nandu")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex("nandu")
ValueError: complex() arg is a malformed string
>>> complex('nandu')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    complex('nandu')
ValueError: complex() arg is a malformed string
>>> complex(5j+9)
(9+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(9)
True
>>> bool(8.9)
True
>>> bool('nandu')
True
>>> bool(True)
True
>>> bool(False)
False
