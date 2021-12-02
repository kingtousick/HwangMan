#  두숫자 받아서 합 차 곱 나누기 값 알려주기
def calculator(x,y) :
    ad = x+y
    mi = x-y
    mu = x*y

    if y==0:
        di="불릉"
    else:
        di = x/y
    return(ad,mi,mu,di)

if __name__=="__main__":
    print("--------------------------------")
    while True :
        x= int(input("첫번째 숫자를 입력하시요(문자입력시 종료)"))
        y= int(input("두번째 숫자를 입력하시요(문자입력시 종료)"))
        # if x.isnumeric() and y.isnumeric():
        #     print("종료합니다.")
        #     break
        print(calculator(x,y))
        break

