'''
조건문(while)
while 조건:
    실행할 코드 작성

1.조건이 참이면 아래 코드가 실행됨
2.조건이 거짓이면 while이 끝남
ex) while True:
        print("안녕")
ex) while False:
        print("하이")



'''
# while 1>0:
#     print("안녕")

# while 1<0:
#     print("안녕")

# i=0
# while i<3:
#     print("while")
#     i+=1

i=0
while i<5:
    print("ChatGPT")
    i+=1


i=1
while i<11:
    if i%2==0:
        print(i)
    i+=1


i=1
a=0
while i<21:
    if i%4==0:
        a+=i
    i+=1
print(a)


i=50
while i<71:
    if i%2==0:
        if i%3==0:
            print(i)
    i+=1

i=100
a=1
while i<111:
    if i%2==1:
        a*=i
    i+=1
print(a)


i=1
a=0
while i<101:
    if i%3==0:
        a+=i
    i+=1
b=0
while i<101:
    if i%7==0:
        b+=i
    i+=1
print(a-b)
