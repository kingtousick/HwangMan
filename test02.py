def codeSaperator(pinCode) :
    yyyymmdd = "19" + pinCode[0:2]+ "-" + pinCode[2:4] +"-"+ pinCode[4:6]
    num = pinCode[6:13]
    print('생년월일 :',yyyymmdd )
    print('주민번호 :', num)


value = input("주민번호를 입력해주세요 : ")
codeSaperator(value)

