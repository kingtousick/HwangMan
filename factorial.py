def factorial(x):
    if x == 0 :
        return 1
    else :
        return x*factorial(x-1)


while True :
    n = input("숫자를 입력하세요")

    if n.isnumeric():
        res = factorial(int(n))
        print("{0}!= {1}".format(n,res))
    else:
        print("종료합니다. 숫자만가능")
        break
