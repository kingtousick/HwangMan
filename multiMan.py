while True :
      n = int(input("숫자를 입력하세요"))

      print("\n\n"+"------{}단------".format(n))

      if(n==100):
            print("종료")
            break
      else:
            for k in range(1,11) :
              print("{} X {} = {}".format(n,k, n*k))
  

            
        
