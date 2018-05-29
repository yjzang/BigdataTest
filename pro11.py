t = input("숫자 5개를 , 로 구분하여 입력하세요 : ")
t_arr= t.split(",")
sum=0
for x in t_arr :
    sum = sum+int(x)

print("평균은 %3.1f 입니다." %(sum/5))



