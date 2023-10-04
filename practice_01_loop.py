# 문제 1)입력 된 단수를 출력하는 코드
# dan=input("단수")
# for i in  range(1,10,1):
#   print("{}x{}={}".format(dan,i,int(dan)*i))


# 문제 2) 2단부터 9단까지 출력하는 코드
# for i in  range(2,10,1):
    for j in range(1,10,1):
        print("{}x{}={}".format(i,j,i*j))
    print("-------------------------------")

 # 문제 3) list a의 평균값을 계산하세요.
    a= [1,2,3,4,5,99,87,54,2,5,4]
    total=0
    for i in range a:
        total=total+i
        total=total+i
    length = len(a)
    result = total/length
    # round(값, 소수점숫자): 반올림
    print(round(result,2)) # 평균값

# 문제4) list b에서 최소값 찾기!

b = [22,1,4,7,98]

print(num_min) # '1'을 출력