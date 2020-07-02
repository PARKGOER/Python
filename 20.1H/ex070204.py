f=open("C:\\Users\\박정호\\Desktop\\Python\\newfile.txt",'r')
lines=f.readlines()
for line in lines :
    print(line)
f.close()
