#Enter Probability for service time

def EPST(b,c):
    a=[]
    print("Enter Probability For Service Time: ")
    for x in range(b,c+1):
        a.append(input())
    import CPST
    print("probability: ")

    for x in a:
        print(x)
    print("Cumulative Probability:")
    CPST.CPST(a)
    
