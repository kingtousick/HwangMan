import pickle


myDic= {'김': '02-2312', '황':'010-5555'}
myList= [40, 30, 90]
myStr= "Hello World Man"

f= open("pic_test", "wb")
pickle.dump(myDic, f)
pickle.dump(myList, f)
pickle.dump(myStr, f)
f.close()

f= open("pic_test", "rb")
data1= pickle.load(f)
data2= pickle.load(f)
data3= pickle.load(f)
f.close()

print(data1)
print(data2)
print(data3)
print(data1['황'])
print(data2[1])