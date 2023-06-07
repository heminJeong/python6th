# #if else
#
# age = 18
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자 입니다.")
#
#
#
# score = 85
# if score >= 90:
#     print("A 등급")
# else:
#     if score >= 80:
#         print("B 등급")
#     else:
#         if score >= 70:
#             print("C 등급")
#         else:
#             print("D 등급")
#
# a = int(input("Enter Number Greater then 2: "))
# if a > 2:
#     print("Correct!! you have Entered : ", a)
# else:
#     print("Wrong!! You have Entered : ", a)
#
# day = input("요일을 입력하세요 : ")
# if day == 'Mon':
#     print("오늘은 월요일")
# elif day == 'Tue':
#     print("오늘은 화요일")
# elif day == 'Wed':
#     print("오늘은 수요일")
# else:
#     print("휴일")
#
# i = 0
# while i < 10:
#     i += 1
#     print("i : ", i)
# else:
#     print("else")
# print("코드 종료")
#
#
# #Infinity loop
# while True:
#     print("멋쟁이 사자")
# print("코드 종료")

#
#
# a = 5
# if a < 6:
#     pass # 해민 개발
# else:
#     print("6 보다 큼")

# 배열 생성 후 접근
import array

# from array import *
#
# stu_roll = array('i', [101, 102, 103, 104, 105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("Array After Insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
# n = len(stu_roll)
# i = 0
#
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# stu_roll.remove(101)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#

s = "Hello World"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.isupper())
print(s.lower())
print(s.isdigit())
print(s.istitle())
print(s.isalpha())