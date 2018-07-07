# print('hello')
#
# #주석_한줄
#
# """양쪽에 따옴표는 주석"""
#
# #파이썬에서 스트링 입력법
#
# # c: 문자열 ' ' , " ", """   """", '''   ''''
#
# print("hello world")
#
# print("Hello")
# print("World")
#
# print('Hello\nWorld')
#
#
# print("'Hello'")
#
# print("\\")
#
# print('"C:\\Download\\hello.cpp"')
#
# #변수명-어떤 값을 저장하는 공간의 이름
# #문자열() - 함수 ... 어떤 기능을 하는 코드
# #파이썬 변수의 특성: 뭐든지 올수 없다.
#
# a = input("뭐든지입력해보세요")
# print('당신의 입력한 갋은 {}입니다.'.format(a))
#
#
# a=input("뭐든지입력해보세요")
# print('당신의 입력한 갋은 {}입니다. {} 맞죠?'.format(a, a))
#
#
#
# a=123
# b=123
# print(a+b)


# int(), str()


# #a= input('숫자를 입력해 주세요: ')
# a= int(input('숫자를 입력해 주세요: '))
# #b= input("숫자를 또 하나 입력해주세요: ")
# b= int(input("숫자를 또 하나 입력해주세요: "))
# #b=int(b)
# print('당신이 입력한 숫자를 모두 더하면 {}입니다.' .format(a+b))



# 조건문 / 반복문
#조건 if / else
# 파이썬의 중요한 특성:파이썬은 들여쓰기(Indentation)로 구문을 구별한다.

# a = int(input('숫자 : '))
# if a>100:
#     print('100보다 크다')
# else:
#     print('100보다 적다')


#>, < , >=, <=, == , !=

print('------------------')
print('------계산기------')
print('------------------')

number1 = int(input('숫자를 하나 입력해주세요 : '))
number2 = int(input('숫자를 하나 더 입력해주세요 : '))

print('뭘 할까요? \n1. 더하기\n2, 빼기\n3, 곱하기\n4, 나누기')

code = int(input('뭘할지 숫자로 입력해주세요. :  '))


if code == 1:
    print('정담은 {}입니다.' .format(number1 + number2))


elif code == 2:
    print('정담은 {}입니다.' .format(number1 - number2))

elif code == 3:
    print('정담은 {}입니다.' .format(number1 * number2))

elif code == 4:
    print('정담은 {}입니다.' .format(number1 / number2))

else:
    print('잘못 입력했습니다')

