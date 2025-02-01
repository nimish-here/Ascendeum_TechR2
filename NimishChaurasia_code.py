# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=int(input('Enter No. of Rows:'))
p=1
for i in range (n-1):
    if(i%2==0):
        for j in range (i,n):
            print(' ',end='')
        for j in range (i+1):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        for j in range (i):
            if(j%2==0):
                print(' ',end='')
            else:
                print(p,end='')
                p+=1
        print()
        p=1
    else:
        for j in range (i,n):
            print(' ',end='')
        for j in range (i+1):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        for j in range (i):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        print()
        p=1
for i in range (n):
    if(i%2==0):
        for j in range (i+1):
            print(' ',end='')
        for j in range (i,n-1):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        for j in range (i,n):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        print()
        p=1
    else:
        for j in range (i+1):
            print(' ',end='')
        for j in range (i,n-1):
            if(j%2==0):
                print(' ',end='')
            else:
                print(p,end='')
                p+=1
        for j in range (i,n):
            if(j%2==0):
                print(p,end='')
                p+=1
            else:
                print(' ',end='')
        print()
        p=1
    
    