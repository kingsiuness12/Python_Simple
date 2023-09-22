# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로  변수에 컬렉션 1개가 저장
# -리스트(List), 튜플(Turple), 딕트(dictionary), 세트(Set)

# 1. 리스트(List) ex) 기차 !!!
# - 시퀀스 자료형(연속 된 값을 저장)
# - 정렬 가능
# - mutalbe(생성 된 후 변경 가능)
# - index 사용(slicing 가능)
# - packing과 unpacking 가능
# - 멤버함수: append(), extend(), insert(), remove(), pop(), sorted() 등등
# - 2차원 리스트는 표(table)과 동일한 형태


# 리스트 초기화(생성)
list_a = [1,2,3]
list_b = []
list_c = ["chosun", 98, 3.14, [1,2,3]]

print(list_c[0]) # 리스트에서 단일 값 추출
print(list_c[1:3]) # 리스트 슬라이싱

# 패킹가 언패킹
list_d = ["A","B","C"] # 패킹
a, b, c = list_d # 언 패킹

# a = list_d[0]
# b = list_d[1]
# c = list_d[2]

# append(): 리스트 맨 마지막에 값 추가!
a = [1,2,3,4,5]
a.append(10)
print(a)

# insert() : 원하는 인덱스에 값 추가!
a.insert(1,"A") # (인덱스, 값)
print(a)

# extend(): 리스트 병합 (List A + List B)
a = [1,2,3]
b = [3,4,5]
# a.append(b) -> [1,2,3,[3,4,5]]
a.extend(b) # a를 기준으로 병합
print(a) # 두 리스트 이어 붙이기
print(a+b) # 또 다른 병합 방식

# remove(): 값으로 삭제 (인덱스 값으로 = 배열 안의 값으로)
a = ["a", "b", "c"]
a.remove("b")
print(a)
# pop(): 인덱스로 삭제 인덱스 번호로 삭제(몇번째 배열인가)
b = ["a", "b", "c"]
c = b.pop(0) # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능! (선택사항)
print(b)
print(c)

# index(): 찾고자 하는 값의 인덱스 반환
a = [1,2,3]
print(a.index(3)) # 인덱스 반환

# sort() and sortd(): 리스트 값 정렬!
# - sort(): 원본 값 정렬(주의)
# - sorted(): 복제 한 값 정렬
a = [9,3,2,1,5,8,10]
b = sorted(a)
c = sorted(a, reverse=True) #내림차순
print(a)
print(b)
print(c)

# 2. 튜플(Tuple) ex): 기차
# - LIST와 대부분 동일
# - 시퀀스 자료형(정렬 불가능)
# - immutable(생성 된 후 변경 불가능)
# - index 사용(Slicing 가능)
# - packig 과 Unpacking 가능
# - () 사용(생략가능)
# - 여러분이 직접 Turple를 생성하는 경우는 없다
# -> 파이썬에서 결과값을 받을 때 Tuple로 제공

print("=" *100)
a = [1, 2, 3]
b = (1, 2, 3)
c = 1, 2, 3

print(a)
a[0] = 99

b[0] = 99
print(b) # Tuple 값은 변경 불가능

# 튜플 원소가 1개인 경우
a = (1, 2, 3)
b = 1, 2, 3
c = (1)
d = 1
e = 1,
print(type(b))
print(type(d))
print(type(e))

num = a
a = b
b = num

print(a)
print(b)
a, b =b, a # Tuple packing & unpacking 사용 - 튜플로 변수 내 자료 전환
print(a)
print(b)

# 3. 세트(set) ex: 복주머늬
# - 수학의 집합 개념
# - 순서 없음 (index 없음, 정렬 불 가능)
# - 중복값을 허용 하지 않음 ( 중요 )
# - {} 사용 (중괄호 사용함)
# - 멤버함수: union(), intersection(). difference() 등등 등 등 등 등 든
set_a = {1, 2, 3}
set_b = {1, 1, 1, 1, 2, 2, 2, 3, 3, 4, ,5}
print(set_b) # 출력시 1,2,3,4,5 중복된 값 하나만 출력

# 중복값 제거 활용 방법
# : a List의 중복값을 제거
a = ["A", "A", "B", "B", "C", "C", "D", "E"] # List type
set(a) # ()안의 값을 set type으로 변환
# a = list(a)
# List -> Set(중복값 제거) -> List
a = list(set(a))
print(type(a))
 print(a)

# 4. 딕트(dict) ex: 복 주머늬
# - 순서가 없음 (인덱스 없음, 정렬 불가능)
# - {key: value} 사용 -> key, value 1pair
# - key 중복 불가. value 중복 가능
# - key 를 통해서만 value에 접근 가능
# - 멤버함수: update(), get(), keys(), values(), items()

# 외부에서 데이터를 받아올 때 대부분 JSON 형식으로 전달
#    - JSON == DICT(동일)
dict_a = {"korea": "Seoul",
          "Canada": "Ottawa",
          "USA": "Washington D.C"}
#         key  //// value
print(dict_a)
import pprint
pprint.pprint(dict_a)


# update() : dict와 dict 병 하 압
a = {"a: 1",
     "b": 2}
b = {"b": 3, "c": 5}
a.update(b) # 병합 시 중복 key 있는 경우 입력값(b)이 우선
print(a)

# pop() : dict 원소를  key를 통해 삭제
print(a)
print(c) # 삭제 된 value(key X)

# in() : ()안의 key값이 존재 확인
print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict, 접근 -> 컬렉션[index or key] ex: a[2]
# print(a["f]) # key가 없으면 Error 발생
print(a.get("f")) # key 가 없으면 None 출력 (Error X)

# keys(), values(), items()
print(a.keys()) # key만 추출
print(a.values()) # value만 추출
print(a.items())# (key, value) 추출

print(list(a.keys())) # 활용방법

# clear(): dict 초기화
print(a)
a.clear()
print(a)

# 숙제 아닌 숙제
# dict 와 set는 중괄호
e = {}
print(type(e))

