'''
딕셔너리(dictionary) {순서가 중요하지 않음}
    python에서 사용하는 자료구조 중 하나 
    key와 value 쌍으로 존재
문법: 중괄호와 :를 사용
    indexing 가능-> key를 이용해서
    indexing method를 사용하는 방법: get
    keys method를 이용해서 dict. 내 key값들 모두 확인할수 있음
value 수정하는 방법
    1)indexing 이용
    2)update method 이용
key와 value쌍을 추가하는 방법
    1)indexing 이용
key와 value쌍을 산제하는 방법
    1)Del사용
"key in dict"사용시 T/F 반환이 가능


'''

# sports={"손흥민":"축구","류현진":"야구","서장훈":"농구"}
# print(type(sports))
# print(sports["류현진"])
# print(sports.get("류현진"))
# print(sports.values())
# sports["서장훈"]="예능"
# sports.update({"서장훈":"예능"})
# print(sports)
# sports["김연아"]="피겨"
# sports.update({"김연아":"피겨"})
# print(sports)
# del sports["김연아"]
# print(sports)
# del sports["서장훈"]
# print(sports)
# print("손흥민" in sports)
# print("강호동" in sports)


fruits={"orange":"50","banana":"100","apple":"200"}
fruit=input("this is fruit store. What do you want?:")
if fruit in fruits:
    print(f"we have {fruit}.{fruits[fruit]} left.")
else:
    print(f"sorry, we don't have {fruit}")