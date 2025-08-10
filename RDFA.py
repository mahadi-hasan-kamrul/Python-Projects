#RANDOM DIGIT FOR ARRIVAL TIME
global firstran
global secondran
def rdfa(p):
    global firstran
    global secondran
    a=[]
    b=1
    c=str(p)
    m=c[2:5]
    d= int(m)
    
    l=[]
    n=[]
    for x in range(0,1001):
        a.append(0+x)
    for x in a:
        x= a[b]
        l.append(int(b))
        y=a[d]
        n.append(int(d))
        print(x,'-',y)
        b=d+1
        d=d+125
        if(d>1000):
            break
    print(l)
    print(n)
    firstran = l
    secondran = n


    
