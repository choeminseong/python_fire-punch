'''
모듈(module)설치
터미널 창에서 pip 설치 명령어 사용
ex)pip install  
    설치된 모듈을 확인하고 싶을때
ex)pip list
    matplotlib
모듈 불러오기
    import 모듈이름
모듈 사용하기
    모듈이름.메소드()
    모듈이름.변수

'''
import matplotlib.pyplot as plt
# plt.figure()
# plt.plot([0,1,2],[1,3,5])
# plt.show()

# plt.figure()
# x1=[0,100]
# y1=[0,100]
# x2=[0,100]
# y2=[0,50]
# plt.plot(x1,y1,"r",x2,y2,"k")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("y=x+1, y=1/2x")
# plt.show()

x=[]
y=[]
for i in range(100):
    x.append(i)
    y.append(-3*i+5)
plt.figure()
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

# x=[]
# y=[]
# x1=[]
# y1=[]
# for i in range(-100,101):
#     x.append(i)
#     y.append(i*i)
#     x1.append(i)
#     y1.append(60*i)
# plt.figure()
# plt.plot(x,y,x1,y1)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.show()