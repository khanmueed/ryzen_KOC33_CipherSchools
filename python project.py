def findleap(start,end):
    start=int(start)
    end=int(end)
    leap=[]
    nonleap=[]
    while start <= end:
        if ((start % 400 == 0) and (start % 100 == 0)) | ((start % 4 ==0) and (start % 100 != 0)):
            leap.append(str(start))
        else:
            nonleap.append(str(start))
        start+=1
    print("leap years are:",leap)
    print("Non leap years are:",nonleap)

start=input("Start Date: ").split("/")
end=input("End Date: ").split("/")
findleap(start[2],end[2])