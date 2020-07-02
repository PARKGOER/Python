n=int(input("n="))
for i in range(1,(n+1)//2+1) :
    for j1 in range(1,(n)//2-i+2) :
        print(" ",end="")
    for j2 in range(1,2*i) :
        print("*",end="")
    for j3 in range(1,(n)//2-i+2) :
        print(" ",end="")
    print("")
for i in range(1,(n+1)//2) :
    for j4 in range(1,i+1) :
        print(" ",end="")
    for j5 in range(1,n-(2*i)+1) :
        print("*",end="")
    for j6 in range(1,i+1) :
        print(" ",end="")
    print("")
