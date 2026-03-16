Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(2,4.5,"c",7+9j,True,False)
type(a)
<class 'tuple'>
len(a)
6
a.index(True)
4
a.count(4.5)
1
#sets{}
a={2,5.7,"nandu",6+9j,True,False}
print(a)
{False, True, 2, (6+9j), 5.7, 'nandu'}
b={5,7,8,4,5,6,0}
print(b)
{0, 4, 5, 6, 7, 8}
type(a)
<class 'set'>
a={1,2,3,4,5,6}
b={4,5,6}
a.add(20)
a
{1, 2, 3, 4, 5, 6, 20}
a.isuperset(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.isuperset(b)
AttributeError: 'set' object has no attribute 'isuperset'. Did you mean: 'issuperset'?
a.isubset(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.isubset(b)
AttributeError: 'set' object has no attribute 'isubset'. Did you mean: 'issubset'?
a.issubset(b)
False
a.issubset(a)
True
a.issuperset(b)
True
a.issuperst(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.issuperst(a)
AttributeError: 'set' object has no attribute 'issuperst'. Did you mean: 'issuperset'?
b.issuperst(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.issuperst(a)
AttributeError: 'set' object has no attribute 'issuperst'. Did you mean: 'issuperset'?
>>> b.issuperset(a)
False
>>> #union()
>>> a={1,2,3,4,5,6}
>>> b={4,5,6,7,8,9}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a={1,2,3,4,5,6,7}
>>> b={5,6,7.8.9.10}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> b={5,6,7,8,9,10}
>>> a.intersection(b)
{5, 6, 7}
>>> #difference
>>> a={1,2,3,4,5,6,7}
>>> b={6,7,8,9,10,11,12}
>>> a.difference(b)
{1, 2, 3, 4, 5}
>>> b.difference(a)
{8, 9, 10, 11, 12}
>>> #update()
>>> a={8,9,10,11,12,13}
>>> b={1,2,3,4,5,6,7,8}
>>> a
{8, 9, 10, 11, 12, 13}
>>> a.update(b)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
>>> b.update(a)
>>> b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
>>> #intersection update
>>> a={4,5,6,7,8,9}
>>> b={1,2,3,4,5,6}
>>> a
{4, 5, 6, 7, 8, 9}
a.intersection_update(b)
\
a
{4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}
#difference update
a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a={3,4,5,6,7,8,9,10}
b={1,2,3,4,5,6,11,12}
a.difference_update(b)
a
{7, 8, 9, 10}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 11, 12}
#symmetri difference
a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.symmetric_difference(b)
{1, 2, 8}
b.symmetric_difference(a)
{1, 2, 8}
a
{3, 4, 5, 6, 7, 8}
#symmetric difference update
a={10,20,30,40,50,60}
b={30,40,50,60,70,80,90}
a.symmetric_difference_update(b)
a
{70, 10, 80, 20, 90}
b.symmetric_difference_update(a)
b
{40, 10, 50, 20, 60, 30}
#pop()
a={1,2,3,4,5,6,7}
b={3,4,5,6,7,8,9}
a.pop()
1
a.remove(5)
a
{2, 3, 4, 6, 7}
#copy()
a={1,2,3,4,5,6}
a.copy()
{1, 2, 3, 4, 5, 6}
a.clear()
a
set()
b=set()
b.add(20)
b
{20}
#discard()
a={2,3,4,5,6,7}
a.discard(5)
a
{2, 3, 4, 6, 7}
len(a)
5
#disjoint
a={4,5}
b={6,5}
a.isdisjoint(b)
False
a={4,,5,6}
SyntaxError: invalid syntax
a={4,5,6}
b={1,2,3}
a.isdisjoint(b)
True
