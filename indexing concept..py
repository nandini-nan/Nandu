Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
>>> #positive indexing
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[5]+a[6]
'in'
>>> a[0]
'i'
>>> a="simple is better than complex"
>>> a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]
'comple'
>>> a="i am learning python"
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> #negavtive indexing
>>> a="i love python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-11]+a[-10]+a[-9]+a[-8]
'love'
>>> a"vijayawada is royal city"
SyntaxError: invalid syntax
>>> a="vijayawada is royal city"
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]
IndexError: string index out of range
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
IndexError: string index out of range
