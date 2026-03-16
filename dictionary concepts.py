Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"nandu","city":"pmr"}
print(a)
{'name': 'nandu', 'city': 'pmr'}
type(a)
<class 'dict'>
a[name]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[name]
NameError: name 'name' is not defined
a["name"]
'nandu'
a.keys()
dict_keys(['name', 'city'])
a.values()
dict_values(['nandu', 'pmr'])
a.items()
dict_items([('name', 'nandu'), ('city', 'pmr')])
a={"year":2026,"month":3}
a.update({"date":28})
a
{'year': 2026, 'month': 3, 'date': 28}
a.update({"date":28,"time":10})
a
{'year': 2026, 'month': 3, 'date': 28, 'time': 10}
a.update({"date":28},{"time":10})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"date":28},{"time":10})
TypeError: update expected at most 1 argument, got 2
#set default
a={"color":""black":"vechicle":"car"}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"colour":"black":"vechicle":"car"}
   
SyntaxError: invalid syntax
a={"colour":"black","vechicle":"car"}
   
a.setdefault("year",2026)
   
2026
a
   
{'colour': 'black', 'vechicle': 'car', 'year': 2026}
a.setdefault(2026,"year")
   
'year'
a
   
{'colour': 'black', 'vechicle': 'car', 'year': 2026, 2026: 'year'}
#pop
   
a={"user":"nandu","mobileno":"9110702678":"mailid":"nandu@gmail.com"}
   
SyntaxError: invalid syntax
a={"user":"nandu","mobileno":"9110702678","mailid":"nandu@gmail.com"}
   
a.opo()
   
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.opo()
AttributeError: 'dict' object has no attribute 'opo'
a.pop("mailid")
   
'nandu@gmail.com'
a
   
{'user': 'nandu', 'mobileno': '9110702678'}
a.popitem()
   
('mobileno', '9110702678')
a
   
{'user': 'nandu'}
#copy
   
a={"time":"1","hour":"2","sec":5}
   
a.copy()
   
{'time': '1', 'hour': '2', 'sec': 5}
a.get()
   
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
a.get("hour")
   
'2'
>>> a
...    
{'time': '1', 'hour': '2', 'sec': 5}
>>> a.clear()
...    
>>> a
...    
{}
>>> a={"name":"nandu","city":"pmr"}
...    
>>> len(a)
...    
2
>>> b={"name":"nandu","city":"pmr","name":"nandu"}
...    
>>> print(b)
...    
{'name': 'nandu', 'city': 'pmr'}
>>> a.count("name")
...    
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a={"name":"nandu","city":"pmr"}
...    
>>> b={"name":"nandu","city":"pmr","name":"nandini"}
...    
>>> print(b)
...    
{'name': 'nandini', 'city': 'pmr'}
>>> b={"name":"nandu","city":"pmr","name1":"nandu"}
...    
>>> print(a)
...    
{'name': 'nandu', 'city': 'pmr'}
>>> print(b)
...    
{'name': 'nandu', 'city': 'pmr', 'name1': 'nandu'}
