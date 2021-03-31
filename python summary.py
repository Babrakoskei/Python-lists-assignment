Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> b = "feminine"
>>> len(b)
8
>>> #the len function is used to find the length of characters in a string
>>> "i" in b
True
>>> "x" in b #only returns true if the character given is in the string
False
>>> "a" not in b
True
>>> "f" not in b
False
>>> #returns True if the characters given are NOT in the String
>>> s = "dancer"
>>> s.index(e)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.index(e)
NameError: name 'e' is not defined
>>> # error caused by not declaring the character as a String
>>> s.index("d")
0
>>> s.index("r")
5
>>> s.index("z")# will bring an error because the character declared does not belong to the above String
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.index("z")# will bring an error because the character declared does not belong to the above String
ValueError: substring not found
>>> f = "coding"
>>> f[0:4]
'codi'
>>> f[0: ]
'coding'
>>> #allow acess to a range of characters in a String
>>> f.isupper()
False
>>> f.capitalize()
'Coding'
>>> f.upper()
'CODING'
>>> "c" in f
True
>>> "g" in f
True
>>> languages = ["English","French","Mandarin"]
>>> languages.sort()
>>> print(languages)#will sort items in the list in ascending order
['English', 'French', 'Mandarin']
>>> languages.pop()
'Mandarin'
>>> #removes the last item on a list
>>> languages.clear()
>>> print(languages)
[]
>>> #clear all items in the list
>>> 