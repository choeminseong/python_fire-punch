'''
리스트 slice하는 방법
    ":" 기호 사용
ex) a=[1,2,3,4]
a[1:3]
a[0:2] = a[:2]
a[2:4] = a[2:]
a[0:4] = a[:]


'''

# a=[1,2,3,4]
# print(a[1:3])
# print(a[:2])
# print(a[2:])
# print(a[:])

# b=[]
# for i in range(10):
#     b.append(i)
# print(b[:3])
# print(b[2:5]+b[8:])

# c=[]
# for i in range(1,21):
#     if i%2==0:
#         c.append(i)
# c.reverse()
# print(c[:3])

d=[]
for i in range(100,200):
    if i%5==0:
        if i%6==0:
            d.append(i)
d.pop()
d.append(210)
d.reverse()
print(d[:])





