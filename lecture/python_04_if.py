# 조건문(condition)

# ~ 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# ~ 모든 조건 은 boolean으로 표현 됨
# ~ 조건문의 경우 if, elif, else 블록 내 종속된 코드를 들여쓰기
# ~ 모든 블록문의 시작점은 마지막에 : (콜론, colon) 추가
# ~ Python에서 블록내에 코드는 반드시 들여쓰기(tab) 강제!!!!

# if (조건1){                    if 조건1:
#    code                        code
# } else if (조건2) {            elif 조건2:
#     code                       code
# }

# if 조건1:
# code
# elif 조건2:
# code
# elif 조건3:
# code
# else:
# code

 # 1. if
 # 2. if~elif~elif
 # 3. if~else
 # 4. if~elif~elsen

 # 점수 계산기
 # - 91~100 : A
 # - 81~90 : B
 # - 71~80 : C
 # - 61~70 : D
 # - 60이하 : F

score = 95 # 0~100 점

#if score>90 and

 #   i have a:
    #print("A")
#elif score>80:
    #print("B")
#elif score>70:
  #  print("C")
#elif

# 문제 1. 어떤 조류의 학생인지 맞히기"?

# (초등, 중등, 고등, 대학생, 학생x)

from datetime import datetime

born = input("당신이 태어난 년도를 입력하세요:")
today = datetime.today().year
print(today)
age = today - int(born) #  2023 - 2004 = 19

if 0 <= age <= 26:
    if  age >= 20:
        print("대학생")
    elif age >= 17:
        print("고등학생")
    elif age >= 14:
        print("중학생")
    elif age >= 8:
        print("초등학생")
else:
        print("이스 낫어 휴먼")

