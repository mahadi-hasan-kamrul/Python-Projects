def DAT():
    print("Enter the time between Arrival\n")
    print("From: ")
    a=int(input())
    print("\nTo :")
    b=int(input())

    print("\nProbability of Occurance :",a/b)
    c=a/b
    print(c)
    import RDFA
    print("Time between Arrival "+"-Cumulative Probability ")
    for x in range(a,b+1):
        print(x,"                  ",c)
        c = c+(a/b)
    print("Random Digit:")
    RDFA.rdfa(c)

