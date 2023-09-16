import math
# # def cha():
# #     a=int(input())
# #     b = int(input())
# #     print("IDK", a+b,"thing")
# # smth()
#
# c = -20
# print("Result = ",c + 20 if c >= 0 else c -5)
n=input("Enter your number ")
while type(n)!=int:
    try:
        n=int(n)
    except ValueError:
        print("smth wrong!")
        n=input("Enter your number ")
if n%2==0:
    print("even")
else:
    print("odd")