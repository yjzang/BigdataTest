from random import randint

r = randint(99,100)
print("=========================")
print(" [숫자 맞추기 게임 시작] ")
print("=========================")

while True :
    num=int(input("숫자 : "))
    if(r<num) :
        print("더 낮게")
    elif(r>num):
        print("더 높게")
    else :
        print("정답입니다.")
        ans=input("게임을 종료하시겠습니까?(y/n) : ")
        if ans=='y' :
            print("=========================")
            print(" [숫자 맞추기 게임 종료] ")
            print("=========================")

            break
        else :
            print("재시작")
            continue