def valueChecker(num) :
    if((num % 2) == 0):
        print("짝수입니다.")
    else:
        print("홀수입니다.")

a = 1
while a > 0 :
    a = int(input("확인할 숫자를 입력하세요(끝내려면 음수입력): "))
    if(a<0):
        print("종료합니다.")
        break
    else:
     valueChecker(a)



