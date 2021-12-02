abp= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for k in range(0,len(abp)):
        print("{0:2d}   {1}".format(k,abp[k:len(abp)]+abp[0:k]))
