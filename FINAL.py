#final Table
from TBAD import *
from ST import *
def FINAL():
    
    sbt=[]
    sett=[]
    wt = []
    tis=[]
    
    print("Customer Number:")
    for x in cuss:
        print(x)
    print("Intra Arrival Time:")
    for x in tbaa:
        print(x)
    print("Arrival Time:")
    v=0
    x=0
    g=0
    p=0
    at=[]

    for y in cuss:
        x = x+(tbaa[v])
        at.append(x)
        v += 1
    for x in at:
        print(x)

    h=0
    
    for x in at:
        if at[h]==0:
            sbt.append(at[h])
            sett.append(sbt[h]+stt[h])
        elif at[h]<sett[h-1]:
            sbt.append(sett[h-1])
            sett.append(sbt[h]+stt[h])
        elif at[h]>sett[h-1]:
            sbt.append(at[h])
            sett.append(sbt[h]+stt[h])
        elif at[h]==sett[h-1]:
            sbt.append(at[h])
            sett.append(sbt[h]+stt[h])
        h += 1
        
    print("Service Beginning Time:")
    for x in sbt:
        print(x)
    print("Service Time:")
    for x in stt:
        print(x)
    print("Service Ending Time:")
    for x in sett:
        print(x)
    print("Waiting Time:")
    for x in cuss:
        if sbt[g]>at[g]:
            wt.append(sbt[g]-at[g])
        elif sbt[g]==at[g] or sbt[g]<at[g]:
                wt.append(0)        
        g += 1

    for x in wt:
        print(x)
    
    print("Time in System:")
    for x in cuss:
        tis.append(stt[p]+wt[p])
        p += 1
    for x in tis:
        print(x)
        
