# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.

# 새로운 크로스 플랫폼 PowerShell 사용 https://aka.ms/pscore6

# PS C:\Users\Ryan\Desktop\스파르타코딩클럽\스파르타코딩\2주차> python
# Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> name = 'bob' # 똑같음
# >>> is_number = True # js에서는 true (대소문자 주의)
# >>> a_list=[] # 빈 리스트
# >>> a_list[0] # 호출하는 것은 똑같음
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> print(a_list)
# []
# >>>
# >>> a dict={}
#   File "<stdin>", line 1
#     a dict={}
#       ^
# SyntaxError: invalid syntax
# >>> a_dict={'name':'bob', 'age':21}
# >>> a_dict=['height']=178 #새로 추가
#   File "<stdin>", line 1
# SyntaxError: cannot assign to literal
# >>> people = [{'name':'bob', 'age':20}, {'name':'carry','age':25}] 
# >>> print(people[0]['name'])  
# bob
# >>>   

# function make_card(image) {

# }


def make_card(image):
    #파이썬은 들여쓰기(스페이스 4번)를 강제한다! 대신 중괄호{} 쓰지 않는다
    print(image)

make_card('hello')


# 조건문
def oddeven(num):
    if num % 2 == 0: #if 다음에 () 없음 : 들여쓰기로 구분
        return True
    else:
        return False

print(oddeven(10))

# 반복문
fruits = ['사과', '배', '감', '귤']
# for (let i = 0; i<fruits.length; i++) {
#     console.log(fruits[i]);
# }

for fruit in fruits: #fruits에서 하나씩 꺼내다가 fruit에 저장해서 쓴다
    print(fruit)



fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0 # 사과 개수 저장하는 변수
for fruit in fruits:
	if fruit == '사과':
		count += 1

print(count)


people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(myname):
    # myname에 들어온 이름의 나이를 출력하는 함수

for person in people:   # people 리스트를 person에 담아둠
    if person['name'] == myname:
        print(person['age'])

get_age('john') #20