def sort(arr) :
    arr.sort()
    print("정렬 완료! : ", arr)

def reverse(arr) :
    arr.reverse()
    print("뒤집기 완료! : ", arr)

a=0
valarr= []
while a<5 :
   val = int(input(f'5 개의 정렬할 숫자를 입력하세요({a+1}번째숫자):'))
   valarr.append(val)
   a+=1

setting = int(input("정렬 1 입력 , 뒤집기 2 입력 : "))
if(setting ==1):
    sort(valarr)
else:
    reverse(valarr)

