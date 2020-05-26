Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

새로운 크로스 플랫폼 PowerShell 사용 https://aka.ms/pscore6

PS C:\Users\Ryan\Desktop\스파르타코딩클럽\스파르타코딩\2주차> python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> name = 'bob' # 똑같음
>>> is_number = True # js에서는 true (대소문자 주의)
>>> a_list=[] # 빈 리스트
>>> a_list[0] # 호출하는 것은 똑같음
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(a_list)
[]
>>>
>>> a dict={}
  File "<stdin>", line 1
    a dict={}
      ^
SyntaxError: invalid syntax
>>> a_dict={'name':'bob', 'age':21}
>>> a_dict=['height']=178 #새로 추가
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> people = [{'name':'bob', 'age':20}, {'name':'carry','age':25}] 
>>> print(people[0]['name'])  
bob
>>>   