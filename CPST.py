#cumulative Probability for service time

def CPST(a):
    
    v=0
    x=0
    z=[]
    for y in a:
    
        x = x+float(a[v])
        print('%0.2f'%x)
        v += 1
        z.append('%0.2f'%x)
    import RDFS
    print("Random DIGIT:")
    RDFS.RDFS(z)
        
    
