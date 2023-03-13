'''
리스트(list)
열거형 변슈를 나타내는 자료구조 중 하나
대괄호를 이용해서 표현
각 요소는 쉼표로 구분
비어있는 리스트는"[]"표현
메소드를 가짐
<특징1>
    맨 오른쪽에 요소를 추가할때 append 메소드 사용
<특징2>
    맨 오른쪽 요소를 삭제할때 pop 메소드 사용
<특징3>
    리스트 전체를 비울때는 clear 메소드 사용
<특징4>
    오름차순 정렬할때 sort 메소드 사용
<특징5>
    리스트를 거꾸로 정렬할때 reverse 메소드 사용

(L to R)=0,1,2
(R to L)=-1,-2,-3
*index
    요소를 이용해서 indexing 값을 찾는다
*count
    요소가 리스트 안에 몇개인지 찾아줌
*insert
    리스트 안에 원하는 자리에 값을 추가할때 사용
    insert(자리,값)
*remove
    리스트 인에 원하는 값을 삭제할때 사용
*extend
    리스트와 리스트를 연결할때 사용
*+
    리스트 연결할때 사용
*len
    리스트의 길이를 알고싶을때 사용
'''
# a=1
# b="리스트"
# c=[1,2,3,4]
# print(c)
# d=["사과","바나나","귤"]
# print(d)
# e=[1,"apple",2,"banan"]
# print(e)

# f=[]
# print(f)
# f.append(100)
# print(f)
# f.append(50)
# print(f)
# f.append(1)
# print(f)

# f.pop()
# print(f)
# f.pop()
# print(f)
# f.pop()
# print(f)

# g=[100,50,1]
# g.clear()
# print(g)

# h=[2,4,1,3]
# h.sort()
# print(h)

# i=["orange","cherry","apple"]
# i.sort()
# print(i)

# j=[2,4,1,3]
# j.reverse()
# print(j)





# a=[2,4,1,3]
# a.sort()
# a.reverse()
# print(a)

# b=[]
# for i in range(1,20):
#     if i%3==0:
#         b.append(i)
#         b.sort()
#         b.reverse()
# print(b)

# c=[]
# def M(c):
#     for i in range(1,10):
#         c.append(i)
#         c.sort()
#         c.reverse()
#         print(i*c)
# M(4)
# M(7)

# a=["가","나","다"]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[-1])
# print(a[-2])
# print(a[-3])
        
# b=[1,2,5,10]
# print(b[1]*b[-1])

# c=[1,2,3,4]
# print(c.index(3))
# print(c.index(4))

# c=[1,2,3,4,3]
# print(c.count(3))
# print(c.count(100))

# d=[1,2,3]
# d.insert(100,1)
# print(d)
# d.insert(1,100)
# print(d)

# e=[1,2,100,3]
# e.remove(100)
# print(e)
# e.remove(1)
# print(e)

# f=[1,2]
# g=[3,4]
# f.extend(g)
# print(f)
# g.extend(f)
# print(g)

# h=[1,2]
# i=[3,4]
# print(h+i)
# print(i+h)
# print(h+i+[5,6])

# k=[1,2,3]
# print(len(k))
# print(len(k+k))




# fruits=["banana","cherry","apple"]
# fruits.sort()
# fruits.reverse()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# fruits=["banana","cherry","apple"]
# fruits.sort()
# fruits.reverse()
# for i in range(3):
#     print(fruits[i])

# fruits=["banana","cherry","apple"]
# fruits.append("watermelon")
# fruits.sort()
# fruits.reverse()
# for i in range(len(fruits)):
#     print(fruits[i])

fruits=["banana","cherry","apple"]
fruits.sort()
fruits.reverse()
for fruit in fruits:
    print(fruit)
