'''
함수
    반복적인 작업을 사용할 때 유용함
    함수를 만드는 작업 필요함
    함수를 호출하는 부분이 필요함
<1번>
    def 함수이름():
        실행할 코드 작성
<2번>
    def 함수이름(입력):
        실행할 코드작성
<3번>
    def 함수이름(입력):
        실행할 코드 작성
        return 출력
*return 함구를 끝마치게 함
'''
# def 민성():
#     print("민성") 
# 민성()
# 민성()

# def 세훈(a):
#     for i in range(a):
#         print("세훈")
# 세훈(3)

# def 무경(a):
#     for i in range(a):
#         print("무경")
#     return i
# 무경(2)


def ChatGPT(a,b):
    for i in range(a+b):
        print("ChatGPT")
ChatGPT(2,3)
ChatGPT(5,10)


def A(a,b):
    print(a+b,a-b,a*b,a/b)
A(3,2)
A(10,5)


def M(a):
    for i in range(1,10):
        print(i*a)
M(3)
M(7)


def T(a,b):
    for i in range(a,b):
        print(a*b/2)
T(3,6)
T(10,20)


def E(a):
    for i in range(1,2*a+1):
        if i%2==0:
            print(i)
E(5)
E(7)
