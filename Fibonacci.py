# 피보나치 수열
# 몇 항 까지 출력할것 인지 입력 받은후 출력
def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

f=[]
if __name__=="__main__":
    while True:
        n= input("\n(피보나치 수열) 출력할 항수를 입력하세요 : ")
        if n.isnumeric():
           f.clear()
           n =int(n)
           for i in range(1,n+1):
               f.append(fibonacci(i))
           for i in f:
               print(i, end='  ')
        else:
            print("종료합니다. 숫자만 가능")
            break






