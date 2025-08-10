#Distribution of Service Time
def DOST():
    print("Enter Service Time:")
    print("From:")
    a=int(input())
    print("\nTO:")
    b=int(input())
    print("Service Time:")
    for x in range(a,b+1):
        print(x)
    import EPST
    EPST.EPST(a,b)


