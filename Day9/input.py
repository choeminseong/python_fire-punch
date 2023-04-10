'''
input(입력)
    입력(input) <--> 출력(print)
문법
    input("입력하때 쓰고싶은 내용")


'''


# input("아무거나 쓰셈")
# 입력한거=input("입력하셈:")
# print(입력한거)

# for i in range(1,4):
#     이름=input("당신의 이름을 입력하세요:")
#     str=f"{이름}님, 반가워요"
#     print(str)

# while True:
#     이름=input("당신의 이름을 입력하세요:")
#     str=f"{이름}님, 반가워요"
#     print(str)

# age=input("나이를 알려주서요:")
# fvr=input("좋아하는 걸 알려주세요:")
# str=f"당신은 {age}이고, {fvr}을 좋아하네요"
# print(str)

# for i in range(1,6):
#     num1=input("첫 번째수:")
#     num2=input("두 번째 수:")
#     str=f"첫 번째수는{num1}이고,두 번째수는{num2}라서, 두 수의 합은 {int(num1)+int(num2)}입니다"
#     print(str)

while True:
    num1=input("첫 번째수:")
    num2=input("두 번째 수:")
    str=f"첫 번째수는{num1},두 번째수는{num2}, 두 수의 합은 {int(num1)+int(num2)}이고, 두 수의 차는{int(num1)-int(num2)}이고, 두 수의 곱은 {int(num1)*int(num2)}이고, 첫 번째수를 두번째 수로 나눈 몫 은는 {int(num2)//int(num1)}, 그리고 나머지는 {int(num1)%int(num2)}입니다"
    print(str)


























