'''
f-string 문법
    f"{}"
    내부에 사용할 변수는 중괄호로 이용
    {}안에는 변수 뿐만아니라, 함수와연산자도 가능
    

'''

str="오늘은 월요일"
print(str)

age=15
name="공세동 최약체 조무경"
str2=f"나의 나이는 {age}살이고, 이름은 {name}입니다"
print(str2)

첫번째수=5
두번째수=15
str3=f"두 수의 합은{첫번째수+두번째수}입니다"
print(str3)

리스트=["banana","orange","apple"]
str4=f"리스트는 {리스트}이고, 리스트의 길이는 {len(리스트)}입니다"
print(str4)