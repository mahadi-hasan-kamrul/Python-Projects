#Service Time
from RDFS import *
from TBAD import *
global stt
def ST():
    global stt
    rds=[]
    st=[]
    print("Enter the Random digit for service Time:")
    for x in cuss:
        rds.append(int(input()))
    h=0
    for x in cuss:
        if int(rds[h])==0:
            st.append(0)
        elif rds[h]>=int(firstrans[0])and rds[h]<=int(secondrans[0]):
            st.append(1)
        elif rds[h]>=int(firstrans[1])and rds[h]<=int(secondrans[1]):
            st.append(2)
        elif rds[h]>=int(firstrans[2])and rds[h]<=int(secondrans[2]):
            st.append(3)
        elif rds[h]>=int(firstrans[3])and rds[h]<=int(secondrans[3]):
            st.append(4)
        elif rds[h]>=int(firstrans[4])and rds[h]<=int(secondrans[4]):
            st.append(5)
        elif rds[h]>=int(firstrans[5])and rds[h]<=int(secondrans[5]):
            st.append(6)
        elif rds[h]>=int(firstrans[6])and rds[h]<=int(secondrans[6]):
            st.append(7)
        elif rds[h]>=int(firstrans[7])and rds[h]<=int(secondrans[7]):
            st.append(8)
        h += 1
    print("Customers:")
    for x in cuss:
        print(x)
    print("Random Digit for service Time:")
    for x in rds:
        print(x)
    print("Service Time:")
    for x in st:
        print(x)
    stt = st
