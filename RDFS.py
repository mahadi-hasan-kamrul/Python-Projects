#RANDOM DIGIT FOR SERVICE TIME
global firstrans
global secondrans
def RDFS(p):
    a=[]
    d=[]
    b=1
    v=0
    n=0
    s=[1]
    global firstrans
    global secondrans
    for x in p:
        c=str(p[n])
        m=c[2:4]
        d.append(int(m))
        n+=1
    

    for x in range(0,101):
        a.append(x)
    for x in a:
        x= a[b]
        y=a[int(d[v])]
        print(x,'-',y)
        b=d[v]+1
        
        v+=1
        if v>5:
            break
        s.append(b)
    print(d)
    print(s)
    firstrans = s
    secondrans = d
