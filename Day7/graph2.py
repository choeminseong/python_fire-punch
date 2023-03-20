import matplotlib.pyplot as plt
# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(i*i*i)
# plt.figure()
# plt.plot(x,y)
# plt.show()


# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(2**i)
# plt.figure()
# plt.plot(x,y)
# plt.show()


# x=[]
# y=[]
# y1=[]
# y2=[]
# y3=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(i*i)
#     y1.append(i*i*-1)
#     y2.append(i*-1)
#     y3.append(i)
# plt.figure()
# plt.plot(x,y,x,y1,x,y2,x,y3)
# plt.show()

x=[]
y=[]
x1=[]
y1=[]
figure,axes=plt.subplots(2,2)
fruits=["apple","banana","cherry","orange"]
counts=[4,6,5,10]
bar_color=["red","yellow","purple","orange"]
axes[0,0].barh(fruits,counts,color=bar_color)
axes[1,0].bar(fruits,counts,color=bar_color)
for i in range(-10,11):
    x.append(i)
    y.append(i)
    axes[0,1].plot(x,y)
    x1.append(i)
    y1.append(i*i)
    axes[1,1].plot(x1,y1)
plt.show()


