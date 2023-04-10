'''
튜플(tuple)
    python에서 사용하는 자료구조 중 하나(리스트와 비슷)
    값이 바뀌면 안되는 상황에서 사용함(리스트와 차이점)
문법
    list[a,b,c]
    tuple(a,b,c)
특징
1.인덱싱(indexing)가능
    대괄호 이용
2.list용 method 사용X
    append,pop,sort,reverse
3.slicing(:)
    이상:미만
'''

a=[1,2,3]
b=(1,2,3)

print(type(a))
print(type(b))

print(a[2])
print(b[2])

a[2]=100
print(a)

print(b[:])