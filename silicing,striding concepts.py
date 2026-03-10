Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#silicing
a="codegnan"
a[4:]
'gnan'
a[:4]
'code'
a[0:3]
'cod'
a[4:8]
'gnan'
a[0:4]
'code'
#positive silicing
a="codegnan it solutions"
a[9:11]
'it'
a[12:21]
'solutions'
a[0:9]
'codegnan '
b="python full stack course"
b[7:11]
'full'
b[0:6]
'python'
b[18:24]
'course'
#negative silicing
a="work hard until you succeed"
a[-17:-12]
'until'
a[-22:-18]
'hard'
a[-27:-23]
'work'
a[-11:-8]
'you'
a[-7:0]
''
a[-7:-1]
'succee'
b="time is very precious"
b[-13:-9]
'very'
b[-21:-17]
'time'
b[-8:-22]
''
b[-8:0]
''
b[-8]
'p'
>>> b[-8:]
'precious'
>>> #striding concept
>>> #positive striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::4]
'd e'
>>> c="machine learning"
>>> c[::4]
'miln'
>>> c[3:9]
'hine l'
>>> c[::6]
'men'
>>> c[::7]
'm n'
>>> c[::2]
'mcielann'
>>> a[5:]
'science'
>>> a[::4]
'd e'
>>> 'd e'
'd e'
>>> c[5::]
'ne learning'
>>> c[::4]
'miln'
>>> c[::8]
'ml'
>>> a="cloud computing"
>>> a[2:14:3]
'o mt'
>>> a[5:10:2]
' op'
>>> a[3:12:4]
'uot'
