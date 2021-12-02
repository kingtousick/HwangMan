a='''황정창, 80, 100, 90, 100, 60
김기태, 50, 77, 61, 78, 55
김성민, 60, 88, 50, 80, 52
송아영, 80, 98, 100, 98, 47
구은비, 85, 80, 48, 100, 65
김병찬, 78, 78, 100, 60, 75
이은정, 65, 60, 100, 70, 85
김수인, 77, 80, 90, 55, 100
박태구, 45, 58, 100, 85, 70'''


k= a.split('\n')

for i in range(len(k)):
    k[i] = k[i].split(',')
    print(k[i])

for i in range(len(k)):
  sum = 0
  for j in range(1,len(k[i])):
      k[i][j] = k[i][j].strip()
      sum += int(k[i][j])
  k[i].append(sum)
  av = int(sum/5)
  k[i].append(av)
  print(i)

for i in range(len(k)):
    print(k[i])


      
      


print('              성적 처리 결과')
print('--------------------------------------------------')
print('')
print('--------------------------------------------------')
