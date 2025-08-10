#Time Between Arrival Determination
from RDFA import *
global cuss
global tbaa
def TBAD():
    global cuss
    global tbaa
    cus=[]
    rd=[]
    tba=[]
    print("Enter The Number Of Customers")
    a=int(input())
    for x in range(1,a+1):
        cus.append(x)
    
    print("Enter The Random Digits:")
    for x in range(1,a+1):
        rd.append(int(input()))
    
    h=0
    for x in cus:
        if int(rd[h])==0:
            tba.append(0)
        elif rd[h]>=int(firstran[0])and rd[h]<=int(secondran[0]):
            tba.append(1)
        elif rd[h]>=int(firstran[1])and rd[h]<=int(secondran[1]):
            tba.append(2)
        elif rd[h]>=int(firstran[2])and rd[h]<=int(secondran[2]):
            tba.append(3)
        elif rd[h]>=int(firstran[3])and rd[h]<=int(secondran[3]):
            tba.append(4)
        elif rd[h]>=int(firstran[4])and rd[h]<=int(secondran[4]):
            tba.append(5)
        elif rd[h]>=int(firstran[5])and rd[h]<=int(secondran[5]):
            tba.append(6)
        elif rd[h]>=int(firstran[6])and rd[h]<=int(secondran[6]):
            tba.append(7)
        elif rd[h]>=int(firstran[7])and rd[h]<=int(secondran[7]):
            tba.append(8)
        h += 1
    print("CUSTOMER:")
    for x in cus:
        print(x)
    print("Random Digit:")
    for x in rd:
        print(x)
    print("Time Between Arrival")
    for x in tba:
        print(x)
    cuss = cus
    tbaa = tba
    
