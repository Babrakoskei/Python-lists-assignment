Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= [[1,2,3],[4,5,6],[7,8,9]]
>>> b=[]
>>> for sublist in a:
...     for numbers in sublist:
...             b.append(numbers)
... 
>>> print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=[1,2,3,4,5,6,7,8,9]
>>> c=[]
>>> c=[a*11 for a in b]
>>> print(c)
[11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> print(b)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=[1,2,3,4,5,6,7,8,9]
>>> c=[]
>>> c=[a*11 for a in b]
>>> print(c)
[11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 

